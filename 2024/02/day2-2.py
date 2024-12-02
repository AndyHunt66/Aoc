# inFile = './testInput.txt'
inFile = './input.txt'
#
# def reportCheck(report)
f = open(inFile, 'r')
reports = [ [int(x.strip()) for x in  line.split(' ')] for line in [line.strip() for line in f.readlines()]]
print(reports)

safeList = []
damper = 0
numSafe = 0
for report in reports:
    safe = True
    reportSafe = []
    increase = report[0] < report[1]
    for a, b in zip(report, report[1:]):
        if (a == b or abs(a-b) > 3) or (increase == (a > b)):
            reportSafe.append(False)
        else:
            reportSafe.append(True)

    safeList.append(safe)
    if safe:
        numSafe = numSafe + 1

print(safeList)
print(numSafe)