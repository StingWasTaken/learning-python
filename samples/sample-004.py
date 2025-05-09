if 3 > 2 or 2 > 3 and 3 > 1 or 1 > 2:
    print('Yes') # it will be evaluated as 3 > 2 or (2 > 3 and 3 > 1) or 1 > 2
else:
    print('No')


if True or False and True or False:
    print('Yes') # it will be evaluated as True or (False and True) or False
else:
    print('No')

# and operator has higher precedence than or operator

if (True or False) and False or False:
    print('Yes') 
else:
    print('No') # It will print No