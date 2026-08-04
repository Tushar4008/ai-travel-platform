file = open("/Users/tusharshukla/Documents/WanderlustWingss/docs/demo.txt")
print(file.read())
file.close()

with open("/Users/tusharshukla/Documents/WanderlustWingss/docs/demo.txt") as file:
    print(file.read())

with open("/Users/tusharshukla/Documents/WanderlustWingss/docs/demo.txt","w") as file:
    file.write("Hello Tushar")

with open("/Users/tusharshukla/Documents/WanderlustWingss/docs/demo.txt","a") as file:
    file.write("\nWelcome Engineer")

with open("/Users/tusharshukla/Documents/WanderlustWingss/docs/demo.txt") as file:
    print(file.read())


with open("/Users/tusharshukla/Documents/WanderlustWingss/docs/booking_history.txt","a") as file:
    file.write("\n\nBooking 2\n\nJapan\n\n65000")

with open("/Users/tusharshukla/Documents/WanderlustWingss/docs/booking_history.txt") as file:
    print(file.read())



