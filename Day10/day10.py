def getInput():
    nodes = []
    with open("./input.txt") as file:
        lines = file.read().split("\n")
        nodes = [(int(x), [], []) for line in lines for x in line.strip()]
        width = len(lines[0])

    for x in range(len(nodes)):
        (id, toNodes, _) = nodes[x]

        if (x+1) % width != 0:
            (rightId, rightToNodes, _) = nodes[x+1]
            if id - rightId == 1:
                rightToNodes.append(x)
            elif rightId - id == 1:
                toNodes.append(x+1)

        if x + width < len(nodes):
            (belowId, belowToNodes, _) = nodes[x+width]
            if id - belowId == 1:
                belowToNodes.append(x)
            elif belowId - id == 1:
                toNodes.append(x+width)

    return nodes

def findPossibleRoutes(nodes):
    queue = []

    for nodeIndex in range(len(nodes)):
        node = nodes[nodeIndex]
        if node[0] == 0:
            queue.append((nodeIndex, nodeIndex))

    while len(queue) > 0:
        (start, nodeIndex) = queue.pop()

        (id, toNodes, startedFrom) = nodes[nodeIndex]
        
        if id == 9:
            startedFrom.append(start)

        for toNodeIndex in toNodes:
            queue.append((start, toNodeIndex))

    return nodes

def partOne(nodes):
    sum = 0
 
    for (_, _, startedFrom) in nodes:
        sum += len(set(startedFrom))

    print("Part One: ", sum)

def partTwo(nodes):
    sum = 0    

    for (_, _, startedFrom) in nodes:
        sum += len(startedFrom)

    print("Part Two: ", sum)

nodes = getInput()
nodes = findPossibleRoutes(nodes)

partOne(nodes)
partTwo(nodes)
