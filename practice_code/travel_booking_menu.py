number_of_packages= int(input("How many packages do you want to view?"))

for i in range(number_of_packages):
    print(f"Package {i+1}")

table = int(input("Enter a number for table generation"))

for i in range(1,11):
    print(f"{table}*{i} = {table*i}")

