def getInput():
    with open("./input.txt") as file:
        lines = file.read().split("\n")
        
    obstacles = []
    for line in lines:
        split = line.split(",")
        x = int(split[0].strip())
        y= int(split[1].strip())
        obstacles.append((y, x))

    return obstacles

def prettyPrintGrid(grid):
    for line in grid:
        print()
        for c in line:
            print(c, end="")

right = (0, 1)
up = (-1, 0)
left = (0, -1)
down = (1, 0)

directions = [right, up, left, down]

gridSize = 71
obstacleCount = 1024

def inBound(x, y, gridSize):
    return 0 <= x < gridSize and 0 <= y < gridSize

def partOne(obstacles):
    grid = [(['.'] * gridSize) for x in range(gridSize)]
    shortestPathGrid = [([0] * gridSize) for x in range(gridSize)]

    for index in range(obstacleCount):
        (x, y) = obstacles[index]
        grid[x][y] = '#'
        
    position = (0, 0)

    queue = []
    queue.append((position))

    while len(queue) > 0:
        position = queue.pop()
        (x, y) = position

        nextPathLength = shortestPathGrid[x][y] + 1
        for direction in directions:
            (dx, dy) = direction
            (newX, newY) = (x + dx, y + dy)
            if inBound(newX, newY, gridSize) and grid[newX][newY] == '.':
                if shortestPathGrid[newX][newY] == 0 or nextPathLength < shortestPathGrid[newX][newY]:
                    shortestPathGrid[newX][newY] = nextPathLength
                    queue.append((newX, newY))

    print("Part One:", shortestPathGrid[gridSize-1][gridSize-1])
    
def partTwo(obstacles):
    grid = [(['.'] * gridSize) for x in range(gridSize)]

    for index in range(obstacleCount):
        (x, y) = obstacles[index]
        grid[x][y] = '#'
    
    
    for index in range(obstacleCount, len(obstacles)):
        newObstacle = obstacles[index]
        (obstacleX, obstacleY) = newObstacle
        grid[obstacleX][obstacleY] = '#'

        position = (0, 0)

        queue = []
        queue.append((position))
        
        shortestPathGrid = [([0] * gridSize) for x in range(gridSize)]

        while len(queue) > 0:
            position = queue.pop()
            (x, y) = position

            nextPathLength = shortestPathGrid[x][y] + 1
            for direction in directions:
                (dx, dy) = direction
                (newX, newY) = (x + dx, y + dy)
                if inBound(newX, newY, gridSize) and grid[newX][newY] == '.':
                    if shortestPathGrid[newX][newY] == 0 or nextPathLength < shortestPathGrid[newX][newY]:
                        shortestPathGrid[newX][newY] = nextPathLength
                        queue.append((newX, newY))

        if shortestPathGrid[gridSize-1][gridSize-1]  == 0:
            break
    print("Part Two:", obstacleY, ",", obstacleX)

obstacles = getInput()

partOne(obstacles)
partTwo(obstacles)
