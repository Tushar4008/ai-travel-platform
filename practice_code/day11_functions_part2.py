def greet(name = "User"):
    print(f"Hello {name}")

greet()
greet("Tushar")

def package_details(destination,days):
    print(f"User selected destination {destination} for {days} days.")

package_details("Thailand",15)
package_details(10,"Japan")

package_details(days=10,destination="Vietnam")

def total_price(*prices):
    total=0
    
    for price in prices:
        total+=price
    
    return total

print(total_price(1000,2000,4000))
print(total_price(1000))
print(total_price(3000,5000))

def customer_details(**details):
    """
    Prints the customer details given when the function is called with different arguments 
    """
    print(details)

customer_details(
                 traveler_name="Tushar",
                 traveler_age=30
                 )

customer_details(
                 destination = "Thailand",
                 duration = 10,
                 total_pax=5,
                 date="01/08/2026"
                 )

cube = lambda x:x*x*x
print(cube(5))

def add_numbers(a:int , b:int) ->int:
    return a+b

print(add_numbers(2,3))