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
    win = GraphWin("The Hangman", width, height)
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

def drawHangmanLetters(textList, lives, win):
    if textList:
        [i.undraw() for i in textList]

    hangmanPoint = Point(win.width / 2, win.height*8/10)
    hangmanText = Text(hangmanPoint, 'The Hangman: ')
    hangmanText.setSize(22)
    hangmanText.setTextColor('red')
    if lives == 7:
        hangmanText.setText('The Hangman: H')
    if lives == 6:
        hangmanText.setText('The Hangman: HA')
    elif lives == 5:
        hangmanText.setText('The Hangman: HAN')
    elif lives == 4:
        hangmanText.setText('The Hangman: HANG')
    elif lives == 3:
        hangmanText.setText('The Hangman: HANGM')
    elif lives == 2:
        hangmanText.setText('The Hangman: HANGMA')
    elif lives == 1:
        hangmanText.setText('The Hangman: HANGMAN')
    hangmanText.draw(win)
    textList.append(hangmanText)

def drawTheHangman(lives, win, width, height):

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
    win = GraphWin("The Hangman", width, height)
    lives = 10
    while lives > 0:
        win.getKey()
        drawTheHangman(lives, win, width, height)
        lives -= 1
    win.getMouse()
    win.close()


def player_screen(name_list, score_dict, win):
    if len(name_list) == 1:
        text1 = Text(Point(win.width/2, win.height/6),
                 "Welcome {0}, we hope you will not get the Hangman! :)".format(name_list[0]))
        if score_dict:
            text2 = Text(Point(win.width/2, win.height/3), "Your current score is: {0}".format(score_dict[name_list[0]]))
            text2.draw(win)
        text1.draw(win)


def multiplayer_screen(name_list, score_dict, win):

    turn_id=0

    if not len(name_list) == 1:
        text1 = Text(Point(win.width/2, win.height/6),
                 "Welcome {0} and {1},\n we hope none of you will get the Hangman! :)".format(name_list[0], name_list[1]))
        if score_dict:
            text2 = Text(Point(win.width/2, win.height/3), "{0} current score is: {1}".format(name_list[0], score_dict[name_list[0]]))
            text3 = Text(Point(win.width / 2, win.height*5/12),
                         "{0} current score is: {1}".format(name_list[1], score_dict[name_list[1]]))
            text2.draw(win)
            text3.draw(win)
        text4 = Text(Point(win.width/2, win.height*7/12),
                 "It is {0}'s turn".format(name_list[turn_id]))
        text4.setFill('blue')
        text1.draw(win)
        text4.draw(win)


def play(secretWord, score_dict, name_list, win):
    secretList = makeCopy(secretWord)
    lives = 7
    countHits = 0
    if win.isClosed():
        height = 600
        width = 400
        win = GraphWin("The Hungman", width, height)


    # name_list = intro(win)
    # turn_id = 0
    # multiplayer_screen(name_list, score_dict, win, turn_id)
    width = win.width
    height = win.height
    multiplayer_screen(name_list, score_dict, win)


    middleLine = Line(Point(0, height/2), Point(width, height/2))
    middleLine.draw(win)
    middleOfWord = Point(width/2, height*9/10)
    word = Text(middleOfWord, secretList)
    word.draw(win)
    textPoint = Point(width/2, height* 7/10)
    displayText = {'start':'Guess a letter.',
                   'good':'Well done, guess again.',
                   'bad':'Not in word, guess again.',
                   'win':'You have guessed the word.',
                   'lose':'You have not guessed the word.',
                   'already':'You already tried this letter'}
    theText = Text(textPoint, displayText['start'])
    theText.draw(win)

    letter_list = []
    textList = []
    alreadyPoint = Point(width / 2, 9*height/12)
    alreadyText = Text(alreadyPoint, 'Letters already tried: ')
    alreadyText.draw(win)

    while lives > 0 and countHits < len(secretWord):
        letter = win.getKey()
        secretList, hit = checkHit(secretWord, secretList, letter)

        if hit == 0 and not letter in letter_list:
            letter_list.append(letter)
            theText.setText(displayText['bad'])
            alreadyText.setText('Letters already tried: {0}'.format(' '.join(str(p) for p in letter_list)))
            drawHangmanLetters(textList, lives, win)
            lives = lives - 1
        elif hit == 0 and letter in letter_list:
            theText.setText(displayText['already'])
            alreadyText.setText('Letters already tried: {0}'.format(' '.join(str(p) for p in letter_list)))
            drawHangmanLetters(textList, lives, win)
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

    return playAgain, lives


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


def intro(win):
    '''add a starting page'''
    # win.setCoords(0, 0, 600, 400)
    text1 = Text(Point(win.width/2, win.height/6),
                 "Info about the game:\nIt's a regular Hangman game.\nTry to guess a secret word letter by letter.")
    text2 = Text(Point(win.width/2, win.height/3), "You have 7 lives until the full word 'HANGMAN' is written on the screen\n Good Luck!")
    text3 = Text(Point(win.width/2, win.height/2),
                 "Enter your Player name(s) and click anywhere else to start.")
    text1.draw(win)
    text2.draw(win)
    text3.draw(win)
    name_list = []

    # Players

    playername1 = Entry(Point(win.width/2, win.height-100), 15)
    playername1.setText("Name player 1")
    playername1.draw(win)
    playername2 = Entry(Point(win.width/2, win.height-70), 15)
    playername2.setText("Name player 2")
    playername2.draw(win)
    win.getMouse()
    name_list.append(playername1.getText())
    name_list.append(playername2.getText())
    text1.undraw()
    text2.undraw()
    text3.undraw()
    playername1.undraw()
    playername2.undraw()

    return name_list


def main():
    filename = "words.txt"
    keepPlaying = True


    height = 600
    width = 400
    win = GraphWin("The Hungman", width, height)

    name_list = intro(win)
    score_dict = {name_list[0]: 0, name_list[1]: 0}

    while keepPlaying:
        secretWord = random.choice(loadFile(filename))
        keepPlaying, player0_score  = play(secretWord, score_dict, name_list, win)
        score_dict[name_list[0]] += player0_score

main()