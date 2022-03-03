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

#menus
starterMenu = ['Salad', 'Tea', 'Sushi']
starterMenuPrice = {'Salad':4, 'Tea':3, 'Sushi':10}

# starter order function
def order_starter():
    #stacks menu
    for food in starterMenu:
        print(food)
    #ask for order
    order = input("What can I get you to get started? ")
    #if order is there it gives response if not
    if order in starterMenu:
        print("Your order is recorded.")
        print("It will be", starterMenuPrice[order], 'dollars.')
    else:
        print("Invalid order, please check capitalization or if the item is in our menu.")
#main menu
mainMenu = ['Pizza', 'Burger', 'Pasta']
mainMenuPrice = {'Pizza':10, 'Burger':9, 'Pasta':11}

#main course order
def order_main():
    #stack menu
    for food in mainMenu:
        print(food)
    #ask for order
    order_main = input("What will be your main course? ")
    if order_main in mainMenu:
        print("Your order is recorded.")
        print("It will be", mainMenuPrice[order_main], 'dollars.')
    else:
        print("Invalid order, please check capitalization or if the item is in our menu.")
#dessert menu
dessertMenu = ['Ice cream', 'Ice tea', 'Milkshake']
dessertMenuPrice = {'Ice cream':5, 'Ice tea':3, 'Milkshake':6}

#dessert order
def order_dessert():
    #stack menu
    for food in dessertMenu:
        print(food)
    #ask for order
    order_dessert = input("What do you want for dessert? ")
    if order_dessert in dessertMenu:
        print("Your order is recorded.")
        print("It will be", dessertMenuPrice[order_dessert], 'dollars.')
    else:
        print("Invalid order, please check capitalization or if the item is in our menu.")

#final confirmation
def confirmation():
    print("For confirmation, you ordered for starter", order, ". You ordered for main course", order_main, ". You ordered for dessert", order_dessert, ".")

order_starter()
order_main()
order_dessert()

