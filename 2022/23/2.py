from collections import defaultdict
import numpy as np

# inFile = './testInput.txt'
inFile = './input.txt'


def canMoveNorth(y, x):
    if '#' in [m[y - 1][x - 1], m[y - 1][x], m[y - 1][x + 1]]:
        return False
    else:
        return True


def canMoveSouth(y, x):
    if '#' in [m[y + 1][x - 1], m[y + 1][x], m[y + 1][x + 1]]:
        return False
    else:
        return True


def canMoveWest(y, x):
    if '#' in [m[y - 1][x - 1], m[y][x - 1], m[y + 1][x - 1]]:
        return False
    else:
        return True


def canMoveEast(y, x):
    if '#' in [m[y - 1][x + 1], m[y][x + 1], m[y + 1][x + 1]]:
        return False
    else:
        return True


def calcMove(y, x, heading):
    ## Heading: North South, West, East : 0,1,2,3
    if m[y - 1][x - 1] == '#' or \
            m[y - 1][x] == '#' or \
            m[y - 1][x + 1] == '#' or \
            m[y][x - 1] == '#' or \
            m[y][x + 1] == '#' or \
            m[y + 1][x - 1] == '#' or \
            m[y + 1][x] == '#' or \
            m[y + 1][x + 1] == '#':

        for head in heading:
            if head == 0:
                if canMoveNorth(y, x):
                    return (y - 1, x)
            elif head == 1:
                if canMoveSouth(y, x):
                    return (y + 1, x)
            elif head == 2:
                if canMoveWest(y, x):
                    return (y, x - 1)
            elif head == 3:
                if canMoveEast(y, x):
                    return (y, x + 1)
    return (y, x)


def addEmptyBorder(mapElves):
    ## Add an empty border all round, if there is an elf on the border
    borderElf = False
    if mapElves[0].count('#') > 0 or mapElves[-1].count('#') > 0:
        borderElf = True
    else:
        for line in mapElves:
            if line[0] == '#' or line[-1] == '#':
                borderElf = True
                break

    if borderElf:
        for line in mapElves:
            line.insert(0, '.')
            line.append('.')
            line = np.array(line)
        mapElves.insert(0, ['.'] * len(mapElves[0]))
        mapElves.append(['.'] * len(mapElves[0]))

    return mapElves


turns = 10

m = [list(line) for line in open(inFile).read().split("\n")]
m = addEmptyBorder(m)
for line in m:
    for i in line:
        print(" {0} ".format(i), end='')
    print()
print("===============")
LEN = len(m)
if LEN != len(m[0]):
    print("Map is not square!")
    exit(1)

elves = dict()
for j in range(LEN):
    for i in range(LEN):
        if m[j][i] == '#':
            elves[(j, i)] = 1

direction = [0, 1, 2, 3]
moves = defaultdict(lambda: 0)
moved = True
turns = 0
while moved:
    moved = False
    turns += 1
    moves = defaultdict(lambda: 0)
    for elf in elves:
        proposed = calcMove(elf[0], elf[1], direction)
        if moves[proposed] == 0:
            moves[proposed] = [[elf], 1]
        else:
            moves[proposed][0].append(elf)
            moves[proposed][1] += 1

    # Carry out the moves
    for move in moves:
        if moves[move][1] == 1:
            if move != moves[move][0][0]:
                ## An elf actually moved
                moved = True
            elves.pop(moves[move][0][0])
            elves[move] = 1

    m = [[]]
    for j in range(LEN):
        for i in range(LEN):
            try:
                if elves[(j, i)]:
                    m[j].append('#')
            except:
                m[j].append('.')
        m.append([])
    m.pop(-1)
    m = addEmptyBorder(m)
    LEN = len(m)
    elves = dict()
    for j in range(LEN):
        for i in range(LEN):
            if m[j][i] == '#':
                elves[(j, i)] = 1
    # for line in m:
    #     for i in line:
    #         print(" {0} ".format(i), end='')
    #     print()
    print("Turn {0}".format(turns))
    direction.append(direction.pop(0))

## Remove empty rows / columns
# Top row
for j in range(LEN):
    if '#' in m[j]:
        break
if j > 0:
    for remove in range(j):
        m.pop(0)

# Bottom row
for j in range(len(m)):
    if '#' in m[len(m) - j - 1]:
        break
if j > 0:
    for remove in range(j):
        m.pop(len(m) - j + 1)

# Left side
for j in range(len(m[0])):
    found = False
    for line in m:
        if line[j] == '#':
            found = True
            break
    if found: break
if j > 0:
    for remove in range(j):
        for line in m:
            line.pop(0)

# Right side
for j in range(len(m[0])):
    found = False
    for line in m:
        if line[len(line) - 1 - j] == '#':
            found = True
            break
    if found:
        break
if j > 0:
    for remove in range(j):
        for line in m:
            line.pop(-1)

for line in m:
    for i in line:
        print(" {0} ".format(i), end='')
    print()
print("===============")

tiles = 0
for j in m:
    tiles = tiles + j.count('.')
print("{0} empty tiles".format(tiles))
print("Turn : {0}".format(turns))