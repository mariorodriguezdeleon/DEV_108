#!/usr/bin/env python3
#===========================================================================
# DEV 108 - 34634
# Mario Rodriguez
# March 24, 2025
# 
# Final Project - Human Mission to Mars Account Management System
#
# This program is used to create user accounts for a fictitional organization - 
# SNASA - Secrete National Aeronautics and Sapce Administration. 
# This program showcases my ability to use what I've learned during my time in
# DEV 108. 
# 
# This program leverages functions, persistent storage and many other skills
# learned in this class.
#
# TODO: 
#   [X] Create a function to 'add' new users
#   [X] Create a function to 'list' all users
#   [X] Create a function to 'search' for user by last name
#   [X] Create a function to 'search living pod'. List assigned and available slots
#   [X] Create a function for administrator to list account information
#   [X] Create a function to 'delete' user accounts
#   [X] Create a function to generate random password
#   [X] Create a function to generate user id's
#   [] Create a function to generate living pod room for user
#===========================================================================

import csv
import sys
import string
import random

FILENAME = 'accounts_file.csv'

# sample users to test the program
sample_users = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]

# closes the program when called by another function if and error occurs within the calling function
# function status: Working
def exit_program():

    print("Terminating program.")
    sys.exit()

# reads the csv file of accounts and returns a list to main() for processing.
# Calls exit_program() to handle some exceptions, including FileNotFoundError.
# function status: Working
def read_accounts():

    try:
        accounts = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                accounts.append(row)
        return accounts
    except FileNotFoundError as e:
        print(f"Could not find {FILENAME} file.")
        print('Please ensure that the file exists and the file path is correct.')
        exit_program()
        return accounts
    except Exception as e:
        print(type(e), e)
        exit_program()

# writer function to record user account data to persistent storage. generates a csv file
# Calls exit_program() to handle some exceptions
# function status: Working
def write_accounts(accounts_list):

    try:
        with open(FILENAME, "w", newline="") as file:
##            raise BlockingIOError("Error raised for testing.")
            writer = csv.writer(file)
            writer.writerows(accounts_list)
    except OSError as e:
        print(type(e), e)
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()

# lists human inhabitants' information: First Name, Last Name, Age, Email, Living POD #
# function status: Working
def list_accounts(accounts_list):

    headers = ['Record #', 'First Name', 'Last Name', 'Age', 'Email', 'POD #']
    print('==========================================================================================================================')
    for col in headers:
        if col == 'POD #':
            print(col.rjust(20), end="")
        else:
            print(col.ljust(20), end="")
    print('\n==========================================================================================================================')
    for row_index, row in enumerate(accounts_list, start=1):
        print(str(row_index).ljust(20), end="")
        for col_index, value in enumerate(row, start=1 ):
            if col_index == 4 or col_index == 6:
                continue
            if col_index == 5:
                print(str(value).ljust(30), end="")
                continue
            if col_index == 7:
                print(str(value).rjust(10), end="")
            else:
                print(str(value).ljust(20), end="")
        print()
    print('==========================================================================================================================')

# displays an administrator view of all user account information. Password protected
# function status: Working
def admin_report(accounts_list):

    max_tries = 5
    AdminPassword = "DEV108ISTHEBEST"

    for i in range(max_tries):
        admin_password = input('Please Enter Admin Password: ')
        if admin_password == AdminPassword:
            headers = ['ID #', 'First Name', 'Last Name', 'Email', 'Password']
            print('==========================================================================================================================')
            for col in headers:
                if col == 'Password':
                    print(col.rjust(30), end="")
                else:
                    print(col.ljust(20), end="")
            print('\n==========================================================================================================================')

            for row_index, row in enumerate(accounts_list, start=1):
                # print(str(row_index).ljust(20), end="")
                # for col_index, value in enumerate(row, start=1 ):
                print(str(row[3]).ljust(18), row[0].ljust(20), row[1].ljust(20), row[4].ljust(40), row[5].ljust(20))
            print('==========================================================================================================================')
            break
        print("Please Try Again")
    else:
        print('Password is Incorrect. Too many attempts')
        print()
         
# add a new user record to the accounts list
# function status: incomplete
# [] System generated POD not set
def add_account(accounts_list):

    print('This is the add function')
    first_name = input('Please enter first name: ')
    last_name = input('Please enter last name: ')

    # test for 
    while True:
        try:
            user_age = int(input('Enter user age: '))
        except ValueError:
            print("Invalid integer. Please try again.")
            continue
        if user_age < 0:
            print("User's age must be grater than 0.")
        else:
            break

    user_id = id_gen(accounts_list) # to be replaced by a random generated id
    emai_address = first_name.lower().strip() + '.' + last_name.lower().strip() + str(user_id) + '@hmm.com'
    user_passwrd = password_gen() # random system generated password
    pod_number = 'A-100' #need to replace by system generated placement

    user = [first_name, last_name, user_age, user_id, emai_address, user_passwrd, pod_number]
    print('appending to list...')
    accounts_list.append(user)
    write_accounts(accounts_list)

# deletes user account by record id
# fucntion status: Working
def delete_account(accounts_list):

    print('Delete Account Function')
    while True:
        try:
            number = int(input("Enter the Record Number: "))
        except ValueError:
            print("Invalid integer. Please try again.")
            continue
        if number < 1 or number > len(accounts_list):
            print("There is no movie with that number. Please try again.")
        else:
            break
    account = accounts_list.pop(number - 1)
    write_accounts(accounts_list)
    print(f"Account for {account[0]} was deleted.\n")

# searches the accounts list for individuals assigned to the specified pod. Returns the names and user id.
# This function provides the total assigned slots and available slot counts
# fucntion status: Working
def search_by_pod_number(accounts_list):
    print('This is the search_pod function')

    count = 0
    slots = 6
    available = 0

    pod_name = input("Enter The POD: ")
    print('===========================================')
    for i, account in enumerate(accounts_list, start=1):
        # print(account)
        if account[6] == pod_name:
            count += 1
            print(account[1].ljust(10), account[0].ljust(10), 'ID #:'.center(10), account[3].ljust(10))
    if count == 0:
            print(f'No Records Found for Pod: {pod_name}')
    else:
        available = slots-count
    print()
    print(f'Pod {pod_name} has {count} slot(s) assigned and {available} slots available.')    
    print('===========================================')
    print()

# serach by last name function which lists records that match the search criteria. Lists 'Last name', 'First Name', 'POD #' of 
# all matching records in the data file
# fucntion status: working
def search_by_last_name(accounts_list):
    print('\nSearch function by Last Name')

    count = 0 # used to test for no records found. If counter remains at 0 a message is displayed to the user 'No records found'

    last_name = input("Enter Last Name: ")
    print('===========================================')
    for i, account in enumerate(accounts_list, start=1):
        # print(account)
        if account[1] == last_name:
            count += 1
            print(account[1].ljust(10), account[0].ljust(10), 'POD #:'.center(10), account[6].ljust(10))
    if count == 0:
            print('No Records Found')
    print('===========================================')
    print()

# generates a randome password that is 8 characters long and includes special characters, upper and lower case letters, and nubers
# function is called by add_account()
# fucntion status: Working
def password_gen():
    print('This is the passowrd generation function')

    password_length = 8 # sets the length for the password

    # assigns characters returned by the modules to lists
    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.punctuation)

    # shuffles the lists to create randomness
    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)

    # calculates %s of number of characters for each part of the password 
    pass1 = round(password_length * (20/100))
    pass2 = round(password_length * (30/100))

    result = [] # list to collect each character that is generated
    for x in range (pass1):
        result.append(s1[x])
        result.append(s2[x])

    for x in range (pass2):
        result.append(s3[x])
        result.append(s4[x])

    random.shuffle(result) # final shuffle of collected characters

    password = "".join(result) # joins the two halfs to create a whole password

    return password

# generates a random integer between 1000-9999 for the user_id. Validates that no duplicates are generated
# function is called by add_account()
# fucntion status: Working
def id_gen(accounts_list):

    user_id = 0
    while True:
        #generate random number from 1000 to 9999
        random_integer = random.randint(1000, 9999)
        print(random_integer)
        for account in accounts_list:
            if random_integer in account:
                random_integer = random.randint(1000, 9999)
        else:
            user_id = random_integer
            break

    return user_id

def pod_assignment():
    print

# dysplays the program menu of commands for the user
# fucntion status: Working.
def display_menu():

    print()
    print("The Mars Mission Personnel Program")
    print()
    print("        COMMAND MENU")
    print("list - List All Available Records")
    print("add - Add Account")
    print("del - Delete Record")
    print("find - Search Record by Last Name")
    print("pod - Search by POD #")
    print("admin - Prints User Account Information")
    print("exit - Exit program")
    print()   

def main():
    
    display_menu()
    accounts_list = read_accounts()
    while True:
        print('Enter "m" to view commands')        
        command = input("Command: ")
        if command.lower() == "list":
            list_accounts(accounts_list)
        elif command.lower() == "add":
            add_account(accounts_list)
        elif command.lower() == "del":
            delete_account(accounts_list)
        elif command.lower() == "find":
            search_by_last_name(accounts_list)
        elif command.lower() == "pod":
            search_by_pod_number(accounts_list)
        elif command.lower() == "admin":
            admin_report(accounts_list)
        elif command.lower() == "m":
            display_menu()
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
