"""
My App 2: Hello with Bokeh plot, Jinja2 template, and Bootstrap
"""
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.palettes import d3
from flask import (
    Flask, request, render_template, abort, Response, redirect, url_for,
    send_file, flash
)
import requests
import pandas as pd
import future
from io import BytesIO
from datetime import datetime
import time
import pytz
import os

app = Flask(__name__)
app.secret_key = os.urandom(40)

URL = 'https://developer.nrel.gov/api/pvdaq/v3/site_data'
SYSTEMID = 1230
DATESTR = '%m/%d/%Y'
STARTDATE = datetime(2002, 9, 1, 0, 0)
STARTSTR = STARTDATE.strftime(DATESTR)
STARTTIME = (time.mktime(pytz.UTC.localize(STARTDATE).utctimetuple())
             - time.timezone)  # 1030838400.0
ENDDATE = datetime(2007, 9, 1, 0, 0)
ENDSTR = ENDDATE.strftime(DATESTR)
ENDTIME = (time.mktime(pytz.UTC.localize(ENDDATE).utctimetuple())
           - time.timezone)  # 1188604800.0
AGGREGATE = 'daily'


@app.route('/', methods=['GET', 'POST'])
@app.route(
    '/<apikey>/<int:systemid>/<float:startdate>/<float:enddate>/<aggregate>',
    methods=['GET', 'POST']
)
def hello(apikey=None, systemid=SYSTEMID, startdate=STARTTIME,
    enddate=ENDTIME, aggregate=AGGREGATE):
    if request.method == 'GET':
        kwargs = {'title': 'NREL PVDAQ'}
        if apikey is not None:
            params = {'api_key': apikey}
            # convert timetuples to MM/DD/YYYY
            startdate = time.strftime(DATESTR, time.gmtime(startdate))
            enddate = time.strftime(DATESTR, time.gmtime(enddate))
            params.update(
                system_id=systemid, start_date=startdate, end_date=enddate,
                aggregate=aggregate
            )
            r = requests.get('%s.json' % URL, params=params)
            if r.ok:
                outputs = r.json()['outputs']
                headers, outputs = outputs[0], outputs[1:]
                data = {h: dat for h, dat in zip(headers, zip(*outputs))}
                df = pd.DataFrame(data)
                df = df.set_index('measdatetime')
                plot = figure(title='system id: %d' % systemid,
                              x_axis_type="datetime",
                              plot_width=1000, plot_height=750)
                dt = df.index.to_datetime()
                color_palette = d3['Category20'][len(headers)-2]
                for h, c in zip(headers, color_palette):
                    if h in ['measdatetime', 'system_id']:
                        continue
                    plot.line(dt, df[h], legend=h, color=c)
                plot.legend.click_policy="hide"
                plot_script, plot_div = components(plot)
                kwargs.update(plot_script=plot_script, plot_div=plot_div)
            else:
                errors = r.json()['errors']
                flash(errors, 'error')
        return render_template('hello.html', **kwargs)
    elif request.method == 'POST':
        apikey = request.form.get('apikey')
        systemid = request.form.get('systemid', SYSTEMID)
        # if system id isn't an integer then set it to the default
        try:
            systemid = int(systemid)
        except ValueError:
            systemid = SYSTEMID
        startdate = request.form.get('startdate', STARTSTR)
        # if start date isn't in MM/DD/YYYY then use the default
        try:
            startdate = datetime.strptime(startdate, DATESTR)
        except ValueError:
            startdate = STARTDATE
        startdate = pytz.UTC.localize(startdate)  # convert to UTC
        # calculate the unicode time (seconds since the epoch) in UTC
        startdate = time.mktime(startdate.utctimetuple()) - time.timezone
        enddate = request.form.get('enddate', ENDSTR)
        # if start date isn't in MM/DD/YYYY then use the default
        try:
            enddate = datetime.strptime(enddate, DATESTR)
        except ValueError:
            enddate = ENDDATE
        enddate = pytz.UTC.localize(enddate)  # convert to UTC
        # calculate the unicode time (seconds since the epoch) in UTC
        enddate = time.mktime(enddate.utctimetuple()) - time.timezone
        aggregate = request.form['aggregateFormControlSelect'] or AGGREGATE
        comma_seperated = request.form.get('commaSeparatedCheck')
        if comma_seperated:
            params = {'api_key': apikey}
            # convert timetuples to MM/DD/YYYY
            startdate = time.strftime(DATESTR, time.gmtime(startdate))
            enddate = time.strftime(DATESTR, time.gmtime(enddate))
            params.update(
                system_id=systemid, start_date=startdate, end_date=enddate,
                aggregate=aggregate
            )
            r = requests.get('%s.csv' % URL, params=params)
            if r.ok:
                f = BytesIO(r.content)
                f.seek(0)
                return send_file(
                    f, attachment_filename="%s.csv" % systemid,
                    as_attachment=True
                )
        kwargs = {'apikey': apikey, 'systemid': systemid,
                  'startdate': startdate, 'enddate': enddate,
                  'aggregate': aggregate}
        return redirect(url_for('hello', **kwargs))
    abort(404)
    abort(Response('Hello'))


if __name__ == '__main__':
    app.run(debug=True)
