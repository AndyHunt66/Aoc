# https://adventofcode.com/2023/day/8
import math

# inFile = './testInput3.txt'
inFile = './input.txt'

f = open(inFile, 'r')
directions = f.readline().strip()
f.readline()
nodes = {}
currentNodes = []
for line in f.readlines():
    nodes[line.split()[0]] = (line.split()[2][1:4], line.split()[3][:3])
    if line.split()[0][2:3] == 'A':
        currentNodes.append(line.split()[0])

print(currentNodes)
step = 0
nodeSteps = {}
while True:
    for idx, node in enumerate(currentNodes):
        if directions[step % (len(directions))] == 'L':
            currentNodes[idx] = nodes[node][0]
        else:
            currentNodes[idx] = nodes[node][1]
        if currentNodes[idx][2:3] == 'Z':
            if currentNodes[idx] not in nodeSteps:
                nodeSteps[currentNodes[idx]] = step+1
                print(step, "-", idx, "-", currentNodes[idx])

    if len(nodeSteps) == len(currentNodes):
        break
    step += 1

print(nodeSteps)
print(*nodeSteps.values())
print(math.lcm(*nodeSteps.values()))
