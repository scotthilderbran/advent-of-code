import os 
import re
from ast import literal_eval
import collections.abc


input = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')

lines = input.readlines()

pairs = []
allPackets = []

for i in range(0, len(lines), 3):
    line = lines[i]
    lineTwo = lines[i+1]
    one = literal_eval(line)
    two = literal_eval(lineTwo)
    pairs.append((one,two))
    allPackets.append(one)
    allPackets.append(two)


allPackets.append([[2]])
allPackets.append([[6]])


def isArr(val):
    return isinstance(val, collections.abc.Sequence)


def inOrderRecursive(left, right):
    if left == []:
        if right == []:
            return None
        else:
            return True

    if right == []:
        return False
    
    if isArr(left) and isArr(right): # if both list
        retVal = inOrderRecursive(left[0], right[0])
        if retVal == None:
            return inOrderRecursive(left[1:], right[1:])
        return retVal
    elif isArr(left):
        retVal = inOrderRecursive(left, [right])
        if retVal != None:
            return retVal
    elif isArr(right):
        retVal = inOrderRecursive([left], right)
        if retVal != None:
            return retVal
    else:
        if left > right:
            return False 
        elif right > left:
            return True
        else: 
            return None

print(len(pairs))

inOrderSum = 0

for i in range(len(pairs)):
    currPair = pairs[i]
    if inOrderRecursive(currPair[0], currPair[1]):
        currIdx = i+1
        inOrderSum += currIdx


print(inOrderSum)

def swap(index, destination): # Swap val at index with val at destination
    global allPackets
    temp = allPackets[destination]
    allPackets[destination] = allPackets[index]
    allPackets[index] = temp
    


# Bubble sort 
while True:
    hasSwapped = False
    for i in range(len(allPackets) - 1):
        inOrder = inOrderRecursive(allPackets[i], allPackets[i+1])
        if not inOrder:
            swap(i, i+1)
            hasSwapped = True
    if not hasSwapped:
        break


sixIdx = 0
twoIdx = 0
for i in range(len(allPackets)):
    packet = allPackets[i]
    if packet == [[6]]:
        sixIdx = i+1
    elif packet == [[2]]:
        twoIdx = i+1

print(sixIdx * twoIdx)
