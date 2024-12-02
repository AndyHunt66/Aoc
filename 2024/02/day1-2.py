inFile = './testInput.txt'
# inFile = './input.txt'

f = open(inFile, 'r')
reports = [ [int(x.strip()) for x in  line.split(' ')] for line in [line.strip() for line in f.readlines()]]
print(reports)

safeList = []

numSafe = 0
for report in reports:
    safe = True
    damper = 0
    for i in range(0,len(report)):
        if report[i] == report[i+1] or abs(a-b) > 3:
            if damper == 0:
                damper = 1
            else:
                safe = False
                break
    if safe:
        increase = report[0] < report[1]
        for a,b in zip(report, report[1:]):
            if increase:
                if (a >  b):
                    if damper == 0:
                        damper = 1
                    else:
                        safe = False
                        break
            else:
                if (a < b):
                    if damper == 0:
                        damper = 1
                    else:
                        safe = False
                        break
    safeList.append(safe)
    if safe:
        numSafe = numSafe + 1

print(safeList)
print(numSafe)