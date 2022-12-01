#inFile = './testInput.txt'
inFile = './input.txt'

fh = open(inFile, 'r')

elves = []
elf = 0

for line in fh:
    if line != "\n":
        elf += int(line.strip())
    else:
        elves.append(elf)
        elf = 0
fh.close()
elves.append(elf) # Either include this line to add the last elf, or rig the input to have a blank line at the end

elves.sort()
print("part 1: ", elves[-1])
print("part 2: ", elves[-1]+elves[-2]+elves[-3])
