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