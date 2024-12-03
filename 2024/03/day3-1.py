import re

testInput = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
inFile = './input.txt'


f = open(inFile, 'r')
input = f.read()

# input = testInput
operations = [operation.split(',') for operation in re.findall("mul\((\d+,\d+)\)",input)]
total = sum([int(a) * int(b) for a,b in operations ])
print(operations)
print(total)
