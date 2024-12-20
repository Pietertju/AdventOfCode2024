def getInput():
    with open("./input.txt") as file:
        lines = file.read().split("\n")
        
    grid = [list(line) for line in lines]

    for x, line in enumerate(grid):
        for y, character in enumerate(line):
            if character == 'S':
                startX = x
                startY = y
            if character == "E":
                endX = x
                endY = y

    return grid, (startX, startY), (endX, endY)

right = (0, 1)
up = (-1, 0)
left = (0, -1)
down = (1, 0)

directions = [right, up, left, down]

def inBound(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[x])

def partOne(grid, endPos):
    distanceFromEndGrid = [([0] * len(grid[x])) for x in range(len(grid))]

    queue = []
    queue.append((endPos))
    previous = (-1, -1)

    cheatDuration = 2
    saveThreshold = 100

    while len(queue) > 0:
        position = queue.pop(0)
        (prevX, prevY) = previous
        (x, y) = position
        nextPathLength = distanceFromEndGrid[x][y] + 1

        # single step size
        for direction in directions:
            (dx, dy) = direction
            (newX, newY) = (x + dx, y + dy)
            if inBound(newX, newY, grid) and grid[newX][newY] != '#' and not (newX == prevX and newY == prevY):
                distanceFromEndGrid[newX][newY] = nextPathLength
                queue.append((newX, newY))
                break

        previous = position

    answer = 0
    for x in range(len(distanceFromEndGrid)):
        for y in range(len(distanceFromEndGrid[x])):
            distanceToEnd = distanceFromEndGrid[x][y]
            if distanceToEnd >= saveThreshold + cheatDuration:
                for direction in directions:
                    (dx, dy) = direction
                    (newX, newY) = (x + (dx*cheatDuration), y + (dy*cheatDuration))

                    if inBound(newX, newY, grid) and grid[newX][newY] != '#':
                        nextDistanceToEnd = distanceFromEndGrid[newX][newY]
                        if nextDistanceToEnd < distanceToEnd:
                            skippedDistance = (distanceToEnd-nextDistanceToEnd) - cheatDuration
                            if skippedDistance >= saveThreshold:
                                answer += 1
    
    print("Part One:", answer)
    return distanceFromEndGrid

def partTwo(grid, distanceGrid):
    distanceMap = {}

    maxCheatTime = 20
    saveThreshold = 100

    for x in range(len(distanceGrid)):
        for y in range(len(distanceGrid[x])):
            if distanceGrid[x][y] > 0 or grid[x][y] == 'E': 
                distanceMap[distanceGrid[x][y]] = (x, y)

    answer = 0
    for x in range(len(distanceGrid)):
        for y in range(len(distanceGrid[x])):
            distanceToEnd = distanceGrid[x][y]
            if distanceToEnd >= saveThreshold + 2:
                for searchDistance in range(0, (distanceToEnd-(saveThreshold+2))+1):
                    (searchX, searchY) = distanceMap[searchDistance]
                    cheatDistance = abs(searchX-x) + abs(searchY-y)
                    skippedDistance = (distanceToEnd-searchDistance) - cheatDistance
                    if cheatDistance <= maxCheatTime and skippedDistance >= saveThreshold:
                        answer += 1

    print("Part Two:", answer)

grid, start, end = getInput()
distanceFromEndGrid = partOne(grid, end)
partTwo(grid, distanceFromEndGrid)