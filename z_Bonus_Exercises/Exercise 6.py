'''Dictionaries:
Use a dictionary to store information about a person you know.Store their first name,
last name, age, and the city in which they live.

You should have keys such as first_name, last_name, age, and city. Print each piece of
information stored in your dictionary.
'''
Vicfirth = {"first_name":"Vicfirth",
            "last_name":"Garcia",
            "age":"19",
            "city":"Sharjah"}

Dawna = {"first_name":"Dawna",
         "last_name":"Pinzon",
         "age":"19",
         "city":"Dubai"}

Miguel = {"first_name":"Miguel",
          "last_name":"Joaquin",
          "age":"22",
          "city":"Dubai"}

for key, value in Vicfirth.items():
    print(key,':', value)
for key, value in Vicfirth.items():
    print(key,':', value)
for key, value in Dawna.items():
    print(key,':', value)
for key, value in Miguel.items():
    print(key,':', value)

print("First Name:", Vicfirth["first_name"])
print("Last Name:", Vicfirth["last_name"])
print("Age:", Vicfirth["age"])
print("City:", Vicfirth["city"])
print("First Name:", Dawna["first_name"])
print("Last Name:", Dawna["last_name"])
print("Age:", Dawna["age"])
print("City:", Dawna["city"])
print("First Name:", Miguel["first_name"])
print("Last Name:", Miguel["last_name"])
print("Age:", Miguel["age"])
print("City:", Miguel["city"])