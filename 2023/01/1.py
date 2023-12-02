import re

# inFile = './testInput.txt'
inFile = './input.txt'

badges = []
f = open(inFile, 'r')
input = [line.strip() for line in f.readlines()]


values = [(10*int(cv[re.search('\d', cv).start()])) +  int(cv[::-1][re.search('\d',  cv[::-1]).start()]) for cv in input]
print(values)
print('Answer is ', sum(values))