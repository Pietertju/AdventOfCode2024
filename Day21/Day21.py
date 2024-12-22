def getInput():
    with open("./input.txt") as file:
        lines = [line.strip() for line in file.read().split("\n")]
        
    return lines

numPad = {
        7: (0, 0), 
        8: (0, 1), 
        9: (0, 2),
        4: (1, 0), 
        5: (1, 1), 
        6: (1, 2),
        1: (2, 0), 
        2: (2, 1), 
        3: (2, 2),
        0: (3, 1),
        10: (3, 2)
    }

keyPad = {
    "UP": 0,
    "A": 1,
    "LEFT": 2,
    "DOWN": 3,
    "RIGHT": 4
}

keyPadQuickRoutes = [
    [
        [[]], [["RIGHT"]], [["DOWN", "LEFT"]], [["DOWN"]], [["DOWN", "RIGHT"], ["RIGHT", "DOWN"]]
    ],
    [
        [["LEFT"]], [[]], [["DOWN", "LEFT", "LEFT"]], [["DOWN" ,"LEFT"], ["LEFT", "DOWN"]], [["DOWN"]]
    ],
    [
        [["RIGHT", "UP"]], [["RIGHT", "RIGHT", "UP"]], [[]], [["RIGHT"]], [["RIGHT", "RIGHT"]]
    ],
    [
        [["UP"]], [["RIGHT", "UP"], ["UP", "RIGHT"]], [["LEFT"]], [[]], [["RIGHT"]]
    ],
    [
        [["UP", "LEFT"], ["LEFT", "UP"]], [["UP"]], [["LEFT", "LEFT"]], [["LEFT"]], [[]]
    ]
]

for x in range(len(keyPadQuickRoutes)):
    for y in range(len(keyPadQuickRoutes)):
        for route in keyPadQuickRoutes[x][y]:
            route.append("A")

numPadQuickRoutes = [[[] for _ in range(len(numPad))] for _ in range(len(numPad))]
for x in numPad:
    for y in numPad:
        (fromX, fromY) = numPad[x]
        (toX, toY) = numPad[y]
        dx = toX - fromX
        dy = toY - fromY
        
        if dx == 0 and dy == 0:
            continue
        if dx < 0:
            xDir = "UP"
        else: 
            xDir = "DOWN"
        if dy < 0:
            yDir = "LEFT"
        else: 
            yDir = "RIGHT"

        possibleWays = []
        possibleWay = []
        if not ((xDir == "DOWN" and x == 1) or (xDir == "DOWN" and (x == 1 or x == 4) and abs(dx) > 1) or (xDir == "DOWN" and (x == 1 or x == 4 or x == 7) and abs(dx) > 2)):
            for _ in range(abs(dx)):
                possibleWay.append(xDir)
            for _ in range(abs(dy)):
                possibleWay.append(yDir)
        
            possibleWay.append("A")
            possibleWays.append(possibleWay)

        if not (dx == 0 or dy == 0):
            if not ((yDir == "LEFT" and x == 0) or (yDir == "LEFT" and (x == 0 or x == 10) and abs(dy) > 1)):
                alternativeWay = []
                
                for _ in range(abs(dy)):
                    alternativeWay.append(yDir)
                for _ in range(abs(dx)):
                    alternativeWay.append(xDir)
                alternativeWay.append("A")
                possibleWays.append(alternativeWay)

        numPadQuickRoutes[x][y] = possibleWays

def partOne(codes):
    answer = 0

    for code in codes:
        fromNumPad = 10
        operationCount = 0
        for character in code:
            if character == 'A':
                toNumPad = 10
            else:
                toNumPad = int(character)

            routes = numPadQuickRoutes[fromNumPad][toNumPad]

            shortestRoutes = getShortestKeyPadRoute(routes)
            
            COUNTER = 2

            for _ in range(COUNTER - 1):
                shortestRoutes = getShortestKeyPadRoute(shortestRoutes)

            fromNumPad = toNumPad
        
            operationCount += len(shortestRoutes[0])

        answer += operationCount * int(code[:-1])

    print("Part One:", answer)

def getShortestKeyPadRoute(routes):
    shortestRoutes = []
    
    for route in routes:
        fromKeyPad = keyPad["A"]
        fullRoute = []
        for move in route:
            toKeyPad = keyPad[move]
            keyPadRoute = keyPadQuickRoutes[fromKeyPad][toKeyPad][0]
            for newMove in keyPadRoute:
                fullRoute.append(newMove)
            fromKeyPad = toKeyPad
        if len(shortestRoutes) == 0:
            shortestRoutes.append(fullRoute)
        elif len(fullRoute) <= len(shortestRoutes[0]):
            if len(fullRoute) < len(shortestRoutes[0]):
                shortestRoutes = []
                shortestRoutes.append(fullRoute)
            else:
                shortestRoutes.append(fullRoute)
    return shortestRoutes

cache = {}

def recursiveGetSubPath(route, depth, maxDepth):
    length = 0
    if depth == maxDepth:
        return len(route)

    fromKeyPad = keyPad["A"]

    for move in route:
        toKeyPad = keyPad[move]
        
        minLength = 0
        keyPadRoutes = keyPadQuickRoutes[fromKeyPad][toKeyPad]

        if (fromKeyPad, toKeyPad, depth) in cache:
            minLength = cache[(fromKeyPad, toKeyPad, depth)]
        else:
            for keyPadRoute in keyPadRoutes:
                newLength = recursiveGetSubPath(keyPadRoute, depth+1, maxDepth)
                if newLength < minLength or minLength == 0:
                    minLength = newLength
        
            cache[(fromKeyPad, toKeyPad, depth)] = minLength
    
        length += minLength
        fromKeyPad = toKeyPad

    return length

def partTwo(codes):
    answer = 0
    for code in codes:
        fromNumPad = 10
        totalLength = 0
        for character in code:
            if character == 'A':
                toNumPad = 10
            else:
                toNumPad = int(character)

            routes = numPadQuickRoutes[fromNumPad][toNumPad]
            minLength = 0
            for route in routes:
                length = recursiveGetSubPath(route, 0, 25)
                if length < minLength or minLength == 0:
                    minLength = length
            
            totalLength += minLength
            fromNumPad = toNumPad
        answer += totalLength * int(code[:-1])
    print("Part Two:", answer)

codes = getInput()
partOne(codes)
partTwo(codes)