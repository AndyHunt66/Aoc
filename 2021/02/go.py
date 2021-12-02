#inFile = './testInput.txt'
inFile = './input.txt'
depth=0
xAxis=0

fh =  open(inFile, 'r')

for line in fh:
  direction = line[0]
  magnitude = int(line[line.index(" ")+1:len(line)])
  if (direction == "f"):
    xAxis+=magnitude
  if (direction == "d"):
    depth+=magnitude
  if (direction == "u"):
    depth -=magnitude


fh.close()
print("Depth:", depth)
print("xAxis:", xAxis)
print("product  :", depth * xAxis)
