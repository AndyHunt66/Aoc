import sys

#inFile = './testInput.txt'
inFile = './input.txt'
increases=0
decreases=0
statics=0
previous=[]

fh = open(inFile, 'r')

for line in fh:
  previous.append(int(line.strip()))
  #print(previous)
  if (len(previous) == 4):
   if (( previous[0] + previous[1] + previous[2] ) < ( previous[1] + previous[2] + previous[3] )):
     increases+=1
   #print (" AAAAAAAAA" , previous[0] + previous[1] + previous[2] ) 
   #print (" BBBBBBBBB" , previous[1] + previous[2] + previous[3] )
   del previous[0]

fh.close()
 
print("Increases:", increases)
print("Decreases:", decreases)
print("Statics  :", statics)
