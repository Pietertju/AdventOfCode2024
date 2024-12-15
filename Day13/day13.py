def getInput():
    lines = []
    with open("./input.txt") as file:
        lines = file.read().split("\n")

    instructions = []
   
    for index in range(len(lines)):
        if index % 4 == 0:
            buttonA = parseLine(lines[index])
        if index % 4 == 1:
            buttonB = parseLine(lines[index])
        if index % 4 == 2:
            prize = parseLine(lines[index])
        if index % 4 == 3:
            instructions.append((buttonA, buttonB, prize))
    return instructions

def parseLine(line):
    if "Prize" not in line:
        x_start = line.find("X+") + 2
        y_start = line.find("Y+") + 2

    else:
        x_start = line.find("X=") + 2
        y_start = line.find("Y=") + 2

    x_end = line.find(",", x_start) 
    x = int(line[x_start:x_end].strip())

    y_end = len(line)  
    y = int(line[y_start:y_end].strip())
    return (x, y)

def partOne(instructions):
    sum = 0
    for instruction in instructions:
        minCost = 999999
        ((ax, ay), (bx, by), (prizeX, prizeY)) = instruction
        for i in range(101):
            startX = i * ax
            neededX = prizeX - startX
            if neededX % bx == 0:
                j = int(neededX / bx)
                if (i * ay) + (j * by) == prizeY and 0 <= j <= 100:
                    cost = (3*i) + j
                    if cost < minCost:
                        minCost = cost
        if minCost != 999999:
            sum += minCost
    print("Part One: ", sum)

def partTwo(instructions):
    sum = 0
    for instruction in instructions:
        ((ax, ay), (bx, by), (prizeX, prizeY)) = instruction
        prizeX += 10000000000000
        prizeY += 10000000000000
        
        # ax*i + bx*j = prizeX
        # ay*i + by*j = prizeY
        # i = (prizeX - bx*j) / ax
        
        # ax*ay*i + bx*j*ay = prizeX*ay
        # ay*ax*i + by*j*ax = prizeY*ax
        # 0*i + bx*j*ay-by*j*ax = prizeX*ay - prizeY*ax
        # prizeX*ay - prizeY*ax = (bx*ay - by*ax)j 
        # j = (prizeX*ay - prizeY*ax) / (bx*ay - by*ax)
        leftHand = (prizeX*ay) - (prizeY*ax)
        rightHand = ((bx*ay) - (by*ax))
        if leftHand % rightHand == 0:
            j = int(leftHand / rightHand)
            if (prizeX - (bx*j)) % ax == 0:
                i = int((prizeX - (bx*j)) / ax)
                sum += (3*i) + j

    print("Part Two: ", sum)

instructions = getInput()

partOne(instructions)
partTwo(instructions)
