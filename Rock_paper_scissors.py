import random

CHOICES = 'rps'

#player_choice


#computer_choice


#game_mechanics

def is_draw(player_choice, computer_choice):
    
    if player_choice == computer_choice:
        return True


def print_winner(player_choice, computer_choice):
   
    if player_choice == 'r' and computer_choice == 's':
        print('Player wins!')
    elif player_choice == 's' and computer_choice == 'p':
        print('Player wins!')
    elif player_choice == 'p' and computer_choice == 'r':
        print('Player wins!')
    else:
        print('Computer wins!')
        print('%s beats %s' % (computer_choice, player_choice))

def play_game():
    
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    if is_draw(player_choice, computer_choice):
        print("It's a draw, both players picked %s: " % player_choice)
    else:
        print("Computer picked: %s" % computer_choice)
        print("Player picked: %s" % player_choice)
        print_winner(player_choice, computer_choice)


if __name__ == "__main__":
    play_game()