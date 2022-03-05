import enchant
import requests

def findValidWords(possibilities, mode, letters):
    firstLetter = possibilities[0] if len(possibilities[0]) == 1 else None
    lastLetter = possibilities[4] if len(possibilities[4]) == 1 else None
    array = search(mode, letters)
    valid = []
    for x in array:
        if firstLetter != None and lastLetter == None:
            if x[0] == firstLetter:
                valid.append(x)
        elif firstLetter == None and lastLetter != None:
            if x[4] == lastLetter:
                valid.append(x)
        elif firstLetter != None and lastLetter != None:
            if x[0] == firstLetter and x[4] == lastLetter:
                valid.append(x)
        else:
            counter = 1
            while counter < 4:
                if len(possibilities[counter]) == 1:
                    if x[counter] == possibilities[counter]:
                        valid.append(x)
                # else:
                #     # loop through something
                counter += 1

    for x in valid:
        print(x)


def checkWord(word):
    englishDict = enchant.Dict("en_US")
    return englishDict.check(word)


def printWords(mode, letters):
    array = search(mode, letters)
    for x in array:
        print(x)


def search(mode, letters):
    if mode == "start":
        URL = f"https://www.wordhippo.com/what-is/starting-with/5-letter-words-{letters}.html"
    elif mode == "end":
        URL = f"https://www.wordhippo.com/what-is/ending-with/5-letter-words-{letters}.html"
    elif mode == "middle":
        URL = f"https://www.wordhippo.com/what-is/containing/5-letter-words-{letters}.html"
    key = "the-meaning-of-the-word"
    keyLen = len(key)
    page = requests.get(URL)
    page = str(page.content)
    foundWords = []
    while page.find(key) != -1:
        word = page[page.find(key)+keyLen+1:page.find(key)+keyLen+6]
        page = page[page.find(key)+keyLen+11:]
        foundWords.append(word)

    # repeat for additional pages while checkLastPage(string) = False
    # if so have selenium click the next button

    counter = 0
    for x in foundWords:
        foundWords.pop(counter) if checkWord(x) == False else None
        counter += 1
    counter = 0
    for x in foundWords:
        foundWords[counter] = foundWords[counter].upper()
        counter += 1
    return foundWords


def checkLastPage(string):
    return True if string.find("forward-tri-link.png") == -1 else False
