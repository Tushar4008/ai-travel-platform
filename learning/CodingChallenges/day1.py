""" Problem

Check whether a number is

Positive
Negative
Zero

Example

Input

10

Output

Positive """

input_number = int(input("Enter a number- "))

if input_number == 0:
    print("Zero")
elif input_number >0:
    print("Positive")
else:
    print("Negative")    