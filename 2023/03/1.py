# https://adventofcode.com/2023/day/3

import re

# inFile = './testInput.txt'
inFile = './input.txt'

def checkHalo(halo):
    for point in halo:
        if (grid[point[1]][point[0]] != '.') and not grid[point[1]][point[0]].isdigit():
            return True


grid = [line.strip() for line in open(inFile, 'r').readlines()]
numbers = [[x for x in re.split('\D', "".join(line)) if x != ''] for line in grid]

goodNumbers = []
print(grid)
for lineNumber, line in enumerate(numbers):
    lastPos = 0
    for number in line:
        halo = []
        pos = grid[lineNumber][lastPos::].find(number) + lastPos
        for loop in range(0,len(number)):
            halo.extend( [(x, y) for x, y in [(pos + loop + i, lineNumber + j) for i in (-1, 0, 1) for j in (-1, 0, 1)
                                     if (i != 0 or j != 0)
                                    and (pos + loop + i >= 0 and lineNumber + j >= 0)
                                    and (pos + loop + i < len(grid[lineNumber]) and lineNumber + j < len(grid))]] )

        print(halo)
        if checkHalo(halo):
            goodNumbers.append(int(number))
        lastPos = pos + len(number)
print(goodNumbers)
print(sum(goodNumbers))
print(len(goodNumbers))
