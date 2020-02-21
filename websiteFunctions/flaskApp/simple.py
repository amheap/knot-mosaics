from flask import Flask, render_template, request, redirect
import numpy as np
import math
import isSuitConnected as sc
import dowker2 as dt
import subprocess
import shlex
import pandas as pd

app = Flask(__name__)

# defining the layout vectors used in returning a specified knot
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

layoutDict = {27:m7_27, 29:m7_29, 31:m7_31, 34:m7_34, 36:m7_36 }

@app.route('/')
def home():
  return render_template("webpage1.html")


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
    min1 = request.form['minOpt1']
    min2 = request.form['minOpt2']
    min3 = request.form['minOpt3']
    # check if nothing is submitted in the form
    if knotName == '': return render_template('webpage1.html', answer='Please specify a knot')
    #df = pd.read_csv("7_1FormatTest.csv")
    df = pd.read_csv("all7x7.csv")
    df = df.sort_values([min1, min2, min3])
    mask = df.Name == knotName
    if not mask.any(): return render_template('webpage1.html', answer='The knot you submitted was not found')
    vector = df[mask].Vector.get_values()[0]
    tileNum = df[mask].TileNum.get_values()[0]
    mosaicNum = df[mask].Mosaic.get_values()[0]
    print(vector)
    vector = np.fromstring(vector ,dtype=int, sep=',')
    
    m1= layoutDict[tileNum].copy()
    m1[m1 == -1] = vector 
    vv = m1.flatten()
    stringMatrix = np.array2string(vv, separator=',').replace('[','').replace(']','').replace(' ','')
    ans = str(mosaicNum) + '-' + str(tileNum) + " layout, " + knotName
    return render_template('webpage1.html', matrix=stringMatrix, answer=ans, knotName=knotName)
  #******
  #Second Part
  #******
  Vorig = request.form['vector'];
  V = Vorig.split(",");
  V = [int(x) for x in V];
  V = np.array(V);
## checks if the mosaic is empty
  if np.sum(V) == 0:
    ans = "not suitably connected."
    return render_template('webpage1.html', answer=ans)
  size = int(math.sqrt(len(V)));
  M = V.reshape(size,size);
  #return "<p>"+str(M)+"</p>"
  connect = sc.isconnected(M);
  #print(connect)
  if not connect:
    ans = "not suitably connected."
    return render_template('webpage1.html', answer=ans, matrix=Vorig)
  else:
    listnotation = dt.dowker2(M);
    notation = [str(x) for x in listnotation];
    #print(listnotation)
    print(notation)
    if listnotation == [0, 0]:
      ans = "the unknot"
      return render_template('webpage1.html', answer=ans, matrix=Vorig)
    inpt = " ".join(notation);
    print(inpt)
    if inpt == 'l i n k':
      ans = "This is a link."
      return render_template('webpage1.html', answer=ans, matrix=Vorig)

    else:
      reducedDT = subprocess.Popen(['./webrunshellDT', inpt], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
      stdout,stderr = reducedDT.communicate();
      stdout = str(stdout);
      print(stdout)
      if stdout[2:-3] == "comp":
        ans = "This is a composite knot"
        return render_template('webpage1.html', answer=ans, matrix=Vorig)
      elif stdout[2:-3] == "unknot":
        ans = "the unknot."
        return render_template('webpage1.html', answer=ans, matrix=Vorig)


      stdout = str(stdout[4:-5]);
      print(stdout)
      reduced = stdout.replace(" ", "");
      print(reduced)
      reduced = "[" + reduced.strip() + "]";
      print(reduced)
      if reduced == "'com'":
        ans = "the unknot"
        return render_template('webpage1.html', answer=ans, matrix=Vorig)
      else:
        finder = subprocess.Popen(['./webidentifyknot', reduced], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout,stderr = finder.communicate();
        stdout = str(stdout);
        stdout = stdout[2:-4];
        #print(stdout)
        #return stdout
        return render_template('webpage1.html', answer=stdout, matrix=Vorig)


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0")
