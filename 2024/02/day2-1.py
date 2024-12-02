# inFile = './testInput.txt'
inFile = './input.txt'

f = open(inFile, 'r')
reports = [ [int(x.strip()) for x in  line.split(' ')] for line in [line.strip() for line in f.readlines()]]
print(reports)

safeList = []
damper = 0
numSafe = 0
for report in reports:
    safe = True
    for a, b in zip(report, report[1:]):
        if a == b or abs(a-b) > 3:
            safe = False
            break
    if safe:
        increase = report[0] < report[1]
        for a,b in zip(report, report[1:]):
            if increase:
                if (a >  b):
                    safe = False
                    break
            else:
                if (a < b):
                    safe = False
                    break
    safeList.append(safe)
    if safe:
        numSafe = numSafe + 1

print(safeList)
print(numSafe)