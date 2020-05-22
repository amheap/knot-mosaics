#!/bin/bash
# takes the full results from a pipeline and outputs the unique knots with the fewest crossings
# takes two areguments: first is full pipeline output, second is file to output results to
# run example:    ./countcrossings.sh full7_9 crossings/7_9

# count number of 9s and 10s in each vector
cat $1 | awk '{ print $3; }' | tr -d -c '9|1\n' | awk '{ print length; }' > temp.tmp
# combine number of crossings with full pipeline output
paste -d " " $1 temp.tmp > temp2.tmp
# sort by number of crossings to get unique knots 
cat temp2.tmp | sort -t" " -k4,4 -n | awk '!_[$2]++' > temp3.tmp
mv temp3.tmp $2
rm temp.tmp
rm temp2.tmp
