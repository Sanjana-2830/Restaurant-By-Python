#Define the menu of Restaurant
menu = {
    'Pizza':90,
    'Burger':70,
    'Coffee': 110,
    'Salad': 50,
    'Pasta':80,
}

print("Welcome to Restaurant By Python")
print("Pizza: Rs90\nBurger: Rs70\nCoffee: Rs110\nSalad: Rs50\nPasta: Rs80")

order_total = 0
item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"Your {item_1} hass been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet!")

