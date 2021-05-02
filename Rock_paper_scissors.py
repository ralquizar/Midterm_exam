import random

CHOICES = 'rps'

#player_choice


#computer_choice
#Need help in computer function

def get_computer_choice():

    computer_choice = random.randint(0, 2)
    computer_choice = CHOICES[computer_choice]
    return computer_choice

#game_mechanics