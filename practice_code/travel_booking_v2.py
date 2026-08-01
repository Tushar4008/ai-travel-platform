def greet(name="Guest"):
    print(f"Hello {name}")

def calculate_total(*prices):
    total = 0

    for price in prices:
        total+=price
    
    return total

def customer_details(**details):
    print(details)

square = lambda x:x*x
print(square(4))

def add(a:int,b:int)->int:
    """
    Returns sum of 2 given integers
    """
    return a+b

def find_max(*numbers):
    max_number = numbers[0]

    for number in numbers:
        if max_number<number:
            max_number=number

    return max_number    

print(f"Max number is: {find_max(5,1,3,7,8,4,9,0,2,11,8)}")

def available_packages(*packages):
    unique_destinations=set(packages)
    return unique_destinations

print(available_packages("Thailand","Japan","India","Dubai","Japan","Vietnam"))