# lab 3 project

import random

# TO DO
# Draft welcome message for the user with rules for the game
# Generate five random numbers from 1-50 to pick five random US States


usStateCapitals = {
    "washington":"olympia", } #fill out entire dictionary with all US states

usStates = ["washington", "oregon", "california", "nevada", "arizona"] # test list to be replaced with random generated states

userResponses = [] # collect user responses

#===== Welcome Message =====
print("Welcome to the game")
print(usStateCapitals.get(usStates[0]))

# getUserResponse = int(input("Enter a number: "))

for i in range(len(usStates)):
    print(f"What is the capital of {usStates[i]}?")
    userResponses.insert(i, input("Enter your response: "))

for i in userResponses:
    print(i)


