""" Create a program that:

Takes the user's name.
Takes age.
Repeats the message:
Hello <name>

age number of times.

If age is below 18, print:

Minor Traveler

instead. """

user_name= input("Enter your name: ")
user_age = int(input("Enter your age: "))

if user_age<18:
        print("Minor Traveler")
 
else:
    for i in range(1,user_age+1):
          print(f"Hello {user_name}")
    