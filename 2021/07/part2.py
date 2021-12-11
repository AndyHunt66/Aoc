import sys
import re
from math import factorial

#inFile = './testInput.txt'
inFile = './input.txt'

crabs = []
with open(inFile, 'r') as fh:
    crabs = sorted([int(x) for x in fh.readline().split(",")])


#Sum of n terms = (n/2) (first term + last term)
# When the first term is 1 and the number of terms is the last term:
#  (n^2 + n)/2

index = 0
bestFuelConsumption = ( sum([(abs(x - crabs[0])**2 + abs(x - crabs[0]))/2 for x in crabs]) )

for i in range(crabs[1],crabs[len(crabs)-1]):
    thisFuel = ( sum([(abs(x - i)**2 + abs(x - i))/2 for x in crabs]) )
    print("Index ", i, " consumption: ",thisFuel)
    if thisFuel < bestFuelConsumption:
        bestFuelConsumption = thisFuel
        index = i

print(bestFuelConsumption)
print(index)
print(crabs)
