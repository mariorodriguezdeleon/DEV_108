# DEV 108 Lab Activity 1
# January 8, 2025
# Mario Rodriguez

# variables
firstName = "Zaphod"
lastName = "Beeblebrox"
num1 = 23
num2 = 2023
myNum1 = 18
myNum2 = 24

# Print 'Hello World'
print("Hello World!")

# Add two numbers together and print the math equation
print(str(myNum1) + " + " + str(myNum2) + " = " + str(myNum2+myNum1))

# Print output message leveraging variables firstName and lastName
print("My name is " + firstName + " " + lastName + ".")

# Print num1 and num2
print(str(num1))
print(str(num2))
print(f'{num1} + {num2} = ' + str(num2+num1))
print()

# Ask for user input
userName = input("What is your name? ")

while userName == "":
    print("You did not tell me your name: ")
    userName = input("Please enter your name: ")
print()
print(f'Hello {userName}! It\'s nice to meet you.')
