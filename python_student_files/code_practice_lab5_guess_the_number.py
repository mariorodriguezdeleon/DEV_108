#!/usr/bin/env python3
#===========================================================================
# Code Practice Lab 5 - Guess the Number
# DEV 108 - 34634
# Mario Rodriguez
# February 9, 2025
#===========================================================================
import random

# global variables
LIMIT = 0
PLAYER_NAME = ''
GUESS_LIMIT = 0
PLAYER_WINS = 0
PLAYER_LOSSES = 0
GAME_DIFFICULTY_LEVEL = 1

# game banner
def display_title():
    print('==============================')
    print('      GUESS THE NUMBER!')
    print('==============================')
    print('          Welcome!')
# function to get user information for game setup
def get_user_input():

    global PLAYER_NAME
    global LIMIT
    global GUESS_LIMIT
    global GAME_DIFFICULTY_LEVEL

    print()
    PLAYER_NAME = input('What is your name? ')
    print()
    print(f'        Hello {PLAYER_NAME}')

    print()
    print('This game has three difficulty levels to choose from\n')
    print('     1. Easy - range between 1-10, limit 5 guesses\n'
          '     2. Medium - range between 1-100, limit 8 guesses\n'
          '     3. Difficult - range between 1-1000, limit 10 guesses\n')

    while True:
        game_mode = input(f'Please enter your selection: ')
        if  game_mode in ["1", "2", "3"]:
            break
        print('That is not a valid choice.\n')
        # game_mode = input('Please enter your selection again: ')

    GAME_DIFFICULTY_LEVEL = game_mode
    setup_game(GAME_DIFFICULTY_LEVEL)
# sets up the game
def setup_game(game_mode):

    global LIMIT
    global GUESS_LIMIT

    if game_mode == '3':
        LIMIT = 1000
        GUESS_LIMIT = 9
    elif game_mode == '2':
        LIMIT = 100
        GUESS_LIMIT = 7
    else:
        LIMIT = 10
        GUESS_LIMIT = 4
# main game driving function
def play_game():

    global GUESS_LIMIT
    global PLAYER_WINS
    global PLAYER_LOSSES

    number = random.randint(1, LIMIT)
    count = 1

    print(f"I'm thinking of a number from 1 to {LIMIT}\n")
    # add countdown to limit turns
    while (guess := int(input("Your guess: "))) != number and GUESS_LIMIT != 0:
        if guess < number:
            print("Too low.")
            count += 1
            GUESS_LIMIT -= 1
        elif guess > number:
            print("Too high.")
            count += 1
            GUESS_LIMIT -= 1

    # print(f"You guessed it in {count} tries.\n")

    # conditional logic to check if user lost of won the game
    if guess == number:
        print( 'You won!')
        print( f'You Guessed it in {count} tries.')
        PLAYER_WINS += 1
    else:
        print ('You loose')
        PLAYER_LOSSES += 1
# prints the score to the screen for the user
def print_stats():
    print('\n============ Your stats ============')
    print(f'       WINS:    {PLAYER_WINS}        ')
    print(f'       LOSSES:  {PLAYER_LOSSES}    ')
    print('====================================\n')
# entry of the program
def main():

    display_title()
    get_user_input() # ask player for their name and game difficulty
    again = "y"

    while again.lower() == "y":
        play_game()
        setup_game(GAME_DIFFICULTY_LEVEL)
        print_stats()

        again = input("Would you like to play again? (y/n): ")
        print()
    print('          Your Final Score')
    print_stats()

    print(f'It was great playing with you {PLAYER_NAME}. Bye!')

# if started as the main module, call the main function
if __name__ == "__main__":
    main()

