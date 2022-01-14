import copy
import sys
import re

# inFile = './testInput.txt'
inFile = './input.txt'

def runOneStep(octopi):
    numFlashes = 0
    for row in range(len(octopi)):
        for octopus in range(len(octopi[row])):
            octopi[row][octopus] += 1
    done = False
    while done is False:
        done = True
        for row in range(len(octopi)):
            for octopus in range(len(octopi[row])):
                if octopi[row][octopus] > 9:
                    done = False
                    # flash()
                    # Top Row
                    if row - 1 >= 0:
                        if octopus - 1 >= 0 and octopi[row-1][octopus-1] != 0:
                            octopi[row-1][octopus-1] += 1
                        if octopi[row-1][octopus] != 0:
                            octopi[row-1][octopus] += 1
                        if octopus + 1 < len(octopi[row]) and octopi[row-1][octopus+1] != 0:
                            octopi[row-1][octopus+1] += 1
                    # Middle Row
                    if octopus - 1 >= 0 and octopi[row][octopus-1] != 0:
                        octopi[row][octopus-1] += 1
                    octopi[row][octopus] = 0
                    numFlashes += 1
                    if octopus + 1 < len(octopi[row]) and octopi[row][octopus+1] != 0:
                        octopi[row][octopus+1] += 1
                    # Bottom Row
                    if row + 1 < len(octopi):
                        if octopus - 1 >= 0 and octopi[row+1][octopus-1] != 0:
                            octopi[row+1][octopus-1] += 1
                        if octopi[row+1][octopus] != 0:
                            octopi[row+1][octopus] += 1
                        if octopus + 1 < len(octopi[row]) and octopi[row+1][octopus+1] != 0:
                            octopi[row+1][octopus+1] += 1
    return numFlashes

octopi = []
with open(inFile, 'r') as fh:
    for line in fh:
        octopi.append([int(x) for x in str(line.strip())])

numFlashes = 0
firstFullFlash = 0
for i in range(1000):
    newFlashes = runOneStep(octopi)
    print("New Flashes: ", newFlashes)
    numFlashes += newFlashes
    if newFlashes == len(octopi) * len(octopi[0]):
        firstFullFlash = i
        print("First Full Flash : ", i+1)
        exit()
    # for row in octopi:
    #     for octopus in row:
    #         print(octopus, end="")
    #     print()
    # print("-------------------------")

print("number of Flashes : ", numFlashes)
# for row in octopi:
#     for octopus in row:
#         print(octopus, end="")
#     print()



