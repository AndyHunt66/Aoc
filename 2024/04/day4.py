import numpy as np

# inFile = './testInput.txt'
inFile = './input.txt'

f = open(inFile, 'r')
grid = np.array([list(line.strip()) for line in f.readlines()])
# print(grid)
transGrid = np.transpose(grid)
# print(transGrid)

forwards = ['X','M','A','S']
backwards = ['S','A','M','X']
crossMas1 = ['M','M','A','S','S']
crossMas2 = ['M','S','A','M','S']
crossMas3 = ['S','M','A','S','M']
crossMas4 = ['S','S','A','M','M']

p1Found = 0
p2Found = 0

diagDownRight = 0
diagDownLeft = 0

for j in  range(len(grid)):
    for i in range(len(grid[j])):
        ## Horizontal forwards and backwards
        word = grid[j][i:i+4]
        if ( len(word) == 4 ) and  ( np.equal(word,forwards).all()  or np.equal(word,backwards).all() ):
            p1Found = p1Found +1

        ## Vertical forwards and backwards
        word = transGrid[j][i:i+4]
        if ( len(word) == 4 ) and ( np.equal(word, forwards).all() or  np.equal(word,backwards).all()):
            p1Found = p1Found +1

        # Diagonal down right
        if  (i < len(grid)- 3) and (j < len(grid)- 3):
            word = [grid[j][i], grid[j+1][i+1], grid[j+2][i+2], grid[j+3][i+3]]
            if np.equal(word,forwards).all() or  np.equal(word,backwards).all():
                p1Found = p1Found +1

        # Diagonal down left
        if  (i > 2) and (j < len(grid)- 3):
            word = [grid[j][i], grid[j+1][i-1], grid[j+2][i-2], grid[j+3][i-3]]
            if  np.equal(word,forwards).all() or  np.equal(word,backwards).all():
                p1Found = p1Found +1

        ## cross-mas
        if (i < len(grid)-2) and (j < len(grid)-2):
            word = grid[j][i], grid[j][i+2], grid[j+1][i+1], grid[j+2][i], grid[j+2][i+2]
            if np.equal( word, crossMas1).all() or np.equal( word, crossMas2).all() or np.equal( word, crossMas3).all() or np.equal( word, crossMas4).all() :
                p2Found = p2Found + 1

print(p1Found)
print(p2Found)
