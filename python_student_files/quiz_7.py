# discount_rate = .1
# item = 89.95
# discount = item * discount_rate
# print("The discount on this item is $", round(discount, 2))

# def sales_tax(amt):
#     sale = amt + (amt * .06)
#     return sale

# def main(): 
#     print("Welcome to the 6% tax calculator!\n")
#     total = int(input("Please enter the total amount: "))
#     print("The total amount after tax is: ", sales_tax(total))

# fruit = ['apple', 'banana', 'grapes', 'mangos', 'oranges']
# fruit.insert(3, 'melon')

# print(fruit)

# fruit.remove('mangos')
# fruit.pop(3)
# print(fruit)


# def divide(numerator, denominator):
#     quotient = numerator / denominator
#     return quotient

# def main():
#     numerator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denominator: "))
#     quotient = divide(numerator, denominator)
#     print("The quotient is ", quotient) 

# if __name__ == "__main__":
#     main() 

# def main():

#     furry_pets = ["dog", "cat", "ferret", "hamster", "bunny"]
#     feathered_pets = ["canary", "parrot", "budgie", "hawk"]
#     all_pets = furry_pets + feathered_pets
#     new_pets =[]
#     i = 0
#     for item in all_pets:
#         if item[i][0] == "c":
#             new_pets.append(item)
#     print("The pet store sells:", all_pets)
#     print("These start with the letter c:", new_pets)

# main()

import csv
def main():
    courses = [["Python", 3],
               ["Trig", 3],
               ["Physics", 4],
               ["Yoga", 2]]
    with open("courses.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(courses)
    course_list = []
    with open("courses.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            course_list.append(row)
        print(course_list)
    for i in range(len(course_list) - 2):
        course = course_list[i]
        print(course[0] + " (" + str(course[1]) + ")")

    number = float(input("Enter a number: "))
    result1 = number * .15
    result2 = result1 / 3
    result3 = result1 + result2
    print(result1)
    print(result2)
    print(result3)

    

    num1 = format(1.23456789, ".5f")
    print(num1)



# main()

# car = "PORSCHE"
# color = "red"
# my_car = car.join(color)
# print(my_car)

# book_name = "a tale for the knight"
# book = book_name.title()
# print(book)

# name = "Mervin the Magician"
# words = name.split()
# print(words[0] + ", you are quite a " + words[2].lower())

# firstName = "Mickey"
# lastName = "Mouse"
# myName = firstName + lastName
# print(myName.lower())
