list_of_discounts = [
    {"id": 1, "discount": 10},
    {"id": 2, "discount": 20},  
    {"id": 3, "discount": 30},
    {"id": 4, "discount": 40},
    {"id": 5, "discount": 50}
]

print("List of discounts:")
for discount in list_of_discounts:
    print(f"ID: {discount['id']}, Discount: {discount['discount']}%")