# inf109
Python exercises for inf109 - autumn 2017

## Assignment 5 

INF109 – Computer Programming for Science 
- This is the fifth of X assignments. You can get a total of 15 points for this assignment.  
- The submission deadline is Monday, XXXXXXXX, 23.59.  
- Please submit your assignment as a single .py file on mitt.uib.no.  
- This assignment text is available only in English, but you can of course use Norwegian in your programs.  
- The tasks should be submitted individually, i.e. it should be your own work. However some cooperation and discussion is allowed.

## Hangman ##

You have seen graphics.py to draw some lines and shapes on your screen. To make it a bit more fun, you will program the popular game Hangman for this week’s assignment using the grahpics.py package.
In the game Hangman the goal of the player is to correctly guess all the letters in a secret word. The secret word is shown with a row of underscores, which also indicates the number of letters in the word. By suggesting a letter at a time, the player can try to find out which word is hidden behind the underscores. If the player guesses a correct letter, then this letter will be displayed on the screen in all the correct positions in the word. The player wins the game if he has correctly guessed all the letters of the word within at most 7 misses.

As an example here, the game will start by displaying 
_ _ _ _ _
if the secret word is hello.
If the player types the letter h, he/she gets to see 
h _ _ _ _
and if he then types l, he gets to see 
h _ l l _
If after that, he types t or h or l, and then he will still see
h _ l l _

## Tasks 
- All tasks are described below and followed each other; you will use functions from previous tasks.

### Task 1A: Hide the secret word
In the game Hangman, our program needs to keep track of which letters of the secret word have been guessed correctly. We need also to be able to display a combination of letters and underscores as described before. For this purpose, a list is useful. Task 1 is to make a Python function makeCopy(secretWord). This function shall take as parameter a string secretWord and it shall return a list secretList that consists of as many ”_” as there are letters in secretWord.

For example, you could do: 
```Python
def makeCopy(secretWord): 
# Return a list of underscores with the same length as the word in the input 
```
You can use this example to test if your function works correctly. 
```
>>> makeCopy(’something’)
[’_’, ’_’, ’_’, ’_’, ’_’, ’_’, ’_’, ’_’, ’_’] 
>>> makeCopy(’python’)
[’_’, ’_’, ’_’, ’_’, ’_’, ’_’] 
>>> makeCopy(’off’) 
[’_’, ’_’, ’_’] 
```
```secretList``` will then be displayed as a Text object in a GraphWin object using function showScreen.
```Python
def showScreen(secretList): 
    height = 500 width = 250 
    win = GraphWin("The Hangman", width , height) 
    middleOfWord = Point(width/2, height/2) 
    word = Text(middleOfWord , secretList) 
    word.draw(win) 
    return (win, height, width) 
```
Then you need to build a function getWord to show the secretList in the graphics windows. 
```Python
def getWord(secretWord):
# Show the secretList in the graphics window using makeCopy and showScreen 
function.
# Make the window close after you have clicked on the screen with your mouse. 
```
You can use this example to test if your function works correctly. 
```
>>> getWord(’something’) 
>>> getWord(’python’) 
>>> getWord(’off’) 
```

## Task 1B: Check hits 
Now we will ask the player to type a letter and we will find out whether the letter is belong to the secret word. We define that a typed letter is correct if this letter is in the secret word and it has not been guessed earlier. If the letter is correct, then the player will get to know all the positions of the letter in the secret word. 
Assume that we are given a string secretWord and we have created a list secretList with secretList = makeCopy(secretWord). 
In this task, you will make a Python function checkHit(secretWord, secretList, ltr). The function shall take as parameters the string secretWord, the list secretList and a letter s. For every appearance of s in secretWord, you shall modify secretList to contain s in the corresponding position. If s is not in secretWord, or if s is already in secretList, then the function shall not modify secretList. The function shall return secretList and an integer hits that indicates how many (new) appearances of s there are in secretWord. The number hits shall be positive only if the letter is correct. If s was already in secretList then hits shall be 0. You can assume that secretWord consists only of lowercase letters and s is a lowercase letter. 
Make it so that the GraphWin object waits for keyboard input. The Text object from the previous task should be updated with the new version of secretList, and the number of hits of the letter that was guessed should be displayed in a Text object underneath the Text object with the secretList. 
You will make the following method: 
```Python
def checkHit(secretWord , secretList , s):
# Return secretList and hit; the updated secretList with the guessed letters, and the number of hits for the currect guessed letter (which is 0 is it doesn’t occur in the word)
```
You will call your checkHit function using makeCopy(“something”) as an argument for secretList and the corresponding word “something” as the argument secretWord and the character “s” as an input test letter.
In your Python code you will just print out the secretList and hit variable values.
```
>>> secretList, hit = checkHit(’something’, makeCopy(’something’), ‘s’) 
>>> print(secretList)
>>> print(hit)
[’s’, ’_’, ’_’, ’_’, ’_’, ’_’, ’_’, ’_’, ’_’] 
1
```
Use the following example to test if your function works correctly with all the previously created functions. 
```Python
secretWord = “something”
secretList =  makeCopy(secreWord)
win, width, height = showScreen(secretList)
middleOfWord = Point(width/2, height/2)
word = Text(middleOfWord, secretList)
word.draw(win)
middleOfHits = Point(width/2, height*3/4)
countHits = 0
hits = Text(middleOfHits, countHits)
hits.draw(win)
# Write the rest of your testing code here. It should have a loop that waits for a
# key to be struck and call checkHit as previously shown. If the player hits a
# correct letter contained in the not so secret word secretWord “something” then
# the variable word is updated and the number of hit displayed under it. As long
# as the number of hits is smaller than the secretWord the guessing can continue.
# When the guessing is done mouse clicking shall close the window.
```


## Task 1C: Draw Hangman letters
In this task you will handle the part that displays the Hangman if errors are made while guessing the word. Here, the actual Hangman will not be a drawn version but a simpler version where only the letters of the word ‘HANGMAN’ appear while the player is making mistakes in guessing the word.
You will have to make a function called drawHangmanLetters. This function is one of the core of our game functions and will be reused later.
This function drawHangmanLetters will have a GraphWin object as argument, and will be responsible for drawing the hangman letters. 
Another argument to this function will be the list of letters corresponding to the current state of the hangman word displayed for every mistake the player has made. This argument list will be called textList and will contain only letters.
Also, the player has 7 lives, so you will have to keep track of them and acting accordingly in your function drawHangmanLetters(textList, lives, win)

```Python
def drawHangmanLetters(textList, lives, win):

    # Your code to manage the undrawing of previous hangman word state

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

    # Your code to manage the undrawing of previous hangman word state
```


In that snippet of your function the drawing part has been handled. However, you will have to deal with the previous and current state of the object drawn in your GraphWin ‘win’. Write the code needed instead of the commented areas.


To actually use your function drawHangmanLetters you will call it from another function main(), which will be the ‘dirigent’ of your code along this assignment.
This function is organized as follows:
```Python
def main():
    filename = "words.txt"
    keepPlayer1 = True

    height = 600
    width = 400
    win = GraphWin("The Hungman", width, height)
    turn_id = 0

    # Rest of your code goes here.
```
KeepPlayer1 boolean and turn_id variables will be used later on the assignment and will simply be used to track if the player wants to play again.

In this main() function you will also handle the call of your function drawHangmanLetters.  It will be called inside a loop and depending on the number of lives that you have, this function will draw the appropriate piece of the hangman. The letters will be drawn upon keyboard key pressing and the window will be closed upon clicking anywhere inside it. Note that it is just to test the drawing part no secret word is to be guessed yet.
You can use this example to test if your function works correctly. 
```
>>> main ()
```



## Task 1D: The play function 
In this task you shall make a Python function play(secretWord, win) which implements the game Hangman for a given secret word secretWord and a given GraphWin object win. The function play shall take in as parameter the string secretWord that consists of lowercase letters. The function shall start by creating secretList using the function makeCopy, and show this list in the GraphWin object. Again, set the initial number of lives to be 7. As long as the player has a positive number of lives, and as long as the player has not guessed correctly all the letters in secretWord, the game shall go on. 
In each iteration you should ask the player to type a lowercase letter that is read into the variable ltr. You should then use the function call secretList, hits = checkHit(secretWord, secretList, ltr) to find out the number of new hits and to update secretList. If hits is 0 then we say that it was a wrong letter, and the player loses a life. Visually, the appropriate letter of the word Hangman will be drawn on the GraphWin object. (Note that this simplification differs from the original version in which the player does not lose a life if he types the same letter several times.) 
At the end of each iteration you should update the Text object with the secretList. The actual drawing part of the text will be detailed in the following code box. To prepare the next task of our game your function will also divide the screen vertically in two as shown in the body of the detailed function.
When the player has no more lives, or when all the letters in secretWord have been guessed correctly, the game will end with a message about victory or loss and the window will be close upon mouse clicking. 
The play function is basically combining the above functions and could be programmed as follows: 

```Python
def play(secretWord, win): # No return value
    # Get a word, which has to be guessed.
    # Visually display the word,  after dividing the screen in two, with unguessed letters as underscores:
    middleLine = Line(Point(0, height/2), Point(width, height/2))
    middleLine.draw(win)
    middleOfWord = Point(width/2, height*9/10)
    word = # Your code for word variable goes here

    # A message should be displayed indicating the outcome:
    textPoint = Point(width/2, height* 7/10)
    displayText = {'start':'Guess a letter.',
                   'good':'Well done, guess again.',
                   'bad':'Not in word, guess again.',
                   'win':'You have guessed the word.',
                   'lose':'You have not guessed the word.',}
    theText = Text(textPoint, displayText['start'])
    theText.draw(win)

    # Also display the hangman word letters, to indicate how many lives are left.
    # User inputs letters using the keyboard, and the word and hangman word letters are updated with every input.
    # After the word is guessed, or the player hangs, you can close the window by clicking in it.
```

A running example is shown as follows, in your main() function: 
```Python
def main():
    # other part of the code you were given before
    # …
    play(’something’, win)
```


Be careful here, you will have to comment out the code specific to TASK 1C you had in your main() before.


And again, you can call it like this:


Follows an example of the screen with 6 successful letters guessed and 6 mistakes.
 




## Task 1E: End game 
In this task we will complete our program. You already have the function main(). Now we will add for the player to have the possibility to play several rounds of Hangman. This means that every time the player has won or lost the game, he should get the option to play one more round with a new word. 
We have many secret words in the ‘words.txt’ text file that the player does not know about. Every line of words.txt contains a word in lowercase letters. The player should be able to play as many rounds as he wants. 
As long as the player wants to guess the letters in a new secret word, your function fetches a secret word from the file words.txt, let the string secretWord contain this word, and call the function play(secretWord, win). 
Here the file named words.txt will contain all the fixed data (the words) the player has to guess for the Hangman game. The variable secretWorld will simply be a random choice from that data file (remember to import random at the beginning of your file!).
Here, the function loadFile(filename) is provided as follows:

```Python
def loadFile(filename):
    secret_word_list = []
    with open(filename, "r") as wordFile:
        for line in wordFile.readlines():
            secret_word = line.rstrip()
            secret_word_list.append(secret_word)
    wordFile.close()
    return secret_word_list
```

Note that it returns a list for the random.choice method to be used on it. Use random.choice(loadfile(filename)) to access your randomized secretWord.

When play is finished with a word, we will ask the player whether he wans to continue or quit, drawing pretty boxes on the screen and using the function getMouse(). The program should stop when the player does not want to play anymore. This will be achieved with the provided function endgame(win).

Here is a piece of code for this last bit: 

```Python
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
```

This function endgame(win) will have to be called from the play(secretWord, win) function to then return the choice of the player in form of a Boolean (False: continue playing, True: stop playing again).
Once you have linked those two function (endgame and play) correctly you will call the play function in your main() ‘dirigent’ function. This call will be done using a loop and the Boolean keepPlayer1 you initialized at the very beginning of your main() function.
Be careful, here you will have to manage the opening and closing of the window for each round played by the user. By designing it like this, if the user clicks on ‘Yes’ to play again the previous window will be closed at the end of the play(secretWord, win) function. You will have to test its state and to reopen it if needed.
 




## Task 1F: Player’s score management
This last task is about putting everything together to create a full single player experience.
To achieve this you are provided yet another new function that will welcome the player in our game. The intro_singleplayer(win) function is given as follows:

```Python
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
```

It is a very basic function that greets the player and provide an ‘Entry’, graphical element for the user to input his player name.
It returns an object name_list which is simply a list with the player name.
Now, as an introduction to the game, in your main() function, you will call this intro_singleplayer(win) function. By doing so, you will obtain a list of player names (only one name for single player).  After obtaining the name, create a dictionary score_dict variable and initialize it with the player name(s) and the current first score (being 0).
Then, you will create another logical step. You remember in task 1D, we created the playing screen; the first half of it was left blank. You will have to create a function player_screen(name_list, score_dict, win). This function will simply display the following text: 
- "Welcome {0}, we hope you will not get the Hangman! :)"
- "Your current score is: {0}"
Place this text wherever on the first half of the playing window so that it is ergonomic. Also, note that {0} represents a place holder for the variable and will have to be formatted.
Call this function player_screen from the play function. Be careful of its arguments, since you’re creating them on the ‘upper’ main() function they will have to be passed down through the play function. Modify your play function accordingly.
You want to be able to follow the player’s score using your freshly created score_dict. Modify your play function so that it returns 2 variables; both playAgain and lives. lives variable will be the score of the player. Then, take the loop you created in your main() function in task 1E and slightly modify it so that it still deals with keepPlayer1 boolean and another variable player1_score that will contain the score of the player after each round and will be store correctly in score_dict. By doing so, score_dcict used in your player_screen function will display and update the player’s score after each round.

You can test out your full player one experience by calling your main function like always. 

## Supplementary or alternative tasks:
### Task 1G: Already used letters
In this task we will modify the principal play function to display for the player the current letters he/she has already used. In the provided code snipet of the first play function (see task 1D), you will add the following entry to the dictionary displayText: ‘already’ : ‘You already tried this letter’.
Then, still in the play function you will add the following text:

```Python
    alreadyPoint = Point(width / 2, 9*height/12)
    alreadyText = Text(alreadyPoint, 'Letters already tried: ')
    alreadyText.draw(win)
```

In your playing loop you will have to manage a list of already used letters and display at anytime the letters the player has already used. Also, if the player hit an already used letter, your game will display the alreadyText message.
The bottom part of your screen shall look like the following when hitting twice the letter ‘o’. Note That in this game version, the Hangman goes on when the player hits an already used letter.

### Task 1H: Multiplayer
The multiplayer will be designed as follows: The 2 players input their names on the multiplayer introduction screen. Then, the first player plays the hangman rounds as long as he pleases. Once the first player is done it is the second player’s turn to play his turns. At anytime, the scores and turns are displayed for the players on the top part of the screen.
As often, this later task is also about wrapping up everything and putting up functions together. Here you will easily modify your previous function player_screen(name_list, score_dict, win). This function will simply display the following text: 
-	"Welcome {0} and {1}, we hope none of you will get the Hangman! :)"
-	"{0} current score is: {1}"
-	“It is {0}’s turn”
Place this text wherever on the first half of the playing window so that it is ergonomic. Also, note that {0} or {1} represent a placeholder for the variables and will have to be formatted.
To be able to indicate the current player’s turn, you will have to add another variable, turn_id, as function argument. The variable turn_id will be manage in the main function, passed to the play function and finally reach the player_screen function you modified for player scores and turns display.
Taken the previous explanation into account, modify yours principal functions main() and play() to manage 2 players hangman game.


## Submission 
Save your program in a .py file called oblig5-abc123.py, where “abc123” should be replaced with your login ID on Mitt UIB. 
Marking/assessment 
For this assignment, you can get a maximum of 15 points. The distribution of points is as follows. 
The program works as expected. Here you will lose marks if your program prints the wrong data or in the wrong format (differs from the example), crashes in any manner, or if function names are not as stated. 
The program is well documented, clear, and with comments. You will lose marks if your program is not commented sufficiently, but also if there are too many comments. You can also lose marks if the program is unclear, meaning that it is difficult for another person to familiarize themselves with the program’s functionality. 
Naming It is required that the names of variables and functions are sensibly chosen and that the naming used is consistent: either mixedCase or with underscore. 1 
Questions and/or complaints on the marking can be directed to one of the group leaders. 
The program works as expected The program is well documented, clear, and with comments Naming 	12 (approximately 7 + 5) 2 1 
	15 
 
1 mixedCase refers to variables such as innlestData, and underscore refers to variables entered like innlest data. Choose one of these two and stick to that. Never start with a capital letter, e.g. InnlestData or similar, as these are reserved for class names, which are partially outside of the curriculum for this course. 


