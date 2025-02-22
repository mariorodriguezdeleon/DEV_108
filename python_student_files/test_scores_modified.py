#!/usr/bin/env python3
#===========================================================================
# Code Practice Lab 7 - Test Scores Enhanced
# Leverage a Python List data structure, and functions
# DEV 108 - 34634
# Mario Rodriguez
# February 22, 2025
#===========================================================================

# display a welcome message
print("The Test Scores program\n")
print("Enter test scores")
print("Enter 'end' to end input")
print("===============================")

def get_scores(test_scores):
    while True:

        score_input = input("Enter test score: ")

        # Check if input is "end"
        if score_input.lower() == "x":
            break

        # Convert input to integer for processing
        # ---- Your code here ----------
        else:
            score = int(score_input)

        # Validate the input score
        if 0 <= score <= 100:
            # ---- Your code here ----------
            test_scores.append(score)
        else:
            # ---- Your code here ----------
            print(f'Test Score must be from 0 through 100. Try again.')

def process_scores(test_scores):
    
    print(test_scores)

    # sum all scores

    # print total number of scores (list len)

    # print AVerage Score

    # print low score

    # print high score

    # print median score (not average but score in the middle)

def main():

    while True:

        test_scores = []
        get_scores(test_scores)

        # process_scores(test_scores)
        print (test_scores)

        another_set = input("Enter another set of test scores (y/n)? ")
        if another_set.lower() != "y":
            break
        else:
            print("\nEnter test scores")
            print("Enter 'x' to end input")
            print("===============================")

if __name__ == '__main__':
    main()