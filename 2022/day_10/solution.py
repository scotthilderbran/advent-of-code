import os

input = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')

lines = input.readlines()

queue = []


for i in range(len(lines)):
    split = lines[i].strip().split()
    operation = split[0] 

    if operation == "addx":
        value = int(split[1])
        queue.append(None)
        queue.append(value)
    else:
        queue.append(None)



xReg = 1
sum = 0
for i in range(len(queue)):
    cycleNum = i + 1

    if cycleNum % 40 == 0:
        signalStrength = cycleNum * xReg

        sum += signalStrength

    if queue[i] != None:
            xReg += queue[i]

        
        

print(sum)

#Part 2 


xReg = 1
sum = 0
signalStrengthSum = 0
for i in range(len(queue)):
    cycleNum = i + 1
    
    if cycleNum % 40 >= xReg and cycleNum % 40 < xReg + 3:
        print("#", end = '')
    else:
        print(".", end = '') 

    if cycleNum % 40 == 0:
        print("")

    if queue[i] != None:
            xReg += queue[i]
