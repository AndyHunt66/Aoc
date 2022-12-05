# inFile = './testInput.txt'
inFile = './input.txt'

stacksInput, moves = open(inFile).read().split("\n\n")
stacksInput = [list(x) for x in stacksInput.split("\n")]
moves = [x.split(" ") for x in moves.split("\n")]

# Stack components are at 1,5,9...4n+1
numStacks = int((len(stacksInput[0])+1)/4)
stacks = []

# We don't need the last line, as it's the stack number
for y in range(1, len(stacksInput[0]), 4):
    stack = []
    for x in range(len(stacksInput)-2, -1, -1):
        if stacksInput[x][y] != ' ':
            stack.append(stacksInput[x][y])
    stacks.append(stack)


for move in moves:
    for x in range(int(move[1])):
        stacks[int(move[5])-1].append(stacks[int(move[3])-1].pop())

for stack in stacks:
    print(stack[-1], end='')
