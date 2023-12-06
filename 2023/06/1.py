# https://adventofcode.com/2023/day/3

# inFile = './testInput.txt'
inFile = './input.txt'

[times, distances] = [[int(x) for x in line.strip()[11::].split(' ') if x] for line in open(inFile, 'r').readlines()]

print(times)
print(distances)
wins = []
for raceNum, time in enumerate(times):
    numWinningPossibilities = 0
    for i in range(1,time):
        if ((time - i)*i) > distances[raceNum]:
            numWinningPossibilities += 1
    wins.append(numWinningPossibilities)

result = 1
for win in wins:
    result *= win
print("result is ", result)