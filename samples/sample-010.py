my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# list[start:stop:step]

print(my_list[-2:1:-1])  # Extracts elements from index -2 to 1 with a step of -1
# Note that we start at the end in this example!!

print(my_list[8:-5:-1])  # The moment you use a negative step, you are supposed to start from the end of the list


print(my_list[8:5])  # This doesn't work because the start index is greater than the stop index

print("Slice operator with reversed step")
list_to_slice = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sliced_list = list_to_slice[:-9]  # Extracts all elements except the last one
print(f"Original list: {list_to_slice}")
print(f"Sliced list: {sliced_list}")


print("Slice operator with reversed step")
list_to_slice = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sliced_list = list_to_slice[:-15]  # If you step out of the list, it will return an empty list
# This is because the slice operator does not raise an error if the range is out of bounds.
print(f"Original list: {list_to_slice}")
print(f"Sliced list: {sliced_list}")


print("Slice operator insert")

fruits = ['apple', 'banana', 'cherry']
print(f"Original fruits: {fruits}")
fruits[0:1] = ['orange', 'kiwi']  # Insert 'orange' and 'kiwi' at index 1
print(f"Fruits after insertion: {fruits}")

# See: https://www.youtube.com/watch?v=mfXTsnYJwjE