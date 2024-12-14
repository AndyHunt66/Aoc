from collections import defaultdict
import re

inFile = './input.txt'


def printRobots(robotsPos):
    telltale = '**********'
    tentative = False
    fieldMap = [ ['.'] * FieldY for i in range(FieldX)]
    for robot in robotsPos:
        fieldMap[robot[0]][robot[1]] = '*'
    for line in fieldMap:
        picString = "".join(line)
        # print(picString)
        if picString.count(telltale) > 1:
            tentative = True
    if tentative:
        for line in fieldMap:
            picString = "".join(line)
            print(picString)
        input("Press Enter to continue...")

FieldX = 101
FieldY = 103
robots = []

f = open(inFile, 'r')

for robot in f.readlines():
    x,y,dx,dy = map(int, re.findall(r'-?\d+',robot))
    robots.append([x,y,dx,dy])
    endPos = 0

seconds = 0
while True:
    seconds = seconds + 1
    print("After {:d} seconds ".format(seconds))
    for robot in robots:
        robot[0] = (robot[0] + robot[2]) % FieldX
        robot[1] = (robot[1] + robot[3]) % FieldY
    printRobots(robots)

