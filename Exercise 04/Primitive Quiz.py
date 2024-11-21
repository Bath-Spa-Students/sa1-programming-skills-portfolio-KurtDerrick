'''## Exercise 4: Primitive Quiz - 30 Marks

In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.

### Steps:
1. Write a program that asks the user "What is the capital of France?" and waits for their response.
2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the answer is wrong.

### Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of the capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct).
Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. Provide feedback for each question.
'''

France=str(input("\n1. What is the capital of France? ")) #question
if France.lower() == "paris":
    print ("Your answer is correct")
else:
    print("Your answer is wrong")

print("\n11. Extra Questions")
    
Belgium = str(input("\n2. What is the capital of Belgium? "))
if Belgium.lower() == "brussels":
    print ("Your answer is correct")
else:
    print("Your answer is wrong")
    
Czech_Republic = str(input("\n3. What is the capital of Czech Republic? ")) 
if Czech_Republic.lower() == "prague":
    print ("Your answer is correct")
else:
    print("Your answer is wrong")

Denmark = str(input("\n4. What is the capital of Denmark? ")) 
if Denmark.lower() == "copenhagen":
    print ("Your answer is correct")
else:
    print("Your answer is wrong")

Finland = str(input("\n5. What is the capital of Finland? ")) 
if Finland.lower() == "helsinki":
    print ("Your answer is correct")
else:
    print("Your answer is wrong")

Germany = str(input("\n6. What is the capital of Germany? ")) 
if Germany.lower() == "berlin":
    print ("Your answer is correct")
else:
    print("Your answer is wrong")
    
Greece = str(input("\n7. What is the capital of Greece? ")) 
if Greece.lower() == "Athens":
    print ("Your answer is correct")
else:
    print("Your answer is wrong")

Hungary = str(input("\n8. What is the capital of Hungary? ")) 
if Hungary.lower() == "budapest":
    print ("Your answer is correct")
else:
    print("Your answer is wrong")
    
Iceland = str(input("\n9. What is the capital of Iceland? ")) 
if Iceland.lower() == "reykjavik":
    print ("Your answer is correct")
else:
    print("Your answer is wrong")
    
Ireland = str(input("\n10. What is the capital of Romania? ")) 
if Ireland.lower() == "dublin":
    print ("Your answer is correct")
else:
    print("Your answer is wrong")

Italy = str(input("\n12. What is the capital of Italy? "))
if Italy.lower() == "rome":
    print ("Your answer is correct")
else:
    print("Your answer is wrong")