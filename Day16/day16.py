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

def getNewMoves(grid, x, y, directionIndex, visited, currentCost, bestPrevious, fromX, fromY):
    newMoves = []
    for i in range(3):
        newDirectionIndex = (directionIndex + (i+1)) % len(directions)
        (dx, dy) = directions[newDirectionIndex]
        (newX, newY) = (x + dx, y + dy)
        if grid[newX][newY] == ".":
            newMove = (x, y, newDirectionIndex)
            newCost = currentCost + 1000
            if abs(directionIndex - newDirectionIndex) == 2:
                continue
            
            if visited[x][y][newDirectionIndex] < 0 or newCost <= visited[x][y][newDirectionIndex]:
                newMoves.append(newMove)
                if newCost == visited[x][y][newDirectionIndex]:
                    if (fromX, fromY, directionIndex) not in bestPrevious[x][y][newDirectionIndex]:
                        bestPrevious[x][y][newDirectionIndex].append((fromX, fromY, directionIndex))
                else:
                     bestPrevious[x][y][newDirectionIndex] = [(fromX, fromY, directionIndex)]
                visited[x][y][newDirectionIndex] = newCost

    return (newMoves, visited, bestPrevious)


def partOneAndTwo(grid, startX, startY, endX, endY):
    directionIndex = 0
    minFoundCost = -1

    # [x][y][directionIndex] = shortesDistance
    visited = [[[-1, -1, -1, -1] for _ in range(len(grid[x]))] for x in range(len(grid))]
    bestPrevious = [[[[], [], [], []] for _ in range(len(grid[x]))] for x in range(len(grid))]
    visited[startX][startY][0] = 0
    visited[startX][startY][1] = 1000
    visited[startX][startY][2] = 2000
    visited[startX][startY][3] = 1000

    
    tilesTaken = [[0 for _ in range(len(grid[x]))] for x in range(len(grid))]

    moveQueue = []
    moveQueue.append((startX, startY, 0))
    moveQueue.append((startX, startY, 1))
    moveQueue.append((startX, startY, 2))
    moveQueue.append((startX, startY, 3))
    while(len(moveQueue) > 0):
        (x, y, directionIndex) = moveQueue.pop(0)
        (dx, dy) = directions[directionIndex]

        currentCost = visited[x][y][directionIndex]
        # print(x, y, directionIndex)       
        if currentCost > minFoundCost and minFoundCost > 0:
            continue

        moveIndex = 1
        while True:
            (nextX, nextY) = (x + (dx * moveIndex), y + (dy * moveIndex))
            
            if grid[nextX][nextY] == "#":
                break

            newStartCost = currentCost + moveIndex
            if grid[nextX][nextY] == "E":
                if newStartCost <= minFoundCost or minFoundCost == -1:
                    visited[nextX][nextY][directionIndex] = newStartCost
                    if newStartCost == minFoundCost:
                        if (x, y, directionIndex) not in bestPrevious[nextX][nextY][directionIndex]:
                            bestPrevious[nextX][nextY][directionIndex].append((x, y, directionIndex))
                    else:
                        bestPrevious[nextX][nextY][directionIndex] = [(x, y, directionIndex)]
                    minFoundCost = newStartCost
                    break

        
            (newMoves, visited, bestPrevious) = getNewMoves(grid, nextX, nextY, directionIndex, visited, newStartCost, bestPrevious, x, y)
                
            for move in newMoves:
                moveQueue.append(move)
            moveIndex += 1
    
    minValue = visited[endX][endY][0]
    minIndex = 0
    for index in range(len(visited[endX][endY])):
        if (visited[endX][endY][index] < minValue or minValue == -1) and visited[endX][endY][index] != -1:
            minValue = visited[endX][endY][index]
            minIndex = index

    queue = []
    for entry in bestPrevious[endX][endY][minIndex]:
        queue.append(((endX, endY, minIndex), entry))

    handled = [(endX, endY, minIndex)]

    while len(queue) > 0:
        entry = queue.pop(0)
        (toX, toY, toDirectionIndex), (fromX, fromY, directionIndex) = entry

        (dx, dy) = directions[directionIndex]
        for i in range(max(abs(toX - fromX), abs(toY - fromY)) + 1):
            newX = fromX + (i * dx)
            newY = fromY + (i * dy)

            tilesTaken[newX][newY] = 1

        if (fromX, fromY, directionIndex) not in handled:
            for item in bestPrevious[fromX][fromY][directionIndex]:
                queue.append(((fromX, fromY, toDirectionIndex ), item))
            handled.append((fromX, fromY, directionIndex))

    sum = 0

    for line in tilesTaken:
        for n in line:
            sum += n
    
    print("Part One:", minValue)
    print("Part Two: ", sum)

grid, (startX, startY), (endX, endY) = getInput()

partOneAndTwo(grid, startX, startY, endX, endY)
