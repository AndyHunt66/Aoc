from collections import defaultdict

#inFile = './testInput.txt'
inFile = './input.txt'

# A, X = rock
# B, Y = paper
# C, Z = scissors

scores = defaultdict(lambda: 0)
scores["A X"] = 4
scores["A Y"] = 8
scores["A Z"] = 3
scores["B X"] = 1
scores["B Y"] = 5
scores["B Z"] = 9
scores["C X"] = 7
scores["C Y"] = 2
scores["C Z"] = 6

strategy = open(inFile).read().split("\n")
score = sum(scores[go] for go in strategy)

print(score)
