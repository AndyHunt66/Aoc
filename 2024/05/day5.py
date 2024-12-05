inFile = './testInput.txt'
# inFile = './input.txt'

f = open(inFile, 'r')
instrInput = [line for line in f.read().split("\n")]

# print(instrInput)
orders = [list(order.split('|')) for order in instrInput[:instrInput.index('')]]
toPrints = [instr.split(',')  for instr in instrInput[instrInput.index('')+1:]]
print(orders)
print(toPrints)
for instr in toPrints:
    for order in orders:
        if instr.index(order[0]) < instr.index(order[1]):
            pass
        else:
            instr.pop(instr.index(order[1]))
            instr.insert(order[1], instr.index(instr[0]))
