# Slice operator

# The slice operator is used to extract a portion of a sequence (string, list, tuple).
# It is defined using the syntax [start:stop:step], where:
# - start: The index to start the slice (inclusive).
# - stop: The index to end the slice (exclusive).
# - step: The interval between each index in the slice (optional).
#
print("Example 1")
string_to_slice = "Hello, World!"
sliced_string = string_to_slice[0:5]  # Extracts characters from index 0 to 4
print(f"Original string: '{string_to_slice}'")
print(f"Sliced string: '{sliced_string}'")

print("Example 2")
string_to_slice = "Hello, World!"
sliced_string = string_to_slice[0:]  # If stop is omitted, it goes to the end of the string
print(f"Original string: '{string_to_slice}'")
print(f"Sliced string: '{sliced_string}'")

print("Example 3")
string_to_slice = "Hello, World!"
sliced_string = string_to_slice[:5]  # If start is omitted, it starts from the beginning
print(f"Original string: '{string_to_slice}'")
print(f"Sliced string: '{sliced_string}'")

print("Example 4")
string_to_slice = "Hello, World!"
sliced_string = string_to_slice[::2]  # Extracts every second character
print(f"Original string: '{string_to_slice}'")
print(f"Sliced string: '{sliced_string}'")

print("Example 5")
string_to_slice = "Hello, World!"
sliced_string = string_to_slice[::-1]  # Reverses the string
print(f"Original string: '{string_to_slice}'")
print(f"Sliced string: '{sliced_string}'")

print("Example 6")
string_to_slice = "Hello, World!"
sliced_string = string_to_slice[1:5:2]  # Extracts characters from index 1 to 4 with a step of 2
print(f"Original string: '{string_to_slice}'")
print(f"Sliced string: '{sliced_string}'")


#
# The slice operator can also be used with lists and tuples.
print("Example with a list:")
print("Example 1")
list_to_slice = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sliced_list = list_to_slice[2:7:2]  # Extracts elements from index 2 to 6 with a step of 2
print(f"Original list: {list_to_slice}")
print(f"Sliced list: {sliced_list}")

print("Example 2")
list_to_slice = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sliced_list = list_to_slice[:-1]  # Extracts all elements except the last one
print(f"Original list: {list_to_slice}")
print(f"Sliced list: {sliced_list}")

print("Example with a tuple:")
tuple_to_slice = (10, 20, 30, 40, 50, 60)
sliced_tuple = tuple_to_slice[1:5]  # Extracts elements from index 1 to 4
print(f"Original tuple: {tuple_to_slice}")
print(f"Sliced tuple: {sliced_tuple}")
