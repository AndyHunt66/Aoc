import re

inFile = './input.txt'


def printrobots(robotspos):
    telltale = '**********'
    tentative = False
    fieldmap = [ ['.'] * FieldX for i in range(FieldY)]
    for printrobot in robotspos:
        fieldmap[printrobot[1]][printrobot[0]] = '*'
    for line in fieldmap:
        picstring = "".join(line)
        if picstring.count(telltale) > 0:
            tentative = True
    if tentative:
        for line in fieldmap:
            picstring = "".join(line)
            print(picstring)
        print("After {:d} seconds ".format(seconds))
        input("Press Enter to continue...")


FieldX = 101
FieldY = 103
robots = []

f = open(inFile, 'r')

for robot in f.readlines():
    x, y, dx, dy = map(int, re.findall(r'-?\d+', robot))
    robots.append([x, y, dx, dy])


seconds = 0
while True:
    seconds = seconds + 1
    for robot in robots:
        robot[0] = (robot[0] + robot[2]) % FieldX
        robot[1] = (robot[1] + robot[3]) % FieldY
    printrobots(robots)

