from collections import defaultdict


def newinsert(localtemplate: dict, subs: dict) -> dict:
#    newTemplate = copy.deepcopy(localtemplate)
    newTemplate = defaultdict(lambda: [])
    for insertionpoint in localtemplate.keys():
        if localtemplate[insertionpoint] == 0:
            continue
        inserted = subs[insertionpoint[0] + insertionpoint[1]]

        if newTemplate[insertionpoint[0], inserted]:
            newTemplate[insertionpoint[0], inserted] += localtemplate[insertionpoint]
        else:
            newTemplate[insertionpoint[0], inserted] = localtemplate[insertionpoint]

        if newTemplate[inserted, insertionpoint[1]]:
            newTemplate[inserted, insertionpoint[1]] += localtemplate[insertionpoint]
        else:
            newTemplate[inserted, insertionpoint[1]] = localtemplate[insertionpoint]

    return newTemplate


def maxandMinElement(localtemplate: dict[str, int]) -> dict:
    countinglist = {}
    # Count the number of times an element appears as the second
    #  part of a pair.
    for element1, element2 in localtemplate:
        if element2 in countinglist:
            countinglist[element2] += localtemplate[element1, element2]
        else:
            countinglist[element2] = localtemplate[element1, element2]

    # Accomodate the first element
    countinglist[firstTwoElements[0]] += localtemplate[firstTwoElements]

    commonestLetter = max(countinglist, key=countinglist.get)
    commonestCount = countinglist.get(commonestLetter)
    leastLetter = min(countinglist, key=countinglist.get)
    leastCount = countinglist.get(leastLetter)
    return {"maxLetter": commonestLetter, "maxCount": commonestCount, "minLetter": leastLetter, "minCount": leastCount}


## Are we running Part 1 or Part 2 of the puzzle?
PART = 2
numiterations = 0
if PART == 1:
    numiterations = 10
else:
    numiterations = 40

#inFile = './testInput1.txt'
inFile = './input.txt'

substitutions = dict()
template = defaultdict(lambda: [])
firstTwoElements = []
with open(inFile, 'r') as fh:
    for line in fh:
        if line == "\n":
            continue
        if "->" in line:
            substitutions[line.strip().split(" -> ")[0]] = line.strip().split(" -> ")[1]
        else:
            linelist = list(line.strip())
            firstTwoElements = (linelist[0], linelist[1])
            for x, y in zip(linelist, linelist[1:]):
                if template[(x,y)]:
                    template[(x,y)] += 1
                else:
                    template[(x, y)] = 1


print(substitutions)
print(template)
for i in range(1, numiterations+1):
    template = newinsert(template, substitutions)
    firstTwoElements = (firstTwoElements[0], substitutions[firstTwoElements[0]+firstTwoElements[1]])
    print("After Run ", i, " ", template)
    print("First Two: ", firstTwoElements)

results = maxandMinElement(template)
print(results)
print("Answer is ", results["maxCount"] - results["minCount"])

# H 4004
# N 598
# Answer is  3406
