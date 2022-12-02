from bitstring import ConstBitStream, ReadError

# inFile = './testInput.txt'
# inFile = './testInput2.txt'
inFile = './input.txt'

versions = []

s = ConstBitStream(hex=open(inFile).read().strip())
# s = ConstBitStream(hex='8A004A801A8002F478') # 16
# s = ConstBitStream(hex='620080001611562C8802118E34') # 12
# s = ConstBitStream(hex='C0015000016115A2E0802F182340') # 23
# s = ConstBitStream(hex='A0016C880162017C3686B18A3D4780') # 31

def parsePackets(s):

    while True:
        try:
            endOfStream = s.peeklist([1,1,1,1,1,1,1,1])
        except ReadError:
            ## We've come to the end of the input
            break
        packetVersion = s.read('uint:3')
        packetTypeId = s.read('uint:3')
        versions.append(packetVersion)

        if packetTypeId == 4:
            ## Literal value
            valueString = ''
            while s.read('bin:1') == "1":
                valueString = valueString + s.read('bin:4')
            valueString = valueString + s.read('bin:4')
        else:
            ## Operator Packet
            lengthTypeId = s.read('bin:1')
            if lengthTypeId == "0":
                lenSubPackets = int(s.read('bin:15'), 2)
                parsePackets(s)
            else:  # lengthTypeId == 1
                numSubPackets = int(s.read('bin:11'), 2)
                parsePackets(s)


parsePackets(s)
print(sum(versions))