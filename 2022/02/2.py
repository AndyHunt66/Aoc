from collections import defaultdict

#inFile = './testInput.txt'
inFile = './input.txt'

# Defining the dict
scores = defaultdict(lambda: 0)
# A = rock
# B = paper
# C = scissors
# X = Lose
# Y = draw
# Z = Win
scores["A X"] = 3 # Lose to rock - scissors
scores["A Y"] = 4
scores["A Z"] = 8
scores["B X"] = 1
scores["B Y"] = 5
scores["B Z"] = 9
scores["C X"] = 2
scores["C Y"] = 6
scores["C Z"] = 7

strategy = open(inFile).read().split("\n")
score = sum(scores[go] for go in strategy)

print(score)
