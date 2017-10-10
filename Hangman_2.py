from graphics import *
import random

'''Task 1A'''
def makeCopy(secretWord):
    secretList = ["_"] * len(secretWord)
    return secretList

def loadFile(filename):
    secret_word_list = []
    with open(filename, "r") as wordFile:
        for line in wordFile.readlines():
            secret_word = line.rstrip()
            secret_word_list.append(secret_word)
    wordFile.close()
    return secret_word_list

def checkHit(secretWord, secretList, s):
    hit = 0
    for i in range(len(secretWord)):
        if secretWord[i] == s and secretList[i] == "_":
            hit = hit + 1
            secretList[i] = s
    return secretList, hit

def showScreen(secretList):
    height = 500
    width = 250
    win = GraphWin("The Antman", width, height)
    middleOfWord = Point(width/2, height/2)
    word = Text(middleOfWord, secretList)
    word.draw(win)
    return (win, width, height)

def getWord(secretWord):
    word = makeCopy(secretWord)
    (win, width, height) = showScreen(word)
    win.getMouse()
    win.close()

def askLtr(secretWord, secretList):
    win, width, height = showScreen(secretList)
    middleOfWord = Point(width/2, height/2)
    word = Text(middleOfWord, secretList)
    word.draw(win)
    textPoint = Point(width/2, height/4)
    displayText = {'start':'Guess a letter',
                   'good':'Well done, guess again.',
                   'bad':'Not in word, guess again',
                   'win':'You have guessed the word.'}
    theText = Text(textPoint, displayText['start'])
    theText.draw(win)
    countHits = 0
    while countHits < len(secretWord) :
        letter = win.getKey()
        secretList, hit = checkHit(secretWord, secretList, letter)
        if hit == 0:
            theText.setText(displayText['bad'])
        else:
            word.setText(secretList)
            theText.setText(displayText['good'])
            countHits = countHits + hit
    theText.setText(displayText['win'])
    win.getMouse()
    win.close()

def drawBottom(win, width, height):
    left = width/4
    right = width - width/4
    bottom = height - height/4
    bottomLeft = Point(width/8, height*3/4)
    bottomRight = Point(width*7/8, height*3/4)
    bottomBar = Line(bottomLeft,
                     bottomRight)
    bottomBar.draw(win)

def drawVerticalTopNoose(win, width, height):
    bottomLeft = Point(width/8, height*3/4)
    topLeft = Point(width/8, height/8)
    verticalBar = Line(bottomLeft,
                       topLeft)
    topLeft = Point(width / 8, height / 8)
    topMiddle = Point(width / 2, height / 8)
    topBar = Line(topLeft, topMiddle)
    topBar.draw(win)
    verticalBar.draw(win)

    left = width/4
    middle = width/2
    top = height/4
    topMiddle = Point(width/2, height/8)
    endNoose = Point(width/2, height/4)
    noose = Line(endNoose, topMiddle)
    noose.draw(win)

def drawHead(win, width, height):
    head = Circle(Point(width/2, height*5/16), height/16)
    head.draw(win)

def drawBody(win, width, height):
    topBody = Point(width/2, height*3/8)
    bottomBody = Point(width/2, height/2)
    midBody = Point(width/2, height*7/16)

    body1 = Circle(topBody, height / 32)
    body2 = Circle(bottomBody, height / 32)
    body3 = Circle(midBody, height / 32)
    body1.draw(win)
    body2.draw(win)
    body3.draw(win)
    return topBody, midBody, bottomBody

def drawLegs(win, width, height):

    heights = [height*3/8, height/2, height*7/16]
    widths = [width/2, width/2, width/2]

    for i in range(3):
        pointleg1 = Point(widths[i] + height / 32, heights[i])
        pointleg2 = Point(widths[i] + height / 16, heights[i])
        pointleg21 = Point(widths[i] - height / 32, heights[i])
        pointleg22 = Point(widths[i] - height / 16, heights[i])
        leg1 = Line(pointleg1, pointleg2)
        leg2 = Line(pointleg21, pointleg22)
        leg1.draw(win)
        leg2.draw(win)

def drawAntennas(win, width, height):
    antenna11 = Point((width/2)-(height/32), height / 4)
    antenna12 = Point((width / 2) - (2*height / 32), (height / 4)-(height / 32))

    antenna21 = Point((width/2)+(height/32), height / 4)
    antenna22 = Point((width / 2) + (2*height / 32), (height / 4)-(2*height / 32))

    ant1 = Line(antenna11, antenna12)
    ant2 = Line(antenna21, antenna22)
    ant1.draw(win)
    ant2.draw(win)

def drawTheAntman(lives, win, width, height):

    if lives == 6:
        drawBottom(win, width, height)
    if lives == 5:
        drawVerticalTopNoose(win, width, height)
    elif lives == 4:
        drawHead(win, width, height)
    elif lives == 3:
        drawBody(win, width, height)
    elif lives == 2:
        drawLegs(win, width, height)
    elif lives == 1:
        drawAntennas(win, width, height)

def task1c():
    height = 500
    width = 250
    win = GraphWin("The Antman", width, height)
    lives = 10
    while lives > 0:
        win.getKey()
        drawTheAntman(lives, win, width, height)
        lives -= 1
    win.getMouse()
    win.close()

def play(secretWord):
    secretList = makeCopy(secretWord)
    lives = 6
    countHits = 0
    height = 500
    width = 250
    win = GraphWin("The Antman", width, height)
    middleOfWord = Point(width/2, height*7/8)
    word = Text(middleOfWord, secretList)
    word.draw(win)
    textPoint = Point(width/2, height/16)
    displayText = {'start':'Guess a letter.',
                   'good':'Well done, guess again.',
                   'bad':'Not in word, guess again.',
                   'win':'You have guessed the word.',
                   'lose':'You have not guessed the word.',
                   'already':'You already tried this letter'}
    theText = Text(textPoint, displayText['start'])
    theText.draw(win)

    letter_list = []
    alreadyPoint = Point(width / 2, height / 10)
    alreadyText = Text(alreadyPoint, 'Letters already tried: ')
    alreadyText.draw(win)

    while lives > 0 and countHits < len(secretWord):
        letter = win.getKey()
        secretList, hit = checkHit(secretWord, secretList, letter)

        if hit == 0 and not letter in letter_list:
            letter_list.append(letter)
            theText.setText(displayText['bad'])
            alreadyText.setText('Letters already tried: {0}'.format(' '.join(str(p) for p in letter_list)))
            drawTheAntman(lives, win, width, height)
            lives = lives - 1
        elif hit == 0 and letter in letter_list:
            theText.setText(displayText['already'])
            alreadyText.setText('Letters already tried: {0}'.format(' '.join(str(p) for p in letter_list)))
            drawTheAntman(lives, win, width, height)
            lives = lives - 1
        else:
            letter_list.append(letter)
            theText.setText(displayText['good'])
            alreadyText.setText('Letters already tried: {0}'.format(' '.join(str(p) for p in letter_list)))
            word.setText(secretList)
            countHits = countHits + hit

    if lives > 0:
        theText.setText(displayText['win'])
    else:
        theText.setText(displayText['lose'])
    playAgain = endGame(win, width, height)
    win.close()
    return playAgain

def endGame(win, width, height):
    theEnd = Text(Point(width/4, height*15/16), 'Play again?')
    yesBox = Rectangle(Point(width/2, height*29/32), Point(width*3/4, height*31/32))
    noBox = Rectangle(Point(width*3/4, height*29/32), Point(width, height*31/32))
    yesText = Text(Point(width*5/8, height*15/16), 'Yes')
    noText = Text(Point(width*7/8, height*15/16), 'No')
    yesBox.setFill('green')
    noBox.setFill('red')
    theEnd.draw(win)
    yesBox.draw(win)
    yesText.draw(win)
    noBox.draw(win)
    noText.draw(win)
    while True:
        clickPoint = win.getMouse()
        if clickPoint.getY() > height*29/32:
            if clickPoint.getX() > width*3/4:
                # play again
                return False
            elif clickPoint.getX() > width/2:
                # not play again
                return True

def main():
    filename = "words.txt"
    keepPlaying = True
    while keepPlaying:
        secretWord = random.choice(loadFile(filename))
        keepPlaying = play(secretWord)


main()