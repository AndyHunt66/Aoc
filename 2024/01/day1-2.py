from collections import defaultdict

# inFile = './testInput.txt'
inFile = './input.txt'

f = open(inFile, 'r')
inputValues = [line.strip() for line in f.readlines()]

list1 = sorted([i.split(' ', 1)[0] for i in inputValues])
list2 = sorted([i.split(' ', 1)[1].strip() for i in inputValues])

sim2 = defaultdict(lambda: 0)
for i in list2:
    sim2[i] = sim2[i]+1

similarity = sum(int(i) * sim2[i] for i in list1)

print(similarity)
