import random

#Defines the condition to allow continous playing.
while True:
#Ask the user to make a selection
    user_action = input('Enter a choice (rock, paper, scissors): ')

    #Establish the computer's options. Select one at random.
    possible_actions = ['rock', 'paper', 'scissors']
    computer_action = random.choice(possible_actions)

    #Print the choices of both players.
    print(f'\nYou chose {user_action}, computer chose {computer_action}.\n')

    #Establish the rules of the game. Determine winner and loser.
    if user_action == computer_action:
        print(f'Both players selected {user_action}. It\'s a tie!')
    elif user_action == 'rock':
        if computer_action == 'scissors':
            print('Rock smashes scissors. You win! :D')
        else:
            print('Paper covers rock. You lose :(')
    elif user_action == 'paper':
        if computer_action == 'rock':
            print('Paper covers rock. You win! :D')
        else:
            print('Scissors cut paper. You lose :(')
    elif user_action == 'scissors':
        if computer_action == 'paper':
            print('Scissors cut paper. You win! :D')
        else:
            print('Rock smashes scissors. You lose :(')

    play_again = input('\nPlay again? (y/n): \n')
    if play_again.lower() != 'y':
        break