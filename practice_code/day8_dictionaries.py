package = {
    "country":"Thailand",
    "city":"Bangkok",
    "price":55000,
    "days":5
}

package["price"]= 60000     #update value

print(package.items())

package.pop("days")         #delete based on key
del package["price"]        #one more way to delete

print(package.items())

package["price"] = 70000

print(package.items())

print(package.get("city"))

print(package.keys())

print(package.values())

for key,value in package.items():
    print(key,value)



