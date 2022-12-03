# inFile = './testInput.txt'
inFile = './input.txt'

rucksacks = []
duplicates = []
for line in open(inFile).read().strip().split("\n"):
    compartment1 = {}
    compartment2 = {}
    rucksack = []
    line = list(line)
    for i in range(len(line)//2):
        compartment1[line[i]] = 1
        compartment2[line[i + len(line)//2]] = 1

    for i in compartment1.keys():
        if i in compartment2:
            duplicates.append(i)

for duplicate in duplicates:
    print(duplicate)
priority = 0
for i in duplicates:
    if i.islower():
        priority += ord(i)-96
    else:
        priority += ord(i)-38
print(priority)
