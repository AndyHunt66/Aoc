# https://adventofcode.com/2023/day/3

# inFile = './testInput.txt'
inFile = './input.txt'

f = open(inFile, 'r')
seeds = [int(x) for x in f.readline().strip()[7::].split(' ')]
seedsDict={}
for seed in seeds:
    seedsDict[seed]={}
print(seedsDict)

f.readline()
f.readline()
seed_to_soil=[]
soil_to_fertilizer=[]
fertilizer_to_water=[]
water_to_light=[]
light_to_temperature=[]
temperature_to_humidity=[]
humidity_to_location=[]

while 1:
    line = f.readline().strip()
    # seed-to-soil map:
    if line == '':
        break
    seed_to_soil.append( [int(x) for x in line.split()])

line = f.readline().strip()
while 1:
    line = f.readline().strip()
    # soil-to-fertilizer map:
    if line == '':
        break
    soil_to_fertilizer.append( [int(x) for x in line.split()])

line = f.readline().strip()
while 1:
    line = f.readline().strip()
    # fertilizer_to_water map:
    if line == '':
        break
    fertilizer_to_water.append( [int(x) for x in line.split()])

line = f.readline().strip()
while 1:
    line = f.readline().strip()
    # water_to_light map:
    if line == '':
        break
    water_to_light.append( [int(x) for x in line.split()])

line = f.readline().strip()
while 1:
    line = f.readline().strip()
    # light_to_temperature map:
    if line == '':
        break
    light_to_temperature.append( [int(x) for x in line.split()])

line = f.readline().strip()
while 1:
    line = f.readline().strip()
    # temperature_to_humidity map:
    if line == '':
        break
    temperature_to_humidity.append( [int(x) for x in line.split()])

line = f.readline().strip()
while 1:
    line = f.readline().strip()
    # humidity_to_location map:
    if line == '':
        break
    humidity_to_location.append( [int(x) for x in line.split()])


for seed in seedsDict:
    # seed_to_soil
    for sts in seed_to_soil:
        if seed >= sts[1] and seed <= sts[1]+sts[2]-1:
            seedsDict[seed]['soil']=(sts[0]+ seed - sts[1])
    if 'soil' not in seedsDict[seed]:
        seedsDict[seed]['soil']=seed

    # soil_to_fertilizer
    for stf in soil_to_fertilizer:
        if seedsDict[seed]['soil'] >= stf[1] and seedsDict[seed]['soil'] <= stf[1]+stf[2]-1:
            seedsDict[seed]['fertilizer'] = stf[0] + seedsDict[seed]['soil'] - stf[1]
    if 'fertilizer' not in seedsDict[seed]:
        seedsDict[seed]['fertilizer']=seedsDict[seed]['soil']

    # fertilizer_to_water
    for ftw in fertilizer_to_water:
        if seedsDict[seed]['fertilizer'] >= ftw[1] and seedsDict[seed]['fertilizer'] <= ftw[1]+ftw[2]-1:
            seedsDict[seed]['water'] = ftw[0] + seedsDict[seed]['fertilizer'] - ftw[1]
    if 'water' not in seedsDict[seed]:
        seedsDict[seed]['water']=seedsDict[seed]['fertilizer']

    # fertilizer_to_light
    for wtl in water_to_light:
        if seedsDict[seed]['water'] >= wtl[1] and seedsDict[seed]['water'] <= wtl[1]+wtl[2]-1:
            seedsDict[seed]['light'] = wtl[0] + seedsDict[seed]['water'] - wtl[1]
    if 'light' not in seedsDict[seed]:
        seedsDict[seed]['light']=seedsDict[seed]['water']

    # light_to_temperature
    for ltt in light_to_temperature:
        if seedsDict[seed]['light'] >= ltt[1] and seedsDict[seed]['light'] <= ltt[1]+ltt[2]-1:
            seedsDict[seed]['temp'] = ltt[0] + seedsDict[seed]['light'] - ltt[1]
    if 'temp' not in seedsDict[seed]:
        seedsDict[seed]['temp']=seedsDict[seed]['light']

    # temperature_to_humidity
    for tth in temperature_to_humidity:
        if seedsDict[seed]['temp'] >= tth[1] and seedsDict[seed]['temp'] <= tth[1]+tth[2]-1:
            seedsDict[seed]['humidity'] = tth[0] + seedsDict[seed]['temp'] - tth[1]
    if 'humidity' not in seedsDict[seed]:
        seedsDict[seed]['humidity']=seedsDict[seed]['temp']

    # humidity_to_location
    for htl in humidity_to_location:
        if seedsDict[seed]['humidity'] >= htl[1] and seedsDict[seed]['humidity'] <= htl[1]+htl[2]-1:
            seedsDict[seed]['location'] = htl[0] + seedsDict[seed]['humidity'] - htl[1]
    if 'location' not in seedsDict[seed]:
        seedsDict[seed]['location']=seedsDict[seed]['humidity']

print(seedsDict)
x = [ seedsDict[seed]['location'] for seed in seedsDict ]
lowestLocation = min(x)
print(lowestLocation)
