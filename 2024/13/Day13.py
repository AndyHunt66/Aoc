import re
import numpy as np

def close_enough_for_jazz(flt, tolerance=1e-04):
    return abs(flt - round(flt)) <= tolerance

inFile = './testInput.txt'
inFile = './input.txt'

f = open(inFile, 'r')

moves = []
prizes = []

for machineLines in f.read().split('\n\n'):
    arr = []
    for line in machineLines.split('\n'):
        arr.append(re.findall(r'\d+', line))
    moves.append(np.array([arr[0], arr[1]], dtype=np.int64))
    prizes.append(np.array(arr[2],dtype=np.int64))

coinsSpent1 = 0
coinsSpent2 = 0
for i in range(len(prizes)):
    moves[i] = moves[i].transpose()

    solution1 = np.linalg.solve(moves[i], prizes[i])
    if close_enough_for_jazz(solution1[0]) and close_enough_for_jazz(solution1[1]):
        coinsSpent1 = coinsSpent1 + (solution1[0]*3) + solution1[1]

    prizes[i]= [prizes[i][0]+10000000000000,prizes[i][1]+10000000000000]
    solution2 = np.linalg.solve(moves[i], prizes[i])
    if close_enough_for_jazz(solution2[0]) and close_enough_for_jazz(solution2[1]):
        coinsSpent2 = coinsSpent2 + (solution2[0]*3) + solution2[1]

print(coinsSpent1)
print(coinsSpent2)