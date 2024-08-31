"""
@ Sehrish_Ilyas
Rock paper scissors
"""
import random
import simpleguitk

COMPUTER_SCORE = 0
HUMAN_SCORE = 0
human_choice = ""
computer_choice = ""

def choice_to_number(choice):
    
    return {'rock': 0, 'paper': 1, 'scissors': 2}[choice]

def number_to_choice(number):
    
    return {0: 'rock', 1: 'paper', 2:'scissors'}[number]

def random_computer_choice():
    
    return random.choice(('rock','paper','scissors'))

def choice_result(human_choice, computer_choice):
   
    global COMPUTER_SCORE
    global HUMAN_SCORE
    
    human_number = choice_to_number(human_choice)
    comp_number = choice_to_number(computer_choice)
    
    if human_number == comp_number:
        print('Tie')
        
    elif (human_number - comp_number)% 3 == 1:
        COMPUTER_SCORE = COMPUTER_SCORE + 1
        print('Computer Wins!')
       
    else:
        HUMAN_SCORE = HUMAN_SCORE + 1
        print('Human Wins!')

# Handler for mouse click on rock button.
def rock():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = 'rock'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)
    
# Handler for mouse click on paper button.
def paper():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = 'paper'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)
    
# Handler for mouse click on Scissors button.
def scissors():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = 'scissors'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)

def endgame():
    global HUMAN_SCORE, COMPUTER_SCORE
    if HUMAN_SCORE == COMPUTER_SCORE:
        return("Tie")
    elif HUMAN_SCORE > COMPUTER_SCORE:
        return("Human Won!")
    else:
        return("Computer Won!")
        
# Handler to draw on canvas
def draw(canvas):    
    try:
        # Draw choices
        canvas.draw_text("Human: " + human_choice, [15,50], 35, "Blue")
        canvas.draw_text("Computer: " + computer_choice, [15,100], 35, "White")
        
        # Draw scores
        canvas.draw_text("Human Score: " + str(HUMAN_SCORE), [15,170], 35, "Blue")
        canvas.draw_text("Computer Score: " + str(COMPUTER_SCORE), [15,220], 35, "White")
        
        canvas.draw_text("Result: "+ endgame(), [15, 300], 35, "Blue")
    except TypeError:
        pass
    
# Create a frame and assign callbacks to event handlers
def play_rps():
    frame = simpleguitk.create_frame("Rock-Paper-Scissors", 575, 450)
    frame.add_button("Rock", rock, 80)
    frame.add_button("Paper", paper, 80)
    frame.add_button("Scissors", scissors, 80)
    frame.set_draw_handler(draw)
    frame.start()
 
play_rps()
