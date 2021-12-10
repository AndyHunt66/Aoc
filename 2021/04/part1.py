import sys
import re

def score(board):
    sum = 0
    for square in board:
        if square != -1:
            sum += square
    return sum

def house(board):
    ## Horizontal lines
    if (board[0] + board[1] + board[2]+board[3]+board[4] == -5):
        return True
    if (board[5] + board[6] + board[7]+board[8]+board[9] == -5):
        return True
    if (board[10] + board[11] + board[12]+board[13]+board[14] == -5):
        return True
    if (board[15] + board[16] + board[17]+board[18]+board[19] == -5):
        return True
    if (board[20] + board[21] + board[22]+board[23]+board[24] == -5):
        return True

    ## Vertical lines
    if (board[0] + board[5] + board[10]+board[15]+board[20] == -5):
        return True
    if (board[1] + board[6] + board[11]+board[16]+board[21] == -5):
        return True
    if (board[2] + board[7] + board[12]+board[17]+board[22] == -5):
        return True
    if (board[3] + board[8] + board[13]+board[18]+board[23] == -5):
        return True
    if (board[4] + board[9] + board[14]+board[19]+board[24] == -5):
        return True

    return False



def processBoard(board):
    ## return the final score of the board and
    ## the index of the call when it won
    for i in range(len(calls)) :
        for j in range(len(board)):
            if board[j] == calls[i]:
                board[j] = -1
                if house(board):
                    boardScore = score(board)
                    return boardScore, i
                break
    return -1, -1


#inFile = './testInput.txt'
inFile = './input.txt'

currentWinningCallIndex = -1
currentBestScore = 0
currentLosingCallIndex = -1
currentWorstScore = 0
board =[]
with open(inFile, 'r') as fh :
    calls = [int(i) for i in fh.readline().strip().split(",")]

    currentWinningCallIndex = len(calls)
    # Consume first blank line after the calls
    line= fh.readline()
    for line in fh:
      line=line.strip()
      if line == "":
          (thisBoardScore, callIndex) =  processBoard(board)
          if score != -1 :
            if callIndex < currentWinningCallIndex:
                  currentWinningCallIndex = callIndex
                  currentBestScore = thisBoardScore
            if callIndex > currentLosingCallIndex:
                  currentLosingCallIndex = callIndex
                  currentWorstScore = thisBoardScore
            board = []
      else:
        for square in re.split(' +',line):
          board.append(int(square))

# Last one
(thisBoardScore, callIndex) =  processBoard(board)
if score != -1 :
    if callIndex < currentWinningCallIndex:
        currentWinningCallIndex = callIndex
        currentBestScore = thisBoardScore
    if callIndex > currentLosingCallIndex:
        currentLosingCallIndex = callIndex
        currentWorstScore = thisBoardScore


print("Best board is number ", currentWinningCallIndex)
print("Best board sum is ", currentBestScore)
print("Best board score is ",currentBestScore * calls[currentWinningCallIndex])
print("Worst board is number ", currentLosingCallIndex)
print("Worst board sum is ", currentWorstScore)
print("Worst board score is ",currentWorstScore * calls[currentLosingCallIndex])
