#! /usr/bin/env python

import psycopg2
import urllib2
import gzip
import threading
import logging
import StringIO
import sys
import os

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.CRITICAL)

URL = r'https://datasets.imdbws.com/'
SCHEMA = {
    'title_crew': {
        'file': 'title.crew.tsv.gz',
        'schema': [
            ('tconst', 'TEXT PRIMARY KEY')
        ],
        'relations': [
            ('directors', 'INTEGER ARRAY REFERENCES name_basics'),
            ('writers', 'INTEGER ARRAY REFERENCES name_basics')
        ]
    },
    'name_basics': {
        'file': 'name.basics.tsv.gz',
        'schema': [
            ('nconst', 'TEXT PRIMARY KEY'),
            ('primaryName', 'TEXT'),
            ('birthYear', 'INTEGER'),
            ('deathYear', 'INTEGER'),
            ('primaryProfession', 'TEXT')
        ],
        'relations': [
            ('knownForTitles', 'TEXT ARRAY REFERENCES title_basics'),
        ]
    },
    'title_name_basics': {
        'schema': [
            ('tconst_id', 'TEXT NOT NULL REFERENCES title_basics ON DELETE CASCADE ON UPDATE CASCADE'),
            ('nconst_id', 'TEXT NOT NULL REFERENCES name_basics ON DELETE CASCADE ON UPDATE CASCADE'),
            ('knownForTitles', 'BOOLEAN DEFAULT FALSE'),
            ('directors', 'BOOLEAN DEFAULT FALSE'),
            ('writers', 'BOOLEAN DEFAULT FALSE'),
            ('', 'PRIMARY KEY (tconst_id, nconst_id)')
        ]
    }
}

DB = {
    'dbname': 'breaking-bytes_imdb',
    'host': 'postgresql-breaking-bytes.alwaysdata.net',
    'port': 5432,
    'user': os.getenv('USER'),
    'password': os.getenv('PASSWORD')
}

NAME_TABLE = 'CREATE TABLE name_basics (%s)' % (
    ', '.join(' '.join(kv) for kv in SCHEMA['name_basics']['schema'])
)
LOGGER.debug('name_basic table:\n%s', NAME_TABLE)
TITLE_NAME_TABLE = 'CREATE TABLE title_name_basics (%s)' % (
    ', '.join(' '.join(kv) for kv in SCHEMA['title_name_basics']['schema'])
)
LOGGER.debug('title_name_basic table:\n%s', TITLE_NAME_TABLE)

LOGGER.debug('reading "%s"', SCHEMA['name_basics']['file'])
try:
    f = urllib2.urlopen(
        URL + SCHEMA['name_basics']['file']
    )
except Exception as exc:
    LOGGER.exception(exc)
else:
    s = StringIO.StringIO(f.read())
finally:
    f.close()
LOGGER.debug('decompressing ...')
with gzip.GzipFile(fileobj=s) as g:
    tsv = g.read()
s.close()
LOGGER.debug('... done')

LOGGER.debug('parsing rows ...')
rows = tsv.split('\n')
LOGGER.debug('header:\n%s', rows[0])
rows = (r.split('\t') for r in rows[1:-1])
records = [tuple(None if r == '\\N' else r
                 for r in row)
           for row in rows]
LOGGER.debug('... done')

COUNT = len(records)
LOGGER.debug('count = %d', COUNT)
THREADS = 100
CHUNKS = COUNT // THREADS
LOGGER.debug('chunksize = %d', CHUNKS)
NAME_EXPR = (
    '''INSERT INTO name_basics VALUES
       (%s, %s, %s, %s, %s)'''
)
TITLE_NAME_EXPR = (
    '''INSERT INTO title_name_basics (tconst_id, nconst_id, knownForTitles)
       VALUES (%s, %s, %s)'''
)


def callback(conn, chunk):
    LOGGER.debug('begin execution ...')
    rowcount = 0
    with conn.cursor() as cur:
        for record in chunk:
            try:
                cur.execute(NAME_EXPR, record[:-1])
                conn.commit()
            except Exception as exc:
                LOGGER.exception(exc)
                conn.rollback()
            else:
                rowcount += cur.rowcount
                sys.stdout.write('.')
            if not record[-1]:
                LOGGER.debug('"%s" has no known titles', record[0])
                continue
            for title_name in record[-1].split(','):
                try:
                    cur.execute(TITLE_NAME_EXPR, (title_name, record[0], True))
                    conn.commit()
                except Exception as exc:
                    LOGGER.exception(exc)
                    conn.rollback()
                else:
                    rowcount += cur.rowcount
                    sys.stdout.write(',')
    LOGGER.debug('rowcount = %d', rowcount)
    LOGGER.debug('... execution complete')


if __name__ == '__main__':
    idx, jdx = 0, None
    if len(sys.argv) > 2:
        idx, jdx = int(sys.argv[1]), int(sys.argv[2])
        COUNT = len(records[idx:jdx])
    elif len(sys.argv) > 1:
        idx = int(sys.argv[1])
        COUNT = len(records[idx:])
    LOGGER.debug('count = %d', COUNT)
    CHUNKS = COUNT // THREADS
    LOGGER.debug('chunksize = %d', CHUNKS)
    threads = []
    # start connection
    with psycopg2.connect(**DB) as conn:
        with conn.cursor() as cur:
            # create name table
            LOGGER.debug('create name table ...')
            try:
                cur.execute(NAME_TABLE)
            except Exception as exc:
                LOGGER.exception(exc)
                conn.rollback()
            else:
                conn.commit()
            # create title-name table
            LOGGER.debug('create title-name table ...')
            try:
                cur.execute(TITLE_NAME_TABLE)
            except Exception as exc:
                LOGGER.exception(exc)
                conn.rollback()
            else:
                conn.commit()
            # insert data
            LOGGER.debug('insert data ...')
            for t in range(THREADS):
                jdx = idx + CHUNKS
                chunk = records[idx:jdx]
                LOGGER.debug('starting chunk %d:%d',
                             idx, jdx)
                thread = threading.Thread(
                    target=callback,
                    name=t,
                    args=(conn, chunk)
                )
                thread.start()
                threads.append(thread)
                idx += CHUNKS
            callback(conn, records[idx:])

        for t in threads:
            LOGGER.debug('waiting for thread: %s', t.name)
            t.join()

    LOGGER.debug('... all data inserted')
