# used to carry a command of codes
# a star reps the no of arguments 
# for keyword arugements we use args_kwargs , for multiple we use *args
# we use colon : to denote end of a function
""" Doc strings used as a comment thing"""

first_name = ''
last_name = ''

def register(first_name, last_name):
    """This is a fn that registers users.
        Takes in the first and last names
    """
    input("Please enter you first name...\n") # \n forces a new line
    print()
    input("Please enter you last name...\n")
    print(f"You are now registered", first_name, last_name)
    return first_name, last_name
register("Cynthia", "Sagini") # call the function

# void function is printing without returning 
# fruitful fn MUST have a return statement



