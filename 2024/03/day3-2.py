import re

testInput = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
inFile = './input.txt'


f = open(inFile, 'r')
input = f.read()


input2 = "do()"+"xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"+"don't()"
input2 = "do()"+input+"don't()"
# print(input2)


operations2 = re.findall("(do\(\)|mul\(\d+?,\d+?\)|don't\(\))", input2)
runningTotal = 0
do = True
operations3 = []
# for i in range(0,len(operations2)):
for operation in operations2:
    if do:
        if operation == "do()":
            pass
        elif operation.startswith("mul("):
            operations3.append(operation)
        elif operation == "don't()":
            do = False
        else:
            print(operation)
            print("STOP")
            exit()
    else:
        if operation == "do()":
            do = True

print(len(operations3))
print(operations3)

for text in operations3:
    operations = [operation.split(',') for operation in re.findall("mul\((\d+,\d+)\)", text)]
    runningTotal = runningTotal + sum([int(a) * int(b) for a, b in operations])

print(runningTotal)