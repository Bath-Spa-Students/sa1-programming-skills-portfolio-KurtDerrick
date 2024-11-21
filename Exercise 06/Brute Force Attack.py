## Exercise 6: Brute Force Attack - 30 Marks
'''
Write a program that simulates a password entry system. The correct password is defined as 12345.
The program should keep asking the user to enter the password until they provide the correct one.

### Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
3. Output an appropriate message when the correct password is entered.

### Optional Requirements:
Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining
attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted.
'''

password = 12345

while password:
  userinput = int(input("Enter passcode: ")) # User enters input
  if int(userinput) != 12345:
      print("Incorrect")   
  elif userinput == 12345:
     print("Correct")
     break # exit loop if user enters correct password

# Advanced requirement
pass_word = ("12345")
max_attempts = 5 # set the maximum number of attempts

attempts = 0  # initialize attempts counter
while attempts < max_attempts:
    user_input = str(input("Enter your password: "))
    # check if user input is correct
    if user_input == pass_word:
        print("Access granted!")
        break  # exit loop on success
    attempts += 1  # increase attempts counter
    if attempts == max_attempts:
        print("Too many incorrect attempts. Authoritize have been alerted.")
        break  # exit loop on max attempts reached
    
