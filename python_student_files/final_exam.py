
# Question 1
# print("Hello!")

# user_name = input('What is your name? ')

# #test for valid age input
# while True:
#     try:
#         user_age =int(input(f'How old are you {user_name}? '))
#         break
#     except ValueError:
#         print('Age value is not numberic. Please enter a number for age.')
#         continue

# for i in range(user_age):
#     print(f'Hello {user_name}!')


# Question 2
# while True:
#     user_input = input("Please enter a string that is over 12 characters: ")
#     if len(user_input) > 12:
#       print(f'Thank you. You entered a word or phrase with {len(user_input)} characters.')
#       break
#     else:
#       print('Enter a word or phrase over 10 characters: Hello\n'
#       'Please enter a word or phrase over 10 characters! Try again.')

# Question 3
# def find_max(num1, num2, num3):
#     return max(num1, num2, num3)

# def main():
    
#     print('Please enter 3 numbers')

#     num1 = float(input('Enter the first number: '))
#     num2 = float(input('Enter the second number: '))
#     num3 = float(input('Enter the third number: '))

#     max_number = find_max(num1, num2, num3)

#     print(f'The largest number is: {max_number}')

# main()

#Question 4
# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end="")
#     print()

#Question 5
# def even_or_odd(myNum):
#     if myNum/2 == 0:
#         return 'even'
#     else:
#         return 'odd'
    
# myNum = int(input('Please enter an integer: '))
# even_odd = even_or_odd(myNum)

# print(f'{myNum} is {even_odd}.')

#Question 6
# x = 19
# x += 10
# print(x)

#Q 7
# x = 6
# y = 12
# z = x + x
# print(z)

# width = 150
# height = 30.0
# print(height/3)

# 

# n = 0
# while True:
#     if n == 3:
#         break
#     print(n)
#     n = n + 1

# for n in "banana":
#     print(n)

# print(3 * '7')

# try:
#    print(1)
#    print(20 / 0)
#    print(2)
# except ZeroDivisionError:
#    print(3)
# finally:
#    print(4)

# for i in range(10):
#    if not i % 2 == 0:
#       print(i+1)

# list = [1, 1, 2, 3, 5, 8, 13]
# print(list[list[4]])

# letters = ['x', 'y', 'z']
# letters.insert(1, 'w')
# print(letters[2])

# fruit = "banana"
# x = fruit[1]

# print(x)

# def print_numbers():
#     print(2)
#     print(3)
#     return
#     print(5)
#     print(10)

# print_numbers()

# def add(a, b):
#     return a+5, b+5

# result = add(3, 2)
# print(result)

# str = "python rocks"

# print (str[1:3])


# valueOne = 5 ** 3
# valueTwo = 5 ** 2

# print(valueOne)
# print(valueTwo)

# def person_age(name, age=20):
#     print(name, age)

# person_age('Emma', 25)

# str1 = "My salary is 4000";
# str2 = "4000"

# print(str1.isdigit())
# print(str2.isdigit())

str = "my name is James bond";
print (str.capitalize())

my_list = ["Hello", "World"]
print("-".join(my_list))

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)