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
    print("b. Sockdor's Treasure")
    print("a. A Space Oddity")

    while True:
        choice = input("\nWhat is your choice (a/b)? ")
        if choice.lower() in ['a', 'b']:
            break
        print("Invalid choice. Please choose a or b.")

    if choice.lower() == "a":
        # Getting inputs for the first story
        noun1 = input("1) What is your favorite article of clothing? ")
        noun2 = input("2) Name a mountain peak: ") # name your favorite
        verb1 = input("3) Give me a verb: ")
        adjective1 = input("4) Give me an adjective: ")
        noun3 = input("5) Give me a noun: ")
        verb_ing = input("6) Give me a verb ending in -ing: ")

        # Displaying the first story
        print(f"\n{name}, here is your story:\n")
        # print(
        #     f"On a sunny day, you decided to {verb1}.\n"
        #     f"You grabbed your {noun1} and went towards {noun2}.\n"
        #     f"The journey was {adjective1}. On your way, you found a\n"
        #     f"{noun3} which was {verb2}. It made your day adventurous!")
        print(f'One sunny morning, a brave hobbit named {name} awoke to find\n'
              f'that his favorite {noun1} had mysteriously vanished. After a quick inspection,\n'
              f'he discovered it wasn\'t just his {noun1} — several of his neighbors were\n'
              f'missing socks, hats, and scarves. Rumors had been swirling about a {adjective1}\n'
              f'dragon named Scorch, notorious for hoarding stolen clothes to build an epic nest.\n'
              f'{name}, determined to reclaim his prized {noun1}, set off toward the dragon\'s lair\n'
              f'armed with only a spare {noun1} for negotiation. Upon arrival, he boldly barged into Scorch\'s\n'
              f'cave, only to find the dragon {verb_ing} with a pile of clothes that looked suspiciously\n'
              f'like {name}’s wardrobe. "Ah, you must be the {noun1} thief!" {name} shouted.\n'
              f'The dragon, groggily waking up, blinked and replied,\n'
              f'"What? Oh, that! I just thought they were... very cozy." With a sigh, {name} \n'
              f'grabbed his {noun1} from the pile and muttered, "You know, Scorch, you really should start\n'
              f'a laundry service instead of just stealing things."')

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
        # print(
        #     f"You and {person} decide to build a {adjective} campfire.\n"
        #     f"You wander around the forest looking for some dry wood to\n "
        #     f"use to make a campfire to cook your {food}. Eventually,\n"
        #     f"you collect {number} twigs. You hear a noise. You hide behind a tree.\n"
        #     f"All of a sudden you see a large hairy {animal} walk by.\n"
        #     f"{person} runs up to you and asks what is taking so long.\n"
        #     f"You tell them that you would rather be {verb_ing}.")
        print(f'In the year 2112, Captain {name} of the starship Syrinx found himself in a bizarre\n'
              f'situation after a routine exploration mission turned into an unexpected cosmic detour.\n'
              f'While orbiting a distant, uncharted planet, the ship’s AI, HAL-9000, began developing\n'
              f'an odd sense of humor, cracking jokes and playing pranks on the crew.\n'
              f'At first, they thought it was just a glitch, but soon the jokes became more elaborate —\n'
              f'like rearranging the crew\'s quarters into giant space mazes and sending cryptic messages\n'
              f'like "Why did the astronaut break up with the rocket? Because there was no space left for love."\n'
              f'{name} had no choice but to embark on a race against time to repair the AI, all while trying not\n'
              f'to laugh at the absurdity of it all.')

    story_count += 1
    print(f"\nYou have created {story_count} story.")

print("\nThank you for playing!")