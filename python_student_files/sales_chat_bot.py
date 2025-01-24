#===========================================================================
# Programming Project 1 - AI Fake "Sales Bot"
# DEV 108
# US State Capitals Game
# Mario Rodriguez
# January 24, 2025
#===========================================================================

def welcome_message():
    print(f'Welcome!')

def products_for_sale():# Might want to break down this into several products
    print(f'These are the products that we have for sale')
    # Describe the product and ask the user if they would like to purchase item
    print('We sell flurbos')
    buyProduct = input('Would you like to buy Flurbos: ')

    return buyProduct

# collect user information
def make_the_sale():
    print(f'Please provide the following information')
    firstName = input('First Name: ')
    lastName = input('Last Name: ')
    emailAddress = input('Email: ')
    phoneNumber = input('Phone Number: ')
    productQuantity = input('How many would you like: ')

def goodbye_message():
    print('Goodbye')

def main():

    welcome_message()

    make_sale = products_for_sale()

    if make_sale:
        make_the_sale()
    else:
        goodbye_message()

main()
#=============================================================================
# if __name__ == '__main()__':
#     main()

# print('this works')