import sys

#inFile = './testInput.txt'
inFile = './input.txt'
increases=0
decreases=0
statics=0
previous=0

fh =  open(inFile, 'r')
previous = int(fh.readline().rstrip('\r\n'))
print("First Line: ", previous)


for line in fh:

    line = int(line.strip())
    sys.stdout.write("Line: " + str(line))
    if line > previous:
      increases+=1
      print("    increase    ", increases, "  ", decreases)
    elif line < previous:
      decreases+=1
      print("    decrease    ", increases, "  ", decreases)
    else :
      statics+=1
    previous = line
 #   input()

fh.close()
print("Increases:", increases)
print("Decreases:", decreases)
print("Statics  :", statics)
