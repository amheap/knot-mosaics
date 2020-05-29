from flask import Flask, render_template, request, redirect
import numpy as np
import math
import isSuitConnected as sc
import dowker2 as dt
import subprocess
import shlex
import pandas as pd
import re #for regex

app = Flask(__name__)

df = pd.read_csv("allKnots.csv")
knownKnots = sorted(df.Name.unique())
# defining the layout vectors used in returning a specified knot
# the m4_12 layout isn't really a layout, just a placeholder for the 3_1 knot
m4_12 = np.zeros([4,4]).astype('int') - 1
m5_17 = np.array([[ 0,  2,  1,  0,  0],
 [ 2, -1, -1,  1,  0],
 [ 3, -1, -1, -1,  1],
 [ 0,  3, -1, -1,  4],
 [ 0,  0,  3,  4,  0]])
m6_22 = np.array([[ 0,  2,  1,  0,  0,  0],
 [ 2, -1, -1,  1,  0,  0],
 [ 3, -1, -1, -1,  1,  0],
 [ 0,  3, -1, -1, -1,  1],
 [ 0,  0,  3, -1, -1,  4],
 [ 0,  0,  0,  3,  4,  0]])
m6_24 = np.array([[ 0,  0,  2,  1,  0,  0],
 [ 0,  2, -1, -1,  1,  0],
 [ 2, -1, -1, -1, -1,  1],
 [ 3, -1, -1, -1, -1,  4],
 [ 0,  3, -1, -1,  4,  0],
 [ 0,  0,  3,  4,  0,  0]])
m6_27 = np.array([[ 0,  2,  1,  2,  1,  0],
 [ 2, -1, -1, -1, -1,  1],
 [ 3, -1, -1, -1, -1,  4],
 [ 0,  3, -1, -1, -1,  1],
 [ 0,  0,  3, -1, -1,  4],
 [ 0,  0,  0,  3,  4,  0]])
m6_32 = np.array([[ 0,  2,  1,  2,  1,  0],
 [ 2, -1, -1, -1, -1,  1],
 [ 3, -1, -1, -1, -1,  4],
 [ 2, -1, -1, -1, -1,  1],
 [ 3, -1, -1, -1, -1,  4],
 [ 0,  3,  4,  3,  4,  0]])
m7_27 = np.array([[ 0,  2,  1,  0,  0,  0,  0],
 [ 2, -1, -1,  1,  0,  0,  0],
 [ 3, -1, -1, -1,  1,  0,  0],
 [ 0,  3, -1, -1, -1,  1,  0],
 [ 0,  0,  3, -1, -1, -1,  1],
 [ 0,  0,  0,  3, -1, -1,  4],
 [ 0,  0,  0,  0,  3,  4,  0]])
m7_29 = np.array([[ 0,  2,  1,  0,  0,  0,  0],
 [ 2, -1, -1,  1,  0,  0,  0],
 [ 3, -1, -1, -1,  1,  0,  0],
 [ 2, -1, -1, -1, -1,  1,  0],
 [ 3, -1, -1, -1, -1,  4,  0],
 [ 0,  3, -1, -1,  4,  0,  0],
 [ 0,  0,  3,  4,  0,  0,  0]]) 
m7_31 = np.array([[ 0,  0,  2,  1,  0,  0,  0],
 [ 0,  2, -1, -1,  1,  0,  0],
 [ 2, -1, -1, -1, -1,  1,  0],
 [ 3, -1, -1, -1, -1, -1,  1],
 [ 0,  3, -1, -1, -1, -1,  4],
 [ 0,  0,  3, -1, -1,  4,  0],
 [ 0,  0,  0,  3,  4,  0,  0]])
m7_32 = np.array([[ 0,  2,  1,  0,  0,  0,  0],
 [ 2, -1, -1,  1,  0,  0,  0],
 [ 3, -1, -1, -1,  1,  0,  0],
 [ 2, -1, -1, -1, -1,  1,  0],
 [ 3, -1, -1, -1, -1, -1,  1],
 [ 0,  3,  4,  3, -1, -1,  4],
 [ 0,  0,  0,  0,  3,  4,  0]])
m7_34 = np.array([[ 0,  2,  1,  0,  0,  0,  0],
 [ 2, -1, -1,  1,  0,  0,  0],
 [ 3, -1, -1, -1,  1,  0,  0],
 [ 2, -1, -1, -1, -1,  1,  0],
 [ 3, -1, -1, -1, -1, -1,  1],
 [ 0,  3, -1, -1, -1, -1,  4],
 [ 0,  0,  3,  4,  3,  4,  0]])
m7_36 = np.array([[ 0,  2,  1,  2,  1,  0,  0],
 [ 2, -1, -1, -1, -1,  1,  0],
 [ 3, -1, -1, -1, -1, -1,  1],
 [ 2, -1, -1, -1, -1, -1,  4],
 [ 3, -1, -1, -1, -1,  4,  0],
 [ 0,  3, -1, -1,  4,  0,  0],
 [ 0,  0,  3,  4,  0,  0,  0]])
m7_37 = np.array([[ 0,  2,  1,  2,  1,  0,  0],
 [ 2, -1, -1, -1, -1,  1,  0],
 [ 3, -1, -1, -1, -1,  4,  0],
 [ 2, -1, -1, -1, -1,  1,  0],
 [ 3, -1, -1, -1, -1, -1,  1],
 [ 0,  3,  4,  3, -1, -1,  4],
 [ 0,  0,  0,  0,  3,  4,  0]])
m7_39 = np.array([[ 0,  2,  1,  2,  1,  0,  0],
 [ 2, -1, -1, -1, -1,  1,  0],
 [ 3, -1, -1, -1, -1,  4,  0],
 [ 2, -1, -1, -1, -1,  1,  0],
 [ 3, -1, -1, -1, -1, -1,  1],
 [ 0,  3, -1, -1, -1, -1,  4],
 [ 0,  0,  3,  4,  3,  4,  0]])
m7_41 = np.array([[ 0,  2,  1,  2,  1,  0,  0],
 [ 2, -1, -1, -1, -1,  1,  0],
 [ 3, -1, -1, -1, -1, -1,  1],
 [ 2, -1, -1, -1, -1, -1,  4],
 [ 3, -1, -1, -1, -1, -1,  1],
 [ 0,  3, -1, -1, -1, -1,  4],
 [ 0,  0,  3,  4,  3,  4,  0]])


layoutDict = {"4-12":m4_12, "5-17":m5_17, "6-22":m6_22, "6-24":m6_24, "6-27":m6_27, "6-32":m6_32, "7-27":m7_27, "7-29":m7_29, "7-31":m7_31, "7-32":m7_32, "7-34":m7_34, "7-36":m7_36, "7-39":m7_39, "7-37":m7_37, "7-41":m7_41}

@app.route('/')
def home():
  #print(knownKnots[:5])
  return render_template("webpage1.html", knotNames=list(knownKnots))


@app.route("/signup", methods = ['POST'])
def signup():
	email = request.form['email']
	#print("The email address is '" + email + "'")
	return redicrect('/')

@app.route("/hello")
def hello():
	return """
<h1>Flask Example</h1>
<ul>
<li><p>Decode</p></li>
<li><p>Form</p></li>
<li><p >get-example</p></li>
</ul>
"""

@app.route("/", methods=['POST'])
def results():
  """
  This function is split into two parts:
  The first for displaying any inputted knot
  The second for taking a mosiac and identifying it
  """
  if list(request.form.keys())[0] == 'knotSearch':
    knotName = request.form['knotSearch']
    knotName = str.strip(knotName)
    # check if nothing is submitted in the form
    if knotName == '': return render_template('webpage1.html', answer='Please specify a knot', knotNames=list(knownKnots))
    # check that the input is of the desired knot-name format ie 'digits(a/n)_digits'
    expectedList = re.findall("^\d+[an]*_\d+$", knotName)
    #print(expectedList)
    if len(expectedList) != 1:
      ans = "Oops! Check the format of your knot name: " + knotName
      return render_template('webpage1.html', answer=ans, knotNames=list(knownKnots), lastSearch=knotName)
    # did they forget the a/n?
    if re.findall("^1[1-6]_", knotName):
      ans = "Need to specify alternating or non-alternating: " + knotName
      return render_template('webpage1.html', answer=ans, knotNames=list(knownKnots), lastSearch=knotName)
    # looking for a knot with crossing number greater than 16?
    if re.findall("^1[7-9]_", knotName):
      ans = "Knots with crossing number greater than 16 have are unknown"
      return render_template('webpage1.html', answer=ans, knotNames=list(knownKnots), lastSearch=knotName)
    min1 = request.form['minOpt1']
    min2 = request.form['minOpt2']
    # set min3 to be the third option that wasn't chosen
    min3 = "Crossings"
    if min3 in [min1, min2]:
      if "Mosaic" in [min1, min2]:
        min3 = "TileNum"
      else:
        min3 = "Mosaic"
    df = pd.read_csv("allKnots.csv")
    df = df.sort_values(by=[min1, min2, min3])
    mask = df.Name == knotName
    if not mask.any(): 
      ans = 'A mosaic for the ' + knotName + ' knot has not yet been discovered'
      return render_template('webpage1.html', answer=ans, knotNames=list(knownKnots), lastSearch=knotName)
    vector = df[mask].Vector.get_values()[0]
    tileNum = df[mask].TileNum.get_values()[0]
    # Check if the tile number is realized (then same with mosaic and crossing)
    if tileNum == df[mask].TileNum.min(): 
      minTile = 'min'
    else: minTile = 'known'
    mosaicNum = df[mask].Mosaic.get_values()[0]
    if mosaicNum == df[mask].Mosaic.min(): 
      minMosaic = 'min'
    else: minMosaic = 'known'
    crossings = df[mask].Crossings.get_values()[0]
    if str(crossings) == re.search("^\d+", knotName).group():
      minCrossing = 'min'
    elif crossings > df[mask].Crossings.min():
      minCrossing = 'known'
    else: minCrossing = 'unknown'
    #print(vector)
    vector = np.fromstring(vector ,dtype=int, sep=',')
    
    m1= layoutDict[str(mosaicNum) + '-' + str(tileNum)].copy()
    m1[m1 == -1] = vector 
    vv = m1.flatten()
    stringMatrix = np.array2string(vv, separator=',').replace('[','').replace(']','').replace(' ','')
    ans = knotName + ', ' + str(mosaicNum) + '-' + str(tileNum) + " layout"
    # A dictionary of all the values used in a response to a searched knot
    resultsDict = {"tiles":tileNum, "mosaic":mosaicNum, "crossings":crossings, "name":knotName, "min1":min1, "min2":min2, "realized":[minTile, minMosaic, minCrossing]}
    return render_template('webpage1.html', matrix=stringMatrix, answer=ans, resultsDict=resultsDict, knotNames=list(knownKnots), lastSearch=knotName)

  #******
  #Second Part
  #******
  Vorig = request.form['vector'];
  V = Vorig.split(",");
  V = [int(x) for x in V];
  V = np.array(V);
  #print(V)
## checks if the mosaic is empty
  if np.sum(V) == 0:
    ans = "Not suitably connected."
    return render_template('webpage1.html', answer=ans, knotNames=list(knownKnots))
  size = int(math.sqrt(len(V)));
  M = V.reshape(size,size);
  #return "<p>"+str(M)+"</p>"
  #print(M)
  connect = sc.isconnected(M);
  #print(connect)
  if not connect:
    ans = "Not suitably connected."
    return render_template('webpage1.html', answer=ans, matrix=Vorig, knotNames=list(knownKnots))
  else:
    listnotation = dt.dowker2(M);
    notation = [str(x) for x in listnotation];
    #print(M)
    #print(listnotation)
    #print(notation)
    if listnotation == [0, 0]:
      ans = "This is the unknot"
      return render_template('webpage1.html', answer=ans, matrix=Vorig, knotNames=list(knownKnots))
    inpt = " ".join(notation);
    #print(inpt)
    if inpt == 'l i n k':
      ans = "This is a link."
      return render_template('webpage1.html', answer=ans, matrix=Vorig, knotNames=list(knownKnots))

    else:
      reducedDT = subprocess.Popen(['./webrunshellDT', inpt], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
      stdout,stderr = reducedDT.communicate();
      stdout = str(stdout);
      #print(stdout)
      if stdout[2:-3] == "comp":
        ans = "This is a composite knot"
        return render_template('webpage1.html', answer=ans, matrix=Vorig, knotNames=list(knownKnots))
      elif stdout[2:-3] == "unknot":
        ans = "This is the unknot."
        return render_template('webpage1.html', answer=ans, matrix=Vorig, knotNames=list(knownKnots))


      stdout = str(stdout[4:-5]);
      #print(stdout)
      reduced = stdout.replace(" ", "");
      #print(reduced)
      reduced = "[" + reduced.strip() + "]";
      #print(reduced)
      if reduced == "'com'":
        ans = "the unknot"
        return render_template('webpage1.html', answer=ans, matrix=Vorig, knotNames=list(knownKnots))
      else:
        finder = subprocess.Popen(['./webidentifyknot', reduced], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout,stderr = finder.communicate();
        #print(stdout)
        stdout = str(stdout);
        stdout = stdout[2:-3];
        return render_template('webpage1.html', answer=stdout, matrix=Vorig, knotNames=list(knownKnots))


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0")
