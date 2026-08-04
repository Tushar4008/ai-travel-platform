📘 Sprint 1 – Python Core
📝 Day 12 Notes – Modules & File Handling

Topic: Modules & File Handling

Sprint: Sprint 1 – Python Core

Day: 12

1️⃣ Business Requirement

As Wanderlust Wings grows, keeping all code in one file becomes difficult.

Instead of one large file:

app.py

We split the application into multiple files:

booking.py
payment.py
travel_utils.py
main.py

This makes the application easier to understand, test, and maintain.

Applications also need to store data permanently, such as:

Booking history
Customer details
Reports
Logs

Python provides Modules for organizing code and File Handling for storing data.

2️⃣ Theory
What is a Module?

A Module is a single Python file (.py) that contains reusable code such as functions, variables, or classes.

Example:

# travel_utils.py

def welcome():
    print("Welcome Traveler")

Importing the module:

import travel_utils

travel_utils.welcome()
Importing Modules
Import Entire Module
import math

print(math.sqrt(25))
Import Specific Function
from math import sqrt

print(sqrt(25))
Import Using Alias
import math as m

print(m.pi)

Alias names improve readability when module names are long.

Creating Custom Modules

Example:

travel_utils.py

Contains reusable functions.

Import inside another file:

import travel_utils
Packages

A Package is a folder containing multiple related modules.

Example:

travel/

    booking.py

    payment.py

    invoice.py

Remember

Module = Python File
Package = Folder containing Modules
File Handling

Python allows applications to:

Read files
Write files
Append data
Reading a File
with open("demo.txt") as file:
    print(file.read())
Writing to a File
with open("demo.txt", "w") as file:
    file.write("Hello")

"w" overwrites existing content.

Appending to a File
with open("demo.txt", "a") as file:
    file.write("\nWelcome")

Appends new data without removing existing content.

Context Manager (with)

Instead of:

file = open("demo.txt")

file.read()

file.close()

Use:

with open("demo.txt") as file:
    print(file.read())

Python automatically closes the file.

File Modes
Mode	Purpose
"r"	Read
"w"	Write (Overwrite)
"a"	Append
"x"	Create New File
"rb"	Read Binary
"wb"	Write Binary
☕ 3️⃣ Java Comparison

Java:

import java.util.Scanner;

Python:

import math

Both languages organize reusable code using imports.

⭐ 4️⃣ Important Concepts
Module

A reusable Python file.

Example:

travel_utils.py
Package

A folder containing multiple modules.

Example:

travel/
File Handling

Used to store and retrieve application data.

Context Manager

The with statement automatically closes files after use.

Preferred over manually calling close().

File Modes
"r" → Read
"w" → Overwrite
"a" → Append
✅ 5️⃣ Best Practices

✔ Split code into multiple modules.

✔ Keep one responsibility per module.

✔ Use with while working with files.

✔ Prefer append mode for logs and history.

✔ Use meaningful module names.

✔ Keep reusable functions inside utility modules.

✔ Use relative or pathlib paths instead of hard-coded absolute paths.

❌ 6️⃣ Mistakes I Made Today
Mistake 1

I answered:

Module = Folder

Correct answer:

Module = Python File

Mistake 2

I answered:

close()

automatically closes files.

Correct answer:

with

automatically closes files even if an exception occurs.

Mistake 3

I used absolute file paths:

"/Users/tusharshukla/Documents/..."

A better approach is to use pathlib or relative paths so the program works on different operating systems.

🧩 7️⃣ Common Interview Coding Patterns
Pattern 1 – Utility Module
# travel_utils.py

def calculate_price():

Keeps reusable business logic separate.

Pattern 2 – File Reader
with open("data.txt") as file:
    print(file.read())
Pattern 3 – File Writer
with open("history.txt", "a") as file:
    file.write(data)
Pattern 4 – Reading Unique Data
countries = set()

for line in file:
    countries.add(line.strip())

Combines File Handling with Sets.

🎤 8️⃣ Basic Interview Questions & Answers
Q1. What is a Module?

A Python file (.py) containing reusable code.

Q2. What is a Package?

A folder containing multiple related Python modules.

Q3. Which keyword imports a module?

import

Q4. Why is with preferred over open() and close()?

It automatically closes the file and prevents resource leaks.

Q5. What does "w" mode do?

Creates a new file or overwrites an existing file.

Q6. What does "a" mode do?

Appends new data to the end of the file without deleting existing content.

Q7. Why do we use Modules?

To improve:

Code organization
Reusability
Maintainability
💼 9️⃣ Senior Engineer Interview Questions & Answers
Q1. Why should projects be divided into modules?

Smaller modules are easier to test, maintain, and understand. They also support collaboration among multiple developers.

Q2. Why is pathlib preferred over hard-coded file paths?

pathlib creates platform-independent paths that work on Windows, macOS, and Linux.

Q3. Why is with considered a best practice?

It automatically closes resources and prevents file descriptor leaks, even when exceptions occur.

Q4. When would you choose append mode ("a") over write mode ("w")?

Use append mode for logs, booking history, audit trails, or any data that should be preserved.

Q5. What should be inside a utility module?

Reusable helper functions that are shared across different parts of the application.

⭐ Tech Lead Discussion

Question:

Your application has grown to 30,000 lines of code in one file. What would you do?

Answer:

Split the application into modules based on responsibility (Booking, Payments, Users, Reports, Utilities, etc.). This improves readability, maintainability, testing, and team collaboration.

⚡ 1️⃣0️⃣ One Minute Revision
Module = Python file.
Package = Folder containing modules.
Use import to access modules.
"r" → Read.
"w" → Write/Overwrite.
"a" → Append.
Use with for automatic file closing.
Store reusable logic in utility modules.
Prefer pathlib over hard-coded file paths.
✈️ 1️⃣1️⃣ Wanderlust Wings Connection

Our backend will eventually look like:

backend/

    routes/
    services/
    models/
    utils/
    database/
    config/

main.py

Examples:

booking_service.py
payment_service.py
user_service.py
travel_utils.py

Each file will have a single responsibility.

💻 1️⃣2️⃣ Daily Coding Challenge

Problem:

Create save_destination(destination) to append destinations to a file.

Difficulty:

⭐ Easy

Concepts Covered:

Functions
File Handling
Append Mode
🔁 1️⃣3️⃣ Revision Coding Challenge

Revised Concepts:

Functions
Sets
File Reading
Duplicate Removal
🏁 1️⃣4️⃣ Day Summary

Today I learned:

Modules
Import Statements
Custom Modules
Packages
Reading Files
Writing Files
Appending Files
Context Managers (with)
File Modes
Organizing Python projects
👨‍💼 1️⃣5️⃣ Tech Lead Notes

Today was another major milestone. You moved from writing single-file scripts to organizing applications into reusable modules and working with persistent data through file handling.

One improvement we'll adopt in future lessons is using pathlib instead of absolute file paths. This will make your applications portable across different operating systems and closer to production standards.

By combining Modules, Functions, and File Handling, you're now writing code that resembles the structure of real backend applications.