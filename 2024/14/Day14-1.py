import re

inFile = './testInput.txt'
inFile = './input.txt'

seconds = 100
# testInput
p1FieldX = 11
p1FieldY = 7
# Actual Input
p1FieldX = 101
p1FieldY = 103

# LU,RU,LL,RL
quads = [0,0,0,0,]

f = open(inFile, 'r')

for robot in f.readlines():
    x,y,dx,dy = map(int, re.findall(r'-?\d+',robot))

    endPos = 0
    endX = (x + ( dx * seconds)) % p1FieldX
    endY = (y + ( dy * seconds)) % p1FieldY

    if endX + 1== (p1FieldX + 1) / 2 or endY + 1 == (p1FieldY + 1) / 2:
        continue
    if endX > p1FieldX / 2:
        endPos = endPos + 1
    if endY > p1FieldY / 2:
        endPos = endPos + 2
    quads[endPos] = quads[endPos] + 1

result = 1
for pos in quads:
    result = result * pos
print(quads)
print(result)