""" Create a program that:

Takes the user's name.
Removes extra spaces.
Converts it to Title Case.
Prints:
Hello Tushar!

if the name starts with T.

Otherwise print

Welcome Traveler! """

name = input("Enter your name- ").strip().title()

if name[0]== 'T':
    print("Hello Tushar!")
else:
    print("Welcome Traveler!")





