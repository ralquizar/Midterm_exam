import random

CHOICES = 'rps'

#player_choice

def get_player_choice():

    player_choice = None
    while player_choice is None:
        player_choice = input('Choices: \n(R)ock \n(P)aper \n(S)cissors \n\nPick: ')
        if player_choice.lower() not in CHOICES:
            player_choice = None
    return player_choice.lower()
    
#computer_choice


#game_mechanics