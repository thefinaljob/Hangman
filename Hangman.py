from __future__ import print_function
import random
#Our theme is: school
word_chosen =''
guessed_letters =[]
num_guess = 10
win_state = False
correct_guess = False

#Code above declares all the variables as global, so that they are able to be used everywhere

print('Our theme is school.')

def choose_word():
    #choses a random word to act as the secret that the player has to guess
    global word_chosen
    #arrays that stores word bank
    listofsecrets = ['teacher','student','math','english','history','science','computer']
    listofsecrets2 = ['world language','google classroom','honors chemistry','ap calculus']
    listofsecrets3 = ['quiz on friday','there is a test tomorrow','computer science and engineering','principles of engineering']
    choice_level = str(raw_input("Please choose your difficulty, easy, medium, or hard: "))
    if choice_level == 'easy':
        word_chosen = random.choice(listofsecrets)
    elif choice_level == 'medium':
        word_chosen = random.choice(listofsecrets2) #what words are chosen depend upon the user's choices
    elif choice_level == 'hard':
        word_chosen = random.choice(listofsecrets3)
    else:
        print("Invalid Input, choose again!")
        choose_word()
        
def disguise():
    
#disguises intitally so that user knows what to expect from word    
    for char in word_chosen:
        if char == ' ':
            print (' ', end='')
        else:
            print ('-', end='')
    print('')

def hangman():
    global win_state
    global num_guess
    global guessed_letters
    global correct_guess
    #makes all variables used in the function global
    letter_guess = raw_input("Enter your guess: ").lower() #makes everything lower case
    while len(letter_guess) != 1:
        print("Cheater! Only one letter is allowed at a time.")
        letter_guess = raw_input('Enter your guess: ')
    guessed_letters.append(letter_guess) #stores character in array
    correct_guess = False
    win_state = True
    for char in word_chosen: #prints out the letters as disguised or revealed, depending upon letters in array
        if char in guessed_letters:
            print (char, end='')
        elif char == ' ':
            print (' ', end='')
        else:
            print ('-', end='')
            win_state = False #makes win state false if there is a dash printed
        if char == letter_guess:
            correct_guess = True
    if correct_guess == False:
        num_guess = num_guess - 1
    if win_state == False:
    #prints out what happens when the user gets a letter wrong
        print('')
        print ("You have", num_guess,"wrong guesses left")
    else:
    #win state event
        print('')
        print('Correct word =', word_chosen)
        print("Congratulations, you have won!")
        print('If you would like to play again, type "Hangman/Taneja_Peram_Hangman.working.py" in the ipython session, or press the up arrow key.')
    
choose_word()
disguise()
while num_guess > 0 and win_state == False:
    #the player has to keep guessing while their guesses are more than one annd they haven't guessed the full word yet
    hangman()

if num_guess < 1:
    #if the number of guesses the player has is less than 1, they lose
    print('')
    print('Correct word is ', word_chosen)
    print("Unfortunately, you have lost!")
    print('If you would like to play again, type "Hangman/Taneja_Peram_Hangman.working.py" in the ipython session, or press the up arrow key.')

