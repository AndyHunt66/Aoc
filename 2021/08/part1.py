import copy
import sys
import re

# inFile = './testInput.txt'
inFile = './input.txt'

allDigits = []
allOutputs = []
with open(inFile, 'r') as fh:
    for line in fh:
        digits, output = (line.strip().split("|"))
        allDigits.append(digits)
        allOutputs.append(output)
sum1478 = 0
for output in allOutputs:
    tempSum = copy.copy(sum1478)
    output = output.split()
    for x in output:
        if len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7:
            sum1478 += 1
    if tempSum == sum1478:
        print("Line found without one of the cardinal numbers")

print("total of 1478 : ", sum1478)
# print(target)
# print(type(crabs))
# print(crabs)
# print(len(crabs))
