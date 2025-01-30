#===========================================================================
# Programming Project 2- Mad Libs
# DEV 108 - 34634
# Mario Rodriguez
# January 27, 2025
#===========================================================================
# from rich import print as rprint

print("Welcome to my Mountain Adventure Mad Libs game.\n")

story_count = 0
while True:
    play = input("Would you like to play (y/n)? ")
    if play.lower() != "y":
        break

    name = input("\nFirst, what is your name? ")
    print(f"\nHello, {name}! Which story line would you like to play with?")
    print("a. A Space Oddity")
    print("b. Sockdor's Treasure")

    while True:
        choice = input("\nWhat is your choice (a/b)? ")
        if choice.lower() in ['a', 'b']:
            break
        print("Invalid choice. Please choose a or b.")

    if choice.lower() == "a":
        # Getting inputs for the first story
        noun1 = input("1) What is a thing you like to carry when you hike? ")
        noun2 = input("2) Name a mountain peak: ") # name your favorite
        verb1 = input("3) Give me a verb: ")
        adjective1 = input("4) Give me an adjective: ")
        noun3 = input("5) Give me a noun: ")
        verb2 = input("6) Give me a verb ending in -ing: ")

        # Displaying the first story
        print(f"\n{name}, here is your story:\n")
        print(
            f"On a sunny day, you decided to {verb1}.\n"
            f"You grabbed your {noun1} and went towards {noun2}.\n"
            f"The journey was {adjective1}. On your way, you found a\n"
            f"{noun3} which was {verb2}. It made your day adventurous!")

    else:
        # Getting inputs for the second story
        food = input("1) What is a food you like? ")
        number = input("2) Give me a number from 5 to 10? ")
        person = input("3) What is the name of a family member or close friend? ")
        adjective = input("4) Give me an adjective: ")
        verb_ing = input("5) Give me a verb ending in -ing: ")
        animal = input("6) Give me a type of animal: ")

        # Displaying the second story
        print(f"\n{name}, here is your story:\n")
        print(
            f"You and {person} decide to build a {adjective} campfire.\n"
            f"You wander around the forest looking for some dry wood to\n "
            f"use to make a campfire to cook your {food}. Eventually,\n"
            f"you collect {number} twigs. You hear a noise. You hide behind a tree.\n"
            f"All of a sudden you see a large hairy {animal} walk by.\n"
            f"{person} runs up to you and asks what is taking so long.\n"
            f"You tell them that you would rather be {verb_ing}.")

    story_count += 1
    print(f"\nYou have created {story_count} story.")

print("\nThank you for playing!")