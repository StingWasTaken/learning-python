# Comparision operators with strings

print('white' == 'white') # True
print('white' != 'black') # True
print('white' != 'white') # False
print('white' == 'White') # False
print('white' == "white") # True

#Control flow


# 1. if statement

x = 3
y = 6

if x > y:
    print('x is greater than y')
elif x < y:
    print('x is less than y')


input_grade = input('Input your climbing grade (V scale with only the number):')
print(f'You are V {input_grade} climber. This means...')

if input_grade.isdigit():
    grade = int(input_grade)
    if grade >= 6:
        print('You are a bro')
    elif grade < 4:
        print('You are not a bro')
    else:
        print('You are mid')