def reportInvalidIndex(report):
    previousDirection = None
    for i in range(1, len(report)):
        direction = report[i-1] - report[i]

        if (abs(direction) > 3):
            return i
        
        if  previousDirection != None and direction * previousDirection <= 0: # check if next pair is the same direction (ascending or descending) as current pair
            # It's possible the error was at one of the first 2 elements, in which case we only catch it here
            if(i == 2 and len(report) >= 4):
                #Check if next direction is indeed same as current (meaning it's possible only first direction was invalid)
                nextDirection = report[i] - report[i+1]
                if(nextDirection * direction > 0): 
                    return 1 # return 1 to avoid OOB

            return i

        previousDirection = direction

    return -1

def getReports():
    with open("input.txt") as file:
        input = file.read()
        lines = input.split("\n")

    reports = []
    for line in lines:
        levels = [int(x) for x in line.split()]
        reports.append(levels)
    
    return reports

def partOne(reports):
    safeReports = 0
    
    for report in reports:
        badIndex = reportInvalidIndex(report)
        if(badIndex < 0):
            safeReports += 1

    # Part 1 answer
    print("Part one: ", safeReports)

def partTwo(reports):
    safeReports = 0
    
    for report in reports:
        badIndex = reportInvalidIndex(report)
        isSafe = False
        if(badIndex < 0):
            isSafe = True
        else:
            if(reportInvalidIndex(report[:badIndex] + report[badIndex+1:]) < 0): # check with skipping the badIndex
                isSafe = True
            elif(reportInvalidIndex(report[:badIndex-1] + report[badIndex:]) < 0): # check skipping before badIndex
                isSafe= True

        if isSafe:
            safeReports+=1

    # Part 2 answer
    print("Part two: ", safeReports)

reports = getReports()
partOne(reports)
partTwo(reports)