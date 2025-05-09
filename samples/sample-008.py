# String Methods

# .strip() method:
# The .strip() method removes any leading and trailing whitespace from a string.
# It does not modify the original string but returns a new string with the whitespace removed.
# Example:
string_with_spaces = "   Hello, World!   "
stripped_string = string_with_spaces.strip()
print(f"Original string: '{string_with_spaces}'")
print(f"Stripped string: '{stripped_string}'")
print()

# .len() method:
# The .len() method returns the length of a string, which is the number of characters it contains.
# Example:
string_to_measure = "Hello, World!"
length_of_string = len(string_to_measure)
print(f"Original string: '{string_to_measure}'")
print(f"Length of string: {length_of_string}")
print()

# .replace() method:
# The .replace() method replaces all occurrences of a specified substring with another substring.
# Example:
string_to_replace = "Hello, World!"
replaced_string = string_to_replace.replace("World", "Python")
print(f"Original string: '{string_to_replace}'")
print(f"Replaced string: '{replaced_string}'")
print()

# .split() method:
# The .split() method splits a string into a list of substrings based on a specified delimiter.
# By default, it splits by whitespace.
# Example:
string_to_split = "apple,banana,cherry"
split_string = string_to_split.split(",")
print(f"Original string: '{string_to_split}'")
print(f"Split string: {split_string}")
print()