import re
import numpy as np

# inFile = './testInput.txt'
# inFile = './testInput2.txt'
inFile = './input.txt'

rounds = 10000

strengths = []
with open(inFile) as f:
    monkeys = [re.split("\n ", monkey) for monkey in [line for line in f.read().split("\n\n")]]


for monkey in monkeys:
    for count, attribute in enumerate(monkey):
        monkey[count] = list(filter(None, re.split("[ :,]", attribute)))
    monkey[0] = int(monkey[0][1])
    monkey[1] = [int(item) for item in monkey[1][2:]]
    monkey[2] = [monkey[2][4], monkey[2][5]]
    monkey[3] = int(monkey[3][3])
    monkey[4] = int(monkey[4][5])
    monkey[5] = int(monkey[5][5])
    monkey.append(0)  # Count of inspections

print(monkeys)
HCM = []
for monkey in monkeys:
    HCM.append(monkey[3])
HighestCommonMultiple = np.prod(HCM)
# print(HighestCommonMultiple)
# exit()
for thisRound in range(rounds):
    for monkey in monkeys:
        for count, item in enumerate(monkey[1]):

            ### Inspect
            monkey[6] += 1
            if monkey[2][1] == "old":
                oper2 = item
            else:
                oper2 = int(monkey[2][1])

            if monkey[2][0] == "+":
                new = item + oper2
            elif monkey[2][0] == "*":
                new = item * oper2

            ### Make allowance for it not being broken
            # new = floor(new/3)

            ## Test
            if new > HighestCommonMultiple:
                new = new % HighestCommonMultiple
            if new % monkey[3] == 0:
                monkeys[monkey[4]][1].append(new)
            else:
                monkeys[monkey[5]][1].append(new)
        monkey[1] = []
    print("round {0}".format(thisRound))

print(monkeys)
inspections = []
for monkey in monkeys:
    inspections.append(monkey[6])
inspections.sort()
print(inspections[-1] * inspections[-2])
