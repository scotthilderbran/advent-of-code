input = open('input.txt', 'r')

# Part 1 

encompassingPairs = 0

for line in input:
    lineSplit = line.strip().split(",")
    firstRange = lineSplit[0].split("-")
    secondRange = lineSplit[1].split("-")

    firstOne = int(firstRange[0])
    firstTwo = int(firstRange[1])

    secondOne = int(secondRange[0])
    secondTwo = int(secondRange[1])

    if firstOne <= secondOne and firstTwo >= secondTwo:
        encompassingPairs += 1
    elif secondOne <= firstOne and secondTwo >= firstTwo:
        encompassingPairs += 1


print(encompassingPairs)

#Part 2 

input.seek(0)

overlappingPairs = 0

for line in input:
    lineSplit = line.strip().split(",")
    firstRange = lineSplit[0].split("-")
    secondRange = lineSplit[1].split("-")

    firstOne = int(firstRange[0])
    firstTwo = int(firstRange[1])

    secondOne = int(secondRange[0])
    secondTwo = int(secondRange[1])

    if firstOne <= secondOne <= firstTwo or firstOne <= secondTwo <= firstTwo:
        overlappingPairs += 1 
    elif secondOne <= firstOne <= secondTwo or secondOne <= firstTwo <= secondTwo:
        overlappingPairs += 1 

print(overlappingPairs)
