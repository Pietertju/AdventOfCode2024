def getInput():
    lines = []
    with open("./input.txt") as file:
        lines = [list(line.strip()) for line in file.read().split("\n")]
    nodeLocations = {}
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            character =  lines[x][y]
            if character.isalnum():
                if character in nodeLocations.keys():
                    nodeLocations[character].append((x,y))
                else:
                    nodeLocations[character] = [(x,y)]

    return lines, nodeLocations

def getAntiNodeLocations(pair, lines, isPartTwo):
    first = pair[0]
    second = pair[1]

    dx = second[0] - first[0]
    dy = second[1] - first[1]

    firstAntiNodeX = first[0] - dx
    firstAntiNodeY = first[1] - dy

    secondAntiNodeX = second[0] + dx
    secondAntiNodeY = second[1] + dy

    antiNodeLocations = []

    if not isPartTwo:
        if 0 <= firstAntiNodeX < len(lines) and 0 <= firstAntiNodeY < len(lines[firstAntiNodeX]):
            antiNodeLocations.append((firstAntiNodeX, firstAntiNodeY))

        if 0 <= secondAntiNodeX < len(lines) and 0 <= secondAntiNodeY < len(lines[secondAntiNodeX]):
            antiNodeLocations.append((secondAntiNodeX, secondAntiNodeY))

        return antiNodeLocations
    else:
        antiNodeLocations.append(first)
        antiNodeLocations.append(second)

        while 0 <= firstAntiNodeX < len(lines) and 0 <= firstAntiNodeY < len(lines[firstAntiNodeX]):
            antiNodeLocations.append((firstAntiNodeX, firstAntiNodeY))
            firstAntiNodeX -= dx
            firstAntiNodeY -= dy
        while 0 <= secondAntiNodeX < len(lines) and 0 <= secondAntiNodeY < len(lines[secondAntiNodeX]):
            antiNodeLocations.append((secondAntiNodeX, secondAntiNodeY))
            secondAntiNodeX += dx
            secondAntiNodeY += dy
        return antiNodeLocations

def partOne(lines, nodeLocations):
    sum = 0

    antiNodeLocations = [([0] * len(lines[0])) for _ in range(len(lines))]
    for key in nodeLocations.keys():
        positions = nodeLocations[key]
        allPairs = [(positions[i], positions[j]) for i in range(len(positions)) for j in range(i, len(positions)) if i != j]
        for pair in allPairs:
            antiNodes = getAntiNodeLocations(pair, lines, False)
            for antiNode in antiNodes:
                antiNodeLocations[antiNode[0]][antiNode[1]] += 1
            
    for x in range(len(antiNodeLocations)):
        for y in range(len(antiNodeLocations[x])):
            if antiNodeLocations[x][y] > 0:
                sum += 1
    print("Part One: ", sum)

    
def partTwo(lines, nodeLocations):
    sum = 0

    antiNodeLocations = [([0] * len(lines[0])) for _ in range(len(lines))]
    for key in nodeLocations.keys():
        positions = nodeLocations[key]
        allPairs = [(positions[i], positions[j]) for i in range(len(positions)) for j in range(i, len(positions)) if i != j]
        for pair in allPairs:
            antiNodes = getAntiNodeLocations(pair, lines, True)
            for antiNode in antiNodes:
                antiNodeLocations[antiNode[0]][antiNode[1]] += 1
            
    for x in range(len(antiNodeLocations)):
        for y in range(len(antiNodeLocations[x])):
            if antiNodeLocations[x][y] > 0:
                sum += 1
    print("Part Two: ", sum)

lines, nodeLocations = getInput()
partOne(lines, nodeLocations)
partTwo(lines, nodeLocations)