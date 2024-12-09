def getInput():
    input = []
    with open("./input.txt") as file:
        input = [int(c) for c in file.read().strip()]

    return input


def partOne(input):
    sum = 0
    poppedFromRightLeftOver = 0
    index = 0
    idLeft = 0
    idRight = int((len(input) + 1) / 2)
    while len(input) > 0:
        element = input.pop(0)
        for _ in range(element):
            sum += index * idLeft
            index += 1
        idLeft += 1
        
        if len(input) <= 0:
            break
        gap = input.pop(0)
        for _ in range(gap):
            if poppedFromRightLeftOver <= 0:
                idRight -= 1
                poppedFromRightLeftOver = input.pop()
                input.pop()
            sum += index * idRight
            poppedFromRightLeftOver -= 1
            index += 1

    for _ in range(poppedFromRightLeftOver):
        sum += index * idRight
        index += 1
    
    print("Part One: ", sum)

def partTwo(input):
    sum = 0
    index = 0

    rightIndex = len(input) - 1
    
    precomputedStartIndexes = [0]*len(input)
    cumulativeIndex = 0
    for i in range(len(input)):
        precomputedStartIndexes[i] = cumulativeIndex
        cumulativeIndex += input[i]
    
    while rightIndex > 0:
        rightFiles = input[rightIndex]
        idRight = int(rightIndex / 2)
                
        # gaps
        foundGap = False
        for i in range(1, rightIndex, 2):
            if input[i] >= rightFiles:
                foundGap = True
                input[i] -= rightFiles
                index = precomputedStartIndexes[i]

                for _ in range(rightFiles):
                    sum += index * idRight
                    index += 1
                precomputedStartIndexes[i] += rightFiles
                break
        if not foundGap:
            index = precomputedStartIndexes[rightIndex]
            for _ in range(rightFiles):
                sum += index * idRight
                index += 1
        rightIndex -= 2

    

    print("Part Two: ", sum)

input = getInput()
partOne([x for x in input])
partTwo(input)
