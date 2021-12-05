import sys

#inFile = './testInput.txt'
inFile = './input.txt'
totals=[0,0,0,0,0,0,0,0,0,0,0,0]
count, gamma, epsilon=0,0,0
gammaTxt=""
epsilonTxt=""

for line in open(inFile, 'r'):
  count+=1
  for i in range(0,len(line)-1):
    totals[i]+=int(line[i])
#print("Length line: " , len(line))
#print(len(totals))
#print(1**3)
for i in range(len(line), 0,-1):
  if (totals[len(line)-i]> (count/2)):
    #print(i," ", gamma)
    gamma+=(2**(i-1))
    #print(i," ", gamma)
    gammaTxt=gammaTxt + "1"
    epsilonTxt=epsilonTxt + "0"
  else:
    epsilon+=(2**(i-1))
    epsilonTxt=epsilonTxt + "1"
    gammaTxt=gammaTxt + "0"

print(totals)
print(count)

print()
print("gamma   = ",gammaTxt, " ", gamma)
print("epsilon = ",epsilonTxt, " ", epsilon)
print("Power   = ", (gamma * epsilon))

