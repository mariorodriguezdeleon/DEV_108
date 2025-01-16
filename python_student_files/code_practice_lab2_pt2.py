# DEV 108 Code Practice Lab 2, pt2
# January 13, 2025
# Mario Rodriguez

# display a welcome message
print("The Area and Perimeter Program")
print()
print("Please Enter The Numbers")
print("======================")

# get length and width from the user
length = int(input("Please enter the length: "))
width = int(input("Please enter the width: "))

# calculate total and average scores
totalArea = length*width
perimeter = (length*2) + (width*2)

# format and display the result
print("======================")
print(f"Area: {totalArea}")
print(f"Perimeter: {perimeter}")
print()
print("Thanks for using this program!")
