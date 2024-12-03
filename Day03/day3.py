import re

def getInput():
    with open("input.txt") as file:
        input = file.read()
    
    return input

def partOne(input):
    
    regex = r'(mul)\((\d+),(\d+)\)'

    matches = re.findall(regex, input)
    sum = 0
    for groups in matches:
        (_, firstNumber, secondNumber) = groups
        sum += int(firstNumber) * int(secondNumber)

    # Part 1 answer
    print("Part one: ", sum)

def partTwo(input):
    regex = r'(do\(\))|(don\'t\(\))|(mul)\((\d+),(\d+)\)'
    matches = re.findall(regex, input)
        
    sum = 0

    shouldSum = True
    for groups in matches:
        (do, dont, _, firstNumber, secondNumber) = groups
        if do == "do()":
            shouldSum = True
            continue
        elif dont == "don't()":
            shouldSum = False
            continue
        
        # a mul statement with most recent do
        if shouldSum:
            sum += int(firstNumber) * int(secondNumber)

    print("Part Two: ", sum)

input = getInput()
partOne(input)
partTwo(input)