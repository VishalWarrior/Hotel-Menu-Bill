#Define the menu of Restaurant

menu = {
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80,
    'French-Frie':99,
    'Spring roll':89,
    'Samosa':25,
    'Chai':15,
    'Mineral Water':15
}

#Greeting
print("Welcome to PYTHON Restaurant")
print(" Pizza: Rs40\n Pasta: Rs50\n Burger: Rs60\n Salad: Rs70\n Coffee: Rs80\n French-Frie: Rs99\n Spring roll: Rs89\n Samosa: Rs25\n Chai:Rs 15\n Mineral Water: Rs15")

order_total = 0

item_1 =input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The total amount of items to pay is {order_total}")
