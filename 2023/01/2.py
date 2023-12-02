import re

# inFile = './testInput2.txt'
inFile = './input.txt'

badges = []
f = open(inFile, 'r')
input = [line.strip() for line in f.readlines()]

numbers = ['one','two', 'three','four','five','six','seven','eight','nine']
answer=0
for cv in input:
    cv = re.sub('one', 'one1one',cv)
    cv = re.sub('two', 'two2two', cv)
    cv = re.sub('three', 'three3three', cv)
    cv = re.sub('four', 'four4four',cv)
    cv = re.sub('five', 'five5five',cv)
    cv = re.sub('six', 'six6six',cv)
    cv = re.sub('seven', 'seven7seven',cv)
    cv = re.sub('eight', 'eight8eight',cv)
    cv = re.sub('nine', 'nine9nine',cv)
    value = (10*int(cv[re.search('\d', cv).start()])) +  int(cv[::-1][re.search('\d',  cv[::-1]).start()])
    print(value)
    answer += value

print(answer)
