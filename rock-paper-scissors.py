import random
from enum import IntEnum

#Defins the classes and names for the game.
class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4

#Establish the winning-losing relations between classes.
victories = {
        Action.Scissors: [Action.Lizard, Action.Paper],
        Action.Paper: [Action.Spock, Action.Rock],
        Action.Rock: [Action.Lizard, Action.Scissors],
        Action.Lizard: [Action.Spock, Action.Paper],
        Action.Spock: [Action.Scissors, Action.Rock]
    }

#Get the user selection.     
def get_user_selection():
    choices = [f'{action.name}[{action.value}]' for action in Action]
    choices_str = ', '.join(choices)
    selection = int(input(f'Enter a choice ({choices_str}): '))
    action = Action(selection)
    return action

#Chose the computer selection at random.
def get_computer_selection():
        selection = random.randint(0, len(Action) - 1)
        action = Action(selection)
        return action    

#Determine the winner and loser of the game.
def determine_winner(user_action, computer_action):
    defeats = victories[user_action]
    if user_action == computer_action:
        print(f'Both players selected {user_action.name}. It\'s a tie')
    elif computer_action in defeats:
        print(f'{user_action.name} beats {computer_action.name}. You win! :D')
    else:
        print(f'{computer_action.name} beats {user_action.name}. You lose :(')

#Create the loop to repeat the game.
while True:
    try:
        user_action = get_user_selection()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    computer_action = get_computer_selection()
    determine_winner(user_action, computer_action)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
