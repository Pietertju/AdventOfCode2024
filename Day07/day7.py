def getInput():
    lines = []
    with open("./input.txt") as file:
        lines = [line.strip() for line in file.read().split("\n")]

    equations = []
    for line in lines:
        splitLine = line.split(":")
        answer = int(splitLine[0])
        numbers = [int(x) for x in splitLine[1].split()]
        equations.append((answer, numbers))

    return equations

def equationPossible(answer, numbers, options):
    operators = len(numbers) - 1
    operations = [0] * operators
   
    while True:
        (correct, faultyIndex) = equationCorrect(answer, numbers, operations)
        if correct:
            return True
        elif sum(operations) == operators * (options-1):
            break
        elif faultyIndex > -1:
            operations[faultyIndex] += 1
            while operations[faultyIndex] > (options-1):
                operations[faultyIndex] = 0
                faultyIndex-=1
                if faultyIndex < 0:
                    return False
                operations[faultyIndex] += 1
            continue

        currentIndex = operators-1
        operations[currentIndex] += 1
        while operations[currentIndex] > (options-1):
            operations[currentIndex] = 0
            currentIndex-=1
            if currentIndex < 0:
                return False
            operations[currentIndex] += 1
    return False

def equationCorrect(answer, numbers, operations):
    ans = numbers[0]
    index = 1
    for operation in operations:     
        if operation == 1:
            ans *= numbers[index]
        elif operation == 0:
            ans += numbers[index]
        elif operation == 2:
            ans = int(str(ans) + str(numbers[index]))

        if ans > answer:
            return False, index - 1
        index += 1
    return answer == ans, -1

def partOne(equations):
    sum = 0
    for (answer, numbers) in equations:
        if equationPossible(answer, numbers, 2):
            sum += answer
    print("Part One: ", sum)

    
def partTwo(equations):
    sum = 0
    index = 1
    for (answer, numbers) in equations:
        print(index, "/", len(equations))
        index += 1
        if equationPossible(answer, numbers, 3):
            sum += answer
    print("Part Two: ", sum)

equations = getInput()
partOne(equations)
partTwo(equations)