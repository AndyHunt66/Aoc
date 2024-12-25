import re

inFile = './testInput.txt'
inFile = './input.txt'


f = open(inFile, 'r')
keys = []
locks = []
s =   f.read().split('\n\n')

for line in s:
    if line.startswith('#####'):
        locks.append([0,0,0,0,0])
        for l in line.split('\n'):
            bumps = [lock.start() for lock in re.finditer('#', l)]
            for i,bump in enumerate(bumps):
                locks[-1][bump]=locks[-1][bump] + 1
        locks[-1]= [x-1 for x in locks[-1]]
    else:
        keys.append([0,0,0,0,0])
        for l in  reversed(line.split('\n')):
            bumps = [key.start() for key in re.finditer('#', l)]
            for i,bump in enumerate(bumps):
                keys[-1][bump]=keys[-1][bump] + 1
        keys[-1]= [x-1 for x in keys[-1]]
print(keys,locks)

numFits = 0
for lock in locks:
    for key in keys:
        fits = True
        for i in range(len(lock)):
            if key[i] + lock[i] > 5:
                fits = False
                continue
        if fits == True:
            numFits = numFits + 1

print(numFits)