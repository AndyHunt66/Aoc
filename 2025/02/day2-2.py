
# inFile = './testInput.txt'
inFile = './input.txt'

with open(inFile, 'r') as f:
    ranges = f.read().strip().split(',') 

total = 0
for idrange in ranges:
    for id in range(int(idrange[:idrange.index('-')]),int(idrange[idrange.index('-')+1:])+1):
        test = str(id)
        t_len = len(test)
        if t_len == 1:
            # No repeateing patterns
            continue
        if t_len == 2:
            # Repeating patterns will be length 1
            if test[:int(t_len/2)] == test[int(t_len/2):]:
                total += id
                continue
        if t_len == 3:
            # Repeating patterns will be length 1
            if test[:1] == test[1:2] == test[2:]:
                total += id
                continue
        if t_len == 4:
            # Repeating patterns will be length 1 or 2
            if test[:1] == test[1:2] == test[2:3] == test[3:]:
                total += id
                continue
            if test[:2] == test[2:]:
                total += id
                continue
        if t_len == 5:
            # Repeating patterns will be length 1
            if test[:1] == test[1:2] == test[2:3] == test[3:4] == test[4:]:
                total += id
                continue
        if t_len == 6:
            # Repeating patterns will be length 1, 2 or 3
            if test[:1] == test[1:2] == test[2:3] == test[3:4] == test[4:5] == test[5:]:
                total += id
                continue
            if test[:2] == test[2:4] == test[4:]:
                total += id
                continue
            if test[:3] == test[3:] :
                total += id
                continue
        if t_len == 7:
            # Repeating patterns will be length 1
            if test[:1] == test[1:2] == test[2:3] == test[3:4] == test[4:5] == test[5:6]== test[6:]:
                total += id
                continue
        if t_len == 8:
            # Repeating patterns will be length 1, 2 or 4
            if test[:1] == test[1:2] == test[2:3] == test[3:4] == test[4:5] == test[5:6] == test[6:7] == test[7:]:
                total += id
                continue
            if test[:2] == test[2:4] == test[4:6] == test[6:]:
                total += id
                continue
            if test[:4] == test[4:] :
                total += id
                continue
        if t_len == 9:
            # Repeating patterns will be length 1 or 3
            if test[:1] == test[1:2] == test[2:3] == test[3:4] == test[4:5] == test[5:6] == test[6:7] == test[7:8] == test[8:]:
                total += id
                continue
            if test[:3] == test[3:6] == test[6:]:
                total += id
                continue
        if t_len == 10:
            # Repeating patterns will be length 1,2 or 5
            if test[:1] == test[1:2] == test[2:3] == test[3:4] == test[4:5] == test[5:6] == test[6:7] == test[7:8] == test[8:9] == test[9:]:
                total += id
                continue
            if test[:2] == test[2:4] == test[4:6] == test[6:8] == test[8:]:
                total += id
                continue
            if test[:5] == test[5:]:
                total += id
                continue


print(total)

