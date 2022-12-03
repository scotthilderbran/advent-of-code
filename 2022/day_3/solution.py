input = open('input.txt', 'r')

# Part 1 


def get_int_of_char(character):
    if character.isupper():
        return ord(character) - 38
    else: 
        return ord(character) - 96


runningSum = 0

for line in input:
    length = int(len(line) / 2)
    firstCompartment = line[:length]
    secondCompartment = line[length:]
    runningTotal = 0
    chars = set()
    for i in range (int(len(firstCompartment))): 
        chars.add(firstCompartment[i])


    for i in range (int(len(secondCompartment))): 
        if secondCompartment[i] in chars:
            character = secondCompartment[i]
            chars.discard(character)
            charVal = get_int_of_char(character)
            
            runningSum += charVal
   

print(runningSum)


# Part 2

runningSum = 0

lines = input.readlines()

lengthOfLines = len(lines)
lineIdx = 0
while lineIdx < lengthOfLines:
    seen = set()
    firstLine = lines[lineIdx]
    for i in range (int(len(firstLine)) -1):
        if firstLine[i] not in seen:
            seen.add(firstLine[i])


    lineIdx += 1

    seenTwo = set()
    secondLine = lines[lineIdx]
    for i in range (int(len(secondLine)) -1):
        if secondLine[i] in seen:
            seenTwo.add(secondLine[i])
    
    lineIdx += 1

    seenThree = set()
    thirdLine = lines[lineIdx]
    for i in range (int(len(thirdLine)) -1):
        if thirdLine[i] in seenTwo:
            seenTwo.discard(thirdLine[i])
            seenThree.add(thirdLine[i])
            runningSum += get_int_of_char(thirdLine[i])

    lineIdx += 1

print(runningSum)
    
   