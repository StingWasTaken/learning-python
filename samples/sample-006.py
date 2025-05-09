#Lists
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])
# Negative indexing means starting from the end
print(fruits[-1])
print(fruits[-2])

print('Append orange:')
fruits.append("orange")
print(fruits)

print('Remove banana:')
fruits.remove("banana")
print(fruits)

print('Insert banana:')
fruits.insert(1, "banana")
print(fruits)

print('Pop:')
fruits.pop()
print(fruits)