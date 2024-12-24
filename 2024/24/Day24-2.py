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

levels = []
tick = 0
while(True):
    levels.append([])
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
            levels[tick].append(gate)
            signals[gate] = gates[gate]['value']

    if allDone(gates):
        break
    tick = tick +1

print(signals)
print("number of ticks:",tick)
output = [str(signals[x]) for x in sorted(signals,reverse=True) if x.startswith('z')]
output = ''.join(output)
output = int(output,2)
# print(int(output,2))
print(output)
number1 = int(''.join([str(signals[x]) for x in sorted(signals,reverse=True) if x.startswith('x')]),2)
number2 = int(''.join([str(signals[x]) for x in sorted(signals,reverse=True) if x.startswith('y')]),2)

print("X: ", number1,"Y: ",number2)
target = number1 + number2
print("Target:",target)
mismatch = output ^ target
print("mismatch:",mismatch)
print("Output:       ", bin(output).replace("0b", ""))
print("Target:       ", bin(target).replace("0b", ""))
print("mismatch:             ",bin(mismatch).replace("0b", ""))
#### testinput2
# for my input, this gives:
# Output:   11111101000
# Target:        101100
# mismatch: 11111000100
# so we've got to turn all those 1s in the mismatch to 0
# z02, z06, z07, z08, z09, z10
# z02 = gnj AND wpb (1 AND 0) : so we need to chnage wpb to 1
#     wpb == nrd XOR fgs ( 1 XOR 1 )

# for my input, this gives: 11100110000011110001111100000000000000
# z14, z15, z16, z17,  need to change from 1 to 0
# z18                 needs to change form 0 to 1
# z22, z23, z24,       need to change form 0 to 1
# z25                 needs to change form 1 to 0
# z31,                needs to change from 0 to 1
# z32                                      1 to 0
# z35, z36,                                0 to 1
# z37                                      1 to 0

# swap z32 with z31
# z25, z27
# z17, z18
# something to flip all of 14,15,16 with 22,23,24

# tfw  OR cgt -> z14    (0 OR 1) = 1
# vqs XOR vss -> z15
# rgp XOR bth -> z16
# cjd XOR qtn -> z17
# jhw XOR tcv -> z18
# kdh XOR gjn -> z22
# tks XOR sbg -> z23
# dwh XOR hsk -> z24
# rmw XOR psg -> z25
# nrr AND sms -> z31
# gds XOR ghr -> z32
# y35 AND x35 -> z35
# rqf XOR pqn -> z36
# jqd XOR mhc -> z37

# All these are unique inputs
# z35 must be one of the wires to be switched, because it comes directly from input values
# ttd AND nhg -> tfw   (0 AND 0) = 0  tfw is only used once   y14 XOR x14 -> ttd
# x14 AND y14 -> cgt   (1 AND 1) = 1  cgt is only used once


# x15 XOR y15 -> vqs   1 XOR 0 = 1
# nhg XOR ttd -> vss   0 XOR 0 = 0                      y14 XOR x14 -> ttd    1 XOR 1 = 0

# ctt OR pwr -> rgp   0 OR 0 = 0     vss AND vqs -> ctt  0 AND 1 = 0
#                                    y15 AND x15 -> pwr  0 AND 1 = 0
# x16 XOR y16 -> bth

# x17 XOR y17 -> cjd
# srg OR cwb -> qtn   0 OR 0 = 0     rgp AND bth -> srg
#                                    y16 AND x16 -> cwb
#

# vrv OR fvv -> jhw    qtn AND cjd -> vrv   srg OR cwb -> qtn
#                      y17 AND x17 -> fvv
# y18 XOR x18 -> tcv

# y22 AND x22 -> kdh
# hbc OR wdr -> gjn

# x23 XOR y23 -> tks
# bjb OR hjf -> sbg

# wqr OR tqk -> dwh
# y24 XOR x24 -> hsk

# wrf OR gnt -> rmw
# y25 XOR x25 -> psg

# x31 XOR y31 -> nrr
# qnv OR bjd -> sms

# y32 XOR x32 -> gds
# pwg OR kpp -> ghr

# sgj OR ptb -> rqf
# x36 XOR y36 -> pqn

# kqk OR wbv -> jqd
# x37 XOR y37 -> mhc

# how many of the signals are only used once?
count = 0
countMap = defaultdict(lambda: 0)
for gate in gates:
    countMap[gates[gate]['inputs'][0]] = countMap[gates[gate]['inputs'][0]] +1
    countMap[gates[gate]['inputs'][1]] = countMap[gates[gate]['inputs'][1]] +1

for gate in countMap:
    if countMap[gate] == 1:
        print(gate)
print(len(countMap))