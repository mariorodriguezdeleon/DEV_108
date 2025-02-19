#!/usr/bin/env python3
#===========================================================================
# Code Practice Lab 4 - Test Scores Enhanced
# DEV 108 - 34634
# Mario Rodriguez
# January 27, 2025
#===========================================================================

# display a welcome message
print("The Test Scores program\n")
print("Enter test scores")
print("Enter 'end' to end input")
print("===============================")

# Outer loop to manage multiple sets of scores
while True:

    total_score = 0
    count = 0
    test_scores = []

    # Inner loop to input scores for a single set
    while True:
        score_input = input("Enter test score: ")

        # Check if input is "end"
        if score_input.lower() == "end":
            break

        # Convert input to integer for processing
        # ---- Your code here ----------
        else:
            score = int(score_input)

        # Validate the input score
        if 0 <= score <= 100:
            # ---- Your code here ----------
            test_scores.append(score)
            total_score += score
            count += 1
        else:
            # ---- Your code here ----------
            print(f'Test Score must be from 0 through 100. Try again.')

    # Calculate the average score
    # ---- Your code here ----------
    average_score = int(total_score/count)

    print('===============================')
    print(f'Total Score: {total_score}')
    print(f'Average Score: {average_score}')
    print(test_scores)
    print()

    # Ask the user if they want to enter another set of scores
    another_set = input("Enter another set of test scores (y/n)? ")
    if another_set.lower() != "y":
        break
    else:
        print("\nEnter test scores")
        print("Enter 'end' to end input")
        print("===============================")


def get_scores():
    print('get_scores')

def process_scores():
    print('process_scores')

def main():
    print('main()')
    get_scores()
    process_scores()

if __name__ == '__main__':
    main()