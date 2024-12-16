def getInput():
    lines = []
    with open("./input.txt") as file:
        lines = [list(line.strip()) for line in file.read().split("\n")]

    return lines

def floodFill(grid, floodFilledGrid, x, y, regionIndex):
    character = grid[x][y]
    queue = []
    queue.append((x,y))
    while len(queue) > 0:
        coords = queue.pop()
        x = coords[0]
        y = coords[1]
        floodFilledGrid[x][y] = regionIndex
        # left
        left = (x, y-1)
        if 0 <= left[0] < len(grid) and 0 <= left[1] < len(grid[x]) and grid[left[0]][left[1]] == character and floodFilledGrid[left[0]][left[1]] == 0:
            queue.append(left)
        # up
        up = (x+1, y)
        if 0 <= up[0] < len(grid) and 0 <= up[1] < len(grid[x]) and grid[up[0]][up[1]] == character and floodFilledGrid[up[0]][up[1]] == 0:
            queue.append(up)
        # right
        right = (x, y+1)
        if 0 <= right[0] < len(grid) and 0 <= right[1] < len(grid[x]) and grid[right[0]][right[1]] == character and floodFilledGrid[right[0]][right[1]] == 0:
            queue.append(right)
        # down
        down = (x-1, y)
        if 0 <= down[0] < len(grid) and 0 <= down[1] < len(grid[x]) and grid[down[0]][down[1]] == character and floodFilledGrid[down[0]][down[1]] == 0:
            queue.append(down)
    return floodFilledGrid

def partOne(grid):
    sum = 0

    floodFilledGrid = [([0] * len(grid[0])) for x in range(len(grid))]

    regionIndex = 1

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if floodFilledGrid[x][y] == 0:
                floodFilledGrid = floodFill(grid, floodFilledGrid, x, y, regionIndex)
                regionIndex += 1

    for region in range(regionIndex):
        testRegion = region+1

        # count area and parameter
        area = 0
        perimeter = 0
        for x in range(len(floodFilledGrid)):
            for y in range(len(floodFilledGrid[x])):
                if floodFilledGrid[x][y] == testRegion:
                    area+=1
                    if y == 0 or y == len(floodFilledGrid[x]) - 1:
                        perimeter += 1
                    if x == 0 or x == len(floodFilledGrid) - 1:
                        perimeter += 1

                    # top
                    newX = x-1
                    newY = y
                    if 0 <= newX < len(floodFilledGrid) and 0 <= newY < len(floodFilledGrid[x]):
                        if floodFilledGrid[newX][newY] != testRegion:
                            perimeter += 1                   

                    # left
                    newX = x
                    newY = y-1
                    if 0 <= newX < len(floodFilledGrid) and 0 <= newY < len(floodFilledGrid[x]):
                        if floodFilledGrid[newX][newY] != testRegion:
                            perimeter += 1

                    # right
                    newX = x
                    newY = y+1
                    if 0 <= newX < len(floodFilledGrid) and 0 <= newY < len(floodFilledGrid[x]):
                        if floodFilledGrid[newX][newY] != testRegion:
                            perimeter += 1

                    # down
                    newX = x+1
                    newY = y
                    if 0 <= newX < len(floodFilledGrid) and 0 <= newY < len(floodFilledGrid[x]):
                        if floodFilledGrid[newX][newY] != testRegion:
                            perimeter += 1

        #print(testRegion, " - ", area, " - ", perimeter)
        sum += area * perimeter                 
    print(floodFilledGrid)
    print(grid)
    print("Part One: ", sum)

def partTwo(grid):
    sum = 0

    print("Part Two: ", sum)

grid = getInput()

partOne(grid)
partTwo(grid)
