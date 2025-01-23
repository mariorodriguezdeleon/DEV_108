# In-Class Assignment
# Dev 108
# January 15, 2025

# Prompt for Variables
magic_number = int(input("Enter your favorite integer number: "))
spell_one = input("Enter a secrete word: ")
spell_two = str(magic_number) + str(len(spell_one))
secret_message = spell_one*magic_number + spell_two

# Print the result for spell one
print(f"The first spell creates: " + spell_one*magic_number)
print(f"The second spell creates: {spell_two}")
print (f'The secrete message is: {secret_message}')
