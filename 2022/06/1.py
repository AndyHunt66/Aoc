# inFile = './testInput.txt'
inFile = './input.txt'

message = list(open(inFile).read())
# message = list("mjqjpqmgbljsphdztnvjfqwrcgsmlb") ## 7
# message = list("bvwbjplbgvbhsrlpgdmjqwftvncz") ## 5
# message = list("nppdvjthqldpwncqszvftbrmjlhg") ## 6
# message = list("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") ## 10


def checkBuffer(buffer):
    if buffer[0] == buffer[1] \
            or buffer[0] == buffer[2] \
            or buffer[0] == buffer[3] \
            or buffer[1] == buffer[2] \
            or buffer[1] == buffer[3] \
            or buffer[2] == buffer[3]:
        return False
    else:
        return True


buf = []
for i in range(len(message)):
    buf.append(message[i])
    if len(buf) < 4:
        continue
    else:
        if checkBuffer(buf):
            print(i+1)
            exit()
        else:
            buf.pop(0)
