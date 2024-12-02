# inFile = './testInput.txt'
from itertools import pairwise

inFile = './input.txt'

def reportCheck(report):
    increase = report[0] < report[1]
    return [ not ((a == b or abs(a-b) > 3) or (increase == (a > b))) for a, b in pairwise(report) ]

f = open(inFile, 'r')
reports = [ [int(x) for x in  line.split()] for line in [line.strip() for line in f.readlines()]]

part1SafeList = []
part2Safe = 0

for report in reports:
    reportSafe = reportCheck(report)
    part1SafeList.append(sum(reportSafe) == len(report)-1)
    if (sum(reportSafe) <= len(report)-2):
        for i in range(0, len(report)):
            damperReport = report[:i] + report[i+1:]

            if sum(reportCheck(damperReport)) == len(damperReport)-1:
                part2Safe = part2Safe + 1
                break

print(part1SafeList)
print("Part 1", sum(part1SafeList))
print("part 2", sum(part1SafeList) + part2Safe)