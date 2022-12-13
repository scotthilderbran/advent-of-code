import os
import sys 

input = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')

lines = input.readlines()

def get_int_of_char(character):
    if character.isupper():
        return ord(character) - 38
    else: 
        return ord(character) - 96



def bfs(startingCoordinates, destinationCoordinates, arr):
    bfsStack = set()
    bfsStack.add(startingCoordinates)

    visited = set()
    visited.add(startingCoordinates)

    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    steps = 0
    while len(bfsStack):
        bfsCopy = bfsStack.copy()
        bfsStack.clear()
        for bfs in bfsCopy:
            currVal = arr[bfs[0]][bfs[1]]
            if bfs == destinationCoordinates:
                return steps
            for dir in dirs:
                newI = bfs[0] + dir[0]
                newJ = bfs[1] + dir[1]
                if newI >= 0 and newI < len(arr) and newJ >= 0 and newJ < len(arr[0]) and arr[newI][newJ] <= currVal + 1:
                    if (newI, newJ) not in visited:
                        visited.add((newI, newJ))
                        bfsStack.add((newI, newJ))
        steps += 1

arr = []

startingPosition = ()
endPosition = ()
aPositions = set()

for i in range(len(lines)):

    line = lines[i].strip()
    lineArr = []

    for j in range(len(line)):
        char = line[j]
        if char == "S":
            startingPositionCoords = (i,j)
            lineArr.append(1)
        elif char == "E":
            endPositionCoords = (i,j)
            lineArr.append(26)
        elif char == "a":
            aPositions.add((i,j))
            lineArr.append(1)
        else:
            lineArr.append(get_int_of_char(char))

    arr.append(lineArr)


# Part 1

print(bfs(startingPositionCoords, endPositionCoords, arr))

# Part 2
bfsStack = set()

minAStart = sys.maxsize

for position in aPositions:

    stepsNeededAtPosition = bfs(position, endPositionCoords, arr)

    if stepsNeededAtPosition is not None:
        minAStart = min(minAStart, stepsNeededAtPosition)


print(minAStart)

