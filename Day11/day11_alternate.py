import time

def getInput():
    stones = []
    with open("./input.txt") as file:
        content = file.read().strip()
        stones = [int(stone) for stone in content.split() ]

    stoneMap = {}

    for stone in stones:
        if stone in stoneMap:
            stoneMap[stone] += 1
        else:
            stoneMap[stone] = 1

    return stoneMap

def blink(stoneMap):
    newStoneMap = {}
    for (stone, frequency) in stoneMap.items():
        if stone == 0:
            if 1 in newStoneMap:
                newStoneMap[1] += frequency
            else:
                newStoneMap[1] = frequency
            continue
        stoneString = str(stone)
        if len(stoneString) % 2 == 0:
            halfWayIndex = int(len(stoneString)/2)
            firstNewStone = int(stoneString[:halfWayIndex])

            if firstNewStone in newStoneMap:
                newStoneMap[firstNewStone] += frequency
            else:
                newStoneMap[firstNewStone] = frequency

            secondNewStone = int(stoneString[halfWayIndex:])

            if secondNewStone in newStoneMap:
                newStoneMap[secondNewStone] += frequency
            else:
                newStoneMap[secondNewStone] = frequency
        else:
            newStone = stone * 2024
            if newStone in newStoneMap:
                newStoneMap[newStone] += frequency
            else:
                newStoneMap[newStone] = frequency
    
    return newStoneMap

def partOne(stoneMap):
    sum = 0
    partOneMap = stoneMap
    
    for _ in range(25):
        partOneMap = blink(partOneMap)

    for (_, frequency) in partOneMap.items():
        sum += frequency

    print("Part One: ", sum)

def partTwo(stoneMap):
    sum = 0
    start = time.time()
    partTwoMap = stoneMap
    
    for _ in range(2500):
        partTwoMap = blink(partTwoMap)

    for (_, frequency) in partTwoMap.items():
        sum += frequency
    
    end = time.time()
    print("Part Two: ", sum, " in ", (end-start)*1000, " ms")

stoneMap = getInput()

#partOne(stoneMap)
partTwo(stoneMap)
