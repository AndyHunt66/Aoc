import sympy as sy

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
            self.op1 = "none"
            self.op2 = "none"
            self.op = "none"


ms = dict()
lines = [*map(Monkey, open(inFile).read().split('\n'))]
for monkey in lines:
    ms[monkey.name] = monkey
run = 0

comp1 = ms['root'].op1
comp2 = ms['root'].op2

changed = True
while True:
    if not changed:
        break
    changed = False
    for key, m in ms.items():
        if m.name in comp1:
            changed = True
            if m.number == 0:
                comp1 = comp1.replace(m.name, "( {0} {1} {2} )".format(m.op1, m.op, m.op2))
            else:
                if m.name == "humn":
                    comp1 = comp1.replace(m.name, "human")
                else:
                    comp1 = comp1.replace(m.name, str(m.number))

changed = True
while True:
    if not changed:
        break
    changed = False
    for key, m in ms.items():
        if m.name in comp2:
            changed = True
            if m.number == 0:
                comp2 = comp2.replace(m.name, "( {0} {1} {2} )".format(m.op1, m.op, m.op2))
            else:
                if m.name == "humn":
                    comp2 = comp2.replace(m.name, "human")
                else:
                    comp2 = comp2.replace(m.name, str(m.number))

human = sy.Symbol('human')
# print(comp1)
print(eval(comp1))
# print(comp2)
print(eval(comp2))

print(sy.simplify(eval(comp1) - eval(comp2)))
print(sy.solve(eval(comp1) - eval(comp2)))
