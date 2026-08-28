import expense_utils

expenses = expense_utils.load_expenses()

while True:
 print("=== Expense Tracker ===")
 print("1. Add Expense"
      "\n2. View Expense"
      "\n3. Calculate Total"
      "\n4. Search by Category"
      "\n5. Exit")

 try:
    user_selection = int(input("Enter your selection: "))
 except ValueError:
    print("Enter a valid input")
    continue

 if user_selection == 1:
    expense_utils.add_expense(expenses)
    print("Expense Added")

 elif user_selection == 2:
    expense_utils.view_expenses(expenses)
    

 elif user_selection == 3:
    total_expense= expense_utils.calculate_total(expenses)
    print(f"Total Expense = ₹{total_expense}")

 elif user_selection == 4:
    expense_utils.search_category(expenses)

 elif user_selection == 5:
    expense_utils.program_exit(expenses)  
    break  

 else:
    print("Enter a Valid Input")


#print(expense_utils.unique_category_expenses(expenses))
   # print(expense_utils.calculate_category_total(expenses))
