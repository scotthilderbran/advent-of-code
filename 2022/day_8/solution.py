import os 
import re
import sys


input = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')

lines = input.readlines()

lineLen = len(lines[0])
totalLines = len(lines)


def expandOut(height, i, iOffset, j, jOffset, firstCall):
    global lines 
    global lineLen
    global totalLines
    heightAtCurr = int(lines[i].strip()[j])
    if height <= heightAtCurr and not firstCall:
        return False
    elif i == 0 or i == totalLines - 1 or j == 0 or j == lineLen - 2:# if on edge
        return True

    return expandOut(height, i + iOffset, iOffset, j + jOffset, jOffset, False)

totalVisible = 0

for i in range(0, len(lines)): 
    strippedLine = lines[i].strip()
    for j in range(0, len(strippedLine)):
        currHeight = int(strippedLine[j])
        if expandOut(currHeight, i, 1, j, 0, True) or expandOut(currHeight, i, - 1, j, 0, True) or expandOut(currHeight, i, 0, j, 1, True) or expandOut(currHeight, i, 0, j, - 1, True):
            totalVisible += 1


print(totalVisible)

# Part two 

def expandOutAndCount(height, i, iOffset, j, jOffset, firstCall, currViewCount):
    global lines 
    global lineLen
    global totalLines
    heightAtCurr = int(lines[i].strip()[j])
    if height <= heightAtCurr and not firstCall:
        return currViewCount + 1
    elif i == 0 or i == totalLines - 1 or j == 0 or j == lineLen - 2:# if on edge
        return currViewCount + 1

    return expandOutAndCount(height, i + iOffset, iOffset, j + jOffset, jOffset, False, currViewCount if firstCall else currViewCount + 1)

maxViewScore = 0

for i in range(0, len(lines)): 
    strippedLine = lines[i].strip()
    for j in range(0, len(strippedLine)):
        currHeight = int(strippedLine[j])
        viewScore = expandOutAndCount(currHeight, i, 1, j, 0, True, 0) * expandOutAndCount(currHeight, i, - 1, j, 0, True, 0) * expandOutAndCount(currHeight, i, 0, j, 1, True, 0) * expandOutAndCount(currHeight, i, 0, j, - 1, True, 0)
        maxViewScore = max(maxViewScore, viewScore)

print(maxViewScore)
