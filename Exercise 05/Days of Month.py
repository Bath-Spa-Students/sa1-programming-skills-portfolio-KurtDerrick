## Exercise 5: Days of the Month - 30 Marks
'''
Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

### Instructions:
1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.

### Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly.
'''
Month = {1:"31 Days",
         2:"28 Days", 
         3:"31 Days", 
         4:"30 Days", 
         5:"31 Days", 
         6:"30 Days", 
         7:"31 Days", 
         8:"31 Days", 
         9:"30 Days", 
         10:"31 Days", 
         11:"30 Days",
         12:"31 Days"}

february = "29"

month = int(input("Enter Month number "))
if month == 1:
    print(Month[1])
elif month == 2:
    leap_year = str(input("Is it a leap year? "))
    if leap_year.lower() == "yes":
        print("29 Days")
    else:
        print(Month[2])
elif month == 3:
    print(Month[3])
elif month == 4:
    print(Month[4])
elif month == 5:
    print(Month[5])
elif month == 6:
    print(Month[6])
elif month == 7:
    print(Month[7])
elif month == 8:
    print(Month[8])
elif month == 9:
    print(Month[9])
elif month == 10:
    print(Month[10])
elif month == 11:
    print(Month[11])
elif month == 12:
    print(Month[12])
