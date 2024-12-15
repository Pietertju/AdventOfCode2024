WIDTH = 101
HEIGHT = 103

def getInput():
    lines = []
    with open("./input.txt") as file:
        lines = file.read().split("\n")

    robots = []
    for line in lines:
        line = line.strip()
        split = line.split(" ")
        position = split[0].split("=")[1]
        positions = position.split(",")
        posX = int(positions[0])
        posY = int(positions[1])

        velocity = split[1].split("=")[1]
        velocities = velocity.split(",")
        velX = int(velocities[0])
        velY = int(velocities[1])

        robots.append(((posX, posY), (velX, velY)))

    return robots

def partOne(robots):
    newPositions = []
    for robot in robots:
        ((px, py), (vx, vy)) = robot
        for _ in range(100):
            px = (px + vx) % WIDTH 
            py = (py + vy) % HEIGHT
            if px < 0:
                px += WIDTH
            if py < 0:
                py += HEIGHT
        newPositions.append((px, py))
    midX = (WIDTH-1) / 2
    midY = (HEIGHT-1) / 2

    quadrantOne = 0
    quadrantTwo = 0
    quadrantThree = 0
    quadrantFour = 0

    for (x, y) in newPositions:
        if x < midX and y < midY:
            quadrantOne += 1
        if x < midX and y > midY:
            quadrantThree += 1
        if x > midX and y < midY:
            quadrantTwo += 1
        if x > midX and y > midY:
            quadrantFour += 1
    
    safetyScore = quadrantOne * quadrantTwo * quadrantThree * quadrantFour
    print("Part One: ", safetyScore)

def prettyPrintRobots(iteration, robotPositions):
    print(iteration)
    grid = [[[0] for _ in range(HEIGHT)] for _ in range(WIDTH)]
    for (px, py, _, _) in robotPositions:
        grid[px][py] = [1]

    for row in grid:
        print()
        for entry in row:
            if entry[0] == 0:
                print(".", end="")
            else: 
                print("#", end="")

def checkTwentyInRow(robotPositions):
    grid = [[0 for _ in range(HEIGHT)] for _ in range(WIDTH)]
    for (px, py, _, _) in robotPositions:
        grid[px][py] += 1
    
    longestRowConsec = 0
    for x in range(len(grid)):
        rowConsec = 0
        for y in range(len(grid[x])):
            if grid[x][y] > 0:
                rowConsec+=1
            else:
                if rowConsec > longestRowConsec:
                    longestRowConsec = rowConsec
                rowConsec = 0

    longestColConsec = 0
    for y in range(len(grid[0])):
        colConsec = 0
        for x in range(len(grid)):
            if grid[x][y] > 0:
                colConsec+=1
            else:
                if colConsec > longestColConsec:
                    longestColConsec = colConsec
                colConsec = 0

    return longestColConsec > 25 or longestRowConsec > 25

def partTwo(robots):
    robotPositions = []
    for robot in robots:
        ((px, py), (vx, vy)) = robot
        robotPositions.append((px, py, vx, vy))

    maxIterations = 9999999
    lastPercentage = 1
    for iteration in range(maxIterations):
        percentage = int((iteration/maxIterations) * 100)
        if percentage != lastPercentage:
            print(percentage, "%")
        lastPercentage = percentage
        newRobotPositions = []
        for (px, py, vx, vy) in robotPositions:
            px = (px + vx) % WIDTH 
            py = (py + vy) % HEIGHT
            if px < 0:
                px += WIDTH
            if py < 0:
                py += HEIGHT
            newRobotPositions.append((px, py, vx, vy))

        if checkTwentyInRow(newRobotPositions):
            prettyPrintRobots(iteration+1, newRobotPositions)
        
        robotPositions = newRobotPositions
        
robots = getInput()

partOne(robots)
partTwo(robots)
