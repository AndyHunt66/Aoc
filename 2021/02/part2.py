import sys

#inFile = './testInput.txt'
inFile = './input.txt'
depth=0
xAxis=0
aim=0


for line in open(inFile, 'r'):
  direction = line[0]
  magnitude = int(line[line.index(" ")+1:len(line)])
  if (direction == "d"):
    aim+=magnitude
  elif (direction == "u"):
    aim-=magnitude
  elif (direction == "f"):
    xAxis+=magnitude
    depth=depth+(aim *magnitude)
  else:
    sys.exit("Couldn't work out what direction to go in : " + direction )    

print("Depth:", depth)
print("xAxis:", xAxis)
print("Aim: ", aim)
print("product  :", depth * xAxis)
