#For loops
#For loop using ranges:
print("First loop:")
for x in range(1, 10):
    print(x)

print("Second loop:")
for x in range(1, 10, 2):
    print(x)

print("Second loop:")
for x in range(1, 10, 2):
    print(x)


# while loops
print("While loop:")
x = 1
while x < 10:
    print(x)
    x += 1

# while loops with break
print("While loop with break:")
y = 1
while y < 10:
    print(y)
    y += 1
    break # this will break the loop after the first iteration


# For loops with lists:
print("For loop with list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    