# Day 14 — Expense Tracker Mini Project & Python Integration

## 🎯 Business Requirement

Build a command-line Expense Tracker application that allows users to:

1. Add an expense
2. View all expenses
3. Calculate total expenses
4. Search expenses by category
5. Save expenses to a file
6. Load previously saved expenses
7. Exit the application safely

This project combines multiple Python concepts learned during Days 1–13.

---

# 🧠 Concepts Used

## 1. Lists

A list is used to store multiple expenses.

Example:

expenses = []

Each expense is added to the list.

Example:

expenses.append(added_expense)

Conceptually:

[
{
"description": "Dinner",
"category": "Food",
"amount": 500
},
{
"description": "Cab",
"category": "Travel",
"amount": 300
}
]

---

## 2. Dictionaries

Each individual expense is stored as a dictionary.

Example:

added_expense = {
"description": description,
"category": category,
"amount": amount
}

A dictionary makes the data easier to understand because each value has a meaningful key.

Example:

expense["category"]

expense["amount"]

---

## 3. Input Validation

User input should not be trusted directly.

For example, the amount must:

* Be an integer
* Be greater than 0

Example logic:

while True:
try:
amount = int(input("Enter the amount: "))

```
    if amount > 0:
        break
    else:
        print("Amount must be greater than 0")

except ValueError:
    print("Invalid amount")
```

The loop continues until the user provides valid input.

---

# 🔁 Why Use `while True`?

The Expense Tracker is a menu-driven application.

The user should be able to perform multiple operations without restarting the program.

Example flow:

Start Application
↓
Show Menu
↓
User Selects Option
↓
Perform Operation
↓
Show Menu Again
↓
Exit Only When User Selects Exit

This can be implemented using:

while True:

The loop is stopped using:

break

---

# 🔄 `continue`

`continue` skips the remaining code in the current iteration and starts the next iteration.

Example:

try:
user_selection = int(input("Enter your selection: "))

except ValueError:
print("Enter a valid input")
continue

If the user enters invalid input, the program displays an error and returns to the menu.

---

# ⚠️ Exception Handling

The Expense Tracker uses exception handling to prevent the application from crashing.

Example:

try:
amount = int(input("Enter the amount: "))

except ValueError:
print("Invalid amount")

Possible exceptions handled:

* `ValueError`
* `FileNotFoundError`

---

# 📁 File Handling

Expenses should remain available even after the program is closed.

Therefore, expenses are saved to a file.

Example format:

Dinner|Food|500
Cab|Travel|300
Movie|Entertainment|700

The `|` character acts as a separator.

---

## Saving Expenses

Each expense dictionary is converted into a line of text.

Conceptually:

{
"description": "Dinner",
"category": "Food",
"amount": 500
}

Becomes:

Dinner|Food|500

All expenses are written to the file.

The save operation should save the complete expense list.

Therefore, a clear function name is:

save_expenses()

---

## Loading Expenses

When the application starts:

1. Open the expenses file.
2. Read the file line by line.
3. Remove unnecessary whitespace.
4. Ignore empty lines.
5. Split each line using `|`.
6. Convert the amount back to an integer.
7. Recreate the expense dictionary.
8. Add the dictionary to the expenses list.

Conceptually:

Text File

Dinner|Food|500

↓

split("|")

↓

["Dinner", "Food", "500"]

↓

{
"description": "Dinner",
"category": "Food",
"amount": 500
}

↓

Add to expenses list

---

# 📦 Predictable Return Types

A function should return a predictable data type whenever possible.

For example:

def load_expenses():

If the file exists:

return saved_expenses

If the file does not exist:

return []

This ensures that the rest of the application can safely work with the result.

Example:

expenses.append(new_expense)

If `load_expenses()` returned `None`, this would cause an error.

Returning an empty list allows the application to start correctly even when there are no previous expenses.

---

# 🔎 Searching Expenses by Category

The application allows the user to search for expenses using a category.

Example:

Food

The program loops through the expenses.

If:

expense["category"] == input_category

The expense is displayed.

A counter can be used to determine whether any matching expense was found.

---

# 🧮 Calculating Total Expenses

The total can be calculated by looping through all expenses.

Example:

total = 0

for expense in expenses:
total += expense["amount"]

This is a linear operation.

Time Complexity:

O(n)

Where:

n = number of expenses

---

# 🗂️ Unique Categories Using a Set

A set can be used to find unique expense categories.

Example:

Food
Travel
Food
Entertainment

A set automatically removes duplicates.

Result:

{
"Food",
"Travel",
"Entertainment"
}

This is useful when only unique values are required.

---

# 🚀 Optimizing Category Totals

Initially, category totals can be calculated using nested loops.

Conceptually:

For every category:
Loop through every expense

This can result in unnecessary repeated work.

A better solution uses a dictionary.

Example thinking:

result = {}

For each expense:

```
Get category
Get amount

If category already exists:
    Add amount

Otherwise:
    Create category with the amount
```

Example result:

{
"Food": 1500,
"Travel": 800,
"Entertainment": 700
}

---

## Optimized Complexity

Using one loop through the expenses:

Time Complexity:

O(n)

Space Complexity:

O(k)

Where:

n = total number of expenses

k = number of unique categories

---

# 🏗️ Separation of Responsibilities

The project separates different responsibilities into functions.

Examples:

add_expense()

Responsible for:

* Collecting expense information
* Validating amount
* Creating an expense dictionary
* Adding it to the expense list

view_expenses()

Responsible for:

* Displaying expenses

calculate_total()

Responsible for:

* Calculating the total amount

search_category()

Responsible for:

* Searching expenses by category

save_expenses()

Responsible for:

* Saving expenses to a file

load_expenses()

Responsible for:

* Loading expenses from a file

program_exit()

Responsible for:

* Saving expenses
* Displaying the exit message

This makes the code easier to understand, test, and maintain.

---

# 🧠 Key Learning

A real application is built by combining multiple small concepts.

This project combines:

Input
↓
Conditions
↓
Loops
↓
Lists
↓
Dictionaries
↓
Sets
↓
Functions
↓
Exception Handling
↓
File Handling

The important learning is not only knowing these concepts individually.

The important skill is knowing how to combine them to build an application.

---

# 🔗 Java Comparison

Python:

expenses = []

Java:

List<Expense> expenses = new ArrayList<>();

Python Dictionary:

{
"category": "Food",
"amount": 500
}

Java equivalent concept:

Map<String, Object>

Python Dictionary lookup:

if category in totals:

Java equivalent concept:

if (totals.containsKey(category))

Python exception handling:

try:
...

except ValueError:
...

Java equivalent concept:

try {
...
} catch (Exception e) {
...
}

---

# 🏆 Day 14 Key Takeaways

* A list can store multiple expense records.
* A dictionary can represent structured data.
* Input should always be validated.
* `while True` can be used for menu-driven applications.
* `break` exits a loop.
* `continue` skips the current iteration.
* Exceptions prevent expected runtime errors from crashing the application.
* Files provide data persistence.
* Functions should have clear responsibilities.
* Functions should return predictable data types.
* A dictionary can be used to optimize repeated aggregation problems.
* One-pass algorithms can reduce time complexity.
* Building projects requires combining multiple concepts together.

---

# 💡 Final Project Architecture

main.py

↓

Controls:

* Application loop
* Menu
* User selection

↓

expense_utils.py

Contains:

* add_expense()
* view_expenses()
* calculate_total()
* search_category()
* unique_categories()
* calculate_category_total()
* save_expenses()
* load_expenses()
* program_exit()

↓

expenses.txt

Stores:

Description | Category | Amount

---

# 🚀 Day 14 Completed

Mini Project:

Expense Tracker CLI Application

Key Achievement:

Built a complete command-line application by integrating Python fundamentals, collections, functions, exception handling, file handling, and algorithm optimization.


# Day 14 — Interview Questions & Answers

## Beginner / Core Questions

### Q1. Why did you use a List to store expenses?

A list is suitable because we need to store multiple expense records and add new expenses dynamically. Lists maintain order and allow modification.

---

### Q2. Why is each expense stored as a Dictionary?

Each expense has multiple related properties:

* Description
* Category
* Amount

A dictionary allows us to access values using meaningful keys.

Example:

expense["category"]

This makes the data more readable than using indexes.

---

### Q3. What is the difference between `break` and `continue`?

`break` completely exits the loop.

`continue` skips the remaining code in the current iteration and starts the next iteration.

In the Expense Tracker:

* `continue` is used after invalid menu input.
* `break` is used when the user selects Exit.

---

### Q4. Why did you use `while True`?

The application is menu-driven and should continue running until the user explicitly chooses to exit.

`while True` keeps the application running, and `break` stops it when the Exit option is selected.

---

### Q5. Why do we use `try-except`?

`try-except` handles expected runtime errors and prevents the program from crashing.

For example:

int("hello")

raises a `ValueError`.

We can handle it and ask the user to enter valid input.

---

### Q6. What happens if `load_expenses()` returns `None`?

If the rest of the application expects a list:

expenses.append(...)

it will fail because `None` does not have an `append()` method.

Therefore, returning an empty list is safer when no saved expenses exist.

---

### Q7. Why should functions return predictable data types?

Predictable return types make the calling code simpler and safer.

For example, if `load_expenses()` always returns a list, the caller does not need to check whether it received:

* A list
* `None`
* Some other type

---

### Q8. What is data persistence?

Data persistence means storing data so that it remains available after the program stops.

In this project, expenses are saved to a text file and loaded again when the application starts.

---

### Q9. Why did you avoid using `eval()` for loading data?

`eval()` executes the provided string as Python code.

If file content is manipulated or contains malicious code, `eval()` can execute that code.

Therefore, using a structured file format and parsing the data is safer.

---

### Q10. What is the difference between `w` and `a` file modes?

`w` writes to a file and overwrites existing content.

`a` appends new content to the end of the existing file.

In this project, writing the complete current expense list uses `w`.

---

# Intermediate Questions

### Q11. What is the time complexity of `calculate_total()`?

The function loops through every expense once.

Therefore:

Time Complexity: O(n)

Space Complexity: O(1)

---

### Q12. What is the time complexity of searching for an expense category?

If we loop through every expense:

Time Complexity: O(n)

In the worst case, we may need to check all expenses.

---

### Q13. How did you optimize category total calculation?

The initial approach could use nested loops.

A better approach uses a dictionary.

For every expense:

1. Check whether the category exists in the dictionary.
2. If it exists, add the amount.
3. Otherwise, create the category.

This processes each expense once.

Average Time Complexity:

O(n)

Space Complexity:

O(k)

Where `k` is the number of unique categories.

---

### Q14. Why is a dictionary useful for aggregation problems?

A dictionary provides efficient average key lookup.

For category totals:

Category → Total Amount

Example:

{
"Food": 1500,
"Travel": 800
}

This allows us to update the total directly instead of repeatedly searching through categories.

---

### Q15. Why is separation of responsibilities important?

Each function should ideally focus on one responsibility.

For example:

* `add_expense()` adds an expense.
* `save_expenses()` saves expenses.
* `load_expenses()` loads expenses.

This improves:

* Readability
* Maintainability
* Testability
* Debugging

---

# Senior Engineer / Discussion Questions

### Q16. How would you improve this project for production?

Possible improvements include:

1. Use classes or dataclasses for expense models.
2. Use JSON or a database instead of a custom text format.
3. Add logging.
4. Add automated tests.
5. Separate UI, business logic, and data access layers.
6. Add validation functions.
7. Add custom exceptions where appropriate.
8. Add type hints consistently.

---

### Q17. Why would JSON be better than a custom `|`-separated format?

JSON provides a structured representation of data.

Example:

[
{
"description": "Dinner",
"category": "Food",
"amount": 500
}
]

It is easier to extend and works naturally with dictionaries and APIs.

---

### Q18. How would you test `calculate_category_total()`?

I would create a fixed list of expenses and verify the returned dictionary.

Example test scenario:

Input:

Food → 500
Food → 300
Travel → 1000

Expected output:

{
"Food": 800,
"Travel": 1000
}

I would also test:

* Empty expense list
* One expense
* Multiple categories
* Repeated categories

---

### Q19. What happens if the application grows significantly?

A single `expense_utils.py` module may become difficult to maintain.

We could separate the application into modules such as:

models/
expense.py

services/
expense_service.py

repositories/
expense_repository.py

ui/
menu.py

main.py

This improves separation of concerns.

---

### Q20. How does this project relate to backend development?

The application already has a basic layered flow:

User Input
↓
Business Logic
↓
Data Processing
↓
Persistence Layer

Later, the CLI can be replaced by:

REST API

The business logic can remain similar.

The persistence layer can change from:

Text File

to:

Database

This is a simplified version of how backend applications are structured.

---

# 🧩 Coding Problem Discussion

### Q21. Why is the optimized category total solution better than the nested-loop solution?

The nested-loop solution repeatedly scans the expense list.

The optimized solution processes each expense once and stores totals in a dictionary.

This reduces unnecessary repeated work.

Nested approach:

Potentially O(n²)

Optimized approach:

O(n)

---

### Q22. When would you choose a Set in this project?

A set is useful when only unique categories are required.

Example:

{
"Food",
"Travel",
"Entertainment"
}

It also provides efficient average membership checking.

---

### Q23. How would you prevent duplicate expenses?

The answer depends on the business definition of a duplicate.

We could compare fields such as:

* Description
* Category
* Amount
* Date

We could create a unique identifier or compare a combination of these values before adding a new expense.

---

### Q24. How would you handle corrupted data in the file?

The loading logic should validate each line before processing it.

Possible checks:

* Ensure the expected number of fields exists.
* Validate that amount is numeric.
* Skip or report malformed records.
* Log the problematic data.

A production application should avoid crashing because of one bad record.

---

# 🏆 Day 14 Interview Takeaway

The most important discussion point from Day 14 is:

"I started with a nested-loop solution for category aggregation, then optimized it using a dictionary so each expense is processed once, reducing the time complexity to O(n)."

This demonstrates:

* Problem-solving
* Data structure selection
* Complexity awareness
* Code optimization

