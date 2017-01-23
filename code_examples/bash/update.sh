#!/bin/bash
# This bash script sorts through a set of folders 
# it grabs the name of the folder
# then, it copies the csv file within the folder 
# that file is copied and renamed based on the name of the folder


# This is where I want my script to start.
TOP_DIR=~/repos/stressdata
NEW_DIR=~/repos/stressdata2

# this is where we want the files to end up
DEST_DIR=~/repos/stress
cd $TOP_DIR


# This is what the target CSV filename looks like
FILE_PAT="Data_Export.csv"

# Find all directories here - that are at least 1 level down, but don't go any 
# further than 1 directory.
# Go into those directories and pull the repository.

shopt -s extglob

# delete all of the spaces in the directory names
for d in $TOP_DIR; do
  nospace=$d|sed -e s/\ //
  echo "$nospace"
  #cp -r $d "$nospace"
done

# deal with month based numbers
monthpaths=$(find $NEW_DIR -name '*month' -type d) 

echo "month paths $monthpaths"

for d in "$monthpaths"; do
  f=$(find $d -name "$FILE_PAT" -type f)
  n=$d|sed -e s/\ month//
  newname="$n.csv"
  echo "renamed month csv = $newname"
  done

# deal with year based numbers
yearpaths=$(find $TOP_DIR -name '*year*' -type d) 
echo "year paths $yearpaths"
for d in "$yearpaths"; do
  echo "found year directory = $d"
  for f in $d/$FILE_PAT; do
    declare -i n
    n=$d|sed -e s/\ year//
    echo $n
    declare -i m
    m=$(( 12 * $n ))
    newname="$m.csv"
    echo "renamed year csv = $newname"
    done
  done

cd $TOP_DIR

