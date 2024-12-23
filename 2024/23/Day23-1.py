from collections import defaultdict
import time

start = time.time()
inFile = './testInput.txt'
inFile = './input.txt'

computers = defaultdict(list)
f = open(inFile, 'r')
cache = {}
for line in f.readlines():
    nodes = line.strip().split('-')
    computers[nodes[0]].append(nodes[1])
    computers[nodes[1]].append(nodes[0])

network = []
t_network = []
for node1,nodes  in computers.items():
    # print(node1, nodes)
    for node2 in nodes:
        for node3 in computers[node2]:
            trinet = (tuple(sorted([node1,node2,node3])))
            if trinet in cache:
                continue
            if node1 in computers[node3]:
                network.append( trinet)
                cache[trinet] = True
                if node1.startswith('t') or node2.startswith('t') or node3.startswith('t') :
                    t_network.append( trinet )
            else:
                cache[trinet] = False
for net in t_network:
    print(net)
    # exit()
print(len(t_network))

end = time.time()
print("Time taken ", end - start)