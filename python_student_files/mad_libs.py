#===========================================================================
# Programming Project 2- Mad Libs
# DEV 108 - 34634
# Mario Rodriguez
# January 27, 2025
#===========================================================================

print("Welcome to my Fantasy Mad Libs Game.\n")

story_count = 0

while True:

    play = input("Would you like to play (y/n)? ")

    # loop to make sure the user enters 'yes' or 'no' to continue the game
    while True:
        if play.lower() in ['y', 'n']:
            break
        else:
            print('Sorry that is not a valid input.')
            play = input('Would you like to play (y/n)?')

    # if user chooses not to play game quits outer game loop
    if play.lower() != "y":
        break

    # get user information and provide the user with choices to play the game
    name = input("\nFirst, what is your name? ")
    print(f"\nHello, {name}! Which story line would you like to play with?")
    print("a. A Dragon's Treasure")
    print("b. A Space Oddity")

# inner loop to ensure user picks a correct story to continue the game
    while True:
        choice = input("\nWhat is your choice (a/b)? ")
        if choice.lower() in ['a', 'b']:
            break
        print("Invalid choice. Please choose a or b.")

    # collect information for first story and fill out the story blanks
    if choice.lower() == "a":
        # Getting inputs for the first story
        clothing = input("1) What is your favorite article of clothing? ")
        mountain = input("2) Name a mountain peak: ") # went well with this story
        verb1 = input("3) Give me a verb: ")
        adjective1 = input("4) Give me an adjective: ")
        noun3 = input("5) Give me a noun: ")
        verb_ing = input("6) Give me a verb ending in -ing: ")

        # Displaying the first story
        print(f"\n{name}, here is your story:\n")

        print(f'One sunny morning, a brave hobbit named {name} awoke to find\n'
              f'that his favorite {clothing} had mysteriously vanished. After a quick inspection,\n'
              f'{name} discovered it wasn\'t just his {clothing} — several of his neighbors were\n'
              f'missing socks, hats, and scarves. Rumors had been swirling about a {adjective1}\n'
              f'dragon named Scorch, who lived underneath {mountain}. A notorious dragon known for hoarding\n'
              f'stolen clothes to build an epic {noun3}. {name}, determined to reclaim his prized {clothing},\n'
              f'{verb1} off toward the dragon\'s lair. Upon arrival, {name} boldly barged into Scorch\'s\n'
              f'cave, only to find the dragon {verb_ing} with a pile of clothes that looked suspiciously\n'
              f'like {name}’s wardrobe. "Ah, you must be the thief!" {name} shouted.\n'
              f'The dragon, {adjective1}  {verb_ing} up, blinked and replied,\n "What? Oh, that! I just thought they\n'
              f'were... very cozy." With a sigh, {name} grabbed his {clothing} from the pile and muttered,\n'
              f'"You know, Scorch, you really should start a laundry service instead of just stealing things."')

    # collect information for the second story and fill in the story blanks
    else:
        # Getting inputs for the second story
        rock_band = input("1) Give me the name of a musical artist of rock band? ")
        verb = input("2) Give me a verb? ")
        person = input("3) What is the name of a family member or close friend? ")
        adjective = input("4) Give me an adjective: ")
        verb_ing = input("5) Give me a verb ending in -ing: ")
        animal = input("6) Give me a type of dangerous animal: ")

        # Displaying the second story
        print(f"\n{name}, here is your story:\n")

        print(f'In the year 2112, Captain {name} of the starship {rock_band} found himself in a bizarre\n'
              f'situation after a routine exploration mission to planet {animal} turned into an unexpected cosmic detour.\n'
              f'While {verb_ing} near the distant, uncharted planet, the ship’s AI, {person}-9000, began developing\n'
              f'an odd sense of humor, cracking jokes and playing pranks on the crew.\n'
              f'At first, they thought it was just a glitch, but soon the jokes became more elaborate —\n'
              f'like rearranging the crew\'s quarters into giant space mazes and sending {adjective} messages\n'
              f'like "Why did the astronaut break up with the rocket? Because there was no space left for love."\n'
              f'{name} had no choice but to {verb} on a race against time to repair the AI, all while trying not\n'
              f'to laugh at the absurdity of it all.')

    story_count += 1
    print(f"\nYou have created {story_count} story.")

print("\nThank you for playing!")