import enchant

# https://www.wordhippo.com/what-is/starting-with/5-letter-words-ae.html

correctLetters = ["?", "?", "?", "?", "?"]
untriedLettersArray = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z"]
untriedLettersStr = ""
words = []
triedLetters = []
tried = 0

def cleanAndPrint():
    cleanCorrectLetters()
    print(correctLetters)
    print(untriedLetters)
def removeTriedLetter(letter):
    global untriedLettersArray, untriedLetters
    counter = 0
    while counter < len(untriedLettersArray):
        if untriedLettersArray[counter] == letter:
            untriedLettersArray.pop(counter)
        counter += 1
    untriedLetters = ""
    for x in untriedLettersArray:
        untriedLetters = untriedLetters + x + ", "
    untriedLetters = untriedLetters[0:len(untriedLetters)-2]
def checkWord(word):
    englishDict = enchant.Dict("en_US")
    return englishDict.check(word)
def addAttempt(word, result):
    global tried, verbose
    words.append(word)
    triedLetters.append(result)
    findCorrectLetters(tried)
    tried += 1
    if(verbose):
        print()

def findCorrectLetters(index):
    global verbose
    resultSequence = triedLetters[index]
    counter = 0
    for x in resultSequence:
        if x == "1":
            if(verbose):
                print(f"[{words[index][counter]}] correct char found but out of position at {counter}")
            removeTriedLetter(words[index][counter])
            intCounter = 0
            for y in correctLetters:
                if intCounter == counter:
                    if y.find("?") != -1:
                        correctLetters[intCounter] = correctLetters[intCounter] + ":!" + str(words[index][counter])
                else:
                    if y.find("?") != -1:
                        correctLetters[intCounter] = correctLetters[intCounter] + ":~" + str(words[index][counter])
                intCounter += 1
        elif x == "2":
            if(verbose):
                print(f"[{words[index][counter]}] correct char found at {counter}")
            removeTriedLetter(words[index][counter])
            correctLetters[counter] = words[index][counter]
        counter += 1

def cleanCorrectLetters():
    global correctLetters
    counter = 0
    for values in correctLetters:
        if values[0:2] == "?:":
            correctLetters[counter] = correctLetters[counter][2:len(values)]
        counter += 1
    counter = 0
    while counter < len(correctLetters):
        check = 'True' if correctLetters[counter].find('!') != -1 else 'False'
        intCounter = 0
        if correctLetters[counter].find("!") != -1:
            pos = correctLetters[counter].find("!") + 1
            symbol = ":~" + correctLetters[counter][pos]
            correctLetters[counter] = correctLetters[counter].replace(symbol, "")
            correctLetters[counter] = correctLetters[counter].replace(symbol[1:len(symbol)], "")
            intCounter += 1
        if correctLetters[counter][0] == ":":
            correctLetters[counter] = correctLetters[counter][1:len(correctLetters[counter])]
        counter += 1

    correctLettersSplit1 = correctLetters[0].split(":")
    correctLettersSplit1 = list(set(correctLettersSplit1))
    correctLettersSplit2 = correctLetters[1].split(":")
    correctLettersSplit2 = list(set(correctLettersSplit2))
    correctLettersSplit3 = correctLetters[2].split(":")
    correctLettersSplit3 = list(set(correctLettersSplit3))
    correctLettersSplit4 = correctLetters[3].split(":")
    correctLettersSplit4 = list(set(correctLettersSplit4))
    correctLettersSplit5 = correctLetters[4].split(":")
    correctLettersSplit5 = list(set(correctLettersSplit5))
    correctLetters = [str(correctLettersSplit1)[2:-2].replace("', '",""),
                      str(correctLettersSplit2)[2:-2].replace("', '",""),
                      str(correctLettersSplit3)[2:-2].replace("', '",""),
                      str(correctLettersSplit4)[2:-2].replace("', '",""),
                      str(correctLettersSplit5)[2:-2].replace("', '","")]


verbose = False
addAttempt("CRANE", "00101")  # 1/6
addAttempt("EAGLE", "11000")  # 2/6
addAttempt("ABBEY", "20010")  # 3/6
addAttempt("ADEPT", "21200")  # 4/6
addAttempt("AGENT", "20200")  # 5/6
# addAttempt("AHEAD", "22222")  # 6/6
cleanAndPrint()

# print("abbey", checkWord("abbey"))