""" Create a list

cities = [
    "Delhi",
    "Goa",
    "Mumbai"
]

Print

Welcome to Delhi
Welcome to Goa
Welcome to Mumbai

using a loop.

Then ask user

Enter your favourite city

If present

Great Choice!

Else

Let's add it soon! """

cities = [
    "Delhi",
    "Goa",
    "Mumbai"
]

for city in cities:
    print(f"Welcome to {city}")

favourite_city=input("Enter your favourite city:")

if favourite_city in cities:
    print("Great Choice")
else:
    print("Let's add it soon!")