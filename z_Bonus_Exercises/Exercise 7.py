'''Loops- Pizza Toppings :
Write a loop that prompts the user to enter a series of pizza toppings until they enter a
'quit' value. As they enter each topping,
Print a message saying you'll add that topping to their pizza.
'''
Toppings = ["Pepporoni", "Sausages", "Pineapple", "Creamy Spinach"]
print(Toppings)

while Toppings:
    user_input = str(input("What toppings would you like on your pizza?: "))
    if user_input == Toppings[0]:
        print("You added Pepporoni to your pizza")
    user_input = str(input("Is that all? "))
    if user_input.lower() == "yes":
        print("Enjoy your pizza <3")
        break
    elif user_input.lower() == "no":
         user_input = str(input("What toppings would you like on your pizza?: "))
    if user_input == Toppings[1]:
        print("You added Sausages to your pizza")
    user_input = str(input("Is that all? "))
    if user_input.lower() == "yes":
        print("Enjoy your pizza <3")
        break
    elif user_input.lower() == "no":
        user_input = str(input("What toppings would you like on your pizza?: "))
    if user_input == Toppings[2]:
        print("You added Pineapple to your pizza")
    user_input = str(input("Is that all? "))
    if user_input.lower() == "yes":
        print("Enjoy your pizza <3")
        break
    elif user_input.lower() == "no":
        user_input = str(input("What toppings would you like on your pizza?: "))
    if user_input == Toppings[3]:
        print("You added Creamy Spinach to your pizza")
    user_input = str(input("is that all? "))
    if user_input.lower() == "yes":
        print("Enjoy tour pizza <3")
        break
    else:
        print("Sorry you added all the toppings. Enjoy your pizza <3")
        break