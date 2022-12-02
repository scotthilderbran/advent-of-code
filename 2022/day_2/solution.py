input = open('input.txt', 'r')

winners = {"A": "Y", "B": "Z", "C" : "X"}
losers = {"A": "Z", "B": "X", "C" : "Y"}
ties = {"A": "X", "B": "Y", "C" : "Z"}

scores = {"X": 1, "Y": 2, "Z" : 3}

totalScore = 0

for line in input:
    firstSelection = line.split(" ")[0]
    secondSelection = line.split(" ")[1].strip()

    roundScore = 0 

    if secondSelection == ties[firstSelection]: 
        roundScore = 3 
    elif secondSelection == winners[firstSelection]:
        roundScore = 6
    
    roundScore += scores[secondSelection]

    totalScore += roundScore


print(totalScore)

# Part 2

input.seek(0)

totalScore = 0

for line in input:
    firstSelection = line.split(" ")[0]
    secondSelection = line.split(" ")[1].strip()

    roundScore = 0

    if secondSelection == "X": # End in loss
        roundScore += scores[losers[firstSelection]]
    elif secondSelection == "Y": # End in draw 
        roundScore += scores[ties[firstSelection]]
        roundScore += 3
    else: # End in win 
        roundScore += scores[winners[firstSelection]]
        roundScore += 6

    totalScore += roundScore


print(totalScore)

   




    




    

