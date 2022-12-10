# inFile = './testInput.txt'
inFile = './input.txt'


def checkToDraw(currentClock):
    if (currentClock % 40)-1 in [register-1, register, register+1]:
        screen[currentClock-1] = "#"
        print(screen)
    pass


with open(inFile) as f:
    instructions = [instruction for instruction in f.read().split("\n")]

screen = ["."] * 240
clock = 0
register = 1

for instruction in instructions:
    # Start Cycle 1
    clock += 1  # in cycle {clock}
    checkToDraw(clock)
    if instruction != "noop":
        clock += 1
        checkToDraw(clock)
        register += int(instruction[5:])

for i in range(len(screen)):
    if (i % 40) == 0:
        print()
    print(screen[i], end='')
