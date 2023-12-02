import re

# inFile = './testInput2.txt'
inFile = './input.txt'

f = open(inFile, 'r')
input = [line.strip() for line in f.readlines()]

answer = 0
for cv in input:
    cv = re.sub('eight', 'e8t', cv)
    cv = re.sub('nine', 'n9', cv)
    cv = re.sub('one', 'o1', cv)
    cv = re.sub('two', '2', cv)
    cv = re.sub('three', '3', cv)
    cv = re.sub('four', '4', cv)
    cv = re.sub('five', '5', cv)
    cv = re.sub('six', '6', cv)
    cv = re.sub('seven', '7', cv)
    value = (10 * int(cv[re.search('\d', cv).start()])) + int(cv[::-1][re.search('\d', cv[::-1]).start()])
    print(value)
    answer += value

print(answer)
