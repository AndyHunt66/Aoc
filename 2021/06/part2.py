import sys
import re


def oneDay(oldShoal):
    newShoal = {0:oldShoal[1],1:oldShoal[2],2:oldShoal[3],3:oldShoal[4],4:oldShoal[5],5:oldShoal[6],6:oldShoal[7]+oldShoal[0],7:oldShoal[8],8:oldShoal[0]}
    return newShoal

def numFish(shoal):
    numFishes = 0
    for j in iter(shoal):
        numFishes += shoal[j]
    return numFishes

#inFile = './testInput.txt'
inFile = './input.txt'
file = open(inFile)
line = file.read().split(",")
file.close()

NUM_DAYS = 256

shoal = {0:0,1 : 0, 2:0,3:0,4:0,5:0,6:0,7:0,8:0}

for item in line:
    shoal[int(item)] = shoal[int(item)] + 1

print(sorted(shoal))
print(shoal)

for i in range(NUM_DAYS ):
    shoal = oneDay(shoal)
    print(shoal)
    print("Day ",i, " passes")
    print("Number of fish: ", numFish(shoal))


