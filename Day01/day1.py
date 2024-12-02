def getLists():
    lines = []
    with open("input.txt") as file:
        input = file.read()
        lines = input.split("\n")

    firstList = []
    secondList = []

    for line in lines:
        numbers = line.split()
        firstList.append(int(numbers[0]))
        secondList.append(int(numbers[1]))
    
    return (firstList, secondList)

def partOne(firstList, secondList):
    sum = 0

    firstList.sort()
    secondList.sort()

    for i in range(len(firstList)):
        sum += abs(firstList[i] - secondList[i])

    print("Part one: ", sum)

def partTwo(firstList, secondList):

    sum = 0
    frequencies = {}
    
    for number in secondList:
        if number in frequencies:
            frequencies[number] += 1
        else:
            frequencies[number] = 1

    for number in firstList:
        if number in frequencies:
            sum += number * frequencies[number]

    print("Part two: ", sum)

(firstList, secondList) = getLists()
partOne(firstList, secondList)
partTwo(firstList, secondList)