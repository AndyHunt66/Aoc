from collections import defaultdict

inFile = './testInput.txt'
inFile = './testInput2.txt'
inFile = './input.txt'

stoneMap = defaultdict(int)
blinks = 75

f = open(inFile, 'r')

for i in f.readline().split(' '):
    stoneMap[int(i)] = 1

newStones = defaultdict(int)

for i in range(blinks):
    # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    if 0 in stoneMap:
        newStones[1] = stoneMap.pop(0)
    for k,v in stoneMap.items():
        # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
        if len(str(k)) %2 == 0:
            firstStone, secondStone = str(k)[:int(len(str(k))/2)], str(k)[int(len(str(k))/2):]
            newStones[int(firstStone)] = newStones[int(firstStone)] + v
            newStones[int(secondStone)] = newStones[int(secondStone)] + v
        else:
        # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
            newStones[k * 2024] = newStones[k * 2024] + v
    stoneMap = newStones.copy()
    newStones = defaultdict(int)
    print(stoneMap)


print(sum(stoneMap.values()))
