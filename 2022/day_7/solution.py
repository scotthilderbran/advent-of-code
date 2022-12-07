import os 
import re
import sys



class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = dict()
        self.totalFileSize = 0 

    def goToChildDir(self, dir):
        if dir in self.children:
            return self.children[dir]
        else:
            self.children[dir] = Directory(dir, self)
            return self.children[dir]


input = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')

lines = input.readlines()

countOfLines = len(lines)

rootDir = Directory("/", None)

currDir = rootDir


lineIdx = 0
while lineIdx < countOfLines:
    line = lines[lineIdx]
    split = line.strip().split(" ")
    if split[0] == '$': 
        command = split[1]
        match command:
            case "cd":
                destination = split[2]
                if destination == "/": # return to root dir
                    currDir = rootDir
                elif destination == "..": # goto parent dir
                    currDir = currDir.parent
                else: # insert and ingress or go to prev inserted dir
                    currDir = currDir.goToChildDir(destination)
                lineIdx += 1
            case "ls":
                lineIdx += 1
    else: # if not command then will be either dir or file
        if split[0] == "dir":
            currDir.goToChildDir(split[1])
        else: 
            currDir.totalFileSize += int(split[0])
        lineIdx += 1



#Total up DFS 

eligibleDirSum = 0

def dfs(dir):
    global eligibleDirSum

    total = dir.totalFileSize

    for child in dir.children:
        total += dfs(dir.children[child])
    

    if total < 100000:
        eligibleDirSum += total
    
    return total


totalFile = dfs(rootDir)

print(eligibleDirSum)


# Part 2 


spaceNeeded = 30000000 - (70000000 - totalFile)

currMinDelete = sys.maxsize

def dfs(dir):
    global spaceNeeded
    global currMinDelete

    total = dir.totalFileSize

    for child in dir.children:
        total += dfs(dir.children[child])
    

    if total > spaceNeeded and total < currMinDelete:
        currMinDelete = total
    
    return total


dfs(rootDir)

print(currMinDelete)










