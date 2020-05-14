# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random

def name_to_number(name):
    # Switches string "name" to number for calculations
    if name == 'rock': 
        return 0
    elif name == 'Spock':
        return 1
    elif name ==     'paper': 
        return 2
    elif name ==     'lizard': 
        return 3
    elif name ==    'scissors': 
        return 4
    else: 
        print "User chose illegal play option!"
        quit()
    

def number_to_name(number):
    # Switches number back to related string "name" for terminal output
    if number == 0:
        return 'rock'
    elif number ==    1: 
        return 'Spock'
    elif number ==    2: 
        return 'paper'
    elif number ==    3: 
        return 'lizard'
    elif number ==    4: 
        return 'scissors'
        
    
def who_wins(pc, cc):    
    #determine and print who wins
    dc = (cc - pc) % 5
    #print pc, cc, dc
    return {
        0: "Player and computer tie!",
        1: "Computer wins!",
        2: "Computer wins!",
        3: "Player wins!",
        4: "Player wins!",
        }[dc]
    

def rpsls(player_choice): 
    # game which creates a random interaction based on five possible inputs
    # print a blank line to separate consecutive games
    print ' '

    # print out the message for the player's choice
    print "Player chooses " + player_choice
    
    # convert the player's choice to player_number using the function name_to_number()
    pc = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    cc = random.randrange(0,4)

    # convert comp_number to comp_choice using the function number_to_name()
    # print out the message for computer's choice
    print "Computer chooses " + number_to_name(cc)

    # compute difference of comp_number and player_number modulo five
    print who_wins(pc, cc)
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")




# always remember to check your completed program against the grading rubric


