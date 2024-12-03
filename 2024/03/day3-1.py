import re

testInput = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
inFile = './input.txt'


f = open(inFile, 'r')
input =  f.read()

# input = testInput
operations = [operation.split(',') for operation in  re.findall("mul\((\d+,\d+)\)",input)]
total = sum([int(a) * int(b) for a,b in operations ])
print(operations)
print(total)

input2 = "do()"+"xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"+"don't()"
input2 = "do()"+input+"don't()"
# print(input2)



operations2 =  [operation.split(',') for operation in re.findall("do\(\)(.*?)don't\(\)",input2)]
print(operations2)
runningTotal = 0
for text in operations2:
    operations = [operation.split(',') for operation in  re.findall("mul\((\d+,\d+)\)",text)]
    runningTotal = runningTotal + sum([int(a) * int(b) for a,b in operations ])

print(runningTotal)