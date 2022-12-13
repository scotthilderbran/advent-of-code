import os
import math

superMod = 2*17*7*11*19*5*13*3

class Monkey:
    def __init__(self, items, operation, test, trueDestination, falseDestination):
        self.items = items
        self.operation = operation
        self.test = test
        self.trueDestination = trueDestination
        self.falseDestination = falseDestination


    def destinationAndAmount(self, item):
        newWorry = self.operation(item) % superMod 
        return [newWorry, self.trueDestination if self.test(newWorry) else self.falseDestination] 





monkeys = []


monkeys.append(Monkey([99, 63, 76, 93, 54, 73], lambda x : x * 11, lambda x : x % 2 == 0, 7, 1))
monkeys.append(Monkey([91, 60, 97, 54], lambda x : x + 1, lambda x : x % 17 == 0, 3, 2))
monkeys.append(Monkey([65], lambda x : x + 7, lambda x : x % 7 == 0, 6, 5))
monkeys.append(Monkey([84, 55], lambda x : x + 3, lambda x : x % 11 == 0, 2, 6))
monkeys.append(Monkey([86, 63, 79, 54, 83], lambda x : x * x, lambda x : x % 19 == 0, 7, 0))
monkeys.append(Monkey([96, 67, 56, 95, 64, 69, 96], lambda x : x + 4, lambda x : x % 5 == 0, 4, 0))
monkeys.append(Monkey([66, 94, 70, 93, 72, 67, 88, 51], lambda x : x * 5, lambda x : x % 13 == 0, 4, 5))
monkeys.append(Monkey([59, 59, 74], lambda x : x +8, lambda x : x % 3 == 0, 1, 3))



inspectionCount = [0 for i in range(len(monkeys))] 

for i in range(10000):
    for j in range(len(monkeys)):
        monkey = monkeys[j]
        copyItems = monkey.items.copy()
        for i in range(len(copyItems)):
            item = copyItems[i]
            inspectionCount[j] += 1

            newItem, destination = monkey.destinationAndAmount(item) 
            
            monkeys[destination].items.append(newItem)
            monkey.items.pop()
    

inspectionCount.sort()

print(inspectionCount)
            

