# https://adventofcode.com/2023/day/3

import re

# inFile = './testInput.txt'
inFile = './input.txt'


def checkHalo(halo):
    isValid = False
    for point in halo:
        if (grid[point[1]][point[0]]) == '*':
            return (True, point)
        if (grid[point[1]][point[0]] != '.') and not grid[point[1]][point[0]].isdigit():
            isValid = True
    return isValid


grid = [line.strip() for line in open(inFile, 'r').readlines()]
numbers = [[x for x in re.split('\D', "".join(line)) if x != ''] for line in grid]

goodNumbers = []
gears = {}
print(grid)
for lineNumber, line in enumerate(numbers):
    lastPos = 0
    for number in line:
        halo = []
        pos = grid[lineNumber][lastPos::].find(number) + lastPos
        for loop in range(0, len(number)):
            halo.extend([(x, y) for x, y in [(pos + loop + i, lineNumber + j) for i in (-1, 0, 1) for j in (-1, 0, 1)
                                             if (i != 0 or j != 0)
                                             and (pos + loop + i >= 0 and lineNumber + j >= 0)
                                             and (pos + loop + i < len(grid[lineNumber]) and lineNumber + j < len(
                    grid))]])

        print(halo)
        haloCheck = checkHalo(halo)
        if type(haloCheck) is bool and haloCheck:
            goodNumbers.append(int(number))
        elif type(haloCheck) is tuple:
            goodNumbers.append(int(number))
            if haloCheck[1]  in gears.keys():
                gears[haloCheck[1]].append((int(number)))
            else:
                gears[haloCheck[1]] = []
                gears[haloCheck[1]].append((int(number)))


        lastPos = pos + len(number)
print(goodNumbers)
print(sum(goodNumbers))
print(len(goodNumbers))
gearRatios=[]
for key, value in gears.items():
    if len(value) == 2:
        gearRatios.append(value[0]*value[1])

print(sum(gearRatios))