# inFile = './testInput.txt'
inFile = './input.txt'

f = open(inFile, 'r')
inputValues = [line.strip() for line in f.readlines()]


currPos = 50
zeroes = 0
# Part 1
for movement in inputValues:
    if movement[0] == 'R':
        currPos = ( currPos + int(movement[1:])) % 100
        print("Moving R . turns", movement[1:], "CurrPos ", currPos)
    else:
        currPos = ( currPos - int(movement[1:]) ) % 100
        print("Moving L . turns", movement[1:], "CurrPos ", currPos)
    
    if currPos == 0:
        zeroes += 1
print("Part 1: ",zeroes)
