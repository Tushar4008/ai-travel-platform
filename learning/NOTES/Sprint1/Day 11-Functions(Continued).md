📘 Sprint 1 – Python Core
📝 Day 11 Notes – Functions (Part 2)

Topic: Advanced Functions

Sprint: Sprint 1 – Python Core

Day: 11

1️⃣ Business Requirement

While building Wanderlust Wings, different customers provide different booking details.

Some provide:

Destination only
Destination + Days
Destination + Hotel
Destination + Hotel + Activities
Destination + Hotel + Flight + Insurance

Instead of creating multiple functions, Python allows us to write flexible functions using default parameters, *args, and **kwargs.

2️⃣ Theory
Default Parameters

A parameter can have a default value.

def greet(name="Guest"):
    print(f"Hello {name}")

Calling:

greet()

Output:

Hello Guest

Calling:

greet("Tushar")

Output:

Hello Tushar
Positional Arguments

Python matches values based on their position.

def package(destination, days):
    print(destination, days)
package("Thailand", 5)

Output:

Thailand 5

Order matters.

Keyword Arguments

Arguments are passed using parameter names.

package(days=5, destination="Thailand")

Output:

Thailand 5

Keyword arguments improve readability.

*args

Allows a function to receive multiple positional arguments.

def total_price(*prices):
    return sum(prices)

Inside the function, prices is stored as a Tuple.

**kwargs

Allows a function to receive multiple keyword arguments.

def customer_details(**details):
    print(details)

Calling:

customer_details(name="Tushar", city="Lucknow")

Inside the function, details is stored as a Dictionary.

Lambda Functions

Anonymous one-line functions.

Normal Function:

def square(x):
    return x * x

Lambda:

square = lambda x: x * x

Used for short operations.

Type Hints

Type hints make code easier to understand.

def add(a: int, b: int) -> int:
    return a + b

Benefits:

Better IDE support
Improved readability
Easier maintenance
Docstrings

Docstrings describe what a function does.

def add(a: int, b: int) -> int:
    """
    Returns the sum of two integers.
    """
    return a + b

Professionals add docstrings to public functions.

☕ 3️⃣ Java Comparison

Python:

def calculate_total(*prices):

Java equivalent would require method overloading or collections because Java does not support **kwargs like Python.

Python provides much more flexibility when designing APIs.

⭐ 4️⃣ Important Concepts
Parameter vs Argument

Parameter:

def greet(name):

name is the parameter.

Argument:

greet("Tushar")

"Tushar" is the argument.

*args
Accepts multiple positional arguments
Stored as a Tuple

Example:

def demo(*args):
**kwargs
Accepts multiple keyword arguments
Stored as a Dictionary

Example:

def demo(**kwargs):
Type Hints

Improve readability without affecting program execution.

Docstrings

Used for documentation and can be accessed using:

help(function_name)
✅ 5️⃣ Best Practices

✔ Use keyword arguments when a function has many parameters.

✔ Add type hints to improve readability.

✔ Write meaningful docstrings.

✔ Use *args only when the number of arguments is unknown.

✔ Use **kwargs for optional named information.

✔ Keep lambda functions short and simple.

✔ Continue following the DRY (Don't Repeat Yourself) principle.

❌ 6️⃣ Mistakes I Made Today
Mistake 1

I selected:

** 

for accepting multiple positional arguments.

Correct answer:

*

Remember:

*args  → Tuple
**kwargs → Dictionary
Mistake 2

I passed positional arguments in the wrong order:

package_details(10, "Japan")

Although valid, the output was incorrect because Python matches arguments by position.

A better approach:

package_details(destination="Japan", days=10)
🧩 7️⃣ Common Interview Coding Patterns
Pattern 1 – Flexible Function
def calculate_total(*prices):

Used when the number of values is unknown.

Pattern 2 – Configuration Function
def customer_details(**details):

Useful for configuration objects and API payloads.

Pattern 3 – Utility Lambda
square = lambda x: x * x

Used with:

map()
filter()
sorted()
Pattern 4 – Documented Function
def add(a: int, b: int) -> int:

Professional Python code combines:

Type hints
Docstrings
Return values
🎤 8️⃣ Basic Interview Questions & Answers
Q1. What is a default parameter?

A parameter with a predefined value that is used when no argument is provided.

Q2. What is the difference between positional and keyword arguments?

Positional arguments depend on order.

Keyword arguments use parameter names and improve readability.

Q3. What is *args?

Allows a function to accept multiple positional arguments.

Stored as a Tuple.

Q4. What is **kwargs?

Allows a function to accept multiple keyword arguments.

Stored as a Dictionary.

Q5. What is a Lambda function?

A small anonymous function written in one line.

Q6. What are Type Hints?

They specify expected parameter and return types to improve readability and IDE support.

Q7. What is a Docstring?

Documentation written inside a function to explain its purpose, parameters, and return value.

💼 9️⃣ Senior Engineer Interview Questions & Answers
Q1. When should you use *args?

When the number of positional arguments is unknown in advance.

Q2. When should you use **kwargs?

When optional named arguments may vary between function calls.

Q3. Why are keyword arguments preferred in production code?

They make function calls self-documenting and reduce mistakes caused by incorrect argument order.

Q4. Why are Type Hints important?

They improve code readability, IDE suggestions, static analysis, and long-term maintainability.

Q5. Should Lambda functions replace all normal functions?

No.

Use Lambda only for small, simple operations. Complex business logic should use normal functions with descriptive names.

⭐ Tech Lead Discussion

Question:

Your booking API receives different optional fields depending on the customer. Which function feature would you use?

Answer:

I would use **kwargs because it allows the function to accept varying keyword arguments without changing the function signature, making the API more flexible and scalable.

⚡ 1️⃣0️⃣ One Minute Revision
Default parameters provide fallback values.
Positional arguments depend on order.
Keyword arguments improve readability.
*args → Multiple positional arguments (Tuple).
**kwargs → Multiple keyword arguments (Dictionary).
Lambda functions are anonymous one-line functions.
Type hints improve readability.
Docstrings document functions.
Use keyword arguments and type hints in production code.
✈️ 1️⃣1️⃣ Wanderlust Wings Connection

Functions in our AI Travel Platform will use these concepts extensively:

def create_booking(
    destination: str,
    travelers: int = 2,
    **booking_details
):
    """Create a booking with optional travel details."""
    pass

This approach keeps the application flexible as new booking options are introduced.

💻 1️⃣2️⃣ Daily Coding Challenge

Problem:

Create find_max(*numbers) without using max().

Difficulty:

⭐ Easy

Concepts Covered:

*args
Loops
Conditional Logic
Return Values
🔁 1️⃣3️⃣ Revision Coding Challenge

Revised Concepts:

*args
Sets
Duplicate Removal
Return Values
🏁 1️⃣4️⃣ Day Summary

Today I learned:

Default Parameters
Positional vs Keyword Arguments
*args
**kwargs
Lambda Functions
Type Hints
Docstrings
Writing flexible and reusable functions
Professional Python coding practices
👨‍💼 1️⃣5️⃣ Tech Lead Notes

Today you moved beyond writing simple functions and started designing flexible APIs. Features like keyword arguments, *args, **kwargs, type hints, and docstrings are common in production Python code and modern frameworks such as Flask and FastAPI.

The biggest point to remember is the distinction between:

*args → Tuple → Variable positional arguments.
**kwargs → Dictionary → Variable keyword arguments.

You're now ready to start organizing larger applications into multiple files and modules.