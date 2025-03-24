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
#   - Create a function to 'add' new users
#   - Create a function to 'list' all users
#   - Create a function to 'search' for users
#   - Create a function to 'search living pod'
#   - Create a function to 'delete' users
#   - Create a function to 'add' new users
#===========================================================================

import csv
import sys

FILENAME = 'accounts_file.csv'

# closes the program if and error occurs
# fucntion status: working
def exit_program():
    print("Terminating program.")
    sys.exit()

# reads the file of accounts and returns a list to main
# function status: working
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

# function status: Working
def write_accounts(accounts_list):
    # print(accounts_list)
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

# function status: incomplete - still needs print formatting
def list_accounts(accounts_lists):
    print('This is the list function')
    for i, accounts_lists in enumerate(accounts_lists, start=1):
        print(f"{i}. {accounts_lists[0]} ({accounts_lists[1]})")
    print()

#function status: incomplete, working
def add_account(accounts_list):

    print('This is the add function')
    first_name = input('Please enter first name: ')
    last_name = input('Please enter last name: ')
    user_age = input('Enter user age: ')
    user_id = 1234 # to be replaced by a random generated id
    emai_address = first_name + '.' + last_name + user_id+'@hmm.com'
    user_passwrd = 'password123' # to be replaced by a random generated id
    pod_number = 'A-100' #need to replace by random generated placement

    user = [first_name, last_name, user_age, user_id, emai_address, user_passwrd, pod_number]
    print('appending to list...')
    accounts_list.append(user)
    write_accounts(accounts_list)

# fucntion status: not started
def delete_account(accounts_list):
    print('Delete Account Function')

# fucntion status: not started
def search_by_pod(accounts_list):
    print('This is the search_pod function')

# fucntion status: not started
def search_by_name(accounts_list):
    print('This is the search function')

# fucntion status: not started
def password_gen():
    print('This is the passowrd generation function')

# fucntion status: not started
def id_gen():
    print('This is the id generation funtion')

# fucntion status: working.
# function needs additional formatting
def display_menu():

    print('This is the menu display function')
    print("The Mars Mission Personel Program")
    print()
    print("COMMAND MENU")
    print("list - List all accounts_listss")
    print("add -  Add a accounts_lists")
    print("del -  Delete a accounts_lists")
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
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

    
if __name__ == "__main__":
    main()
