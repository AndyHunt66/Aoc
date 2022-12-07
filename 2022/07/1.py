from collections import defaultdict


def parseDir(current):
    while len(totalListing) > 0:
        command = list(totalListing.pop(0).split(" "))
        if command[0] == "$":
            if command[1] == "cd":
                if command[2] == "..":
                    current = current[:current.rfind('/')]
                    continue
                else:
                    current = current + "/" + command[2]
                    continue
            if command[1] == "ls":
                while len(totalListing) > 0 and not totalListing[0].startswith("$"):
                    listing = list(totalListing.pop(0).split(" "))
                    if listing[0] == "dir":
                        continue
                    dirList[current] += int(listing[0])
                continue
            else:
                print("messed up with line ", command)
                exit(1)
        else:
            print("Messed up on line ", command)
            exit(1)


# inFile = './testInput.txt'
inFile = './input.txt'
limit = 100000
totalListing = open(inFile).read().split("\n")

dirList = defaultdict(lambda: 0)

cwd = '/root'
totalListing.pop(0)
parseDir(cwd)


totalDirs = defaultdict(lambda: 0)
for key, value in dirList.items():
    while len(key) > 0:
        totalDirs[key] += value
        key = key[:key.rfind('/')]

# print(totalDirs)
total = 0
for thisDir in totalDirs.values():
    if thisDir < limit:
        total += thisDir
print("Total of Dirs under 100000:", total)

totalFS = 70000000
requiredFS = 30000000
root = totalDirs["/root"]
unused = totalFS - root
required = requiredFS - unused
best = 99999999999
bestDir = ""
for key, value in totalDirs.items():
    if key == "/root":
        continue
    if (value > required) and value < best:
        best = value
        bestDir = key
print("Directory to delete:", bestDir, totalDirs[bestDir])
