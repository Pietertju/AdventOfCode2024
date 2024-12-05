def getInput():
    lines = []
    with open("./example.txt") as file:
        lines = [line.strip() for line in file.read().split("\n")]
    
    orderings = []
    neededPages = []
    readingOrder = True
    for line in lines:
        if line == "":
            readingOrder = False
            continue
        if readingOrder:
            values = line.split("|")
            orderings.append((int(values[0].strip()), int(values[1].strip())))
        else:
            neededPages.append([int(page.strip()) for page in line.split(",")])
    return orderings, neededPages
                        
def partOne(orderings, neededPages):
    sum = 0

    incorrectlyOrdered = []
    for pages in neededPages:
        inOrder = True
        handledPages = []
        for page in pages:
            handledPages.append(page)
            for (before, after) in orderings:
                if page == before:
                    if after in handledPages:
                        inOrder = False
                        break
                elif page == after:
                    if not(before in handledPages) and before in pages:
                        inOrder = False
                        break
            if not inOrder:
                break
        if inOrder:
            sum += pages[int((len(pages) + 1) / 2) - 1]
        else:
            incorrectlyOrdered.append(pages)
    print("Part one: ", sum)
    return incorrectlyOrdered

def orderPages(orderings, pages):
    relevantOrderings = []
    for (before, after) in orderings:
        if after in pages and before in pages:
            relevantOrderings.append((before, after))

    correctOrdering = []

    # this doesnt actually matter since the fact that the middle page number must be deterministic for the solution to be possible,
    # we know that there won't be pages without rules attached to them as that would make multiple orders possible
    for page in pages:
        pagePresent = False
        for (before, after) in relevantOrderings:
            if before == page or after == page:
                pagePresent = True
                break

        if not pagePresent:
            correctOrdering.append(page)
    
    # We make the assumption that an ordering is possible (i.e. no loops)
    while len(correctOrdering) != len(pages):
        addedNumber = False
        for (before, after) in relevantOrderings:
            if before in correctOrdering:
                continue
            hasAfter = False
            for (before2, after2) in relevantOrderings:
                if before == after2 and not before2 in correctOrdering:
                    hasAfter = True
                    break
            if not hasAfter:
                correctOrdering.append(before)
                addedNumber= True
                break

        # We have safely added all numbers that appear as before, now we can safely add all not yet added numbers that appear as afters
        if not addedNumber:
            for (before, after) in relevantOrderings:
                if not after in correctOrdering:
                    correctOrdering.append(after)

        

    return correctOrdering

def partTwo(orderings, incorrectlyOrdered):
    sum = 0

    for pages in incorrectlyOrdered:
        correctOrder = orderPages(orderings, pages)
        sum += correctOrder[int((len(correctOrder) + 1) / 2) - 1]

    print("Part Two: ", sum)

orderings, neededPages = getInput()
incorrectlyOrdered = partOne(orderings, neededPages)
partTwo(orderings, incorrectlyOrdered)