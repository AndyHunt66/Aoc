inFile = './testInput.txt'
# inFile = './input.txt'

f = open(inFile, 'r')
instrInput = [line for line in f.read().split("\n")]


# print(instrInput)
orders = [list(order.split('|')) for order in instrInput[:instrInput.index('')]]
toPrints = [instr.split(',')  for instr in instrInput[instrInput.index('')+1:]]
print(orders)
print(toPrints)
correctToPrint = toPrints.copy()
correcteds = []
for instr in toPrints:
    # print(instr)
    for order in orders:
        try:
            if instr.index(order[0]) < instr.index(order[1]):
                pass
            else:
                correctToPrint.pop(correctToPrint.index(instr))
                instr.pop(instr.index(order[1]))
                instr.insert( instr.index(instr[0])+1, order[1])
                correcteds.append(instr)

        except ValueError:
            pass
print(correctToPrint)
total1 = 0
total2 = 0
for correct in correctToPrint:
    if correct != ['']:
        middleIndex = int((len(correct) - 1)/2)
        total1 = total1 + int(correct[middleIndex])

for corrected in correcteds:
    if corrected != ['']:
        middleIndex = int((len(corrected) - 1)/2)
        total2 = total2 + int(corrected[middleIndex])


print(total1)
print(total2)

