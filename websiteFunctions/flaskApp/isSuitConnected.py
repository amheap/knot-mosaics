# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:41:27 2019

@author: Greg Vinal
"""
def isconnected(K):
### Given the matrix of a knot mosaic, we need to tell if it is suitably connected before we do anything. ###
     import numpy as np  ### Some setup ###
     length = len(K)
     truth = True
     ### Here, we are sorting the tiles into the types: for each side we need to tell if it has a strand leaving it (on) or not (off) ###
     lefton   = [1,4,5,7,8,9,10]
     leftoff  = [0,2,3,6]
     righton  = [2,3,5,7,8,9,10]
     rightoff = [0,1,4,6]
     upon     = [3,4,6,7,8,9,10]
     upoff    = [0,1,2,5]
     downon   = [1,2,6,7,8,9,10]
     downoff  = [0,3,4,5]
     ###Now, we take the matrix K and wrap it on all sides with 0's.###
     topper = np.zeros((1,length))
     sides = np.zeros((length+2,1))
     ontop = np.append(topper,K,axis = 0)
     tandb = np.append(ontop,topper, axis = 0)
     lefttandb = np.append(tandb,sides, axis = 1)
     newK = np.append(sides,lefttandb, axis = 1)
     ### We can finally start iterating. The premise here is simple:        ###
     ### if a tile has the right side leaving it, the one on its right      ###
     ### should also have a strand leaving it, similarly with ups and downs ###
     for i in range(length + 1):
         for j in range(length + 1):
             if newK[i,j] in rightoff and newK[i,j+1] in lefton:
                     truth = False
             elif newK[i,j] in righton and newK[i,j+1] in leftoff:
                     truth = False
             if newK[j,i] in downoff and newK[j+1,i] in upon:
                     truth = False
             elif newK[j,i] in downon and newK[j+1,i] in upoff:
                     truth = False
     return truth
