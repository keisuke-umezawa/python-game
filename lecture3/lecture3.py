# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randrange(0, 100)

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    secret_number = random.randrange(0, 100)

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    secret_number = random.randrange(0, 1000)
    
def input_guess(guess):
    # main game logic goes here	
    guess_number = int(guess)
    print "Guess was", guess_number
    
    if guess_number > secret_number:
        print "Lower"
    elif guess_number < secret_number:
        print "Higher"
    else:
        print "Correct"

    
# create frame
frame = simplegui.create_frame("Guess Number", 80, 100)



# register event handlers for control elements and start frame
frame.add_input("What is your guess number?", input_guess, 200)
frame.add_button("Range is [0,100)", range100)
frame.add_button("Range is [0,1000)", range1000)
# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
