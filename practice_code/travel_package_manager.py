packages = [
    "Thailand",
    "Bali",
    "Goa"
]

for package in packages:
    print(package)

packages.append("Dubai")

packages.insert(2,"Japan")

packages.remove("Goa")

print(packages)

print(f"Total packages: {len(packages)}")

user_selected_package = input("Which package are you searching?")

if user_selected_package in packages:
    print("Package Available")
else:
    print("Package Not Available")