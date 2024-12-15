def getInput():
    with open("./test.txt") as file:
        lines = file.read().split("\n")
        
    grid = []
    readingCommands = False
    commandString = ""
    for line in lines:
        if line.isspace() or line == "":
            readingCommands = True
            continue
        if readingCommands:
            commandString += line.strip()
        else:
            grid.append(list(line.strip()))


    for x, line in enumerate(grid):
        for y, character in enumerate(line):
            if character == '@':
                return grid, (x, y), commandString
    
up = (-1, 0)
down = (1, 0)
right = (0, 1)
left = (0, -1)

def prettyPrintGrid(grid, pos):
    (x, y) = pos
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if i == x and j == y:
                print("@", end="")
            else:
                print(c, end="")
        print()

def partOne(grid, startX, startY, commands):
    sum = 0
    pos = (startX, startY)
    grid[startX][startY] = "."
    for char in commands:
        if char == "^":
            direction = up
        elif char == "v":
            direction = down
        elif char == ">":
            direction = right
        elif char == "<":
            direction = left

        (x, y) = pos

        (dx, dy) = direction
        (newX, newY) = (x + dx, y + dy)
        if grid[newX][newY] == "#":
            continue
        elif grid[newX][newY] == ".":
            pos = (newX, newY)
        elif grid[newX][newY] == "O":
            (nextX, nextY) = (newX + dx, newY + dy)
            while grid[nextX][nextY] == "O":
                (nextX, nextY) = (nextX + dx, nextY + dy)
            if grid[nextX][nextY] == ".":
                grid[nextX][nextY]  = "O"
                grid[newX][newY] = "."
                pos = (newX, newY)

    # prettyPrintGrid(grid, pos)

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == "O":
                sum += (100*x) + y

    print("Part One: ", sum)

def moveBoxes(grid, pos, boxQueue, direction):
    possible = True
    allBoxes = []

    (dx, dy) = direction
    while len(boxQueue) > 0:
        (boxX, boxY, character) = boxQueue.pop()
        allBoxes.append((boxX, boxY, character))
        (newBoxX, newBoxY) = (boxX + dx, boxY + dy)
        if grid[newBoxX][newBoxY] == "#":
            possible = False
            break
        elif grid[newBoxX][newBoxY] == "[":
            boxLeft = (newBoxX, newBoxY, "[")
            boxRight = (newBoxX, newBoxY+1, "]")
            if boxLeft not in allBoxes:
                boxQueue.append(boxLeft)
            if boxRight not in allBoxes:
                boxQueue.append(boxRight)
        elif grid[newBoxX][newBoxY] == "]":
            boxRight = (newBoxX, newBoxY, "]")
            boxLeft = (newBoxX, newBoxY-1, "[")
            if boxLeft not in allBoxes:
                boxQueue.append(boxLeft)
            if boxRight not in allBoxes:
                boxQueue.append(boxRight)

    if possible:
        for box in allBoxes:
            (boxX, boxY, c) = box
            grid[boxX][boxY] = "."
        for box in allBoxes:
            (boxX, boxY, c) = box
            (newBoxX, newBoxY) = (boxX + dx, boxY + dy)
            grid[newBoxX][newBoxY] = c
        (x, y) = pos
        pos = (x + dx, y + dy)
    return grid, pos


def partTwo(grid, startX, startY, commands):
    sum = 0
    newGrid = []
    for line in grid:
        newLine = []
        for character in line:
            if character == ".":
                newLine.append(".")
                newLine.append(".")
            elif character == "O":
                newLine.append("[")
                newLine.append("]")
            elif character == "@":
                startY = len(newLine) 
                newLine.append(".")
                newLine.append(".")
            elif character == "#":
                newLine.append("#")
                newLine.append("#")
        newGrid.append(newLine)

    pos = (startX, startY)
    
    for char in commands:
        if char == "^":
            direction = up
        elif char == "v":
            direction = down
        elif char == ">":
            direction = right
        elif char == "<":
            direction = left

        (x, y) = pos

        (dx, dy) = direction
        (newX, newY) = (x + dx, y + dy)
        if newGrid[newX][newY] == "#":
            continue
        elif newGrid[newX][newY] == ".":
            pos = (newX, newY)
        elif newGrid[newX][newY] == "[":
            boxLeft = (newX, newY, "[")
            boxRight = (newX, newY+1, "]")
            newGrid, pos = moveBoxes(newGrid, pos, [boxLeft, boxRight], direction)
        elif newGrid[newX][newY] == "]":
            boxRight = (newX, newY, "]")
            boxLeft = (newX, newY-1, "[")
            newGrid, pos = moveBoxes(newGrid, pos, [boxLeft, boxRight], direction)

    # prettyPrintGrid(newGrid, pos)

    for x in range(len(newGrid)):
        for y in range(len(newGrid[x])):
            if newGrid[x][y] == "[":
                sum += (100*x) + y
    print("Part Two: ", sum)
        
grid, (startX, startY), commands = getInput()
partOneGrid = [[c for c in line] for line in grid]
partOne(partOneGrid, startX, startY, commands)
partTwo(grid, startX, startY, commands)
