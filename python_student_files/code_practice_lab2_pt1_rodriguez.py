# DEV 108 Code Practice Lab 2, pt1
# January 13, 2025
# Mario Rodriguez

# display a welcome message
print("The Test Scores program")
print()
print("Enter 3 test scores")
print("======================")

# initialize variables

# get scores from the user
score1 = int(input("Enter test score: "))
score2 = int(input("Enter test score: "))
score3 = int(input("Enter test score: "))

# calculate total and average scores
total_score = score1+score2+score3
average_score = round(total_score / 3)

# format and display the result
print("======================")
print(f"Your Scores {score1} {score2} {score3}")
print("Total Score:  ", total_score,
      "\nAverage Score:", average_score)
print()
print("Bye!")
