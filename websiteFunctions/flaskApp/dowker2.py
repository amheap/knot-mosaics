def dowker2(M):
    import numpy as np
    ''' Returns the dt notation of a knot mosaic matrix
     :param M - a square numpy array representing a knot mosaic

     :returns finalDT - a list of the dt notation (only even numbers)
    '''
    ### This function finds the first 2 in the knot
    def firsti(M):
        i = -1
        val = 0
        while val == 0:
            i += 1
            val = M.item(i)
        a = i // len(M)
        b = i % len(M)
        return [a, b]
    ## We need to initialize some things to start at the 2 and follow the knot from there
    ## These 5 take care of the walking
    starti = firsti(M)[0]
    startj = firsti(M)[1]
    lastcell = [starti, startj]
    currenti = starti
    currentj = startj + 1
    ## These three take care of the output
    pairs = []
    length = len(M)
    i = 1
    path = [2]
    ## this will take care of links
    tilesvisit = 1
    crosstiles = np.count_nonzero(M==7) + np.count_nonzero(M==8) + np.count_nonzero(M==9) + np.count_nonzero(M==10);
    linknumber = np.count_nonzero(M) + crosstiles;
    ## Nothing interesting happens until 9 & 10
    while [currenti, currentj] != [starti, startj]:
        #if len(path) > length:
        #    return 'link'
        tilesvisit += 1
        path.append(M[currenti, currentj])
        if M[currenti, currentj] == 1 and lastcell == [currenti, currentj - 1]:
            lastcell = [currenti, currentj]
            currenti += 1
        elif M[currenti, currentj] == 1 and lastcell == [currenti + 1, currentj]:
            lastcell = [currenti, currentj]
            currentj += -1
        elif M[currenti, currentj] == 2 and lastcell == [currenti + 1, currentj]:
            lastcell = [currenti, currentj]
            currentj += 1
        elif M[currenti, currentj] == 2 and lastcell == [currenti, currentj + 1]:
            lastcell = [currenti, currentj]
            currenti += 1
        elif M[currenti, currentj] == 3 and lastcell == [currenti, currentj + 1]:
            lastcell = [currenti, currentj]
            currenti += -1
        elif M[currenti, currentj] == 3 and lastcell == [currenti - 1, currentj]:
            lastcell = [currenti, currentj]
            currentj += 1
        elif M[currenti, currentj] == 4 and lastcell == [currenti - 1, currentj]:
            lastcell = [currenti, currentj]
            currentj += -1
        elif M[currenti, currentj] == 4 and lastcell == [currenti, currentj - 1]:
            lastcell = [currenti, currentj]
            currenti += - 1
        elif M[currenti, currentj] == 5 and lastcell == [currenti, currentj - 1]:
            lastcell = [currenti, currentj]
            currentj += 1
        elif M[currenti, currentj] == 5 and lastcell == [currenti, currentj + 1]:
            lastcell = [currenti, currentj]
            currentj += -1
        elif M[currenti, currentj] == 6 and lastcell == [currenti + 1, currentj]:
            lastcell = [currenti, currentj]
            currenti += -1
        elif M[currenti, currentj] == 6 and lastcell == [currenti - 1, currentj]:
            lastcell = [currenti, currentj]
            currenti += 1
        elif M[currenti, currentj] == 7 and lastcell == [currenti + 1, currentj]:
            lastcell = [currenti, currentj]
            currentj += -1
        elif M[currenti, currentj] == 7 and lastcell == [currenti - 1, currentj]:
            lastcell = [currenti, currentj]
            currentj += 1
        elif M[currenti, currentj] == 7 and lastcell == [currenti, currentj + 1]:
            lastcell = [currenti, currentj]
            currenti += -1
        elif M[currenti, currentj] == 7 and lastcell == [currenti, currentj - 1]:
            lastcell = [currenti, currentj]
            currenti += 1
        elif M[currenti, currentj] == 8 and lastcell == [currenti + 1, currentj]:
            lastcell = [currenti, currentj]
            currentj += 1
        elif M[currenti, currentj] == 8 and lastcell == [currenti - 1, currentj]:
            lastcell = [currenti, currentj]
            currentj += -1
        elif M[currenti, currentj] == 8 and lastcell == [currenti, currentj + 1]:
            lastcell = [currenti, currentj]
            currenti += 1
        elif M[currenti, currentj] == 8 and lastcell == [currenti, currentj - 1]:
            lastcell = [currenti, currentj]
            currenti += -1

        ## Here, we need to find which are overcrossings and undercrossings. That's
        ## not too hard. Then, when we hit one of these crossing tiles, we want to take
        ## whatever number we are on, record it, and record the index of where we found
        ## it. Then, later we can match each entry with the same index, and then just take the
        ## tuple of numbers and string them together for our actual DT notation.
        elif M[currenti, currentj] == 9 and lastcell == [currenti, currentj - 1]:
            pairs.append((currenti * length + currentj, i))
            i += 1
            lastcell = [currenti, currentj]
            currentj += 1
        elif M[currenti, currentj] == 9 and lastcell == [currenti, currentj + 1]:
            pairs.append((currenti * length + currentj, i))
            i += 1
            lastcell = [currenti, currentj]
            currentj += -1
        elif M[currenti, currentj] == 9 and lastcell == [currenti + 1, currentj]:
            if i % 2 == 0:
                pairs.append((currenti * length + currentj, -i))
            else:
                pairs.append((currenti * length + currentj, i))
            i += 1
            lastcell = [currenti, currentj]
            currenti += -1
        elif M[currenti, currentj] == 9 and lastcell == [currenti - 1, currentj]:
            if i % 2 == 0:
                pairs.append((currenti * length + currentj, -i))
            else:
                pairs.append((currenti * length + currentj, i))
            i += 1
            lastcell = [currenti, currentj]
            currenti += 1
        elif M[currenti, currentj] == 10 and lastcell == [currenti, currentj - 1]:
            if i % 2 == 0:
                pairs.append((currenti * length + currentj, -i))
            else:
                pairs.append((currenti * length + currentj, i))
            i += 1
            lastcell = [currenti, currentj]
            currentj += 1
        elif M[currenti, currentj] == 10 and lastcell == [currenti, currentj + 1]:
            if i % 2 == 0:
                pairs.append((currenti * length + currentj, -i))
            else:
                pairs.append((currenti * length + currentj, i))
            i += 1
            lastcell = [currenti, currentj]
            currentj += -1
        elif M[currenti, currentj] == 10 and lastcell == [currenti + 1, currentj]:
            pairs.append((currenti * length + currentj, i))
            i += 1
            lastcell = [currenti, currentj]
            currenti += -1
        elif M[currenti, currentj] == 10 and lastcell == [currenti - 1, currentj]:
            pairs.append((currenti * length + currentj, i))
            i += 1
            lastcell = [currenti, currentj]
            currenti += 1

    # This part converts pairs to only the even numbers of the Dowker Notation, 
    # in the correct order
    pairs = np.array(pairs)
    evens = pairs[1::2]
    odds = pairs[::2]
    finalDT = [len(odds), 0]
    crossn = np.count_nonzero(M==9) + np.count_nonzero(M==10)
    if tilesvisit != linknumber:
        finalDT = 'link'
    else:
        for i in range(len(odds)):
            finalDT.append(evens[evens[:,0] == odds[:,0][i]][0][1])
    return finalDT

#A = np.array([[0,2,1,0],[2,9,10,1],[3,10,4,6],[0,3,5,4]])
#print(dowker2(A))
#[0,2,1,0,2,9,10,1,3,10,4,6,0,3,5,4]


## Basically, this program has two parts: the big block of text that's the 'ifelse'
## statements which "walk" along the knot, and the added comments in the 9 & 10 cases
## which output the actual dawker notation.

## The output of this function as it stands is a list of tuples whose first entries are
## the index where each 9 & 10 lives, and secondly where
