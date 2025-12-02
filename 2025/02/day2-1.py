# inFile = './testInput.txt'
inFile = './input.txt'

f = open(inFile, 'r')
ranges = f.read().strip().split(',') 

total = 0
for idrange in ranges:
    for id in range(int(idrange[:idrange.index('-')]),int(idrange[idrange.index('-')+1:])+1):
        test = str(id)
        t_len = len(test)
        if t_len % 2:
            continue
        else:
            if test[:int(t_len/2)] == test[int(t_len/2):]:
                total += id

print(total)

