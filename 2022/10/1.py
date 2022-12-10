# inFile = './testInput.txt'
# inFile = './testInput2.txt'
inFile = './input.txt'


def checkRegister(currentClock):
    # print("during cycle {0}  register {1}".format(currentClock, register))
    if currentClock in (20, 60, 100, 140, 180, 220):
        strengths.append(currentClock*register)
        print("During cycle  {0} register {1} signal strength: {2}".format(currentClock, register, currentClock*register))


strengths = []
with open(inFile) as f:
    instructions = [instruction for instruction in f.read().split("\n")]

clock = 0
register = 1
checkRegister(clock)

for instruction in instructions:
    clock += 1 # in cycle {clock}
    checkRegister(clock)
    if instruction == "noop":
        pass
    else:
        clock += 1
        checkRegister(clock)
        register += int(instruction[5:])

print(sum(strengths))
