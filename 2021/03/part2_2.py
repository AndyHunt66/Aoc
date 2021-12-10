import copy
## 1 - Add up all the 1s in each position
## 2 - Compare the total of 1s in each position with the total number of rows
##   2a - if ( Pn(number_of_1s) >= total_rows/2) then Pn=1 otherwise Pn=0
## 3 - if ROWxPn = NumberPn  then keep ROWx
## 4 - If only 1 ROW left, stop, otherwise do it all again

#inFile = './testInput.txt'
inFile = './input.txt'

## 1 - Add up all the 1s in each position
def addAll1s(values):
    totals = []
    for i in range(len(values[0])):
        totals.append(0)
    for line in values:
        for i in range(0,len(line)):
           totals[i]+=int(line[i])
    return totals

## 2 - Compare the total of 1s in each position with the total number of rows
##   2a - if ( Pn(number_of_1s) >= total_rows/2) then Pn=1 otherwise Pn=0
def calculateGammaAndEpsilon(totals, totalNumberOfRows):
    gamma, epsilon = "", ""
    for i in range(len(totals)):
        if totals[i] >= totalNumberOfRows/2 :
            gamma=gamma+"1"
            epsilon=epsilon+"0"
        else:
            gamma=gamma+"0"
            epsilon=epsilon+"1"
    return gamma, epsilon

def calculateNewEpsilon(totals, totalNumberOfRows):
    epsilon = ""
    for i in range(len(totals)):
        if totals[i] > totalNumberOfRows/2 :
            epsilon=epsilon+"0"
        else:
            epsilon=epsilon+"1"
    return epsilon


## 3 - if ROWxPn = NumberPn  then keep ROWx
def filterPositiveValues(values,iteration,gamma):
    outValues = []
    for i in range(len(values)-1, -1,-1):
        if ( values[i][iteration] != gamma[iteration] ):
            outValues.append(values[i])
            del values[i]

    return values,outValues

## 3 - if ROWxPn = NumberPn  then discard ROWx
def filterZeroValues(values,iteration,gamma):
    outValues = []
    for i in range(len(values)-1, -1,-1):
        if ( values[i][iteration] != gamma[iteration] ):
            outValues.append(values[i])
            del values[i]

    return values,outValues


def report():
    print("---------------")
    print("Values " , values)
    print("Totals ", totals)
    print("Gamma ",gamma)
    print("Epsilon ",epsilon)
    print("Iteration", iteration)

## Main
originalValues = []
values = []
outValues = []
for line in open(inFile, 'r'):
    originalValues.append(line.strip())

iteration =0;
values = copy.copy(originalValues)
while (len(values) > 1):
    totals = addAll1s(values)
    gamma,epsilon = calculateGammaAndEpsilon(totals, len(values))
    values , outValues = filterPositiveValues(values,iteration, gamma)
    report()
    iteration+=1

oxyGenRating = gamma
print("FRIST")


iteration =0;
values = originalValues
count=0
totals = []
epsilon = ""
while (len(values) > 1):
    count=0
    for value in values:
       count+=int(value[iteration])
    totals.append(count)

    if count >= len(values)/2 :
        epsilon=epsilon+"0"
    else:
        epsilon=epsilon+"1"

    for i in range(len(values)-1,-1,-1):
        if values[i][iteration] != epsilon[iteration]:
            del values[i]
    report()
    iteration+=1



#while (len(values) > 1):
#    totals = addAll1s(values)
#    epsilon = calculateNewEpsilon(totals, len(values))
#    report()
#    values , outValues= filterZeroValues(values,iteration, epsilon)
#    iteration+=1
#report()
co2ScrubRating = values[0]

print("--Oxy ",oxyGenRating, " --CO2 ",co2ScrubRating)

lifeSupportRating = int(oxyGenRating, 2) * int(co2ScrubRating, 2)
print("Life Support Rating: ",lifeSupportRating)

## 4175451 -- too high
