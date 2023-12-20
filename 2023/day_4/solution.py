input = open('input.txt', 'r')

# Parse input into array of tuples of sets 
# [ (<Winning Nums>, <Card Nums>)]



def parseLinesToCardArray(lines):
    cards = []
    for line in lines:
        line = line.strip()
        line = line.split(":")
        line = line[1].split("|")
        winningNumbers = line[0].strip().split()
        cardNumbers = line[1].strip().split()
        winningSet = {s for s in winningNumbers}
        cardNumberSet = {s for s in cardNumbers}

        cards.append((winningSet, cardNumberSet))
    return cards

def getCardValue(card):
    winningNumbers = card[0]
    cardNumbers = card[1]
    cardScore = 0

    for number in cardNumbers:
        if number in winningNumbers:
            if cardScore == 0:
                cardScore = 1
            else:
                cardScore = cardScore * 2
    return cardScore

def getCardMatches(card):
    winningNumbers = card[0]
    cardNumbers = card[1]
    matches = 0

    for number in cardNumbers:
        if number in winningNumbers:
            matches += 1
    return matches

def addCountToSubsequentIndexes(array, number, startingIndex):
    for i in range (startingIndex, startingIndex + number):
        array[i] = array[i] + 1



def part_1(cards):
    total = 0
    for card in cards:
        cardScore = getCardValue(card)
        total += cardScore
    return total


def part_2(cards):
    baseArray = [1 for card in cards]
    winningCountArray = []
    for card in cards:
        winningCountArray.append(getCardMatches(card))

    for index, cardCount in enumerate(baseArray):
        for i in range(0, cardCount):
            addCountToSubsequentIndexes(baseArray, winningCountArray[index], index + 1)
    return sum(baseArray)

cards = parseLinesToCardArray(input)

print(part_1(cards))

print(part_2(cards))
