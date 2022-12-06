import os 
import re


input = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')

def build_stacks(): 
    stacks = []

    stacks.append(['H', 'B', 'V' , 'W' , 'N', 'M', 'L', 'P'])
    stacks.append(['M', 'Q', 'H'])
    stacks.append(['N', 'D', 'B' , 'G' , 'F', 'Q', 'M', 'L'])
    stacks.append(['Z', 'T', 'F' , 'Q' , 'M', 'W', 'G'])
    stacks.append(['M', 'T', 'H' , 'P' ])
    stacks.append(['C', 'B', 'M' , 'J' , 'D', 'H', 'G', 'T'])
    stacks.append(['M', 'N' , 'B', 'F', 'V', 'R'])
    stacks.append(['P', 'L', 'H' , 'M' , 'R', 'G', 'S'])
    stacks.append(['P', 'D', 'B' , 'C' , 'N'])
    return stacks

# Part 1

stacks = build_stacks()

for line in input:
    numbers = re.findall('\d+', line)

    qty = int(numbers[0])
    sourceStack = stacks[int(numbers[1]) - 1]
    destinationStack = stacks[int(numbers[2]) - 1]
    stackToMove = sourceStack[-qty:][::-1]

    stacks[int(numbers[1]) - 1] = sourceStack[0:len(sourceStack) - qty]
    
    destinationStack += stackToMove



finalString = ''


for stack in stacks:
    finalString += stack.pop()

print(finalString)

# Part 2 

input.seek(0)

stacks = build_stacks()

for line in input:
    numbers = re.findall('\d+', line)

    qty = int(numbers[0])
    sourceStack = stacks[int(numbers[1]) - 1]
    destinationStack = stacks[int(numbers[2]) - 1]

    stackToMove = sourceStack[-qty:]
    stacks[int(numbers[1]) - 1] = sourceStack[0:len(sourceStack) - qty]
    
    destinationStack += stackToMove

finalString = ''

for stack in stacks:
    finalString += stack.pop()

print(finalString)