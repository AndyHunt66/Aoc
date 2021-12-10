import sys

#inFile = './testInput.txt'
inFile = './input.txt'
depth, xAxis, aim = 0,0,0

for line in open(inFile, 'r'):
  direction, magnitude = line.split(' ')
  magnitude = int(magnitude)
  if (direction == "down"):
    aim+=magnitude
  elif (direction == "up"):
    aim-=magnitude
  elif (direction == "forward"):
    xAxis+=magnitude
    depth=depth+(aim *magnitude)
  else:
    sys.exit("Couldn't work out what direction to go in : " + direction )    

print("Depth:", depth)
print("xAxis:", xAxis)
print("Aim: ", aim)
print("product  :", depth * xAxis)
