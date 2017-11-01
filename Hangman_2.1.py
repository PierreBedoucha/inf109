from graphics import *
import random

'''TASK 1A'''
def makeCopy(secretWord):
    secretList = ["_"] * len(secretWord)
    return secretList

print(makeCopy("something"))
print(makeCopy("off"))

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

getWord("something")
getWord("off")

'''TASK 1B'''
def checkHit(secretWord, secretList, s):
    hit = 0
    for i in range(len(secretWord)):
        if secretWord[i] == s and secretList[i] == "_":
            hit = hit + 1
            secretList[i] = s
    return secretList, hit

secretWord = "something"
secretList = makeCopy(secretWord)
win, width, height = showScreen(secretList)
middleOfWord = Point(width/2, height/2)
word = Text(middleOfWord, secretList)
word.draw(win)
middleOfHits = Point(width/2, height*3/4)
countHits = 0
hits = Text(middleOfHits, countHits)
hits.draw(win)
while countHits < len(secretWord):
    letter = win.getKey()
    secretList, hit = checkHit(secretWord, secretList, letter)
    if not hit == 0:
        word.setText(secretList)
        hits.setText(countHits)
        countHits = countHits + hit
win.getMouse()
win.close()


'''TASK 1C'''
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

'''TASK 1C'''
def loadFile(filename):
    secret_word_list = []
    with open(filename, "r") as wordFile:
        for line in wordFile.readlines():
            secret_word = line.rstrip()
            secret_word_list.append(secret_word)
    wordFile.close()
    return secret_word_list


'''TASK 1D, TASK 1E: basic play function to call from main()'''
# def play(secretWord, win):
#     secretList = makeCopy(secretWord)
#     lives = 7
#     countHits = 0
#
#     '''Add fr window manageent on TASK 1E'''
#     if win.isClosed():
#         height = 600
#         width = 400
#         win = GraphWin("The Hungman", width, height)
#
#     width = win.width
#     height = win.height
#
#     middleLine = Line(Point(0, height/2), Point(width, height/2))
#     middleLine.draw(win)
#     middleOfWord = Point(width/2, height*9/10)
#     word = Text(middleOfWord, secretList)
#     word.draw(win)
#     textPoint = Point(width/2, height* 7/10)
#     displayText = {'start':'Guess a letter.',
#                    'good':'Well done, guess again.',
#                    'bad':'Not in word, guess again.',
#                    'win':'You have guessed the word.',
#                    'lose':'You have not guessed the word.',}
#     theText = Text(textPoint, displayText['start'])
#     theText.draw(win)
#
#     textList = []
#     while lives > 0 and countHits < len(secretWord):
#         letter = win.getKey()
#         secretList, hit = checkHit(secretWord, secretList, letter)
#
#         if hit == 0:
#             theText.setText(displayText['bad'])
#             drawHangmanLetters(textList, lives, win)
#             lives = lives - 1
#         else:
#             theText.setText(displayText['good'])
#             word.setText(secretList)
#             countHits = countHits + hit
#     if lives > 0:
#         theText.setText(displayText['win'])
#     else:
#         theText.setText(displayText['lose'])
#     # win.getMouse()
#     '''TASK 1E: To replace win.getMouse() with endGame(win) function'''
#     playAgain = endGame(win)
#     win.close()
#     '''TASK 1E: Add playAgain variable return'''
#     return playAgain

'''TASK 1E'''
def endGame(win):
    theEnd = Text(Point(win.width/4, win.height*15/16), 'Play again?')
    yesBox = Rectangle(Point(win.width/2, win.height*29/32), Point(win.width*3/4, win.height*31/32))
    noBox = Rectangle(Point(win.width*3/4, win.height*29/32), Point(win.width, win.height*31/32))
    yesText = Text(Point(win.width*5/8, win.height*15/16), 'Yes')
    noText = Text(Point(win.width*7/8, win.height*15/16), 'No')
    yesBox.setFill('green')
    noBox.setFill('red')
    theEnd.draw(win)
    yesBox.draw(win)
    yesText.draw(win)
    noBox.draw(win)
    noText.draw(win)
    while True:
        clickPoint = win.getMouse()
        if clickPoint.getY() > win.height*29/32:
            if clickPoint.getX() > win.width*3/4:
                # play again
                return False
            elif clickPoint.getX() > win.width/2:
                # not play again
                return True

'''TASK 1F'''
def intro_singleplayer(win):
    '''add a starting page'''
    text1 = Text(Point(win.width/2, win.height/6),
                 "Info about the game:\nIt's a regular Hangman game.\nTry to guess a secret word letter by letter.")
    text2 = Text(Point(win.width/2, win.height/3), "You have 7 lives until the full word 'HANGMAN' is written on the screen\n Good Luck!")
    text3 = Text(Point(win.width/2, win.height/2),
                 "Enter your Player name(s) and click anywhere else to start.")
    text1.draw(win)
    text2.draw(win)
    text3.draw(win)
    name_list = []

    # Player
    playername1 = Entry(Point(win.width/2, win.height-100), 15)
    playername1.setText("Name player 1")
    playername1.draw(win)
    win.getMouse()
    name_list.append(playername1.getText())
    text1.undraw()
    text2.undraw()
    text3.undraw()
    playername1.undraw()

    return name_list

'''TASK 1F'''
def player_screen(name_list, score_dict, win):
    text1 = Text(Point(win.width / 2, win.height / 6),
                 "Welcome {0}, we hope you will not get the Hangman! :)".format(name_list[0]))
    if score_dict:
        text2 = Text(Point(win.width / 2, win.height / 3),
                     "Your current score is: {0}".format(score_dict[name_list[0]]))
        text2.draw(win)
    text1.draw(win)

'''TASK 1F Single player. Enhanced play function for score management.'''
# def play(secretWord, score_dict, name_list, win):
#     secretList = makeCopy(secretWord)
#     lives = 7
#     countHits = 0
#
#     '''Add fr window manageent on TASK 1E'''
#     if win.isClosed():
#         height = 600
#         width = 400
#         win = GraphWin("The Hungman", width, height)
#
#     width = win.width
#     height = win.height
#
#     player_screen(name_list, score_dict, win)
#
#     middleLine = Line(Point(0, height/2), Point(width, height/2))
#     middleLine.draw(win)
#     middleOfWord = Point(width/2, height*9/10)
#     word = Text(middleOfWord, secretList)
#     word.draw(win)
#     textPoint = Point(width/2, height* 7/10)
#     displayText = {'start':'Guess a letter.',
#                    'good':'Well done, guess again.',
#                    'bad':'Not in word, guess again.',
#                    'win':'You have guessed the word.',
#                    'lose':'You have not guessed the word.',}
#     theText = Text(textPoint, displayText['start'])
#     theText.draw(win)
#
#     textList = []
#     while lives > 0 and countHits < len(secretWord):
#         letter = win.getKey()
#         secretList, hit = checkHit(secretWord, secretList, letter)
#
#         if hit == 0:
#             theText.setText(displayText['bad'])
#             drawHangmanLetters(textList, lives, win)
#             lives = lives - 1
#         else:
#             theText.setText(displayText['good'])
#             word.setText(secretList)
#             countHits = countHits + hit
#     if lives > 0:
#         theText.setText(displayText['win'])
#     else:
#         theText.setText(displayText['lose'])
#     '''To replace win.getMouse() with endGame(win) function for TASK 1E'''
#     # win.getMouse()
#     playAgain = endGame(win)
#     win.close()
#     '''Add playAgain variable return for TASK 1E'''
#     '''Add lives variable as score for TASK 1F'''
#     return playAgain, lives


'''TASK 1G, TASK 1H
from earlier TASK 1D for: score management, already used letters, and single/multiplayer'''
def play(secretWord, score_dict, name_list, turn_id, win):
    secretList = makeCopy(secretWord)
    lives = 7
    countHits = 0

    if win.isClosed():
        height = 600
        width = 400
        win = GraphWin("The Hungman", width, height)

    width = win.width
    height = win.height

    # Here we use the multiplayer screen version
    multiplayer_screen(name_list, score_dict, turn_id, win)

    middleLine = Line(Point(0, height / 2), Point(width, height / 2))
    middleLine.draw(win)
    middleOfWord = Point(width / 2, height * 9 / 10)
    word = Text(middleOfWord, secretList)
    word.draw(win)
    textPoint = Point(width / 2, height * 7 / 10)
    displayText = {'start': 'Guess a letter.',
                   'good': 'Well done, guess again.',
                   'bad': 'Not in word, guess again.',
                   'win': 'You have guessed the word.',
                   'lose': 'You have not guessed the word.',
                   'already': 'You already tried this letter'}
    theText = Text(textPoint, displayText['start'])
    theText.draw(win)

    letter_list = []
    textList = []
    alreadyPoint = Point(width / 2, 9 * height / 12)
    alreadyText = Text(alreadyPoint, 'Letters already tried: ')
    # TASK 1G: un/comment for already used letters
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
            # TASK 1G: un/comment for already used letters
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
    playAgain = endGame(win)
    win.close()

    return playAgain, lives

'''TASK 1H'''
def intro_multiplayer(win):
    '''add a starting page'''
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

'''TASK 1H'''
def multiplayer_screen(name_list, score_dict, turn_id, win):
    if not len(name_list) == 1:
        text1 = Text(Point(win.width / 2, win.height / 6),
                     "Welcome {0} and {1},\n we hope none of you will get the Hangman! :)".format(name_list[0],
                                                                                                  name_list[1]))
        if score_dict:
            text2 = Text(Point(win.width / 2, win.height / 3),
                         "{0} current score is: {1}".format(name_list[0], score_dict[name_list[0]]))
            text3 = Text(Point(win.width / 2, win.height * 5 / 12),
                         "{0} current score is: {1}".format(name_list[1], score_dict[name_list[1]]))
            text2.draw(win)
            text3.draw(win)
        text4 = Text(Point(win.width / 2, win.height * 7 / 12),
                     "It is {0}'s turn".format(name_list[turn_id]))
        text4.setFill('blue')
        text1.draw(win)
        text4.draw(win)



'''TASK 1C'''
def main():
    filename = "words.txt"
    keepPlayer1 = True

    height = 600
    width = 400
    win = GraphWin("The Hungman", width, height)
    turn_id = 0

    '''TASK 1C: only this part of the code with the needed variables'''
    # textList = []
    # lives = 7
    # while lives > 0:
    #     win.getKey()
    #     drawHangmanLetters(textList, lives, win)
    #     lives -= 1
    # win.getMouse()
    # win.close()

    '''TASK 1D: commnent out TASK 1C above'''
    # play('something', win)

    '''TASK 1E'''
    # while keepPlayer1:
    #     secretWord = random.choice(loadFile(filename))
    #     keepPlayer1 = play(secretWord, win)

    '''TASK 1F: single player with score management'''
    # name_list = intro_singleplayer(win)
    # score_dict = {name_list[0]: 0}

    '''TASK 1H: Multiplayer with score management'''
    keepPlayer2 = True
    name_list = intro_multiplayer(win)
    score_dict = {name_list[0]: 0, name_list[1]: 0}

    '''TASK 1F: only this loop for Single player with score management'''
    while keepPlayer1:
        secretWord = random.choice(loadFile(filename))
        '''TASK 1F: Score management only'''
        # keepPlayer1, player1_score = play(secretWord, score_dict, name_list, win)
        '''TASK 1G: modified play function with score management and already used letters'''
        keepPlayer1, player1_score = play(secretWord, score_dict, name_list, turn_id, win)

        score_dict[name_list[0]] += player1_score

    '''TASK 1H: To add or remove for SINGLE/MULTI'''
    turn_id = 1
    while keepPlayer2:
        secretWord = random.choice(loadFile(filename))
        keepPlayer2, player2_score = play(secretWord, score_dict, name_list, turn_id, win)
        score_dict[name_list[1]] += player2_score



main()

