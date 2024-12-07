import itertools as it

inFile = './testInput.txt'
inFile = './input.txt'

f = open(inFile, 'r')


plan = [[int(a), [b for b in c.split(' ') if b]] for a,c in [line.strip().split(':') for  line in f.readlines()]]

valids = []
invalids = []
newValids = []
stillInvalids = []
for target,operands in plan:
    # print(target)
    valid = False
    for operators in it.product('*+', repeat=len(operands)-1):
        sumList =  list(it.chain(*it.zip_longest(operands, operators)))[:-1]
        while len(sumList) > 1:
            sumString = ' '.join(sumList[0:3])
            sumList = sumList[3:]
            interim = eval(sumString)
            if interim <= target:
                sumList = [str(interim)] + sumList
            else:
                sumList = []
                break
        if len(sumList) > 0 and int(sumList[0]) == target:
            valids.append(target)
            valid = True
            break
    if not valid:
        invalids.append([target,operands])
print("Length plan: ",len(plan))
print("Length valids: ",len(valids))
print("Length invalids: ",len(invalids))
print("Part 1 ",sum(valids))
currentInvalids = 1
for target, operands in invalids:
    valid = False
    print("Current Invalid", currentInvalids, target, operands)
    currentInvalids = currentInvalids + 1
    for operators in it.product('*+c', repeat=len(operands)-1):
        sumList =  list(it.chain(*it.zip_longest(operands, operators)))[:-1]
        while len(sumList) > 1:
            if sumList[1] == 'c':
                sumString = sumList[0] + sumList[2]
                sumList = sumList[3:]
                interim = int(sumString)
            else:
                sumString = ' '.join(sumList[0:3])
                sumList = sumList[3:]
                interim = eval(sumString)

            if interim <= target:
                sumList = [str(interim)] + sumList
            else:
                sumList = []
                break
        if len(sumList) > 0 and int(sumList[0]) == target:
            newValids.append(target)
            valid = True
            break
    if not valid:
        stillInvalids.append([target,operands])

print("Length plan: ",len(plan))
print("Length valids: ",len(valids))
print("Length invalids: ",len(invalids))
print("Length newValids: ",len(newValids))
print("Length stillInvalids: ",len(stillInvalids))

print("Part 1 ",sum(valids))
print("Part 2 ",sum(valids)+sum(newValids))

exit()

