from collections import defaultdict

# inFile = './testInput.txt'
inFile = './input.txt'

f = open(inFile, 'r')
input = [line.strip() for line in f.readlines()]

list1 = sorted([i.split(' ',1)[0] for i in input])
list2 = sorted([i.split('  ',1)[1] for i in input])
print(list1)
print(list2)
sim1 = defaultdict(lambda: 0)
sim2 = defaultdict(lambda: 0)
for i in list1:
    sim1["i"]=sim1["i"]+1

print(sim1)