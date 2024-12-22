def getInput():
    with open("./input.txt") as file:
        secrets = [int(line.strip()) for line in file.read().split("\n")]
        
    return secrets

def mixNumber(number, value):
    return value ^ number

def pruneNumber(number):
    number = number % 16777216
    if number < 0:
        number += 16777216
    return number

def nextSecret(number):
    nextSecret = mixNumber(number, number * 64)
    nextSecret = pruneNumber(nextSecret)

    nextSecret = mixNumber(nextSecret, nextSecret // 32)
    nextSecret = pruneNumber(nextSecret)

    nextSecret = mixNumber(nextSecret, nextSecret * 2048)
    nextSecret = pruneNumber(nextSecret)

    return nextSecret

def partOne(secrets):
    answer = 0

    for secret in secrets:
        for _ in range(2000):
            secret = nextSecret(secret)
        answer += secret

    print("Part One:", answer)

def partTwo(secrets):
    maps = [{} for _ in secrets]
    for mapIndex, secret in enumerate(secrets):
        
        price = secret % 10
        if price < 0:
            price += 10
        sequence = []
        for _ in range(2000):
            secret = nextSecret(secret)
            newPrice = secret % 10
            delta = newPrice - price
            if len(sequence) == 4:
                sequence.pop(0)
            sequence.append(delta)
            if len(sequence) == 4:
                tupleSequence = (sequence[0], sequence[1], sequence[2], sequence[3])
                if not (tupleSequence in maps[mapIndex]):
                    maps[mapIndex][tupleSequence] = newPrice
            price = newPrice

    mostBananas = 0

    for i in range(-9, 9):
        for j in range(-9, 9):
            for k in range(-9, 9):
                for l in range(-9, 9):
                    sequence = (i, j, k, l)
                    bananas = 0
                    for map in maps:
                        if sequence in map:
                            bananas += map[sequence]
                    if bananas >= mostBananas and bananas > 0:
                        mostBananas = bananas

    print("Part Two", mostBananas)

secrets = getInput()
#partOne(secrets)
partTwo(secrets)