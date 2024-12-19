import numpy as np
inFile = './testInput.txt'
inFile = './input.txt'

f = open(inFile, 'r')
a,b =  f.read().split('\n\n')
towels = [i.strip() for i in  a.split(',')]
patterns  = [i for i in b.split('\n') if i != '']
print(patterns)
print(towels)

def doesthestartofthispattermatchanytowels(currpattern: str):
    global recdepth
    recdepth = recdepth + 1
    match = False
    for towel in towels:
        if currpattern in towels:
            return True

        if currpattern.startswith(towel):
            if len(currpattern) == len(towel):
                recdepth = recdepth - 1
                return True
            else:
                newpattern = currpattern[len(towel):]
                if doesthestartofthispattermatchanytowels(newpattern):
                    return True
    recdepth = recdepth - 1
    return match

matches = 0
for pattern in patterns:
    print("Checking pattern", pattern , end=' ')
    if  doesthestartofthispattermatchanytowels(pattern):
        print("Yes")
        matches = matches + 1
    else:
        print("No")

print(matches)
