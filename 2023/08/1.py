# https://adventofcode.com/2023/day/8

# inFile = './testInput2.txt'
inFile = './input.txt'


f = open(inFile, 'r')
directions = f.readline().strip()
f.readline()
nodes = {}
for line in f.readlines():
    nodes[line.split()[0]] = (line.split()[2][1:4], line.split()[3][:3])
    # print(nodes)

currentNode = nodes['AAA']
step = 0
while currentNode != nodes['ZZZ']:
    if directions[step % (len(directions))] == 'L':
        currentNode = nodes[currentNode[0]]
    else:
        currentNode = nodes[currentNode[1]]
    step += 1

print(step)