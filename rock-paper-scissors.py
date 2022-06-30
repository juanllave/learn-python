import random
from enum import IntEnum

#Defines the condition to allow continous playing.
#while True:
#Ask the user to maKe a selection after defining the possible actions.
class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
        
def get_user_selection():
    choices = [f'{action.name}[{action.value}]' for action in Action]
    choices_str = ', '.join(choices)
    selection = int(input(f'Enter a choice ({choices_str}): '))
    action = Action(selection)
    return action

#Establish the computer's options. Select one at random.
def get_computer_selection():
        selection = random.randint(0, len(Action) - 1)
        action = Action(selection)
        return action    

#Print the choices of both players.
def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f'Both players selected {user_action.name}. It\'s a tie')
    elif user_action == Action.Rock:
        if computer_action == Action.Scissors:
            print('Rock smashes scissors. You win! :D')
        else:
            print('Paper covers rock. You lose :(')
    elif user_action == Action.Paper:
        if computer_action == Action.Rock:
            print('Paper covers rock. You win! :D')
        else:
            print('Scissors cut paper. You lose :(')
    elif user_action == Action.Scissors:
        if computer_action == Action.Paper:
            print('Scissors cut paper. You win! :D')
        else:
            print('Rock smashes scissors. You lose :(')

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
