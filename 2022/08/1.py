import numpy

# inFile = './testInput.txt'
inFile = './input.txt'

with open(inFile) as f:
    trees = f.read().split("\n")
    trees = [[int(tree) for tree in list(treeRow)] for treeRow in trees]
trees = numpy.array(trees)
visibles = []
viewingDistances = []

for indexY, row in enumerate(trees):
    visibleRow = []
    viewingRow = []
    for indexX, tree in enumerate(row):
        if indexX == 0 or indexX == len(row)-1 or indexY == 0 or indexY == len(trees)-1:
            visible = True
            viewingDistance = 0
        else:
            # Visibility Check
            visible = (tree > max(row[:indexX])) or (tree > max(row[indexX+1:])) or (tree > max(trees[:indexY, indexX])) or (tree > max(trees[indexY+1:, indexX]))

            # Viewing Distance Check
            viewingDistanceEast = next((i for i, blocker in enumerate(row[indexX+1:], 1) if tree <= blocker), len(row)-indexX-1)
            viewingDistanceWest = next((i for i, blocker in enumerate(reversed(row[:indexX]), 1) if tree <= blocker), indexX)
            viewingDistanceNorth = next((i for i, blocker in enumerate(reversed(trees[:indexY, indexX]), 1) if tree <= blocker), indexY)
            viewingDistanceSouth = next((i for i, blocker in enumerate(trees[indexY+1:, indexX], 1) if tree <= blocker), len(trees)-indexY-1)
            viewingDistance = viewingDistanceSouth * viewingDistanceWest * viewingDistanceEast * viewingDistanceNorth
        visibleRow.append(visible)
        viewingRow.append(viewingDistance)
    visibles.append(visibleRow)
    viewingDistances.append(viewingRow)


# print(trees)
# print(visibles)
print("Number of hidden trees: ", sum(sum(visRow) for visRow in visibles))
print("Highest scenic score: ", max(max(viewingRow) for viewingRow in viewingDistances))
