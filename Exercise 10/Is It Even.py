## Exercise 10: Is it even? - 35 Marks
'''
Write a program that tests if a value is even or odd. Follow the instructions outlined below:

### Instructions:
* The program should ask the user for a number from within the main function.
* The entered number should be passed to a function that determines if the value is even or odd.
* The function should return a message indicating whether the number is even or odd.
* The message returned by the function should be printed from within the main function.
'''

def even(number): # set even function
    return number % 2 == 0 # if number is divisible by 2 and the remainder is 0
def odd(number): # set odd function
    return number % 2 == 1 # if number is divisible by 2 and the remainder is 1
def main():
    number = int(input("Enter a number: ")) # ask user to pick number
    
    if even(number):
        print("The number you entered is EVEN")
    elif odd(number):
        print("The number you entered is ODD")