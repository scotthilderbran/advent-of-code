input = open('input.txt', 'r')

# Part 1 

maximum = 0

runningSum = 0

for line in input:
    if line.strip():
        runningSum += int(line)
        continue

    maximum = max(runningSum, maximum)
    runningSum = 0


print(maximum)



# Part 2 

input.seek(0)

runningSums = [] # v poorly optimized

runningSum = 0

for line in input:
    if line.strip():
        runningSum += int(line)
        continue
    runningSums.append(runningSum)
    runningSum = 0

runningSums.sort(reverse=True)

topThreeSum = 0
for i in range(3):
    topThreeSum += runningSums[i] 

print(topThreeSum)