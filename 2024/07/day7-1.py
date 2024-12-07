import itertools as it

inFile = './testInput.txt'
inFile = './input.txt'

f = open(inFile, 'r')


plan = [[int(a), [b for b in c.split(' ') if b]] for a,c in [line.strip().split(':') for  line in f.readlines()]]

valids = []
for target,operands in plan:
    print(target)
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
            break
print("Part 1 ",sum(valids))



exit()

