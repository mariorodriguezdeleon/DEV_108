# In-Class Assignment - Leap Year Checker and Age Group Identifier
# January 22, 2025

#Leap year Checker====================================================
year = int(input("Enter a year: "))

if year % 4 == 0 or year % 400 == 0:
    print(f'{year} is a leap year.')
else:
    print(f'{year} is not a leap year.')

#Age Group Identifier=================================================
birthYear = int(input("Enter your birth year: "))
userAge = 2025 - birthYear

print(f"Your age is {userAge}.")

if userAge >= 65:
    print("You are a Senior")
elif userAge >= 20:
    print("You are an Adult")
elif userAge >= 13:
    print("You are a Teenager")
elif userAge >= 0:
    print("You are a Child")

