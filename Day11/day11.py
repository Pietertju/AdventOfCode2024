def getInput():
    stones = []
    with open("./input.txt") as file:
        content = file.read().strip()
        stones = [int(stone) for stone in content.split() ]
    return stones

def stonesAfterBlinks(stone, blinks):
    
    if blinks <= 0:
        return 1
    
    if (stone, blinks) in cache:
        return cache[(stone, blinks)]

    numberOfStones = 0

    newStones = blinkStone(stone)

    for newStone in newStones:
        numberOfStones += stonesAfterBlinks(newStone, blinks-1)

    cache[(stone, blinks)] = numberOfStones
    return numberOfStones
    
def blinkStone(stone):
    if stone == 0:
        return [1]
    
    stoneString = str(stone)
    if len(stoneString) % 2 == 0:
        halfWayIndex = int(len(stoneString)/2)
        return [int(stoneString[:halfWayIndex]), int(stoneString[halfWayIndex:])]        
    else:
        return [(stone * 2024)]

def partOne(stone):
    sum = 0
    
    for stone in stones:
        sum += stonesAfterBlinks(stone, 25)
    
    print("Part One: ", sum)

def partTwo(stones):
    sum = 0

    for stone in stones:
        sum += stonesAfterBlinks(stone, 75)
    
    print("Part Two: ", sum)

stones = getInput()

cache = {}

partOne(stones)
partTwo(stones)
