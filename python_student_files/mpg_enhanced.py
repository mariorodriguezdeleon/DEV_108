#!/usr/bin/env python3
#===========================================================================
# Code Practice Lab 4 - Enhanced Miles Per Gallon Program
# DEV 108 - 34634
# Mario Rodriguez
# January 27, 2025
#===========================================================================

# display a welcome message
print("The Miles Per Gallon program")
print()

while True:

    # get miles driven from the user
    miles_driven = float(input("Enter miles driven: "))
    # get gallons of gas used from the user
    gallons_used = float(input("Enter gallons of gas used: "))
    # get cost per gallon from the user
    cost_per_gallon = float(input("Enter cost per gallon: "))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    else:
        # calculate miles per gallon
        mpg = round(miles_driven / gallons_used, 2)

        # calculate the total gas cost
        #-------------- your code here ------------------
        total_gas_cost = round(gallons_used*cost_per_gallon, 2)

        # calculate the cost per mile
        # -------------- your code here ------------------
        cost_per_mile = round(total_gas_cost / miles_driven , 2)

        # print the results
        print()
        print(f'Miles Per Gallon: {mpg}')
        print(f'Total Gas Cost: {total_gas_cost}')
        print(f'Cost per Mile: {cost_per_mile}')
        print()

    # ask the user for another trip or exit
    another_trip = input('Get entries for another trip (y/n)? ')

    if another_trip.lower() != "y":
        break

print("Bye!")



