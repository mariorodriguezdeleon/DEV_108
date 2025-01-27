#===========================================================================
# Programming Project 1 - AI Fake "Sales Bot"
# DEV 108
# The Wasteland Surplus with Codsworth
# Mario Rodriguez
# January 24, 2025
#===========================================================================
# from rich import print as rprint
import datetime
#===========================================================================
#TODO
# User response validation needs work (dif between str and numbers)
# Formating print to console
# Work on 'welcome message'
# Allow for multiple items to be purchased 'shopping cart'
#============================================================================

MY_INVENTORY = {
    'Plumbus':250,
    'Science Bobblehead':500,
    'Junkjet':1000
}

TAX = 10/100

def welcome_message():
    print(f'===============================================\n'
          f'     Welcome to the Wasteland City Surplus\n'
          f'===============================================\n')
    print("My name is Codsworth, and I will be your\n"
          "personal shopping companion")

    _inventory = input('Would you like to see our inventory?\n'
                       'Enter "yes" or "no": ')
    return _inventory

def goodbye_message():
    print()
    print('Thank you for stopping by and visiting\n'
          'our little shop. Goodbye!')

def inventory_description():

    _key_list = list(MY_INVENTORY.keys()) # pull list of items in inventory
    _learn_more = True # flag used to keep calling item_description() to provide item information

    print()
    print(f'These are the products that we have for sale')
    print()
    # list all inventory items
    for i in range(len(_key_list)):
        print(f'{i+1}. {_key_list[i]}')
    print()

    print(f'If you\'d like to learn more about any item in our\n'
          f'inventory, please feel free to enter the item number of the \n'
          f'product you\'d like to learn more about or "no" to exit".')
    _item_to_describe = input('Enter item number: ')

    # ask user if they would like to learn about the products
    while _learn_more:
        if _item_to_describe == 'no':
            _learn_more = False
            break
        else:
            item_descriptions(_item_to_describe)
            print()
        _item_to_describe = input("Enter item number to learn more or no to exit: ")

    print()
    _purchase_product = input('Enter the item number you\'d like to purchase or \'no\' to exit: ')

    return _purchase_product

def item_descriptions(item):

    _key_list = list(MY_INVENTORY.keys()) #import inventory list
    # print(_key_list) # test to see if list populates

    if item == '1':
        print('===============================================================================')
        print(f'{_key_list[0]} \nPrice: ${MY_INVENTORY.get(_key_list[0])}')
        print()
        print(f'A {_key_list[0]} is an all-purpose home device!\n'
              f'Plumbus can generate and store vast amounts of heat,\n'
              f'allowing it to be used for cooking, ironing or just heating the room.\n'
              f'Plumbus can secrete various agents from itself and has adaptive rubbing\n'
              f'surfaces, making it useful for cleaning. A Plumbus is able to receive radio\n'
              f'waves and convert them to sound, even recording and playing them back, \n'
              f'so it can be used as a radio and/or receiver.')
        print('===============================================================================')
    elif item == '2':
        print('===============================================================================')
        print(f'{_key_list[1]} \nPrice: ${MY_INVENTORY.get(_key_list[1])}')
        print()
        print(f'This {_key_list[1]} collectors items will round out any bobblehead collection\n'
              f'while giving you that extra spark of luck while traversing the vast wastes.\n'
              f'Never leave home without your lucky charm!')
        print('===============================================================================')
    elif item == '3':
        print('===============================================================================')
        print(f'{_key_list[2]} \nPrice: ${MY_INVENTORY.get(_key_list[2])}')
        print()
        print(f'A {_key_list[2]} is a heavy "ballistic" weapon that fires any junk\n'
              f'items loaded into its hopper, e.g. desk fans, tin cans, teddy bears,\n'
              f'Nuka-Cola bottles, etc. Items must be loaded in manually, and fired \n'
              f'items can be picked up after being shot, making this a ranged weapon\n'
              f'with theoretically unlimited ammunition. This a must have utility in any\n'
              f'wastelander\'s toolbox. Get yours today!')
        print('===============================================================================')
    else:
        print()
        print("Sorry, but we are out of stock for that item.")

def close_the_sale(item):

    _item_cost = 0
    _total_cost = 0
    _subtotal = 0
    _key_list = list(MY_INVENTORY.keys())

    print()
    print(f'That sounds wonderful!\n'
          f'I\'m sure that you\'ll be happy with your new purchase\n'
          f'We accept cash, caps or flurbos!!')

    if item == 1:
        _item_cost = int(MY_INVENTORY.get('Plumbus'))
    elif item == 2:
        _item_cost = int(MY_INVENTORY.get('Science Bobblehead'))
    elif item == 3:
        _item_cost = int(MY_INVENTORY.get('Junkjet'))

    # collect user information to complete the sale and provide receipt
    print()
    print(f'Before we finalize your purchase\n'
          f'Please provide the following information\n')

    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    email_address = input('Email: ')
    phone_number = input('Phone Number: ')
    product_quantity = input('How many would you like: ')

    _subtotal = _item_cost * int(product_quantity)
    _total_cost = _subtotal + (_subtotal*(1*TAX))

# print receipt
    print(datetime.datetime.now())
    print('========= Customer Information =========')
    print(f'Customer Name: {first_name} {last_name}')
    print(f'Customer email: {email_address}')
    print(f'Customer phone number: {phone_number}')
    print('=========================================')
    print('========= Sale Information ==============')
    print(f'Items Purchased: {_key_list[item]}\n'
          f'Items Cost: ${MY_INVENTORY.get(_key_list[item])}\n'
          f'Purchased Qty: {product_quantity}')
    print(f'Subtotal: {_subtotal}')
    print(f'Tax: 10%')
    print(f'Final Total: {_total_cost}.')

def main():

    _make_sale = "no"

    list_inventory = welcome_message()
    if list_inventory.lower() == 'yes':
        _make_sale = inventory_description() # returns customer choice to continue or end the program

    if _make_sale.lower() != 'no':
        close_the_sale(int(_make_sale)) # sends customer request to close the sale

    goodbye_message()
#=============================================================================
if __name__ == '__main__':
    main()
