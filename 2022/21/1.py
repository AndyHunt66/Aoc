# inFile = './testInput.txt'
inFile = './input.txt'


class Monkey:
    def __init__(self, x):
        a, *b = x.split(' ')
        self.name = a.strip(':')
        if len(b) > 1:
            self.op1 = b[0]
            self.op2 = b[2]
            self.op = b[1]
            self.number = 0
        else:
            self.number = int(b[0])


monkeys = dict()
lines = [*map(Monkey, open(inFile).read().split('\n'))]
for monkey in lines:
    monkeys[monkey.name] = monkey
run = 0

while True:
    for m in monkeys.values():
        if m.number == 0:
            if monkeys[m.op1].number != 0 and monkeys[m.op2].number != 0:
                calc = str(monkeys[m.op1].number) + m.op + str(monkeys[m.op2].number)
                m.number = eval(calc)
    if monkeys['root'].number != 0:
        break
print(monkeys['root'].number)

