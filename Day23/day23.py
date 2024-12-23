def getInput():
    lines = []
    with open("./input.txt") as file:
        lines = [line.strip() for line in file.read().split("\n")]

    connections = {}
    for line in lines:
        splitLine = line.split("-")
        fromConnection = splitLine[0].strip()
        toConnection = splitLine[1].strip()

        if not (fromConnection in connections):
            connections[fromConnection] = [toConnection]
        else:
            connections[fromConnection].append(toConnection)

        if not (toConnection in connections):
            connections[toConnection] = [fromConnection]
        else:
            connections[toConnection].append(fromConnection)
    
    return connections

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def partOne(connections):
    validTuples = []

    for connection in connections:
        if connection.startswith('t'):
            aConnections = connections[connection]
            for toConnection in aConnections:
                bConnections = connections[toConnection]
                intersect = intersection(aConnections, bConnections)
                for thirdConnection in intersect:
                    validTuples.append((connection, toConnection, thirdConnection))

    res = set(map(tuple, map(sorted, validTuples)))
    #print(res)
    print("Part One: ", len(res))

def bron_kerbosch(connections, r=set(), p=None, x=set()):
    if p is None:
        p = set(connections.keys())

    if not p and not x:
        yield r
    else:
        u = next(iter(p | x))  # Choose a pivot vertex
        for v in p - set(connections[u]):
            yield from bron_kerbosch(connections, r | {v}, p & set(connections[v]), x & set(connections[v]))
            p.remove(v)
            x.add(v)

def find_largest_complete_subgraph(graph):
    cliques = list(bron_kerbosch(graph))
    return max(cliques, key=len)

def partTwo(connections):
    largest = sorted(find_largest_complete_subgraph(connections))
    for thing in largest:
        print(thing, end=",")
connections = getInput()
partTwo(connections)
