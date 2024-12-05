inFile = './testInput.txt'
inFile = './input.txt'

f = open(inFile, 'r')
instrInput = [line for line in f.read().split("\n")]

def makeCorrect(instruction):
    corrected = False
    for order in orders:
        try:
            if instruction.index(order[0]) > instruction.index(order[1]):
                instruction.pop(instruction.index(order[1]))
                instruction.insert( instruction.index(order[0])+1, order[1])
                corrected = True

        except ValueError:
            pass
    return corrected

# print(instrInput)
orders = [list(order.split('|')) for order in instrInput[:instrInput.index('')]]
toPrints = [instr.split(',')  for instr in instrInput[instrInput.index('')+1:]]

correcteds = []
for instr in toPrints:
    if makeCorrect(instr):
        while(makeCorrect(instr)):
            pass
        correcteds.append(instr)


total2 = 0
for corrected in correcteds:
    if corrected != ['']:
        middleIndex = int((len(corrected) - 1)/2)
        total2 = total2 + int(corrected[middleIndex])

print(correcteds)

print(total2)

