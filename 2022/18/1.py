from collections import defaultdict
# from matplotlib import pyplot as plt

# inFile = './smallTestInput.txt'
# inFile = './testInput.txt'
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

# print("Voids:\n",voids)
# print("Lava:\n",sorted(data))
#
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# for xs, ys, zs in data:
#     ax.scatter(xs, ys, zs )
# plt.show()
internalVoids = []
for void in voids:
    xMinusBlocked = False
    for x in range(void[0], minX - 1, -1):
        if [x, void[1], void[2]] in data:
            xMinusBlocked = True
            break
    if not xMinusBlocked:
        continue
    xPlusBlocked = False
    for x in range(void[0], maxX + 2):
        if [x, void[1], void[2]] in data:
            xPlusBlocked = True
            break
    if not xPlusBlocked:
        continue

    yMinusBlocked = False
    for y in range(void[1], minY - 2, -1):
        if [void[0], y, void[2]] in data:
            yMinusBlocked = True
            break
    if not yMinusBlocked:
        continue
    yPlusBlocked = False
    for y in range(void[1], maxY + 2):
        if [void[0], y, void[2]] in data:
            yPlusBlocked = True
            break
    if not yPlusBlocked:
        continue

    zMinusBlocked = False
    for z in range(void[2], minZ - 2, -1):
        if [void[0], void[1], z] in data:
            zMinusBlocked = True
            break
    if not zMinusBlocked:
        continue
    zPlusBlocked = False
    for z in range(void[2], maxZ + 2):
        if [void[0], void[1], z] in data:
            zPlusBlocked = True
            break
    if not zPlusBlocked:
        continue

    internalVoids.append(void)

# print("Internal Voids:\n",internalVoids)

voidFaces = defaultdict(lambda: 0)
for [x, y, z] in internalVoids:
    # The letter indicates which plane the surface is in
    voidFaces["x{0}-{1}-{2}".format(x, y, z)] += 1
    voidFaces["x{0}-{1}-{2}".format(x - 1, y, z)] += 1
    voidFaces["y{0}-{1}-{2}".format(x, y, z)] += 1
    voidFaces["y{0}-{1}-{2}".format(x, y - 1, z)] += 1
    voidFaces["z{0}-{1}-{2}".format(x, y, z)] += 1
    voidFaces["z{0}-{1}-{2}".format(x, y, z - 1)] += 1

shared_items = {k: faces[k] for k in faces if k in voidFaces}
print("Shared: ", len(shared_items))

newFaces = defaultdict(lambda: 0)
for face in faces:
    if face not in voidFaces:
        newFaces[face] = faces.get(face)

shared_items = {k: newFaces[k] for k in newFaces if k in voidFaces}
print("Shared: ", len(shared_items))
surfaceArea = sum(face == 1 for face in newFaces.values())
print("New Surface Area: ", surfaceArea)

# 2002 , the output of this program, is too low
# it only took a couple of guesses to get to the righ tvalue,
#  but I hav eno idea where the error in the program is
# 2008 too low
# 2014 too high
# 2010 not right
# 2012 -> Correct!
