import os

input = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')


visitedLast = set()
visitedFirst = set()

H = (0,0)
T = (0,0)

def moveKnot(H,T):
    diffX = H[0] - T[0]
    diffY = H[1] - T[1]

    if abs(diffX) <= 1 and abs(diffY) <= 1:
        pass
    elif abs(diffX) >= 2 and abs(diffY) >= 2:
        T = (H[0] - 1 if H[0] > T[0] else H[0] + 1, H[1] - 1 if H[1] > T[1] else H[1] + 1)
    elif abs(diffX) >= 2:
        T = (H[0] - 1 if H[0] > T[0] else H[0] + 1, H[1])
    elif abs(diffY) >= 2:
        T = (H[0], H[1] - 1 if H[1] > T[1] else H[1] + 1)
    return T

xOffset = {"U": 0, "D": 0, "L": -1, "R": 1}
yOffset = {"U": 1, "D": -1, "L": 0, "R": 0}

knotSize = 9

T = [(0,0) for _ in range(knotSize)]

visitedLast.add(T[8])
visitedFirst.add(T[0])

for line in input:
    dir, amt = line.split()
    amt = int(amt)
    for _ in range(amt):
        H = (H[0] + xOffset[dir], H[1] + yOffset[dir])
        T[0] = moveKnot(H, T[0])

        for i in range(1,9):
            T[i] = moveKnot(T[i-1], T[i])
            
        visitedLast.add(T[8])
        visitedFirst.add(T[0])

print(len(visitedFirst))
print(len(visitedLast))