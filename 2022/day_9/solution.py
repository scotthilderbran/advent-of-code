import os

input = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')

def isAdjacent(H, T):
    isXAdjacent = T[0] == H[0] or T[0] == H[0] - 1 or T[0] == H[0] + 1 

    isYAdjacent = T[1] == H[1] or T[1] == H[1] - 1 or T[1] == H[1] + 1 

    return isXAdjacent and isYAdjacent

visit = set()

visit.add("0-0")


currentH = [0,0]
currentT = [0,0]


visualizer = [["x","-","-","-","-","-"],["-","-","-","-","-","-"],
["-","-","-","-","-","-"],["-","-","-","-","-","-"],["-","-","-","-","-","-"]]


#Retrace steps until adjecent to original tail position
# def modelDrag(starting, xOffset, yOffset, unitsMoved):
#     global visit
#     for i in range (0, unitsMoved - 1):
#         offSetX = starting[0] + (i * xOffset)
#         offsetY = starting[1] + (i * yOffset)
        
#         visitString = str(offSetX) + "-" + str(offsetY)
#         print(visitString)
        
#         if visitString not in visit:
#             visualizer[offsetY][offSetX] = "x"
#             visit.add(visitString)




# for line in input:
#     lineSplit = line.strip().split(" ")

#     dir = lineSplit[0]
#     unit = int(lineSplit[1])
#     print(line)
    

#     if dir == "U":
#         currentH[1] += unit
#         if not isAdjacent(currentH, currentT):
#             currentT[0] = currentH[0]
#             print(currentH)
#             currentT[1] = currentH[1] - 1
#             print("current head ", currentH)
#             print("current tail ", currentT)
#             modelDrag(currentT, 0, -1, unit)
#     elif dir == "D":
#         currentH[1] -= unit
#         if not isAdjacent(currentH, currentT):
#             currentT[0] = currentH[0] + 1 
#             currentT[1] = currentH[1]
#             print("current head ", currentH)
#             print("current tail ", currentT)
#             modelDrag(currentT, 0, 1, unit)
#     elif dir == "L":
#         currentH[0] -= unit
#         if not isAdjacent(currentH, currentT):
#             currentT[0] = currentH[0] + 1
#             currentT[1] = currentH[1]
#             print("current head ", currentH)
#             print("current tail ", currentT)
#             modelDrag(currentT, 1, 0, unit)
#     elif dir == "R":
#         currentH[0] += unit
#         if not isAdjacent(currentH, currentT):
#             currentT[0] = currentH[0] - 1
#             currentT[1] = currentH[1]
#             print("current head ", currentH)
#             print("current tail ", currentT)
#             modelDrag(currentT, -1, 0, unit)
#     print("visited set:", visit)

#Retrace steps until adjecent to original tail position
def modelDrag(currentT, currentH, xOffset, yOffset, unitsMoved):
    global visit
    countOffset = 1
    offSetX = currentH[0] + (countOffset * xOffset)
    offsetY = currentH[1] + (countOffset * yOffset)
    while not isAdjacent([offSetX, offsetY], currentT):
        visitString = str(offSetX) + "-" + str(offsetY)
        print("inmodeldrag")
        print(visitString)
        
        if visitString not in visit:
            visualizer[offsetY][offSetX] = "x"
            visit.add(visitString)
        offSetX = currentH[0] + (countOffset * xOffset)
        offsetY = currentH[1] + (countOffset * yOffset)
        countOffset += 1
    visitString = str(offSetX) + "-" + str(offsetY)
    print(visitString)
    
    if visitString not in visit:
        visualizer[offsetY][offSetX] = "x"
        visit.add(visitString)



for line in input:
    lineSplit = line.strip().split(" ")

    dir = lineSplit[0]
    unit = int(lineSplit[1])
    print(line)
    

    if dir == "U":
        currentH[1] += unit
        if not isAdjacent(currentH, currentT):
            modelDrag(currentT, currentH, 0, -1, unit)
            currentT[0] = currentH[0]
            print(currentH)
            currentT[1] = currentH[1] - 1
            print("current head ", currentH)
            print("current tail ", currentT)
            
    elif dir == "D":
        currentH[1] -= unit
        if not isAdjacent(currentH, currentT):
            modelDrag(currentT, currentH, 0, 1, unit)
            currentT[0] = currentH[0] + 1 
            currentT[1] = currentH[1]
            print("current head ", currentH)
            print("current tail ", currentT)
    elif dir == "L":
        currentH[0] -= unit
        if not isAdjacent(currentH, currentT):
            modelDrag(currentT, currentH, 1, 0, unit)
            currentT[0] = currentH[0] + 1
            currentT[1] = currentH[1]
            print("current head ", currentH)
            print("current tail ", currentT)
            
    elif dir == "R":
        currentH[0] += unit
        if not isAdjacent(currentH, currentT):
            modelDrag(currentT, currentH, -1, 0, unit)
            currentT[0] = currentH[0] - 1
            currentT[1] = currentH[1]
            print("current head ", currentH)
            print("current tail ", currentT)
    #print("visited set:", visit)




print(visit)
print(len(visit))

for i in range(len(visualizer)-1, -1, -1):
    print(visualizer[i])