# exploring_lists_in_python.py
#===========================================================================
# In-Class Assignment - Exploring Lists in Python
# DEV 108 - 34634
# Mario Rodriguez
# February 19, 2025
#===========================================================================

# Part 1: Welcome to the Python Zoo ========================================

zoo_animals = ['python', 'elephan', 'badger', 'hippo', 'lion', 'monkey']
print(zoo_animals[0])
print(zoo_animals[5])
zoo_animals[2] = 'tiger'
zoo_animals.append('zebra')
zoo_animals.insert(1, 'warthog')
zoo_animals.sort()
print(zoo_animals)

# Part 2: The Number Puzzle ================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
squares = []
even_numbers = []

for i in numbers:
    squares.append(i*i)

for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)

numbers.reverse()

print(numbers)
print(squares)
print(even_numbers)

# Part 3: Grocery Shopping Adventure ========================================

shopping_list =['Milk', 'Eggs', 'Bread', 'Cheese', 'Avocados', 'Tomatoes', 'Bacon', 'Banana', 'Coffee']
print(shopping_list)
shopping_list.remove('Tomatoes')
print(shopping_list)
shopping_list.pop()

if 'Milk' in shopping_list:
    print(f'Milk is on the list')
else:
    print('Milk is not on the list')

print(f'There are {shopping_list.count('Banana')} Bananas in the list')
print(f'There are {len(shopping_list)} items in the list')
