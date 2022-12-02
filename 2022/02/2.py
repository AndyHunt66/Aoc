# inFile = './testInput.txt'
inFile = './input.txt'


# A = rock
# B = paper
# C = scissors
# X = Lose
# Y = draw
# Z = Win

scores = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}

strategy = open(inFile).read().strip().split("\n")
score = sum(scores[go] for go in strategy)

print(score)
