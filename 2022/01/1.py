#inFile = './testInput.txt'
inFile = './input.txt'

fh =  open(inFile, 'r')
highest=0

elf=0
for line in fh:
    if line != "\n":
        elf += int(line.strip())
    else:
        if elf > highest:
            highest = elf
        elf=0
fh.close()
print("Highest:", highest)
