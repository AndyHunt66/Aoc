# inFile = './testInput.txt'
inFile = './input.txt'

# A, X = rock
# B, Y = paper
# C, Z = scissors

scores = {"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}

strategy = open(inFile).read().strip().split("\n")
score = sum(scores[go] for go in strategy)

print(score)
