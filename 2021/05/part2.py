import sys
import re


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)


class Line(object):
    def __init__(self, startPointInternal, endPointInternal):
        self.startPoint = startPointInternal
        self.endPoint = endPointInternal
        self.allPoints = []
        incrementer = 1
        self.type = ""
        if startPointInternal == endPointInternal:
            self.type = "point"
        elif startPointInternal.x == endPointInternal.x:
            self.type = "vertical"
            rangeStart = startPointInternal.y
            rangeEnd = endPointInternal.y
        elif startPointInternal.y == endPointInternal.y:
            self.type = "horizontal"
            rangeStart = startPointInternal.x
            rangeEnd = endPointInternal.x
        else:
            self.type = "diagonal"
            rangeStart = startPointInternal.x
            rangeEnd = endPointInternal.x
            yRangeStart = startPointInternal.y
            yRangeEnd = endPointInternal.y
            if yRangeStart > yRangeEnd:
                yIncrementer = -1
            else:
                yIncrementer = 1


        if rangeStart > rangeEnd:
                incrementer = -1
        else:
                incrementer = 1
        for j in range(rangeStart, rangeEnd + incrementer, incrementer):
                if self.type == "horizontal":
                    self.allPoints.append(Point(j, self.startPoint.y))
                elif self.type == "vertical":
                    self.allPoints.append(Point(self.startPoint.x, j))
                elif self.type == "diagonal":
                    self.allPoints.append(Point(self.startPoint.x, self.startPoint.y))
                    self.startPoint.x+=incrementer
                    self.startPoint.y+=yIncrementer



#inFile = './testInput.txt'
inFile = './input.txt'


vents = []
largestX = 0
largestY = 0
seafloor = []
with open(inFile, 'r') as fh:
    for line in fh:
        # 0,9 -> 5,9
        #     pattern = '^([0..9]+),([0-9]+) -> ([0..9]+),([0-9]+)$'
        pattern = '^([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)'
        print(line)
        match = re.search(pattern, line)
        if match:
            startPoint = (Point(match.group(1), match.group(2)))
            endPoint = (Point(match.group(3), match.group(4)))
            thisLine = Line(startPoint, endPoint)
            vents.append(thisLine)
            if largestX < int(match.group(1)):
                largestX = int(match.group(1))
            if largestX < int(match.group(3)):
                largestX = int(match.group(3))
            if largestY < int(match.group(2)):
                largestY = int(match.group(2))
            if largestY < int(match.group(4)):
                largestY = int(match.group(4))

for i in range(largestX+1):

    yArray = []
    for thisY in range(largestY+1):
        yArray.append(0)
    seafloor.append(yArray)
print("Largest X ", largestX)
print("Largest Y ", largestY)

print(len(seafloor))

for vent in vents:
    for point in vent.allPoints:
        seafloor[point.x][point.y] += 1

numHighPoints = 0
for row in seafloor:
    for column in row:
        if column > 1:
            numHighPoints += 1

print("Number of High Points: ", numHighPoints)
