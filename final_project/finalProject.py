#!/usr/bin/env python3
#===========================================================================
# Final Project - Human Mission to Mars Account Setup
# A concept program to create an application for user account creation for a 
# fictitional organization. This program showcases the ability to use funtions
# and CSV files to create and store the user data
# DEV 108 - 34634
# Mario Rodriguez
# February 22, 2025
#
# TODO: 
#   [X] Create a function to 'add' new users
#   [X] Create a function to 'list' all users
#   [X] Create a function to 'search' for user by last name
#   [] Create a function to 'search living pod'
#   [X] Create a function to 'delete' users
#   [] Create a function to generate random password
#   [] Create a function for administrator
#===========================================================================

import csv
import sys

FILENAME = 'accounts_file.csv'

# closes the program when called by another function if and error occurs within the calling function
# fucntion status: Working
def exit_program():
    print("Terminating program.")
    sys.exit()

# reads the file of accounts and returns a list to main for processing
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
        exit_program()
        return accounts
    except Exception as e:
        print(type(e), e)
        exit_program()

# writer function to record user account data to persistent storage. generates a csv file
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

# lists user account information: First Name, Last Name, Age, Email, Living POD #
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

# displays an administrator view of all account information for all human users. Password protected
# function status: Working
def admin_report(accounts_list):

    counter = 5
    AdminPassword = "DEV108ISTHEBEST"

    while True:
        # counter -= 1
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
                print(row[3].ljust(18), row[0].ljust(20), row[1].ljust(20), row[4].ljust(40), row[5].ljust(20))
            print('==========================================================================================================================')
            break
        else:
            print('Password is Incorrect')
            break
            

# add a new user record to the accounts list
# function status: incomplete
# [] Password generator not set
# [] System generated POD not set
def add_account(accounts_list):

    print('This is the add function')
    first_name = input('Please enter first name: ')
    last_name = input('Please enter last name: ')
    user_age = input('Enter user age: ')
    user_id = 1234 # to be replaced by a random generated id
    emai_address = first_name.lower().strip() + '.' + last_name.lower().strip() + str(user_id) + '@hmm.com'
    user_passwrd = 'password123' # to be replaced by a random generated id
    pod_number = 'A-100' #need to replace by random generated placement

    user = [first_name, last_name, user_age, user_id, emai_address, user_passwrd, pod_number]
    print('appending to list...')
    accounts_list.append(user)
    write_accounts(accounts_list)

# fucntion status: not started
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
    print(f"{account[0]} was deleted.\n")

# fucntion status: not started
def search_by_pod_number(accounts_list):
    print('This is the search_pod function')

# serach by last name function which lists records that match the search criteria. Lists 'Last name', 'First Name', 'POD #'
# fucntion status: working
def search_by_las_name(accounts_list):
    print('\nSearch function by Last Name')

    last_name = input("Enter Last Name: ")
    print('===========================================')
    for i, account in enumerate(accounts_list, start=1):
        # print(account)
        if account[1] == last_name:
            print(account[1].ljust(10), account[0].ljust(10), 'POD #:'.center(10), account[6].ljust(10))
        else:
            print('No record found')
    print('===========================================')
    print()

# fucntion status: not started
def password_gen():
    print('This is the passowrd generation function')

# fucntion status: not started
def id_gen():
    print('This is the id generation funtion')

# fucntion status: working.
# function needs additional formatting
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
        command = input("Command: ")
        if command.lower() == "list":
            list_accounts(accounts_list)
        elif command.lower() == "add":
            add_account(accounts_list)
        elif command.lower() == "del":
            delete_account(accounts_list)
        elif command.lower() == "find":
            search_by_las_name(accounts_list)
        elif command.lower() == "pod":
            search_by_pod_number(accounts_list)
        elif command.lower() == "admin":
            admin_report(accounts_list)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
