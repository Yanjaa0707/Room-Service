guests = {'111':'Jay', '222':'Sunoo', '333':'Heeseung'}
correct_info = False

room = input ("Please, enter room number: ")
if room in guests.keys():
    correct_info = True
else:
    correct_info = False

name = input ("Please, enter your name: ")

if correct_info and guests[room].lower() == name.lower():
    correct_info =  True
else: correct_info = False

#currently working
"""starter_menu = ['Salad', 'Tea', 'Sushi']
starter_menu_price = {'Salad':10, 'Tea':3, 'Sushi':5}

# starter order function
def order_food():
    #stacks menu
    for food in starter_menu:
        print(food)
    #ask for order
    order = input("What is your order?")
    
    if starter_menu == order:
        print("Your order is recorded.")
    else:
        print("Wrong order, please check capitalization or if the item is in our menu.")
    
order_food()"""