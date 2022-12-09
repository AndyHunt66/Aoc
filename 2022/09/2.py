import math
from collections import defaultdict

import numpy

# inFile = './testInput.txt'
# inFile = './testInput2.txt'
inFile = './input.txt'

ropeLength = 9

with open(inFile) as f:
    instructions = [(d, int(l)) for d, l in [i.split() for i in f.read().split("\n")]]

for knot in range(ropeLength):
    head = (0, 0)
    tail = (0, 0)
    if knot > 0:
        priorRoute = route
        route = []
        for move in priorRoute:
            previousHead = head
            head = move
            # if not adjacent
            if (abs(head[0]-tail[0]) == 2 and abs(head[1]-tail[1]) == 1) \
                    or (abs(head[0]-tail[0]) == 1 and abs(head[1]-tail[1]) == 2) \
                    or (abs(head[0]-tail[0]) == 2 and abs(head[1]-tail[1]) == 2):
                # Diagonal move
                tail = (tail[0] + numpy.sign(head[0]-tail[0]), tail[1] + numpy.sign(head[1] - tail[1]))

            elif abs(head[0]-tail[0]) > 1 or abs(head[1]-tail[1]) > 1:
                # straight move
                tail = (tail[0] + math.floor((head[0]-tail[0])/2), tail[1] + math.floor((head[1]-tail[1])/2))

            route.append(tail)

    else:
        route = []
        # route.append(tail)

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
                route.append(tail)

    visited = defaultdict(lambda: 0)
    for position in route:
        visited[position] += 1
    print("number of places visited by knot number :", knot+1, len(visited))
