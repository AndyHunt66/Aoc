from collections import defaultdict
import time

# start = time.time()
inFile = './testInput.txt'
inFile = './testInput2.txt'
inFile = './input.txt'

def allDone(gates):
    for gate in gates:
        if gates[gate]['value'] is None:
            return False
    return True

f = open(inFile, 'r')
signals = {}
gates = {}
s, g =   f.read().split('\n\n')
s = s.split('\n')
g = g.split('\n')
for node in s:
    signals[node[:3]] = int(node[-1:])
for gate in g:
    gate = gate.split(' ')
    if len(gate) > 1:
        gates[gate[4]] = {'inputs': [gate[0],gate[2]], 'oper':gate[1], 'value': None}

print(signals)
print(gates)

tick = 0
while(True):
    tick = tick +1
    for gate in gates:
        if gates[gate]['value'] is not None:
            continue
        if gates[gate]['inputs'][0] in signals and gates[gate]['inputs'][1] in signals:
            if gates[gate]['oper'] == 'AND':
                gates[gate]['value'] = signals[gates[gate]['inputs'][0]] and signals[gates[gate]['inputs'][1]]
            if gates[gate]['oper'] == 'OR':
                gates[gate]['value'] = signals[gates[gate]['inputs'][0]] or signals[gates[gate]['inputs'][1]]
            if gates[gate]['oper'] == 'XOR':
                gates[gate]['value'] = signals[gates[gate]['inputs'][0]] ^ signals[gates[gate]['inputs'][1]]
            signals[gate] = gates[gate]['value']

    if allDone(gates):
        break
print(signals)
print("number of ticks:",tick)
output = [str(signals[x]) for x in sorted(signals,reverse=True) if x.startswith('z')]
output = ''.join(output)
print(int(output,2))