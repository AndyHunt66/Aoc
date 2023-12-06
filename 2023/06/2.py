# https://adventofcode.com/2023/day/3

# inFile = './testInput.txt'
inFile = './input.txt'

[time, distance] = [int("".join([x for x in line.strip()[11::] if x != ' '])) for line in open(inFile, 'r').readlines()]

winningPossibilities = len([x for x in range(1, time) if ((time - x) * x) > distance])
print("result is ", winningPossibilities)
