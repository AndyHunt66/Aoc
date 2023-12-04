# https://adventofcode.com/2023/day/2

import re

# inFile = './testInput.txt'
inFile = './input.txt'

powers = []

f = open(inFile, 'r')
input = [line.strip() for line in f.readlines()]

# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
for i in input:
    redSeen = 0
    greenSeen = 0
    blueSeen = 0
    i = i[5::]
    rounds = re.split('; |: ', i)
    for round in rounds:
        choice = re.split(' |, ', round)
        if len(choice) == 1:
            game = int(choice[0])
        for j in range(1, len(choice), 2):
            if choice[j] == 'red':
                redSeen = max(redSeen, int(choice[j - 1]))
            if choice[j] == 'green':
                greenSeen = max(greenSeen, int(choice[j - 1]))
            if choice[j] == 'blue':
                blueSeen = max(blueSeen, int(choice[j - 1]))
        # print(choice)
    powers.append(redSeen * greenSeen * blueSeen)

#     print(rounds)
# print(powers)
print('Answer = ', sum(powers))
