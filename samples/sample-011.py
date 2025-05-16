# Try/except. Same as  try/catch in C#

text = input("Enter a number: ")

try:
    # Attempt to convert the input to an integer
    number = int(text)
    print(f"You entered a number: {number}")
except ValueError:
    # Handle the case where the conversion fails
    print("That's not a valid number!")


text = input("Enter a number: ")

try:
    # Attempt to convert the input to an integer
    number = int(text)
    print(f"You entered a number: {number}")
except ValueError:
    # Handle the case where the conversion fails
    print("That's not a valid number!")
finally:
    # This block will always execute
    print("Thank you for using the program!")