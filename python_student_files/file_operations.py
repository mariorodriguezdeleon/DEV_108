#===========================================================================
# In-Class Assignment - File Handling
# Read, Write and Append to a file
# DEV 108 - 34634
# Mario Rodriguez
# March 5, 2025
#===========================================================================

# To Do
# Task 1: Write to file
with open('student_notes.txt', 'w') as file:
    file.write('1. Python is a interpreted high programming language.\n')
    file.write('2. It supports multiple programming paridigms.\n')
    file.write('3. Pyton has a simple syntax similar to English.\n')
    file.write('4. It is widely used in web development, data science, and automation.\n')
    file.write('5. The Python standard library provides many built-in useful modules.\n')

# Task 2: Read from file
with open('student_notes.txt', 'r') as file:
    # print(file.read())
    for line in file:
        print(line)
    
# Task 3: Append
with open('student_notes.txt', 'a') as file:
    file.write('6. Python can be used for scripting and rapid application development.\n')
    file.write('7. It has a vast community and extensive online documentation.\n')

# Task 4: Display Updated Content
print('=======================================================================\n')
with open('student_notes.txt', 'r') as file:
    # print(file.read())
    for line in file:
        print(line)