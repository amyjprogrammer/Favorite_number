"""asking for a Favorite number,storing that info and retrieving it"""

import json

def retrieve_number():
    """retrieving favorite number from json"""
    favorite_number = 'number.json'
    try:
        with open(favorite_number) as f:
            number = json.load(f)
    except FileNotFoundError:
        return none
    else:
        return number

def new_number():
    """Prompt for a favorite number"""
    number = input("Please enter your favorite number: ")
    favorite_number = 'number.json'
    with open(favorite_number, 'w') as f:
        json.dump(number, f)
    return number

def favorite_number():
    """Greet user with favorite number or that we will store the number."""
    number = retrieve_number()
    if number:
        print (f"Is this your favorite number {number}?")
        number_check = input("Yes or No: ")
        if number_check == 'Yes':
            print (f'Thank you.  Once again, Your favorite number is {number}.')
        else:
            number = new_number()
            print (f"We will remember your favorite number {number} next time.")
    else:
        number = new_number()
        print (f"We will remember your favorite number {number} next time.")


favorite_number()
