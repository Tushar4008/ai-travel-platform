try:
    age=int(input("Enter your age "))

except ValueError:
    print("Enter the correct age in integer format")

else: 
    print(f"User age is {age}")

try:
    result = 10/0

except ZeroDivisionError:
    print("Calculation is undefined")

else:
    print(result)


try:
    numbers=[10,20,30]
    last_number = numbers[4]

except IndexError:
    print("Index error check your code again")

else:
    print(last_number)

try: 
    with open("/Users/tusharshukla/Documents/WanderlustWingss/docs/demo2.txt") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found")

finally:
    print("Closing resources")


