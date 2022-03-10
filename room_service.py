"""
Yanjaa's Room Service chatbot
"""

guests = {'111':'Jay', '222':'Sunoo', '333':'Heeseung'}
correct_info = False

#ask for room number
room = input ("Please, enter room number: ")
room = room.lower()
if room in guests.keys():
    correct_info = True
else:
    correct_info = False

name = input ("Please, enter your name: ")
#check if inputed name in in the guests list
if correct_info and guests[room].lower() == name.lower():
    correct_info =  True
else: correct_info = False

#food menus
starterMenu = ['Salad', 'Tea', 'Sushi']
starterMenuPrice = {'Salad':4, 'Tea':3, 'Sushi':10}

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
for food in mainMenu:
        print(food)
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
for food in dessertMenu:
        print(food)
#ask for order
order_dessert = input("What do you want for dessert? ")
if order_dessert in dessertMenu:
        print("Your order is recorded.")
        print("It will be", dessertMenuPrice[order_dessert], 'dollars.')
else:
        print("Invalid order, please check capitalization or if the item is in our menu.")
    

#ask for delivery time
deliveryTime = ["Morning", 'Afternoon', 'Evening', 'Night']
for time in deliveryTime:
        print(time)
delivery = input("When would you like it to be delivered? ")

#final confirmation
print("For confirmation, you ordered for starter", order, ". You ordered for main course", order_main, ". You ordered for dessert", order_dessert, ". It will be delivered in the ", delivery.lower(), '.')
