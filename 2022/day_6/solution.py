import os 


input = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')

line = input.readlines()[0]

seen = set()

sizeOfMarker = 4

first = 0
second = 1  

seen.add(line[first])

while len(seen) < sizeOfMarker:
    currChar = line[second]
    if currChar in seen:
        while line[first] != currChar:
            seen.remove(line[first])
            first += 1
        seen.remove(line[first])
        first += 1

    seen.add(currChar)
    second += 1


print("Solution:",second)