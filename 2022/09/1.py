from collections import defaultdict

# inFile = './testInput.txt'
inFile = './input.txt'

with open(inFile) as f:
    instructions = [(d, int(l)) for d,  l in [i.split() for i in f.read().split("\n")]]
print(instructions)
route = defaultdict(lambda: 0)
head = (0, 0)
tail = (0, 0)
route[tail] = 1
for direction, distance in instructions:
    for i in range(distance):
        previousHead = head
        if direction == "R":
            head = (head[0]+1, head[1])
        elif direction == "L":
            head = (head[0]-1, head[1])
        elif direction == "U":
            head = (head[0], head[1]+1)
        elif direction == "D":
            head = (head[0], head[1]-1)
        else:
            print("Something's gone wrong:", head, tail)

        # if not adjacent
        if abs(head[0]-tail[0]) > 1 or abs(head[1]-tail[1]) > 1:
            tail = previousHead
        route[tail] += 1
visited = len(route)
print("number of places visited :", visited)
