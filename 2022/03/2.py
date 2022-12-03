# inFile = './testInput.txt'
inFile = './input.txt'

badges = []
f = open(inFile, 'r')
rucksack1 = list(f.readline().strip())
while len(rucksack1) != 0:
    rucksack2 = list(f.readline().strip())
    rucksack3 = list(f.readline().strip())

    for i in range(len(rucksack1)):
        if rucksack1[i] in rucksack2 and rucksack1[i] in rucksack3:
            badges.append(rucksack1[i])
            break
    rucksack1 = list(f.readline().strip())

priority = 0
for i in badges:
    if i.islower():
        priority += ord(i)-96
    else:
        priority += ord(i)-38
print(priority)
