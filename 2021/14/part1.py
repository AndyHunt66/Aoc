
def insert(template: [], subs: dict) -> []:
    newTemplate = []
    newTemplate.append(template[0])
    for i,j in zip(template,template[1:]):
        newTemplate.append(subs[i+j])
        newTemplate.append(j)
    return newTemplate

 ## Are we running Part 1 or Part 2 of the puzzle?
PART=1
numiterations = 0
if PART == 1:
    numiterations = 10
else:
    numiterations = 40

#inFile = './testInput1.txt'
inFile = './input.txt'

substitutions = dict()
template = []
with open(inFile, 'r') as fh:
    for line in fh:
        if line == "\n":
            continue
        if "->" in line:
            substitutions[line.strip().split(" -> ")[0]] = line.strip().split(" -> ")[1]
        else:
            template = list(line.strip())

print(substitutions)
print(template)
for x in range(numiterations):
    print(x, " - ", end='')
    template = insert(template,substitutions)
#    print(template)
    print(len(template))
    print("==========================")

commonestLetter = max(template, key=template.count)
commonestCount = template.count(commonestLetter)
leastLetter =   min(template, key=template.count)
leastCount = template.count(leastLetter)
print( commonestLetter, commonestCount)
print( leastLetter, leastCount)

print("Answer is ", commonestCount - leastCount)