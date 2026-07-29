available_packages = {
    "Thailand",
    "Japan",
    "Dubai",
    "Singapore"
}

input_destination = input("Enter your destination: ").strip().title()

if input_destination in available_packages:
    print("Package Available")
else:
    print("Package not Available")

