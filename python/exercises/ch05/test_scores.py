#!/usr/bin/env python3
#===========================================================================
# Code Practice Lab 6 - Test Scores
# DEV 108 - 34634
# Mario Rodriguez
# February 14, 2025
#===========================================================================

# display a welcome message
print("The Test Scores application")
print()
print("Enter test scores")
print("Enter 'x' to end input")
print("======================")

# initialize variables
counter = 0
score_total = 0
# test_score = 0

while True:

    # request input from the user
    test_score = input("Enter test score (or 'x' to quit): ")

    # test to see if the input is the exit character for the program
    if test_score.lower() != "x":
        test_score = int(test_score) # if input is not exit character convert input to integer
    else:
        break
    if test_score >= 0 and test_score <= 100:
        score_total += test_score
        counter += 1
    else:
        print("Test score must be from 0 through 100. Score discarded. Try again.")   

# added this check to ensure that if the user exit the program at initiation the division by 0 is mitigated
if counter == 0:
    counter += 1

# calculate average score
average_score = round(score_total / counter)
                
# format and display the result
print("======================")
print(f"Total Score: {score_total}"
      f"\nAverage Score: {average_score}")
print()
print("Bye")