# inFile = './testInput.txt'
inFile = './input.txt'

message = list(open(inFile).read())
# message = list("mjqjpqmgbljsphdztnvjfqwrcgsmlb") ## 7
# message = list("bvwbjplbgvbhsrlpgdmjqwftvncz") ## 5
# message = list("nppdvjthqldpwncqszvftbrmjlhg") ## 6
# message = list("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") ## 10


# bufferLength = 4
bufferLength = 14
buf = [message[0]]
for i in range(1, len(message)):
    if buf.count(message[i]):
        buf.append(message[i])
        buf = buf[buf.index(message[i])+1:]
    else:
        if len(buf) == bufferLength or len(buf) == bufferLength-1:
            print(i+1)
            exit()
        else:
            buf.append(message[i])
