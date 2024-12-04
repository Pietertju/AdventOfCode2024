def getInput():
    lines = []
    with open("./input.txt") as file:
        lines = file.read().split("\n")
    
    return lines

def countXMAS(lines, x, y):
    searchString = "XMAS"
    found = False
    occurences = 0
    for xDelta in range(-1, 2):
        for yDelta in range(-1, 2):
            found = True
            for letterIndex in range(1, len(searchString)):
                newX = x+(xDelta*letterIndex)
                newY = y + (yDelta*letterIndex)
                if newX < 0 or newX >= len(lines) or newY < 0 or newY >= len(lines[x]):
                    found=False
                    break
                if(lines[newX][newY]) != searchString[letterIndex]:
                    found = False
                    break
            if found:
                occurences += 1
                
    return occurences

def containsX_MAS(lines, x, y):
    masFound = 0
    for xDelta in range(-1, 2, 2):
        for yDelta in range(-1, 2, 2):
            newX = x +xDelta
            newY = y + yDelta
            oppositeX = x - xDelta
            oppositeY = y - yDelta
            if newX < 0 or newX >= len(lines) or newY < 0 or newY >= len(lines[x]) or oppositeX < 0 or oppositeX >= len(lines) or oppositeY < 0 or oppositeY >= len(lines[x]):
                found=False
                break

            if(lines[newX][newY] == 'M' and lines[oppositeX][oppositeY] == 'S'):
                masFound += 1
    return masFound == 2
    
                        
def partOne(lines):
    sum = 0

    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if(lines[x][y] == 'X'):
                sum += countXMAS(lines, x, y)

    # Part 1 answer
    print("Part one: ", sum)

def partTwo(lines):
    sum = 0

    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if(lines[x][y] == 'A'):
                if containsX_MAS(lines, x, y):
                    sum += 1

    print("Part Two: ", sum)

lines = getInput()
partOne(lines)
partTwo(lines)