# nameformat.py

def sayHello(firstName):
    """
    A simple function that takes a first name input and says hello to that name.
    """
    return f"Hello {firstName}!"

def fullName(firstName, lastName):
    """
    A function that takes a first and last name and returns a string value
    with a first and last name concatenated with a space.
    """
    return f"{firstName} {lastName}"

def lastNameFirst(firstName, lastName):
    """
    A function that takes a first and last name and returns a string value
    with a last name and first name, concatenated with a comma and a space.
    """
    return f"{lastName}, {firstName}"