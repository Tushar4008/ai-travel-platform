package = {
    "country":"Thailand",
    "city":"Bangkok",
    "price":55000,
    "days":5
}

for key,value in package.items():
    print(key,value)

package["price"]= 60000

package["hotel"] = "Mercure"

package.pop("days")

print(package.keys())

print(package.values())

print(package.items())

input_value = input("Which detail do you want to see?").strip().lower()

print(package.get(input_value))