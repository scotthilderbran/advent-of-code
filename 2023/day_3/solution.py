
input = open('input.txt', 'r')

chars = {}

xVariations = [-1, 0, 1]
yVariations = [-1, 0, 1]

def getFullNumber(lines, xVal , yVal):
    currentNum = lines[yVal][xVal]
    lines[yVal][xVal] = "."
    currentXVal = xVal
    while currentXVal - 1 >= 0 and lines[yVal][currentXVal - 1].isdigit():
        currentXVal = currentXVal - 1
        currentNum = lines[yVal][currentXVal] + currentNum
        lines[yVal][currentXVal] = "."
        

    currentXVal = xVal
    while currentXVal + 1 < len(lines[0]) and lines[yVal][currentXVal + 1].isdigit():
        currentXVal = currentXVal + 1 
        currentNum = currentNum + lines[yVal][currentXVal]
        lines[yVal][currentXVal] = "."
    
    return currentNum

def textToArray(lines):
    outputArr = []
    for line in lines:
        strippedLine = line.strip()
        outputArr.append(list(strippedLine))
    return outputArr

def part_1(lines):
    sum = 0
    for rowIndex, line in enumerate(lines):
        for colIndex, char in enumerate(line):
            if char != "." and not char.isdigit():
                # Check all adjancents for numbers
                for xVar in xVariations:
                    for yVar in yVariations:
                        # if any adjacent is a number, get the number and add to total
                        # when getting the number, modify the array in place
                        xVal = colIndex + xVar
                        yVal = rowIndex + yVar
                        if yVal >= 0 and yVal < len(lines) and xVal >= 0 and xVal < len(lines[0]):
                            if lines[yVal][xVal].isdigit():
                                fullNumber = getFullNumber(lines, xVal, yVal)
                                sum += int(fullNumber)
                                
                        
    return sum

def part_2(lines):
    print("arone")
    sum = 0
    for rowIndex, line in enumerate(lines):
        for colIndex, char in enumerate(line):
            if char == "*":
                print("found a gear")
                gears = []
                # Check all adjancents for numbers
                for xVar in xVariations:
                    for yVar in yVariations:
                        # if any adjacent is a number, get the number and add to total
                        # when getting the number, modify the array in place to avoid duplicate numbers
                        xVal = colIndex + xVar
                        yVal = rowIndex + yVar
                        if yVal >= 0 and yVal < len(lines) and xVal >= 0 and xVal < len(lines[0]):
                            if lines[yVal][xVal].isdigit():
                                fullNumber = getFullNumber(lines, xVal, yVal)
                                gears.append(int(fullNumber))
                if len(gears) == 2:
                    ratio = gears[0] * gears[1]
                    sum += ratio
                                
                        
    return sum


# parsedArray = textToArray(input)

# print("part 1", part_1(parsedArray))
# Need to make copy of array for part 2 since we are modifying it

# print("part 2", part_2(parsedArray))
