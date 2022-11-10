from collections import defaultdict, namedtuple

def printcode(heatmap: defaultdict[(int,int), int]):
    ## Horrible slow way of doing this, but there's not a lot of data
    maxX=0
    maxY=0
    for point in heatmap:
        if point.x > maxX:
            maxX = point.x
        if point.y > maxY:
            maxY = point.y

    for myY in range( 0, maxY +1 ):
        for myX in range(0, maxX +1):
            if heatmap[Point(myX, myY)]:
                print("X", end='')
            else:
                print(" ", end='')
        print()


def fold(heatmap: defaultdict[(int,int), int], direction: str, pos: int):
    todelete=[]
    toadd=[]
    for p in heatmap:
        if direction == "x":
            if p.x > pos:
                todelete.append(p)
                #NewX = (2pos)-x
                toadd.append(Point((2*pos)-p.x, p.y) )
        else:
            if p.y > pos:
                todelete.append(p)
                #Newy = (2pos)-y
                toadd.append(Point(p.x, (2*pos)-p.y) )

    for remove in todelete:
        del heatmap[remove]
    for add in toadd:
        heatmap[add]=1

 ## Are we running Part 1 or Part 2 of the puzzle?
PART=2

#inFile = './testInput1.txt'
inFile = './input.txt'
Point = namedtuple('Point', ['x', 'y'])

folds = []
heatmap =  defaultdict(lambda: [])
with open(inFile, 'r') as fh:
    for line in fh:
        if line == "\n":
            continue
        if line.startswith("fold"):
            folds.append(line.strip().split(" ")[2].split("="))
        else:
            heatmap[Point(int(line.strip().split(",")[0]),int(line.strip().split(",")[1] ))] = 1

print(folds)
print(heatmap)
for nextfold in folds:
    print(nextfold[0],int(nextfold[1]))
    fold(heatmap,nextfold[0],int(nextfold[1]))
    print("===========================")
    print(heatmap)
    print("Number of dots: ", len(heatmap.keys()))
    if PART == 1:
        break
printcode(heatmap)
