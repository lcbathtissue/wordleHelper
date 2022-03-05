import Words

# https://www.wordleunlimited.com/

correctLetters = ["?", "?", "?", "?", "?"]
untriedLettersArray = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z"]
untriedLetters = ""
allPossibilities = []
words = []
triedLetters = []
tried = 0

def updateUntriedLetterString():
    global untriedLettersArray, untriedLetters
    untriedLetters = ""
    for x in untriedLettersArray:
        untriedLetters = untriedLetters + x
    untriedLetters = untriedLetters[0:]
def removeDeadLetter(letter):
    global untriedLettersArray, untriedLetters
    counter = 0
    for x in untriedLettersArray:
        if x == letter:
            untriedLettersArray.pop(counter)
            break
        counter += 1
    updateUntriedLetterString()
def generateLetterPossibilities():
    global correctLetters, untriedLetters, allPossibilities
    returnArray = []
    allPossibilities = correctLetters.split(" ")
    counter = 0
    for x in allPossibilities:
        if len(x) != 1:
            allPossibilities[counter] = untriedLetters + allPossibilities[counter]
        counter += 1
    counter = 0
    for x in allPossibilities:
        if len(x) != 1:
            if x.find("!") != -1:
                allPossibilities[counter] = allPossibilities[counter][0:x.find("!")]
        counter += 1
def cleanAndPrint():
    global allPossibilities
    cleanCorrectLetters()
    print(correctLetters)
    print(untriedLetters)
    generateLetterPossibilities()
    print(allPossibilities)
def removeTriedLetter(letter):
    global untriedLettersArray, untriedLetters
    counter = 0
    while counter < len(untriedLettersArray):
        if untriedLettersArray[counter] == letter:
            untriedLettersArray.pop(counter)
        counter += 1
    updateUntriedLetterString()
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
        elif x == "0":
            removeDeadLetter(words[index][counter])
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
    counter = 0
    for x in correctLetters:
        if len(x) != 1:
            correctLetters[counter] = fixLogicString(correctLetters[counter])
        counter += 1
    correctLetters = str(correctLetters)[2:-2].replace("', '", " ")
def fixLogicString(string):
    letterStr = ""
    notLetterStr = ""
    counter = 0
    while counter < len(string):
        if counter % 2 == 0:
            if string[counter] == "!":
                notLetterStr = notLetterStr + string[counter + 1]
            elif string[counter] == "~":
                letterStr = letterStr + string[counter + 1]
            # print(string[counter], string[counter+1])
        counter += 1

    returnString = letterStr + "!" + notLetterStr
    return returnString

verbose = False
addAttempt("CRANE", "02000")  # 1/6
addAttempt("STORY", "10210")  # 2/6
addAttempt("BROCK", "02200")  # 3/6
addAttempt("GROSS", "22202")  # 4/6
# addAttempt("AGENT", "20200")  # 5/6
# addAttempt("AHEAD", "22222")  # 6/6
cleanAndPrint()

def checkOneCharRemaining():
    # only works if 4/5 characters fully solved
    global allPossibilities
    checkArray = [ 0, 0, 0, 0, 0 ]
    counter = 0
    for x in allPossibilities:
        if len(x) == 1:
            checkArray[counter] = 1
        counter += 1
    counter = 0
    countNumOne = 0
    badPos = None
    for x in allPossibilities:
        if len(x) == 1:
            countNumOne += 1
        else:
            badPos = counter
        counter += 1
    startStr = ""
    counter = 0
    while counter < badPos:
        startStr = startStr + allPossibilities[counter]
        counter += 1

    endStr = ""
    counter = badPos + 1
    while counter < len(allPossibilities):
        endStr = endStr + allPossibilities[counter]
        counter += 1

    remLetters = "DFHIJLMPQUVWXZS"
    for x in remLetters:
        formedWord = f"{startStr}{x}{endStr}"
        if Words.checkWord(formedWord) == True:
            print(formedWord)

# checkOneCharRemaining()
# Words.printWords("middle", "ros")
# Words.findValidWords(allPossibilities, "middle", "ro")
