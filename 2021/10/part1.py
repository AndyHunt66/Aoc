import copy
import sys
import re


def getFirstCorruptChar(line):
    stack = []
    for char in line:
        if char in closers:
            stack.append(char)
        else:
            if char == closers[stack[-1]]:
                stack.pop()
            else:
                return char
    return 0

def completeLine(line):
    stack = []
    for char in line:
        if char in closers:
            stack.append(char)
        else:
            if char == closers[stack[-1]]:
                stack.pop()
    completion = []
    while len(stack) > 0:
        completion.append(closers[stack.pop()])
    return completion

# inFile = './testInput.txt'
inFile = './input.txt'


program = []
with open(inFile, 'r') as fh:
    for line in fh:
        program.append(line.strip())

closers = {'(': ')', '[': ']', '{': '}', '<': '>'}

syntaxPoints = {')': 3, ']': 57, '}': 1197, '>': 25137}
completionPoints = {')': 1, ']': 2, '}': 3, '>': 4}

syntaxScore = 0
completionScores = []
for line in program:
    error = getFirstCorruptChar(line)
    if error != 0:
        print(error)
        syntaxScore += syntaxPoints[error]
    else:
        completionScore = 0
        completion = completeLine(line)
        print(completion)
        for char in completion:
            completionScore *= 5
            completionScore += completionPoints[char]
        completionScores.append(completionScore)

print("Syntax Score: ", syntaxScore)
completionScores = sorted(completionScores)
completionScore = completionScores[round(len(completionScores)/2)]
print("Completion Score: ", completionScore)




