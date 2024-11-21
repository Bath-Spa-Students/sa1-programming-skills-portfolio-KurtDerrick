## Exercise 8: Simple Search - 30 Marks
'''
Write a program that searches for a specific string within a list of strings.
The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".

### Optional Requirements:
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input.
'''

name_list = ["Jake" "Zac", "Ian", "Ron", "Sam", "Dave"] # List of names

print("Your task is to find the person we're looking for. You only get 1 try. Goodluck")
print(name_list)
choose = str(input("Enter the name we're looking for: "))
if choose == "Sam":
    print("You Found Him, Congrats")
else:
    print("This person is not who we're looking for. You failed")