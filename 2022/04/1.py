import re

# inFile = './testInput.txt'
inFile = './input.txt'
total1 = 0
total2 = 0
data = open(inFile).read().split("\n")
for pair in data:
    w,x,y,z = [int(i) for i in (re.split('[,-]', pair))]
    if w == y or x == z:
        total1 += 1
    elif (w < y and x > z) or (w > y and x < z):
            total1 += 1
    elif (w < y and x < y) or (w > z and x > z):
        pass
    else:
        total2 += 1
total2 += total1
print(total1)
print(total2)

