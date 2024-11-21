## Exercise 9: Hello - 10 Marks
'''
Fill in the blanks in the code below so that the function hello() prints "Hello" to the console.
python

def hello():
    ____  # Fill in this blank to print "Hello" to the console

def main():
    ____  # Fill in this blank to call the hello() function

if __name__ == "__main__":
    main()
'''

def hello(): #function for hello
    print("Hello") #now every time we put hello() it will print Hello
    
def main(): #fuction for hello
    hello() #since we already have this fuction it will print Hello
    
if hello() == main(): #if hello() is equal to main()
    main() #it will print main() which is also Hello