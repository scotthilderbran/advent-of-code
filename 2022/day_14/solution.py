import os 

input = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')

lines = input.readlines()


arr =  q = [ [ "." for i in range(700) ] for j in range(200) ]

def printAll(arr):
    for i in range(0,15):
        line = arr[i][485:515]
        print(line)


def insertStruct(curr, destination):

    global arr

    arr[curr[0]][curr[1]] = "#"



    if curr == destination:
        return

    if curr[0] < destination[0]:
        insertStruct((curr[0] + 1, curr[1]), destination)

    if curr[0] > destination[0]:
        insertStruct((curr[0] - 1, curr[1]), destination)

    if curr[1] > destination[1]:
        insertStruct((curr[0],  curr[1] - 1), destination)

    if curr[1] < destination[1]:
        insertStruct((curr[0],  curr[1] + 1), destination)
    
    
maxDepth = 0

placedCount = 0

def simulateSandFalling(curr):
    global maxDepth
    global arr
    global placedCount

    
    #fall immediately down
    # print("arr below", arr[curr[0] + 1][curr[1]])
    if arr[curr[0] + 1][curr[1]] == "." and curr[0] + 1 < maxDepth + 2:
        simulateSandFalling((curr[0] + 1, curr[1]))
    elif arr[curr[0] + 1][curr[1] - 1] == "." and curr[0] + 1 < maxDepth + 2:  # down left
        simulateSandFalling((curr[0] + 1, curr[1] - 1))
    elif arr[curr[0] + 1][curr[1] + 1] == "." and curr[0] + 1 < maxDepth + 2:# down right
        simulateSandFalling((curr[0] + 1, curr[1] + 1))
    else: 
        arr[curr[0]][curr[1]] = "o"
        placedCount += 1



for line in lines:
    strippedLine = line.strip() 

    split = strippedLine.split(" -> ")

    idx = 0

    for i in range(0, len(split) - 1):

        currSplit = split[i].split(",")
        destinationSplit = split[i+1].split(",")

        maxDepthHere = max(int(currSplit[1]), int(destinationSplit[1]))

        maxDepth = max(maxDepth, maxDepthHere)


        insertStruct((int(currSplit[1]), int(currSplit[0])),(int(destinationSplit[1]), int(destinationSplit[0])))

numOfSand = 0

while arr[0][500] != "o":
     simulateSandFalling((0, 500))
     numOfSand += 1

print(numOfSand)
