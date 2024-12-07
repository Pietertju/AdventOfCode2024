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
    totalPossibilities = options ** operators
    operations = [0] * operators
    if equationCorrect(answer, numbers, operations):
        return True
    for _ in range(totalPossibilities-1):
        currentIndex = 0
        operations[currentIndex] += 1
        while operations[currentIndex] > (options-1):
            operations[currentIndex] = 0
            currentIndex+=1
            operations[currentIndex] += 1

        if equationCorrect(answer, numbers, operations):
            return True
        
    return False

def equationCorrect(answer, numbers, operations):
    ans = numbers[0]
    index = 1
    for operation in operations:
        if operation == 0:
            ans *= numbers[index]
        elif operation == 1:
            ans += numbers[index]
        elif operation == 2:
            ans = int(str(ans) + str(numbers[index]))
        index += 1
    return answer == ans

def partOne(equations):
    sum = 0
    for (answer, numbers) in equations:
        if equationPossible(answer, numbers, 2):
            sum += answer
    print("Part One: ", sum)

    
def partTwo(equations):
    sum = 0
    for (answer, numbers) in equations:
        if equationPossible(answer, numbers, 3):
            sum += answer
    print("Part Two: ", sum)

equations = getInput()
partOne(equations)
partTwo(equations)