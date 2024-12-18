import itertools

def getInput():
    with open("./input.txt") as file:
        lines = file.read().split("\n")
        
    registerA = int(lines[0].split(":")[1].strip())
    registerB = int(lines[1].split(":")[1].strip())
    registerC = int(lines[2].split(":")[1].strip())
    programList = [int(x.strip()) for x in lines[4].split(":")[1].strip().split(",")]

    return registerA, registerB, registerC, programList

def runProgram(regA, regB, regC, programIds):
    instructionsPointer = 0
    output = []
    while instructionsPointer < len(programIds):
        opcode = programIds[instructionsPointer]
        literalOperant = programIds[instructionsPointer+1]
        if 0 <= literalOperant <= 3:
            comboOperant = literalOperant
        elif literalOperant == 4:
            comboOperant = regA
        elif literalOperant == 5:
            comboOperant = regB
        elif literalOperant == 6:
            comboOperant = regC
        else:
            print("WTF!!!!!!!!!")

        if opcode == 0: # adv
            numerator = regA
            denominator = 2 ** comboOperant

            regA = int(numerator / denominator)
        elif opcode == 1: # bxl
            regB = regB ^ literalOperant
        elif opcode == 2: # bst
            regB = comboOperant % 8
        elif opcode == 3: # jnz
            if regA != 0:
                instructionsPointer = literalOperant
                continue
        elif opcode == 4: # bxc
            regB = regB ^ regC
        elif opcode == 5: # out
            out = comboOperant % 8
            output.append(out)
        elif opcode == 6: # bdv
            numerator = regA
            denominator = 2 ** comboOperant

            regB = int(numerator / denominator)
        elif opcode == 7: # cdv
            numerator = regA
            denominator = 2 ** comboOperant

            regC = int(numerator / denominator)
        instructionsPointer += 2
    return output

def partOne(regA, regB, regC, programIds):
    output = runProgram(regA, regB, regC, programIds)

    print("Part One: ", end="")
    for out in output[:-1]:
        print(out, end=",")
    print(output[-1])

def partTwo(regA, regB, regC, programIds):

    digitsInBaseEight = len(programIds)
    baseEightString = "0"*digitsInBaseEight
    baseEightArray = [0] * digitsInBaseEight
    baseEightArray[0] = 1

    index = 0
    while 0 <= index < digitsInBaseEight:
        baseEightString = "".join(map(str,baseEightArray))
        regA = int(baseEightString, 8)
        output = runProgram(regA, regB, regC, programIds)
        if output[-(index+1):] == programIds[-(index+1):]:
            index += 1
            continue

        baseEightArray[index] += 1
        while baseEightArray[index] >= 8:
            baseEightArray[index] = 0
            index -= 1
            baseEightArray[index] += 1
            if index < 0: 
                break
            
    print(regA)

a, b, c, programs = getInput()
partOne(a, b, c, programs)
partTwo(a, b, c, programs)
