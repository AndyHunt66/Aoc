# inFile = './testInput.txt'
inFile = './input.txt'

def reportCheck(report):
    increase = report[0] < report[1]
    reportSafe = []
    for a, b in zip(report, report[1:]):
        if (a == b or abs(a-b) > 3) or (increase == (a > b)):
            reportSafe.append(False)
        else:
            reportSafe.append(True)
    return reportSafe

f = open(inFile, 'r')
reports = [ [int(x.strip()) for x in  line.split(' ')] for line in [line.strip() for line in f.readlines()]]
print(reports)

part1SafeList = []
part2Safe = 0

for report in reports:

    reportSafe = reportCheck(report)
    part1SafeList.append(sum(reportSafe) == len(report)-1)
    if (sum(reportSafe) <= len(report)-2):
        for i in range(0, len(report)):
            damperReport = []
            if i != 0:
                damperReport = report[:i]
                damperReport.extend(report[i+1:])
            else:
                damperReport = report[i+1:]

            reportSafe = reportCheck(damperReport)
            if sum(reportSafe) == len(damperReport)-1:
                part2Safe = part2Safe + 1
                break

print(part1SafeList)
print("Part 1", sum(part1SafeList))
print("part 2", sum(part1SafeList) + part2Safe)