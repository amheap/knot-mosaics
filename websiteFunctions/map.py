def website(V):
  import numpy as np
  import math
  import isSuitConnected as sc
  import dowker2 as dt
  import subprocess
  import shlex
  V = np.array(V);
  size = int(math.sqrt(len(V)));
  M = V.reshape(size,size);
  connect = sc.isconnected(M);
  ##print(connect)
  if connect == "False":
    return "This is not suitably connected."
  else:
    listnotation = dt.dowker2(M);
    notation = [str(x) for x in listnotation];
    inpt = " ".join(notation);
    #print(inpt)
    if inpt == 'link':
      return "Link"
    else:
      reducedDT = subprocess.Popen(['./webrunshellDT', inpt], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
      stdout,stderr = reducedDT.communicate();
      stdout = str(stdout);
      stdout = str(stdout[4:-5]);
      #print(stdout)
      reduced = stdout.replace(" ", "");
      #print(reduced)
      reduced = "[" + reduced.strip() + "]";
      #print(reduced)
      if reduced == "'com'":
        return "Composite"
      else:
        finder = subprocess.Popen(['./webidentifyknot', reduced], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout,stderr = finder.communicate();
        stdout = str(stdout);
        stdout = stdout[2:-4];
        #print(stdout)
        return stdout
