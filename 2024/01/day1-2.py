from collections import defaultdict

# inFile = './testInput.txt'
inFile = './input.txt'

f = open(inFile, 'r')
input = [line.strip() for line in f.readlines()]

list1 = sorted([i.split(' ',1)[0] for i in input])
list2 = sorted([i.split('  ',1)[1].strip() for i in input])
# print(list1)
# print(list2)

sim2 = defaultdict(lambda: 0)
for i in list2:
    sim2[i]=sim2[i]+1

similarity = 0
for i in list1:
    similarity = similarity + (int(i) * sim2[i])

print(similarity)