#!/usr/bin/env python3
#===========================================================================
# Code Practice Lab 7 - Test Scores Enhanced
# Leverage a Python List data structure, and functions
# DEV 108 - 34634
# Mario Rodriguez
# February 22, 2025
# TODO
# - Modify program to leverage a list data structure
# - Implement two new functions 'get_scores' and 'process_scores
#       - 'get_scores' prompts user to input scores and store in list
#       - 'process_scores' prints 
#           - 'Total', 'Number of scores', 'Average', 'Low', 'High', and 'Median' scores
#===========================================================================

# display a welcome message
def welcome_message():
    print("The Test Scores program\n")
    print("Enter test scores")
    print("Enter 'x' to end input")
    print("===============================")

# prompts user for scores and stores scores in a list
def get_scores(test_scores):

    while True:

        score_input = input("Enter test score: ")

        # Check if input is "end"
        if score_input.lower() == "x":
            break

        # Convert input to integer for processing
        else:
            score = int(score_input)

        # Validate the input score
        if 0 <= score <= 100:
            test_scores.append(score)
        else:
            print(f'Test Score must be from 0 through 100. Try again.')

# processes the list of scores to provide information related to the list
def process_scores(test_scores):
    
    print()
    print(test_scores)
    print()

    # sum all scores
    sum_of_scores = sum([n for n in test_scores])
    print(f'Total:              {sum_of_scores}')

    # print total number of scores (list len)
    print(f'Number of scores:   {len(test_scores)}')

    # print Average Score
    average_score = sum(([n for n in test_scores])) / len(test_scores)
    print(f'Average Score:      {average_score}')

    # print low score
    min_score = min(test_scores)
    print(f'Low Score:          {min_score}')

    # print high score
    max_score = max(test_scores)
    print(f'High Score:         {max_score}')

    # print median score (not average but score in the middle)
    test_scores.sort()
    median_score = test_scores[len(test_scores) % 2]
    print(f'Median Score:       {median_score}')

# main program processing
def main():

    welcome_message()

    while True:

        test_scores = []
        get_scores(test_scores)
        process_scores(test_scores)

        another_set = input("\nEnter another set of test scores (y/n)? ")
        if another_set.lower() != "y":
            break
        else:
            print("\nEnter test scores")
            print("Enter 'x' to end input")
            print("===============================")

if __name__ == '__main__':
    main()