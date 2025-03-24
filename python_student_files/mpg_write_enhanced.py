#!/usr/bin/env python3
#===========================================================================
# Code Practice Lab 8 - MPG Write Enhanced
# Write data to a CSV file
# DEV 108 - 34634
# Mario Rodriguez
# March 1, 2025
# TODO
# 
#===========================================================================

import csv

FILENAME = 'trips.csv'

def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven
          
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used

def write_trips(trips):
    # open file and write user input data
    with open(FILENAME, 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerows(trips)

def read_trips():
    
    trips = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            trips.append(row)

    return trips

def list_trips(trips):
    # code to go here
    print('Distance\tGallons\t     MPG')
    for row in range(len(trips)):
        trip = trips[row]
        print(f'{trip[0]}\t\t {trip[1]}\t     {trip[2]}')
    print()

def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    # store trips for current session by leveraging the read_trips() function
    trips = read_trips()
    list_trips(trips)

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()

        # list to store current trip information
        trip = [miles_driven, gallons_used, mpg]
        # append current trip to list of trips
        trips.append(trip)

        write_trips(trips)
        list_trips(trips)
        
        more = input("More entries? (y or n): ")

    # test to see trips are bing captures
    # print(trips)
    # print()
    print("Bye!")

if __name__ == "__main__":
    main()