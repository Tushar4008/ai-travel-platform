package_price = 5000
budget=10000
available_seats=20
passport_available=True
destination='Thailand'

print("=== Arithmetic ===")
print(package_price + 5000)  # 10000
print(package_price - 5000)  #5000
print(package_price * 2)    #10000
print(package_price / 2)    #2500.0
print(package_price // 3)   #1666
print(package_price % 3)    #2


print("\n=== Comparison ===")
print(budget >= package_price)  # True
print(package_price == 25000)   #False
print(available_seats > 0)      # True

print("\n=== Logical ===")
print(budget >= package_price and passport_available)   # True
print(budget >= 50000 or passport_available)            #False  
print(not passport_available)                            # False

print("\n=== Membership ===")
print("Thai" in destination)    #True
print("India" in destination)   #False

print("\n=== Assignment ===")
budget += 5000  
print(budget)       #15000

