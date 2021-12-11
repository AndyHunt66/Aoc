import sys
import re

# inFile = './testInput.txt'
inFile = './input.txt'

crabs = []
with open(inFile, 'r') as fh:
    crabs = sorted([int(x) for x in fh.readline().split(",")])

target = crabs[round(len(crabs) / 2)]
fuel = sum([abs(x - target) for x in crabs])

print("Fuel consumed : ", fuel)
# print(target)
# print(type(crabs))
# print(crabs)
# print(len(crabs))
