import sys
import re

def oneDay(oldShoal):
    newShoal = []
    babyFishes = []
    for fish in oldShoal:
        if fish == 0:
            babyFishes.append(8)
            newShoal.append(6)
        elif fish > 0 and fish < 9:
            newShoal.append(fish - 1)
        else:
            print("something went wrong, this fish is " , fish)
            exit(1)
    newShoal.extend(babyFishes)
    return newShoal

inFile = './testInput.txt'
#inFile = './input.txt'
file = open(inFile)
line = file.read().split(",")
file.close()

NUM_DAYS = 18

shoal = []
for item in line:
    shoal.append(int(item))


print(shoal)

for i in range(NUM_DAYS):
    shoal = oneDay(shoal)
    print(shoal)
    print("Day ",i, " passes")
    print("Number of fish: ", len(shoal))
