def simple_division():
    try:
        # handling dangerous code
        number = int(input("Please enter a number to divide by 10\n"))
        result = 10 / number
        print(f"The answer is result {result}")
    except ZeroDivisionError:
        # This is where we handle the errors
        print("Oops! Cannot divide the number")
    except ValueError:
        # This is where we handle the errors
        print(f"Error: {number is not valid}")
    except Exception as e:
        print(f"Something went wrong: {e}")
simple_division()

# types of erros: ValueError (passed wrong value eg used string instead of int), TypeError(used the wrong type of data), Syntax error