# main.py
#===========================================================================
# Code Practice Lab 4 - Test Scores Enhanced
# DEV 108 - 34634
# Mario Rodriguez
# February 15, 2025
#===========================================================================

import nameformat

def main():
    print("The NameFormat module\n")
    print("Hello!\n")

    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")

    while True:
        print("\n* * MENU * * \n")
        print("1 - Say Hello")
        print("2 - Output Full Name")
        print("3 - Output Last Name, First Name")
        print("4 - Read Documentation")
        print("5 - Exit")

        choice = input("\nWhat is your choice? ")

        if choice == "1":
            print(nameformat.sayHello(first_name))
        elif choice == "2":
            print(nameformat.fullName(first_name, last_name))
        elif choice == "3":
            print(nameformat.lastNameFirst(first_name, last_name))
        elif choice == "4":
            # Printing the docstrings for each function in the module
            print("\nDocumentation:\n")
            help(nameformat.sayHello)
            help(nameformat.fullName)
            help(nameformat.lastNameFirst)
        elif choice == "5":
            print("\nGoodbye!\n")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.\n")

if __name__ == "__main__":
    main()
