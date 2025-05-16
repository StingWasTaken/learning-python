# Evil global variables
number = 0

print("Global variable number:", number)

def modify_global_variable():
    global number  # Declare that we want to use the global variable
    number = 42  # Modify the global variable
    print("Modified global variable number:", number)

modify_global_variable()