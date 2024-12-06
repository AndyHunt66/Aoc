import numpy as np

inFile = './testInput.txt'
inFile = './input.txt'

f = open(inFile, 'r')
plan = np.array([list(line.strip()) for  line in f.readlines()])
rowNum,colNum = np.where(plan == '^')
pos =  rowNum[0], colNum[0]


direction = 'N'
distance = 0
exited = False
while not exited:

    # Rotate the plan counter clockwise
    plan = list(zip(*plan))[::-1]
    # Re-identify the pos
    pos =    len(plan) - 1 - pos[1], pos[0]

    row = np.array( plan[pos[0]] )

    if np.any(row == '#') and np.where(row == '#')[0][0] < pos[1]:
        hashIndex = np.where(row[:pos[1]] == '#')[0][-1]
    else:
        hashIndex = -1
        exited = True
    for i in range(hashIndex+1,pos[1]+1):
        row[i] = 'X'
    plan[pos[0]]=row
    # We've moved, so update pos
    pos = pos[0], hashIndex + 1



distance = sum(sum(np.char.count(plan, 'X')))
print(distance)