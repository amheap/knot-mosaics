from flask import Flask, render_template, request, redirect
import numpy as np
import math
import isSuitConnected as sc
import dowker2 as dt
import subprocess
import shlex
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("allKnots.csv")
knownKnots = sorted(df.Name.unique())
# defining the layout vectors used in returning a specified knot
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

layoutDict = {"5-17":m5_17, "6-22":m6_22, "6-24":m6_24, "6-27":m6_27, "6-32":m6_32, "7-27":m7_27, "7-29":m7_29, "7-31":m7_31, "7-32":m7_32, "7-34":m7_34, "7-36":m7_36 }

@app.route('/')
def home():
  print(knownKnots[:5])
  return render_template("webpage1.html", knotNames=list(knownKnots))


@app.route("/signup", methods = ['POST'])
def signup():
	email = request.form['email']
	print("The email address is '" + email + "'")
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
    min1 = request.form['minOpt1']
    min2 = request.form['minOpt2']
    # set min3 to be the third option that wasn't chosen
    min3 = "Crossings"
    if min3 in [min1, min2]:
      if "Mosaic" in [min1, min2]:
        min3 = "TileNum"
      else:
        min3 = "Mosaic"
    # check if nothing is submitted in the form
    if knotName == '': return render_template('webpage1.html', answer='Please specify a knot', knotNames=list(knownKnots))
    #df = pd.read_csv("7_1FormatTest.csv")
    df = pd.read_csv("allKnots.csv")
    df = df.sort_values(by=[min1, min2, min3])
    mask = df.Name == knotName
    if not mask.any(): return render_template('webpage1.html', answer='The ' + knotName + ' knot was not found', knotNames=list(knownKnots))
    vector = df[mask].Vector.get_values()[0]
    #print(df[mask].Crossings.get_values())
    #print(df[mask].TileNum.get_values())
    tileNum = df[mask].TileNum.get_values()[0]
    mosaicNum = df[mask].Mosaic.get_values()[0]
    crossings = df[mask].Crossings.get_values()[0]
    #print(vector)
    vector = np.fromstring(vector ,dtype=int, sep=',')
    
    m1= layoutDict[str(mosaicNum) + '-' + str(tileNum)].copy()
    m1[m1 == -1] = vector 
    vv = m1.flatten()
    stringMatrix = np.array2string(vv, separator=',').replace('[','').replace(']','').replace(' ','')
    ans = knotName + ', ' + str(mosaicNum) + '-' + str(tileNum) + " layout"
    # A dictionary of all the values used in a response to a searched knot
    resultsDict = {"tiles":tileNum, "mosaic":mosaicNum, "crossings":crossings, "name":knotName, "min1":min1, "min2":min2}
    return render_template('webpage1.html', matrix=stringMatrix, answer=ans, resultsDict=resultsDict, knotNames=list(knownKnots))

  #******
  #Second Part
  #******
  Vorig = request.form['vector'];
  V = Vorig.split(",");
  V = [int(x) for x in V];
  V = np.array(V);
## checks if the mosaic is empty
  if np.sum(V) == 0:
    ans = "Not suitably connected."
    return render_template('webpage1.html', answer=ans, knotNames=list(knownKnots))
  size = int(math.sqrt(len(V)));
  M = V.reshape(size,size);
  #return "<p>"+str(M)+"</p>"
  connect = sc.isconnected(M);
  #print(connect)
  if not connect:
    ans = "Not suitably connected."
    return render_template('webpage1.html', answer=ans, matrix=Vorig, knotNames=list(knownKnots))
  else:
    listnotation = dt.dowker2(M);
    notation = [str(x) for x in listnotation];
    #print(listnotation)
    print(notation)
    if listnotation == [0, 0]:
      ans = "This is the unknot"
      return render_template('webpage1.html', answer=ans, matrix=Vorig, knotNames=list(knownKnots))
    inpt = " ".join(notation);
    print(inpt)
    if inpt == 'l i n k':
      ans = "This is a link."
      return render_template('webpage1.html', answer=ans, matrix=Vorig, knotNames=list(knownKnots))

    else:
      reducedDT = subprocess.Popen(['./webrunshellDT', inpt], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
      stdout,stderr = reducedDT.communicate();
      stdout = str(stdout);
      print(stdout)
      print('HERE')
      if stdout[2:-3] == "comp":
        ans = "This is a composite knot"
        return render_template('webpage1.html', answer=ans, matrix=Vorig, knotNames=list(knownKnots))
      elif stdout[2:-3] == "unknot":
        ans = "This is the unknot."
        return render_template('webpage1.html', answer=ans, matrix=Vorig, knotNames=list(knownKnots))


      stdout = str(stdout[4:-5]);
      print(stdout)
      reduced = stdout.replace(" ", "");
      print(reduced)
      reduced = "[" + reduced.strip() + "]";
      print(reduced)
      if reduced == "'com'":
        ans = "the unknot"
        return render_template('webpage1.html', answer=ans, matrix=Vorig, knotNames=list(knownKnots))
      else:
        finder = subprocess.Popen(['./webidentifyknot', reduced], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout,stderr = finder.communicate();
        print(stdout)
        stdout = str(stdout);
        stdout = stdout[2:-4];
        #return stdout
        return render_template('webpage1.html', answer=stdout, matrix=Vorig, knotNames=list(knownKnots))


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0")
