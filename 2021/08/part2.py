import sys
import re

# inFile = './testTestInput.txt'
# inFile = './testInput.txt'
inFile = './input.txt'

allDigits = []
allOutputs = []
knowns = [0] * 10


def matchItems(match1, match2):
    matches = [x for x in match2 if x in match1]
    return len(matches)


def checkElement(toTest):
    if len(toTest) == 5:
        if knowns[1] != 0:
            if matchItems(toTest, knowns[1]) == 2:
                return 3
            if knowns[4] != 0:
                if matchItems(toTest, knowns[4]) == 3:
                    return 5
                else:
                    return 2
        if knowns[2] != 0:
            if matchItems(toTest, knowns[2]) == 3:
                return 5
            elif matchItems(toTest, knowns[2]) == 4:
                return 3
        if knowns[4] != 0 and matchItems(toTest, knowns[4]) == 2:
            return 2
        if knowns[5] != 0:
            if matchItems(toTest, knowns[5]) == 3:
                return 2
            elif matchItems(toTest, knowns[5]) == 4:
                return 3
        if knowns[6] != 0 and matchItems(toTest, knowns[6]) == 5:
            return 5
        if knowns[7] != 0 and matchItems(toTest, knowns[7]) == 3:
            return 3
        if knowns[9] != 0 and matchItems(toTest, knowns[9]) == 5:
            return 3
    elif len(toTest) == 6:
        if knowns[1] != 0 and matchItems(toTest, knowns[1]) == 1:
            return 6
        if knowns[2] != 0 and matchItems(toTest, knowns[2]) == 5:
            return 0
        if knowns[3] != 0 and matchItems(toTest, knowns[3]) == 5:
            return 9
        if knowns[4] != 0 and matchItems(toTest, knowns[4]) == 4:
            return 9
        if knowns[5] != 0 and matchItems(toTest, knowns[5]) == 4:
            return 0
        if knowns[7] != 0 and matchItems(toTest, knowns[7]) == 2:
            return 6

    return -1


with open(inFile, 'r') as fh:
    for line in fh:
        digits, output = (line.strip().split("|"))
        allDigits.append(digits)
        allOutputs.append(output)
sum1478 = 0
totalSum = 0
# allOutputs = ['abc abd ef']
for line in allDigits:

    digit = line.split()
    print("---------------")
    print(digit)
    digit.sort(key=len)
    print(digit)
    knowns = [0] * 10
    unknowns = []
    for x in digit:
       # print(x)

        if len(x) == 2:
            knowns[1] = sorted(list(x))
            continue
        if len(x) == 3:
            knowns[7] = sorted(list(x))
            continue
        if len(x) == 4:
            knowns[4] = sorted(list(x))
            continue
        if len(x) == 7:
            knowns[8] = sorted(list(x))
            continue

            # Skip the ones we've already found
        for known in knowns:
            if known == sorted(list(x)):
                continue

        score = checkElement(x)
        if score != -1:
            knowns[score] = sorted(list(x))
        else:
            unknowns.append(x)
        # print("AAAA",outputs)
        # print("HERE", knowns)

    outputs = allOutputs[allDigits.index(line)]
    linetotal = 0;
    outputs = outputs.split()
    print(knowns)
    for i in range(0,4):
        output = sorted(list(outputs[i]))
        if knowns.index(output) == -1:
            print("ooops!")
            exit
        linetotal += knowns.index(output) * 10 ** (3-i)
    print("Line total: ", linetotal)
    totalSum += linetotal

print("Total: ", totalSum)

