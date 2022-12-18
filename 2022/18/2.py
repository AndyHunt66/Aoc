from collections import defaultdict


def isInternal(void: list, recurse: bool):
    if void in data:
        # print("This void is not a void ", void)
        return False
    if void in internalVoids:
        # print("Already checked this one", void)
        return True

    xMinusBlocked = False
    for x in range(void[0], minX - 1, -1):
        if [x, void[1], void[2]] in data:
            ## Check the *previous* block
            if recurse :
                if isInternal([x+1, void[1], void[2]], False):
                    xMinusBlocked = True
                    break
                else:
                    return False
            else:
                xMinusBlocked = True
                break
    if not xMinusBlocked:
        return False

    xPlusBlocked = False
    for x in range(void[0], maxX + 2):
        if [x, void[1], void[2]] in data:
            if recurse:
                if isInternal([x-1, void[1], void[2]], False):
                    xPlusBlocked = True
                    break
                else:
                    return False
            else:
                xPlusBlocked = True
                break
    if not xPlusBlocked:
        return False

    yMinusBlocked = False
    for y in range(void[1], minY - 2, -1):
        if [void[0], y, void[2]] in data:
            if recurse:
                if isInternal([void[0], y+1, void[2]], False):
                    yMinusBlocked = True
                    break
                else:
                    return False
            else:
                yMinusBlocked = True
                break
    if not yMinusBlocked:
        return False

    yPlusBlocked = False
    for y in range(void[1], maxY + 2):
        if [void[0], y, void[2]] in data:
            if recurse:
                if isInternal([void[0], y-1, void[2]], False):
                    yPlusBlocked = True
                    break
                else:
                    return False
            else:
                yPlusBlocked = True
                break
    if not yPlusBlocked:
        return False

    zMinusBlocked = False
    for z in range(void[2], minZ - 2, -1):
        if [void[0], void[1], z] in data:
            if recurse:
                if isInternal([void[0], void[1], z+1], False):
                    zMinusBlocked = True
                    break
                else:
                    return False
            else:
                zMinusBlocked = True
                break
    if not zMinusBlocked:
        return False

    zPlusBlocked = False
    for z in range(void[2], maxZ + 2):
        if [void[0], void[1], z] in data:
            if recurse:
                if isInternal([void[0], void[1], z-1], False):
                    zPlusBlocked = True
                    break
                else:
                    return False
            else:
                zPlusBlocked = True
                break
    if not zPlusBlocked:
        return False

    return True


# inFile = './smallTestInput.txt'
inFile = './testInput.txt'
inFile = './input.txt'

data = [[int(x), int(y), int(z)] for (x, y, z) in [point.split(",") for point in open(inFile).read().split("\n")]]
data = sorted(data)
faces = defaultdict(lambda: 0)
for [x, y, z] in data:
    # The letter indicates which plane the surface is in
    faces["x{0}-{1}-{2}".format(x, y, z)] += 1
    faces["x{0}-{1}-{2}".format(x - 1, y, z)] += 1
    faces["y{0}-{1}-{2}".format(x, y, z)] += 1
    faces["y{0}-{1}-{2}".format(x, y - 1, z)] += 1
    faces["z{0}-{1}-{2}".format(x, y, z)] += 1
    faces["z{0}-{1}-{2}".format(x, y, z - 1)] += 1
# print(faces)

surfaceArea = sum(face == 1 for face in faces.values())
print("Surface area : {0}".format(surfaceArea))

## Part 2
externalVoids = []
internalVoids = []
voids = []
maxX = max(x for x, y, z in data)
maxY = max(y for x, y, z in data)
maxZ = max(z for x, y, z in data)
minX = min(x for x, y, z in data)
minY = min(y for x, y, z in data)
minZ = min(z for x, y, z in data)

for x in range(minX, maxX):
    for y in range(minY, maxY):
        for z in range(minZ, maxZ):
            if [x, y, z] in data:
                pass
            else:
                voids.append([x, y, z])
for void in voids:
    if isInternal(void, True):
        internalVoids.append(void)
    else:
        externalVoids.append(void)

voidFaces = defaultdict(lambda: 0)
for [x, y, z] in internalVoids:
    # The letter indicates which plane the surface is in
    voidFaces["x{0}-{1}-{2}".format(x, y, z)] += 1
    voidFaces["x{0}-{1}-{2}".format(x - 1, y, z)] += 1
    voidFaces["y{0}-{1}-{2}".format(x, y, z)] += 1
    voidFaces["y{0}-{1}-{2}".format(x, y - 1, z)] += 1
    voidFaces["z{0}-{1}-{2}".format(x, y, z)] += 1
    voidFaces["z{0}-{1}-{2}".format(x, y, z - 1)] += 1

# print("Voids:\n", voids)
# print("Lava:\n", sorted(data))
newFaces = defaultdict(lambda: 0)
for face in faces:
    if face not in voidFaces:
        newFaces[face] = faces.get(face)
#print("Internal voids\n", internalVoids)

surfaceArea = sum(face == 1 for face in newFaces.values())
print("New Surface Area: ", surfaceArea)
#
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# for xs, ys, zs in data:
#     ax.scatter(xs, ys, zs, marker=(6, 0, 0))
# plt.show()
