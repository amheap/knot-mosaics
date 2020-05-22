#!/bin/bash

# this script takes results from running countcrossings.sh and puts them into the database for the website in the correct format
# takes as input the output from coutcrossings.sh, the mosaic number, then the number of tiles of the layout
# run example:     ./addResultsToWebsite 7_1 7 27
# NOTE this script creates a copy of the csv file for the website as a backup (allKnots.csv.bak), TRY NOT TO MESS UP
# changing format
sed 's/, /,/g' $1 | sed 's/ /,/g' |  sed 's/\[/"/' | sed 's/\]/"/' > temp1.tmp
# making backup and adding info on layout used
cp ~/researchwork/git/knot-mosaics/websiteFunctions/flaskApp/allKnots.csv ~/researchwork/git/knot-mosaics/websiteFunctions/flaskApp/allKnots.csv.bak
sed "s/$/,$2,$3/" temp1.tmp >> ~/researchwork/git/knot-mosaics/websiteFunctions/flaskApp/allKnots.csv

rm temp1.tmp

