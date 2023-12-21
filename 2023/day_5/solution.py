input = open('input.txt', 'r')

seeds = input.readline().strip().split(":")[1].strip().split()


def getMaps(input):
    maps = []

    currentMap = []

    for line in input:
        strippedLine = line.strip()
        if strippedLine and strippedLine[0].isdigit():
            split = strippedLine.split()
            currentMap.append([int(s) for s in split])
        elif len(currentMap) > 0: 
            maps.append(currentMap)
            currentMap = []
    maps.append(currentMap)
    return maps


def getDestinationNumber(mapping, currentNumber):
    for map in mapping:
        destinationStart = int(map[0])
        rangeStart = int(map[1])
        rangeEnd = rangeStart + int(map[2])
        if currentNumber >= rangeStart and currentNumber <= rangeEnd:
            offset = currentNumber - rangeStart
            return destinationStart + offset
    return currentNumber




def part_1(seeds, maps):
    locations = []
    for seed in seeds:
        currentNumber = int(seed)
        for mapping in maps:
            currentNumber = getDestinationNumber(mapping, currentNumber)
        locations.append(currentNumber)
    return min(locations)


def part_2(seeds, maps):
    intervalTuples = []

    for i in range(0, len(seeds),2):
        intervalTuples.append((int(seeds[i]), int(seeds[i]) + int(seeds[i+1])))
    
    for seedMappings in maps:
        nextTuples = []

        q = intervalTuples
        while q:
            interval = q.pop()
            intervalStart = interval[0]
            intervalEnd = interval[1]
            shouldAddInterval = True
            for mapping in seedMappings:
                # find overlap
                destinationStart = int(mapping[0])
                rangeStart = int(mapping[1])
                rangeEnd = rangeStart + int(mapping[2])

                # in overlapping scenario
                if intervalStart < rangeEnd and intervalEnd > rangeStart:
                    shouldAddInterval = False
                    overlapLeftBound = max(intervalStart, rangeStart)
                    overlapRightBound = min(intervalEnd, rangeEnd)

                    lengthOfOverlap = overlapRightBound - overlapLeftBound

                    startOffset = overlapLeftBound - rangeStart

                    start = destinationStart + startOffset
                    end = start + lengthOfOverlap
                    destinationRange = (start, end)
                     #Add overlap
                    nextTuples.append(destinationRange)

                    # Enqueue non overlapping ranges
                    if intervalStart < rangeStart and intervalEnd > rangeEnd: # Queue both sides
                        q.append((intervalStart, rangeStart -1))
                        q.append((rangeEnd+1, intervalEnd))
                    elif intervalStart < rangeStart:
                        q.append((intervalStart, rangeStart -1))
                    elif intervalEnd > rangeEnd:
                        q.append((rangeEnd + 1, intervalEnd))
            if shouldAddInterval:
                nextTuples.append(interval)
    
        intervalTuples = nextTuples
    minimumSeed = float('inf')
    for tuple in intervalTuples:
        minimumSeed = min(minimumSeed, tuple[0])
    return minimumSeed
                    

        


maps = getMaps(input)


print(part_1(seeds, maps))


print(part_2(seeds, maps))
