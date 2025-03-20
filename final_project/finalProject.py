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
def exit_program():
    print("Terminating program.")
    sys.exit()

# reads the file of accounts and returns a list to main
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

def list(accounts_lists):
    print('This is the list function')

def add(accounts_list):

    print('This is the add function')
    first_name = input('Please enter first name: ')
    last_name = input('Please enter last name: ')
    user_age = input('Enter user age: ')
    user_id = input('Enter random number: ') # to be replaced by a random generated id
    emai_address = first_name+'.'+last_name+'@hmm.com'
    user_passwrd = input('Enter temp password: ') # to be replaced by a random generated id
    pod_number = input('Please enter a pod number for the user: ')

    user = [first_name, last_name, user_age, user_id, emai_address, user_passwrd, pod_number]
    accounts_list.append(user)

def delete_account(accounts_list):
    print('Delete Account Function')

def search_pod(accounts_list):
    print('This is the search_pod function')

def search_name(accounts_list):
    print('This is the search function')

def password_gen():
    print('This is the passowrd generation function')

def id_gen():
    print('This is the id generation funtion')

def display_menu():
    print('This is the menu display function')

def main():
    
    display_menu()
    accounts_list = read_accounts()
    while True:
        command = input('Command: ')
        if command = 'Add'

    
if __name__ == "__main__":
    main()
