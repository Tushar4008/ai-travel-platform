def safe_division(a,b):
    try:    
        if b==0:
            raise ZeroDivisionError
        else:
            return a/b
    except ZeroDivisionError:
        return f"Cannot divide by zero"

print(safe_division(4,0))

def load_packages():
    try:
        countries=set()
        with open("/Users/tusharshukla/Documents/WanderlustWingss/docs/packages.txt") as file: 
                for line in file:
                    countries.add(line.strip())
        return countries
    except FileNotFoundError:
        print("The file doesn't exist")
        return countries 

print(load_packages())

