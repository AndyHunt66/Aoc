This one doesn't work - starting again
import sys

def extractHighsAndLows(sourceList, target, ord):
  matches=[]
  notMatches=[]
  for i in range(len(sourceList)):
    if sourceList[i][ord] == target[ord]:
      matches.append(sourceList[i])
    else:
      notMatches.append(sourceList[i])
  return matches , notMatches

def getDominators(values):
  gammaNew, epsilonNew = 0,0
  gammaTxt, epsilonTxt = "",""
  for i in range(0,len(line)-1):
    totals[i]+=int(line[i])

  count = len(values)
  for i in range(len(line), 0,-1):
    if (totals[len(line)-i]> (count/2)):
      #print(i," ", gamma)
      gammaNew+=(2**(i-1))
      #print(i," ", gamma)
      gammaTxt=gammaTxt + "1"
      epsilonTxt=epsilonTxt + "0"
    else:
      epsilonNew+=(2**(i-1))
      epsilonTxt=epsilonTxt + "1"
      gammaTxt=gammaTxt + "0"
  print(gammaNew," - ", epsilonNew)
  return gammaNew , epsilonNew

inFile = './testInput.txt'
totals=[0,0,0,0,0]
#inFile = './input.txt'
#totals=[0,0,0,0,0,0,0,0,0,0,0,0]
gammaTxt=""
epsilonTxt=""
values =[]

for line in open(inFile, 'r'):
  values.append(line.strip())
gamma, epsilon = getDominators(values)
print(totals)

print()
print("gamma   = ",gammaTxt, " ", gamma)
print("epsilon = ",epsilonTxt, " ", epsilon)
print("Power   = ", (gamma * epsilon))

nextIteration, default = extractHighsAndLows(values,gammaTxt,0)
nextIteration2, default2 = extractHighsAndLows(nextIteration,gammaTxt,1)
nextIteration3, default3 = extractHighsAndLows(nextIteration2,gammaTxt,2)
nextIteration4, default4 = extractHighsAndLows(nextIteration3,gammaTxt,3)
nextIteration5, default5 = extractHighsAndLows(nextIteration4,gammaTxt,4)
print(nextIteration)
print(nextIteration2)
print(nextIteration3)
print(nextIteration4)
print(nextIteration5)