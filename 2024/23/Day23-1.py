from collections import defaultdict

inFile = './testInput.txt'
inFile = './input.txt'

computers = defaultdict(list)
f = open(inFile, 'r')

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
            trinet = (sorted([node1,node2,node3]))
            if node1 in computers[node3] and trinet not in network:
                network.append( trinet)
                if node1.startswith('t') or node2.startswith('t') or node3.startswith('t') :
                    t_network.append( trinet )

for net in t_network:
    print(net)
    # exit()
print(len(t_network))