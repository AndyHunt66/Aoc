from math import floor

inFile = './testInput.txt'
# inFile = './testInput2.txt'
# inFile = './input.txt'

def printPlan(plan):
    for i in range(planY):
        print(plan[i*planX:(i+1)*planX])

def moveOne(plan, pos, move):
    if plan[pos + dist[move]] == '.':
        # Just move one square - swap the empty for the entity
        plan[pos + dist[move]] = plan[pos]
        plan[pos] = '.'
        return plan , True
    elif plan[pos + dist[move]] == '#':
        # hit a wall - no change
        return plan, False
    else:
        # Hit a box
        plan , didItMove = moveOne(plan,pos + dist[move], move)
        if didItMove:
            plan[pos + dist[move]] = plan[pos]
            plan[pos] = '.'
            return plan, True
        else:
            return plan, False
def moveTwo(plan, pos, move):
    # pos is left side of the box
    if plan[pos + dist[move]] == '#' or plan[pos + dist[move] +1 ] == '#':
        return plan, False
    if plan[pos + dist[move]] == '.' and plan[pos + dist[move] +1 ] == '.':
        # Might be a sideways move so we can't just swap
        if move == '<':
            plan[pos] = ']'
            plan[pos - 1] = '['
            plan[pos + 1] = '.'
        elif move == '>':
            plan[pos] = '.'
            plan[pos + 1] = '['
            plan[pos + 2] = ']'
        else:
            plan[pos + dist[move]] = '['
            plan[pos + dist[move] + 1] = ']'
            plan[pos] = '.'
            plan[pos + 1] = '.'
            return plan , True

    # else we hit a box
    if (plan[pos + dist[move]] == '.' or plan[pos + dist[move]+1] == '.') or (plan[pos + dist[move]] == '['):
        # We've only hit one box
        plan , didItMove = moveTwo(plan,pos + dist[move], move)
        return plan, didItMove
    else:
        # we've hit two boxes - so it must be a vertical move
        ## Check the left box
        tempLeftPlan, didItMoveLeft = moveTwo(plan, pos + dist[move] - 1, move)
        tempRightPlan, didItMoveRight = moveTwo(plan, pos + dist[move] + 1, move)

        if didItMoveRight and didItMoveLeft:
            # we can start from the tempLeft PLan and add in the moves from tight
            plan, didItMove = moveTwo(tempLeftPlan, pos + dist[move] + 1, move)
            return plan, True
        else:
            return plan, False


def moveOnePart2(plan, pos, move):
    if plan[pos + dist[move]] == '.':
        # Just move one square - swap the empty for the entity
        plan[pos + dist[move]] = plan[pos]
        plan[pos] = '.'
        return plan , True
    elif plan[pos + dist[move]] == '#':
        # hit a wall - no change
        return plan, False
    else:
        # Hit a box
        boxLeft , boxRight = 0
        if plan[pos + dist[move]] == '[':
            boxLeft = pos + dist[move]
            boxRight = pos + dist[move] + 1
        else:
            boxLeft = pos + dist[move] -1
            boxRight = pos + dist[move]

        plan , didItMove = moveTwo(plan,boxLeft + dist[move], move)
        if didItMove:
            plan[pos + dist[move]] = plan[pos]
            plan[pos] = '.'
            return plan, True
        else:
            return plan, False


def calcGPS(plan):
    gps = 0
    for idx, entity in enumerate(plan):
        if entity == 'O':
            distY = floor(idx / planX)
            distX = idx % planX
            gps = gps +  (100 * distY) + distX
    return gps

plan = []
moves = []
f = open(inFile, 'r')
a,b =  f.read().split('\n\n')
planX = a.find('\n')
planY = a.count('\n') + 1
plan = [list(a.replace('\n',''))]
moves  = list(b.replace('\n',''))

dist = {'<':-1, '^': -1 * planY, '>': 1, 'v': planY}

# part1
for moveNum, move in enumerate(moves):
    currPlan = plan[moveNum]
    startPos = currPlan.index('@')
    currPlan , didItMove = moveOne(currPlan,startPos,move)
    # printPlan((currPlan))
    plan.append(currPlan)
    # input("Press Enter to continue...")


printPlan(plan[-1])
print(calcGPS(plan[-1]))

# part 2
plan2 = []
plan2.append(plan[0])
plan2[0] = list("".join(plan2[0]).replace('#','##').replace('O','[]').replace('.','..').replace('@','@.'))
planX = planX * 2

printPlan(plan2[0])
print()
for moveNum, move in enumerate(moves):
    currPlan = plan2[moveNum]
    startPos = currPlan.index('@')
    currPlan , didItMove = moveOne(currPlan,startPos,move)
    # printPlan((currPlan))
    plan2.append(currPlan)
    # input("Press Enter to continue...")
printPlan(plan2[-1])
