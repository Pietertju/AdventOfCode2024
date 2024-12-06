def getInput():
    lines = []
    with open("./input.txt") as file:
        lines = [list(line.strip()) for line in file.read().split("\n")]
        for x, line in enumerate(lines):
            for y, character in enumerate(line):
                if character == '^':
                    return lines, (x, y) 
                        
def partOne(lines, startX, startY):
    sum = 0

    directions = [(-1, 0), (0, 1), (1,0), (0,-1)]
    directionIndex = 0
    currentDirection = directions[directionIndex]

    curX = startX
    curY = startY

    visitedPlaces = [([0] * len(lines[0])) for x in range(len(lines))]
    
    while (not ((curX == 0 or curX == len(lines)-1) or (curY == 0 or curY == len(lines[curX])-1))):
        visitedPlaces[curX][curY] = 1
        nextX = curX + currentDirection[0]
        nextY = curY + currentDirection[1]
        while lines[nextX][nextY] == '#':
            directionIndex += 1
            if directionIndex >= len(directions):
                directionIndex = 0
            currentDirection = directions[directionIndex]
            nextX = curX + currentDirection[0]
            nextY = curY + currentDirection[1]
        curX = nextX
        curY = nextY

    visitedPlaces[curX][curY] = 1  

    for x in visitedPlaces:
        for y in x:
            sum += y

    print("Part one: ", sum)
    return visitedPlaces
    
def partTwo(lines, startX, startY, route):
    directions = [(-1, 0), (0, 1), (1,0), (0,-1)]
    sum = 0
    for x, _ in enumerate(lines):
        for y, _ in enumerate(lines[x]):
            if lines[x][y] == '.' and route[x][y] == 1:
                lines[x][y] = "#"
                isLoop = False
                directionIndex = 0
                currentDirection = directions[directionIndex]
                curX = startX
                curY = startY
                hitObstaclesAndDirection = []
                while (not ((curX == 0 or curX == len(lines)-1) or (curY == 0 or curY == len(lines[curX])-1))):
                    nextX = curX + currentDirection[0]
                    nextY = curY + currentDirection[1]

                    while lines[nextX][nextY] == '#':

                        for ((hitX, hitY), hitDirection)  in hitObstaclesAndDirection:
                            if hitX == nextX and hitY == nextY and hitDirection == directionIndex:
                                isLoop = True
                                break
                        if isLoop:
                            break
                        hitObstaclesAndDirection.append(((nextX,nextY), directionIndex))
                        directionIndex += 1
                        if directionIndex >= len(directions):
                            directionIndex = 0
                        currentDirection = directions[directionIndex]
                        nextX = curX + currentDirection[0]
                        nextY = curY + currentDirection[1]

                    if isLoop:
                        break
                    curX = nextX
                    curY = nextY

                if isLoop:
                    sum += 1
                lines[x][y] = '.'

    print("Part Two: ", sum)

lines, (startX, startY) = getInput()
route = partOne(lines, startX, startY)
partTwo(lines, startX, startY, route)