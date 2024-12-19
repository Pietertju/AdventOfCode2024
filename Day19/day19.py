def getInput():
    with open("./input.txt") as file:
        lines = file.read().split("\n")
        
    availablePatterns = [towel.strip() for towel in lines[0].strip().split(",")]
    neededPatterns = [pattern for pattern in lines[2:]]

    return availablePatterns, neededPatterns

cache = {}

def getPossibleWays(pattern, availablePatterns):
    possibleWays = 0

    if pattern in cache:
        return cache[pattern]

    if len(pattern) == 1:
        if pattern in availablePatterns:
            return 1
        else:
            return 0

    if pattern in availablePatterns:
        possibleWays += 1


    for index in range(1, len(pattern), 1):
        patternLeft = pattern[:index]
        patternRight = pattern[index:]
        waysLeft = 1 if patternLeft in availablePatterns else 0
        waysRight = getPossibleWays(patternRight, availablePatterns)
        possibleWays += waysLeft * waysRight
        cache[pattern] = possibleWays
    
    return possibleWays

def partOne(availablePatterns, neededPatterns):
    answer = 0
    for neededPattern in neededPatterns:
        possibleWays = getPossibleWays(neededPattern, availablePatterns)
        if possibleWays > 0:
            answer += 1

    print("Part One:", answer)

def partTwo(availablePatterns, neededPatterns):
    answer = 0

    for neededPattern in neededPatterns:
        possibleWays = getPossibleWays(neededPattern, availablePatterns)
        answer += possibleWays

    print("Part Two:", answer)

availablePatterns, neededPatterns = getInput()

partOne(availablePatterns, neededPatterns)
partTwo(availablePatterns, neededPatterns)
