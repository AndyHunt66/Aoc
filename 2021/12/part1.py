from iteration_utilities import duplicates
import copy
import sys
import re
import networkx as nx



def getnodesfromnode(node):
    pathsfromnode = []
    for path in cavemap:
        if path[0] == node:
            pathsfromnode.append(path[1])
        if path[1] == node:
            pathsfromnode.append(path[0])
    return pathsfromnode

def findpath(paths):
    for thispath in paths:
        if thispath[-1] == "end":
            continue
        possiblenodes = getnodesfromnode(thispath[-1])
        validpaths = []

        ## remove any paths that lead to small caves already visited
        for nextnode in possiblenodes:

            ## Don't go back to the start
            if nextnode == "start":
                continue
            ## Any path from here to a large (upper case) cave is valid
            if nextnode.isupper():
                validpaths.append(nextnode)
                continue
            ## Only add this path if nextnode doesn't already exist in path
            valid = True

            ## for Part 2
            doubleexists = False
            thispathlower = []
            for node in thispath:
                if node != "start" and node != "end" and node.islower():
                    if node in thispathlower:
                        doubleexists = True
                        break
                    thispathlower.append(node)

            for node in thispath:
                if PART == 1:
                    if nextnode == node:
                        valid = False
                        break
                else: #PART = 2
                    if nextnode == node and doubleexists:
                        valid = False
                        break
            if valid:
                validpaths.append(nextnode)
        if len(validpaths) == 0:
            paths.remove(thispath)
        for x in range( len(validpaths)-1, -1,-1 ):
            if x == 0:
                thispath.append(validpaths[x])
                continue
            newpath = copy.deepcopy(thispath)
            newpath.append(validpaths[x])
            paths.append(newpath)

    for thispath in paths:
            if thispath[-1] != "end":
                for path in paths:
                    print(path)
                print("===========================")
                findpath(paths)
                break

## Are we running Part 1 or Part 2 of the puzzle?
PART=2

#inFile = './testInput3.txt'
inFile = './input.txt'

cavemap  = []
with open(inFile, 'r') as fh:
    for line in fh:
        cavemap.append(line.strip().split("-"))

print(cavemap)
paths = []
path = []
path.append("start")
paths.append(path)

findpath(paths)
for path in paths:
    print(path)
print("===========================")
print("Number of paths: ", len(paths))