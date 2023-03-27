# knot-mosaics

This repository contains the work done by Dr. Aaron Heap, Dr. Doug Baldwin, and their students, James Canning and Greg Vinal, at SUNY Geneseo.
In the main directory are the files used to run the pipeline that finds all possible knot mosaics on a given layout.
The websiteFunctions/flaskApp directory contains all the files needed to run the Knot Mosaic Maker website.
The pythonFiles directory contains files used to draw knots.
The shellfindFiles directory contains dummy files used for runshellfind.

## Knot Tables

*************************************
NOTE: The tables of knots that that are included in the 'tables' directory go up to crossing number 13. Tables that contain knots with larger crossing number are too large for this github repository to store. Here's a link to the full table with crossing number 0 to 16:

https://drive.google.com/file/d/1kLz41m4Ywb4vtOfes6FPxPv2YjkG5Bch/view?usp=sharing

This file can also be found in compressed gzip format at `websiteFunctions/flaskApp/knotTable0-16.gz`.
*************************************

## Flask Website

### Docker

We're having success with `docker run --rm -p 5000:5000 --name knot-mosaics --read-only --tmpfs /app/shellfindFiles --tmpfs /tmp knot-mosaics` and the included Dockerfile.

#### Running Docker Container in Azure App Service using Azure Container Registry (ACR)

1. `docker build --tag knot-mosaics .` to build a new image for your working copy.
2. `docker login {acr name}.azurecr.io` to authenticate to your Azure Container Registry. (Use ACR Acces Keys, or alternative method.)
3. `docker tag knot-mosaics {acr name}.azurecr.io/knot-mosaics` to tag your image with your Azure Container Registry URL.
4. `az acr login --name {acr name}` to use the Azure CLI to authenticate to your ACR.
5. `docker push --all-tags {acr name}.azurecr.io/knot-mosaics` to push all your tagged knot-mosaics images to Azure.
6. Update your App Service instance to use the new image you just pushed.

## Pipeline

How to start a new pipeline
In main directory copy the base_dt_make and basePipe files into new files
Ex: 
cp base_dt_make 7-31_dt_make
cp basePipe 7-31Pipe

Edit the top of the new dt_make file to specify layout and minimum crossing number 

vi 7-31_dt_make ~ or open with whatever text editor you prefer
choose the layout, written as a string of the form 'mosiacSize-numberTiles'
options are defined in layoutDict below
layout = '7-31'

choose the minimum crossing number of knots you're looking for
minCrossings = 9

Choose which knots you want to identify with the identifyKnot file
Copy the baseIdentifyKnot file and change which table it uses
cp baseIdentifyKnot identifyKnot7-16

Edit the new identifyKnot file:
table=tables/knotTable0-16
-- this might involve creating a table that has only the knots you want to search for. The runtime is reduced by leaving out the smaller knots so that it doesn't waste time and memory writing the unknot to the output millions of times. To do this just copy one of the existing knotTables and delete the lines you don't want



Edit the new Pipe file to reference the new dt_make file, and the appropriate identifyKnot file

## This runs all the programs into each other

## change the dt_make file and the identifyKnot file to the ones you want
./7-31_dt_make | ./runshellfindDT | ./identifyKnot7-16

Open a new screen: screen -S _nameOfScreen_
Or open a previous screen: screen -r _nameOfScreen_

Start the pipeline
time ./7-31Pipe > Results/_nameOfOutputFile_
_nameOfOutputFile_ ~ whatever name you choose
Ex: time ./7-31Pipe > Results/full7-31
Detach screen 
Press ctrl+a then d. Pipeline will continue running on the screen
Doing this will create a new file in the Results/ directory with whatever name you chose. While the pipeline is running you can access the current results in that file with any linux commands without harming the run at all
To go back to a screen type :
	screen -r _nameOfScreen_
Search for a knot in a finished or unfinished run
If your pipeline is outputting to a file called full7-31 for example, you can search to see if a knot has been found using grep.
Ex:
grep 11a_493 full7-31
If this knot has not been found, it will return nothing. If the knot has been found, it will return every line with that knot name. This might be excessive. To only get the first few results, pipe the grep output into the head command.
grep 11a_493 full7-31 | head

Get unique knots and number of crossings from a run
If a run has finished (or even if it hasn't and you just want to check the progress), the script called countCrossings.sh will find each unique knot from the output with the fewest crossings in its diagram. Use in the following format:

./countCrossings.sh _fileWithPipelineOutput_ _crossingFile_
Where _crossingFile_ is whatever you choose to name it. If this file doesn't exist already it will be created. Ex:
./countCrossings.sh full7-31 crossings/7-31
This might take a while, finishing within a couple hours at most, usually a few minutes

Add results to the website 
After a run has finished and you have run countCrossings.sh to get the crossing file, you can run the script addResultsToWebsite.sh to add these results to the website csv
This script is in the following directories: 
/Results/crossings/ 
Here is the format to run addResultsToWebsite.sh. Type the following with spaces in between:
The script (./addResultsToWebsite.sh)
The file containing the results from countCrossings.sh
The mosaic number of the layout used
The number of tiles in the layout
Example: 
	./addResultsToWebsite.sh 7_1 7 27

This script will adjust the format of the results and add them to the end of allKnots.csv in the following directory: websiteFunctions/flaskApp/
It will also save a backup csv before adding the new ones as allKnots.csv.bak in case you make a mistake. This backup will be overwritten the next time you run addResultsToWebsite.sh unless you rename it.
Restart a run that has stopped
Copy the base_dt_make.startup file into a new file name
Ex: 
cp base_dt_make.startup 7-31_dt_make.startup
cp basePipe 7-31Pipe.startup
Find the last output vector of the run before it stopped
Ex:
tail -n 1 full7-31
~returns: 9n_1, 9_44, [10,8,9,7,10,7,7,9,10,10,9,10,9,10,8,7,8]
Edit the top of the new dt_make.startup file to specify layout and minimum crossing number, and define start1 and start2 variables based on the last outputted vector
In this case

Edit the new Pipe file to reference the new dt_make file, and the appropriate identifyKnot file

## This runs all the programs into each other

## change the dt_make file and the identifyknot file to the ones you want
./7-31_dt_make | ./runshellfindDT | ./identifyAllKnots


Run the website
You need to have Flask installed in your version of python
Go to knot-mosaics/websiteFunctions/flaskApp/ directory and run 
python simple.py
I usually do this on a separate screen named website so it stays running and I can detach from the screen
This sets the website running on port 5000. To see it, open a web browser and go to 
localhost:5000

Drawing Knots
Use the draw_knots.py file to create images of mosaics. This can take a csv file and draw all those knots, or take an individual knot mosaic and draw that. Drawing functions are defined in mosaic_drawing.py
NOTE: The csv file used must be of a specific column format (or you have to change the Python code a little). That format is:
(OtherName)  |  Name  |  Vector  |  Crossings  |  Mosaic  |  TileNum
The OtherName column can be given any name, it is not used. This format is the same as the one used in the website's knot database, allKnos.csv

