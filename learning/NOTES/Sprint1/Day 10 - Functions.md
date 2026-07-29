📘 Sprint 1 – Python Core
📝 Day 10 Notes – Functions (Part 1)

Topic: Python Functions

Sprint: Sprint 1 – Python Core

Day: 10

1️⃣ Business Requirement

While building Wanderlust Wings, many features need to perform repeated tasks such as:

Searching travel packages
Calculating trip prices
Applying discounts
Booking trips
Generating invoices

Writing the same code repeatedly makes applications difficult to maintain.

Instead, we create Functions that can be reused whenever needed.

Example:

def search_package(destination):
    print(f"Searching packages for {destination}")

Now we can call it multiple times:

search_package("Thailand")
search_package("Japan")
search_package("Dubai")

This avoids duplicate code and keeps applications organized.

2️⃣ Theory
What is a Function?

A Function is a reusable block of code designed to perform a specific task.

Instead of writing the same code multiple times, we define it once and call it whenever required.

Syntax
def function_name():
    # Function body

Example:

def welcome():
    print("Welcome to Wanderlust Wings")

Calling the function:

welcome()

Output:

Welcome to Wanderlust Wings
Function with Parameters

A parameter is a variable that receives data.

def greet(name):
    print(f"Hello {name}")

Calling:

greet("Tushar")

Output:

Hello Tushar
Multiple Parameters
def package_details(destination, days):
    print(f"{destination} package for {days} days")

Calling:

package_details("Thailand", 5)

Output:

Thailand package for 5 days
Return Statement

Functions can send a value back using return.

def add_numbers(a, b):
    return a + b

Usage:

result = add_numbers(10, 20)

print(result)

Output:

30
Local Variables

Variables declared inside a function.

def demo():
    x = 10

x can only be accessed inside demo().

Global Variables

Variables declared outside functions.

name = "Tushar"

def greet():
    print(name)

The function can access the global variable.

Variable Scope
Variable Type	Accessible Where?
Local	Inside the function only
Global	Entire program
☕ 3️⃣ Java Comparison

Python

def calculate_price(price, discount):
    return price - discount

Java

public static int calculatePrice(int price, int discount){
    return price - discount;
}

Both follow the same idea:

Define once
Call many times
Return a result
⭐ 4️⃣ Important Concepts
Parameter vs Argument
Parameter

Variable declared in the function definition.

def greet(name):

name is the Parameter.

Argument

Actual value passed to the function.

greet("Shaurya")

"Shaurya" is the Argument.

print() vs return
print()

Displays output only.

def add(a, b):
    print(a + b)

Cannot reuse the result.

return

Returns the value.

def add(a, b):
    return a + b

Can be stored, reused, or passed to another function.

Function Call

Defining:

def welcome():
    print("Welcome")

Calling:

welcome()

Without () the function is not executed.

✅ 5️⃣ Best Practices

✔ Give functions meaningful names.

Good:

calculate_price()

Bad:

fun1()

✔ Keep functions focused on one responsibility.

Example:

calculate_price()

Should only calculate the price.

✔ Prefer return over print() when another part of the application needs the result.

✔ Pass values as parameters instead of relying heavily on global variables.

✔ Follow the DRY Principle (Don't Repeat Yourself).

❌ 6️⃣ Mistakes I Made Today
Mistake 1

I confused Parameter with Argument during the quiz.

Remember:

def greet(name):

name → Parameter

greet("Shaurya")

"Shaurya" → Argument

Mistake 2

I wrote:

print(local_variable)

This prints the function object.

Correct:

print(local_variable())

The parentheses execute the function.

🧩 7️⃣ Common Interview Coding Patterns
Pattern 1 – Utility Function
def add_numbers(a, b):
    return a + b

Used for reusable calculations.

Pattern 2 – Validation Function
def check_destination(destination):
    return destination in available

Used in:

Login validation
Email validation
Product availability
Pattern 3 – Business Logic Function
def calculate_discount(price, discount):
    return price - discount

Keeps business logic separate from user interaction.

Pattern 4 – Formatting Function
def package_details(destination, days):
    return f"{destination} package for {days} days"

Used to prepare user-friendly messages.

🎤 8️⃣ Basic Interview Questions & Answers
Q1. What is a Function?

A reusable block of code that performs a specific task.

Q2. Which keyword defines a Function?

def

Q3. What is a Parameter?

A variable declared in the function definition.

Q4. What is an Argument?

The actual value passed to a function when it is called.

Q5. What is the difference between print() and return?

print() displays a value.

return sends a value back to the caller for further use.

Q6. What is a Local Variable?

A variable accessible only inside the function where it is defined.

Q7. What is a Global Variable?

A variable defined outside functions that can be accessed throughout the program.

Q8. Why do we use Functions?
Code Reusability
Better Readability
Easier Maintenance
Reduced Duplication
Easier Testing
💼 9️⃣ Senior Engineer Interview Questions & Answers
Q1. What is the DRY Principle?

DRY (Don't Repeat Yourself) means avoiding duplicate code by extracting common logic into reusable functions.

Q2. Why is return preferred over print()?

return makes functions reusable because the returned value can be:

Stored
Modified
Sent to another function
Returned from an API

print() only displays information.

Q3. What is Single Responsibility Principle (SRP)?

Each function should perform one task only.

Example:

calculate_price()

should only calculate the price.

Q4. Why should global variables be minimized?

Too many global variables make programs harder to debug and maintain because any part of the program can modify them.

Passing values as parameters is usually a better approach.

Q5. How do Functions improve testing?

Small functions can be tested independently, making bugs easier to locate and fix.

⭐ Tech Lead Discussion

Question:

You notice the same pricing logic repeated in five different modules of an application. What would you do?

Answer:

Extract the pricing logic into a single reusable function, such as calculate_price(). This follows the DRY principle, reduces maintenance effort, and ensures future changes only need to be made in one place.

⚡ 1️⃣0️⃣ One Minute Revision
Functions are reusable blocks of code.
Use def to define a function.
Call a function using ().
Parameters receive values.
Arguments are the actual values passed.
return sends values back to the caller.
print() only displays output.
Local variables exist only inside the function.
Global variables exist outside functions.
Functions support clean, reusable, and maintainable code.
✈️ 1️⃣1️⃣ Wanderlust Wings Connection

Functions will form the foundation of every module in our AI Travel Platform.

Examples:

def search_packages():
    pass

def calculate_price():
    pass

def apply_coupon():
    pass

def book_trip():
    pass

def generate_invoice():
    pass

Each function has a single responsibility, making the application easier to maintain, test, and extend.

💻 1️⃣2️⃣ Daily Coding Challenge

Problem:

Create a function find_larger(a, b) that returns the larger number.

Difficulty:

⭐ Easy

Concepts Covered:

Functions
Parameters
Return
Conditional Statements
🔁 1️⃣3️⃣ Revision Coding Challenge

Revised Concepts:

Functions
Sets
Membership Operator (in)
Return Values
🏁 1️⃣4️⃣ Day Summary

Today I learned:

What Functions are and why they are important.
How to define and call Functions.
The difference between Parameters and Arguments.
The importance of the return statement.
The difference between print() and return.
Local vs Global Variables.
The DRY principle.
How Functions improve code organization and maintainability.
Real-world uses of Functions in backend development and AI applications.
👨‍💼 1️⃣5️⃣ Tech Lead Notes

This lesson marks an important transition in your programming journey. Up to now, you were writing sequential scripts. From this point forward, you'll begin structuring programs into small, reusable functions—the same approach used in production systems.

One concept to keep reinforcing is the distinction between parameters (defined in the function) and arguments (passed during the function call). Also remember that calling a function requires parentheses (), while referencing a function without () only refers to the function object.

With Lists, Tuples, Dictionaries, Sets, and now Functions, you have built a strong Python foundation. The next lessons will focus on combining these concepts into larger, modular programs that closely resemble real-world software and prepare you for building the backend of Wanderlust Wings.