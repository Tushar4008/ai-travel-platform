def add_expense(expenses):
    description = input("Enter the description: ").strip().title()
    category = input ("Enter the category: ").strip().title()
    while True:
     try:
        amount = int(input ("Enter the amount: "))
        if amount > 0:
            break
        else:
            print("Amount can't be less than 0")
     except ValueError:
            print("Invalid Amount, the amount should be an Integer and greater than 0")

    added_expense={"description":description,
                   "category":category,
                   "amount":amount}

    expenses.append(added_expense)

def view_expenses(expenses):
 if expenses:
    for expense in expenses:
        print(*expense.values(), sep=' | ')
 else:
     print("No expenses added please add a new one")


def calculate_total(expenses):
     total=0   
     for expense in expenses:
         total+=expense.get("amount")
     return total 

def search_category(expenses):
     input_category=input("Enter the category: ").strip().title()
     count=0
     for expense in expenses:
          if expense["category"] == input_category:
                print(*expense.values(), sep=' | ')
                count+=1
     if count==0:
        print("Category not present")

def program_exit(expenses):
    save_expense(expenses)
    print("GoodBye! See you again!")

def load_expenses():
    saved_expenses=[]
    try:
        with open("/Users/tusharshukla/Documents/WanderlustWingss/learning/Expense_Tracker/expenses.txt",'r') as file:
            for line in file:
                 line=line.strip()
                 if line:
                    description,category,amount=line.split("|")
                    saved_expenses.append({'description':description,'category':category,'amount':int(amount)})
        return saved_expenses            
    except FileNotFoundError:
            print("No previous expenses found. Starting a new expense tracker.")
            return saved_expenses

def unique_category_expenses(expenses):
     unique_catagory=set()   
     for expense in expenses:
          unique_catagory.add(expense.get("category"))
     return unique_catagory

def calculate_category_total(expenses):
    unique_category_total={}
    for expense in expenses:
        if expense['category'] in unique_category_total:
            unique_category_total[expense['category']]=int(expense['amount'])+int(unique_category_total[expense['category']])
        else:
            unique_category_total[expense['category']]=int(expense['amount'])

    return unique_category_total

    #  unique_category_total={}
    #  unique_category=unique_category_expenses(expenses)
    #  for category in unique_category:
    #       total=0
    #       for expense in expenses:
    #            if expense["category"] == category:
    #                 total+=expense.get("amount")
    #       unique_category_total[category]=total 
    #  return unique_category_total

def save_expense(expenses):
    try:
        with open("/Users/tusharshukla/Documents/WanderlustWingss/learning/Expense_Tracker/expenses.txt",'w') as file:
            for item in expenses:
                line = f"{item["description"]}|{item["category"]}|{item["amount"]}\n"
                file.write(line)
    except FileNotFoundError:
            print("File doesn't exist")
    
          