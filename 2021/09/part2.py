import copy
import sys
import re

inFile = './testInput.txt'
# inFile = './input.txt'

## True if the first coordinate pair is LOWER than the 2nd
def compare2Spots(y,x,y1,x1):
    #print(y,x,y1,x1)
    if caveFloor[y][x] < caveFloor[y1][x1]:
        return True
    else:
        return False

## j is vertical - row - YAxis
## i is horizonral - column - Xaxis
def isSpotLowest(j,i):
    ##check up
    if j >= 1:
        if not compare2Spots(j,i,j-1,i):
            return False

    ## check down
    if j < caveYAxis - 1:
        if not compare2Spots(j,i,j+1,i):
            return False

    ## Check Left
    if i >= 1:
        if not compare2Spots(j,i,j,i-1):
            return False

    ## Check Right
    if i < caveXAxis - 1:
        if not compare2Spots(j,i,j,i+1):
            return False

    return True





caveFloor=[]
with open(inFile, 'r') as fh:
    for line in fh:
        caveFloor.append([int(x) for x in str(line.strip())])
caveXAxis=len(caveFloor[0])
caveYAxis=len(caveFloor)
risk=0
for j in range(caveYAxis):
    for i in range(caveXAxis):
        if isSpotLowest(j,i):
            risk+=caveFloor[j][i] + 1


print("CaveFloor : ", caveFloor)
print("Cave floor width : ",caveXAxis)
print("Cave floor depth : ", caveYAxis)
print("Risk  ", risk)