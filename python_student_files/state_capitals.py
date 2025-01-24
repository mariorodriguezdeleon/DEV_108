#===========================================================================
# Code Practice lab 3 - Simple Quiz
# DEV 108
# US State Capitals Game
# Mario Rodriguez
# January 22, 2025

#===========================================================================
# TO DO
# Draft welcome message for the user with rules for the game
# Generate five random numbers from 1-50 to pick five random US States
# User response validation
# Keep playing loop until player quits
# Update print format of text
#===========================================================================
# import random

# Dictionary of US States and US State Capitals
usStateCapitals = { #fill out entire dictionary with all US states
    "Alabama":"Montgomery",
    "Alaska":"Juneau",
    "Arizona":"Phoenix",
    "Arkansas":"Little Rock",
    "California":"Sacramento",
    "Colorado":"Denver",
    "Connecticut": "hartford",
    "Delaware":"Dover",
    "Florida":"Tallahassee",
    "Georgia":"Atlanta",
    "Hawaii":"Honolulu",
    "Idaho":"Boise",
    "Illinois":"Springfield",
    "Indiana":"Indianapolis",
    "Iowa":"Des Moines",
    "Kansas":"Topeka",
    "Kentucky":"Frankfort",
    "Louisiana":"Baton Rouge",
    "Maine":"Augusta",
    "Maryland":"Annapolis",
    "Massachusetts":"Boston",
    "Michigan":"Lansing",
    "Minnesota":"Saint Paul",
    "Mississippi":"Jackson",
    "Missouri":"Jefferson City",
    "Montana":"Helena",
    "Nebraska":"Lincoln",
    "Nevada":"Carson City",
    "New Hampshire":"Concord",
    "New Jersey":"Trenton",
    "New Mexico":"Santa Fe",
    "New York":"Albany",
    "North Carolina":"Raleigh",
    "North Dakota":"Bismarck",
    "Ohio":"Columbus",
    "Oklahoma":"Oklahoma City",
    "Oregon":"Salem",
    "Pennsylvania":"Harrisburg",
    "Rhode Island":"Providence",
    "South Carolina":"Columbia",
    "South Dakota":"Pierre",
    "Tennessee":"Nashville",
    "Texas":"Austin",
    "Utah":"Salt Lake City",
    "Vermont":"Montpelier",
    "Virginia":"Richmond",
    "Washington":"Olympia",
    "West Virginia":"Charleston",
    "Wisconsin":"Madison",
    "Wyoming":"Cheyenne"
}

# holder lists for states and capitals -> to be updated by random generation once ramdom module is implemented
usStates = ["Washington", "Oregon", "California", "Nevada", "Arizona"] # test list to be replaced with random generated states
stateCapital = ["Olympia", "Salem", "Sacramento", "Carson City", "Phoenix"] #test list to be replaced with random generated states

#===== Welcome Message ======
def welcome_message():
    print(f'==========================================')
    print(f'         US State Capitals Game           ')
    print(f'==========================================')
    print(f'Would you like to test your knowledge of \nUS State Capitals?')
    play_game = (input(f'Please type "yes" or no to continue: '))

    return play_game
#===== Outro Message ========
def goodbye_message():
    print(f'See you next time. Goodbye! ')
#===== Game Engine ==========
def the_game():

    user_response = []  # collect user responses
    user_score = 0 # user score

    for i in range(len(usStates)):
        print(f"What is the capital of {usStates[i]}?\n")
        print(f"1. {stateCapital[0]}\n"
              f"2. {stateCapital[1]}\n"
              f"3. {stateCapital[2]}\n"
              f"4. {stateCapital[3]}\n"
              f"5. {stateCapital[4]}")

        print()
        user_response.insert(i, input("Enter your guess: "))
        print()

        if stateCapital[int(user_response[i])-1] == usStateCapitals.get(usStates[i]):
            user_score += 1
            print(f'That is correct!')
            print()
        else:
            print(f'Sorry, {stateCapital[int(user_response[i])]} is not the capital of {usStates[i]}')
            print()

    # Print user score and message to the user
    if user_score == 5:
        print(f'Your Total Score: {user_score}. You are a Rockstar!')
        print()
    elif user_score == 4:
        print(f'Your Total Score: {user_score}. Almost 100%!')
        print()
    elif user_score == 3 or user_score == 2:
        print(f'Your Total Score: {user_score}. Keep studying!')
        print()
    elif user_score <= 2:
        print(f'Your Total Score: {user_score}. Maybe this is not your area of interest!')
        print()

    # for i in user_response:  # print out user responses as test
        # print(i)
#===== Game Setup (TBD) =====
# def game_setup()
#===== Main =================
# def main():
#     start_game = welcome_message()
#     if start_game == "yes":
#         the_game()
#     else:
#         goodbye_message()

# if __name__ == "__main__":
#     main()





