I'm continuing my AI Full Stack Journey.

Current Sprint: Sprint 2 – Python Pro
Current Day: Day 10

Attached:
- learning/ROADMAP.md
- learning/LEARNING_LOG.md

Let's continue from where we left off.

# 📚 Learning Log

## Day 1 | 16 Jul 2026

### Sprint
Sprint 0 – Foundation

### Completed
- Created GitHub repository
- Configured Git & GitHub
- Fixed remote repository issue
- Created project structure
- Prepared learning roadmap

### Learnings
- Git basics
- Repository structure
- Long-term project planning

### Challenges
- Repository not found
- Wrong Git remote
- Accidentally initialized Git in Documents

### Next
Sprint 1 – Python Core
Day 1 – Python Fundamentals

### Completed

- Learned Python basics
- Understood Variables
- Learned Dynamic Typing
- Learned Python Data Types
- Learned Type Conversion
- Practiced f-strings
- Completed coding exercises
- Completed assignment
- Completed quiz
- Senior code review completed

### Learnings

- Python uses Dynamic Typing.
- Variables don't require explicit type declaration.
- Strings are enclosed in quotes.
- `type()` is used to determine variable type.
- `+` concatenates strings.
- `*` repeats strings.
- Follow `snake_case` naming convention.

### Mistakes Corrected

- Mistook `"10"` for an integer instead of a string.
- Expected `"5" * 3` to perform multiplication instead of string repetition.
- Expected `"30" + "5"` to include spaces instead of concatenating directly.

Day 2 – Operators & Expressions

### Completed

- Learned Arithmetic Operators
- Learned Comparison Operators
- Learned Logical Operators
- Learned Assignment Operators
- Learned Membership Operators
- Learned Identity Operators
- Learned Operator Precedence
- Completed Hands-on Coding
- Built Booking Eligibility Program
- Completed Assignment
- Completed Quiz
- Senior Code Review Completed

### Learnings

- `/` always returns a float.
- `//` performs floor division.
- `%` returns the remainder.
- `**` is used for exponentiation.
- `==` compares values.
- `is` compares object identity.
- `and`, `or`, and `not` are used to combine or negate conditions.
- Operators are the foundation of decision-making in software.

### Mistakes Corrected

- Stored numeric values (`budget`, `package_price`) as strings instead of integers.
- Used `passport_available == True` instead of simply `passport_available`.
- Used `age > 18` instead of `age >= 18` for the business requirement.
- Incorrectly commented the output of `False or True`.
- Incorrectly commented the result of `5000 - 5000`.

### Sprint

Sprint 1 – Python Core

### Lesson

Day 3 – User Input & Strings

### Completed

- Learned the `input()` function
- Understood that `input()` always returns a string
- Practiced type conversion using `int()`
- Learned string indexing
- Learned string slicing
- Learned common string methods
- Built an interactive Traveler Details program
- Built a Travel Profile application
- Completed assignment
- Completed quiz
- Senior code review completed

### Learnings

- `input()` always returns a string.
- User input should be converted to the required data type.
- Strings support indexing and slicing.
- `strip()` removes leading and trailing spaces.
- `title()` formats names and destinations.
- `lower()` helps perform case-insensitive comparisons.
- `startswith()` and `endswith()` are useful for string validation.
- Interactive programs collect input from users instead of relying on hardcoded values.

### Mistakes Corrected

- Used `favorite_Destination` instead of `favorite_destination` (snake_case).
- Printed values without descriptive labels.
- Repeated `strip()` calls for multiple variables instead of recognizing opportunities for future refactoring.

## Day 5 | 20 Jul 2026

### Sprint

Sprint 1 – Python Core

### Lesson

Day 4 – Control Statements (if, elif, else)

### Completed

- Learned `if` statements
- Learned `if-else`
- Learned `if-elif-else`
- Learned Nested `if`
- Understood Python indentation
- Built Travel Package Eligibility program
- Built Travel Package Recommender
- Completed Daily Coding Challenge
- Completed Revision Coding Challenge
- Completed Quiz
- Senior Code Review Completed
- Tech Lead Review Completed
- Refactored assignment after code review

### Learnings

- `if` executes code only when a condition is `True`.
- `elif` is used when checking multiple mutually exclusive conditions.
- `else` handles the remaining case.
- Nested `if` is useful when one decision depends on another.
- Proper indentation is mandatory in Python.
- Business requirements should be translated into a logical decision flow.
- Initializing variables before conditional blocks improves code reliability.

### Mistakes Corrected

- Replaced multiple independent `if` statements with `if-elif-else`.
- Replaced `traveler_age > 17` with `traveler_age >= 18`.
- Initialized `booking_status` and `recommended_package` before using them.
- Corrected the quiz answer for the `if-elif-else` execution flow.
- Improved code readability by restructuring business logic.

### Daily Coding Challenge

**Problem:** Check whether a number is Positive, Negative or Zero.

**Difficulty:** ⭐ Easy

**Pattern:** Decision Making

**Time Complexity:** O(1)

**Space Complexity:** O(1)

### Revision Coding Challenge

Revised concepts from:

- User Input
- String Methods
- `startswith()`
- `strip()`
- `title()`
- `if` Statements

Day 5 – Loops (`for` & `while`)

---

## Completed

- Learned `for` loops
- Learned `while` loops
- Learned `range()`
- Learned nested loops
- Understood infinite loops
- Printed multiplication tables
- Built Travel Package Viewer
- Solved FizzBuzz
- Completed Daily Coding Challenge
- Completed Revision Coding Challenge
- Completed Refactoring Challenge
- Completed Quiz
- Senior Code Review Completed
- Tech Lead Review Completed

---

## Learnings

- `for` loops are used when the number of iterations is known.
- `while` loops are used when repetition depends on a condition.
- `range(start, stop, step)` controls loop execution.
- Strings are iterable.
- Nested loops allow multi-level iteration.
- Infinite loops occur when loop conditions never become false.
- Every loop should be analyzed for efficiency.

---

## Mistakes Corrected

- Learned that `range()` excludes the stop value.
- Improved variable naming for readability.
- Learned the importance of checking combined conditions first in FizzBuzz.
- Improved output formatting for better readability.
- Understood that not every algorithm can be further optimized.

---

## Daily Coding Challenge

### Problem

FizzBuzz

### Difficulty

⭐ Easy

### Pattern

Iteration + Conditional Logic

### Time Complexity

O(n)

### Space Complexity

O(1)

### Optimization

Already optimal because every number must be processed once.

---

## Revision Coding Challenge

Revised concepts from:

- Variables
- Input
- Strings
- Conditional Statements
- Loops

---

## Tech Lead Feedback

Today's work demonstrated a shift from writing individual statements to recognizing algorithmic patterns.

Highlights:

- Correct implementation of FizzBuzz by checking the combined condition first.
- Good understanding of `for` vs `while`.
- Clean loop implementation.
- Strong improvement in writing readable and maintainable code.

---
# Day 7 | 23 Jul 2026

## Sprint

Sprint 1 – Python Core

---

## Lesson

Day 6 – Lists

---

## Completed

- Learned what Lists are
- Created Lists
- Used Positive & Negative Indexing
- Updated List elements
- Used append()
- Used insert()
- Used remove()
- Used pop()
- Used len()
- Used Membership Operator (`in`)
- Iterated through Lists
- Completed Travel Package Manager
- Completed Daily Coding Challenge
- Completed Revision Coding Challenge
- Completed Refactoring Review
- Completed Quiz
- Senior Code Review Completed
- Tech Lead Review Completed

---

## Learnings

- Lists are ordered and mutable.
- Lists can store multiple values in one variable.
- Indexing starts at 0.
- Negative indexing accesses elements from the end.
- append() adds an element to the end of a List.
- insert() adds an element at a specific position.
- remove() deletes an element by value.
- pop() removes an element by index and returns it.
- len() returns the total number of elements.
- The `in` operator checks whether an element exists in a List.
- Lists are commonly processed using loops.

---

## Mistakes Corrected

- Removed an unnecessary duplicate `print()` statement.
- Learned not to overwrite Python built-in function names like `sum`.
- Improved understanding of user input normalization for case-insensitive searches.
- Improved code readability by using clearer variable names.

---

## Daily Coding Challenge

### Problem

Calculate the sum of all numbers in a List without using the built-in `sum()` function.

### Difficulty

⭐ Easy

### Pattern

Iteration + Accumulator

### Time Complexity

O(n)

### Space Complexity

O(1)

### Optimization

Already optimal because every element must be visited exactly once.

---

## Revision Coding Challenge

Revised concepts from:

- Variables
- User Input
- Strings
- Conditional Statements
- Loops
- Lists

---

## Tech Lead Feedback

Today's lesson marked an important transition from working with single values to managing collections of data.

Highlights:

- Correct use of List methods.
- Strong understanding of indexing.
- Proper use of loops to process Lists.
- Good implementation of membership checks using the `in` operator.
- Improvement in writing cleaner and more maintainable code.
- Introduction to writing production-style collection handling.

# Day 7 | 24 Jul 2026

## Sprint

Sprint 1 – Python Core

---

## Lesson

Day 7 – Tuples

---

## Completed

- Learned what Tuples are
- Created Tuples
- Accessed Tuple elements using indexing
- Used Positive & Negative Indexing
- Learned Tuple Packing
- Learned Tuple Unpacking
- Used `count()` method
- Used `index()` method
- Iterated through Tuples
- Completed Flight Information Assignment
- Completed Daily Coding Challenge
- Completed Revision Coding Challenge
- Completed Quiz
- Senior Code Review Completed
- Tech Lead Review Completed

---

## Learnings

- Tuples are ordered and immutable.
- Tuples can store multiple values of different data types.
- Tuple elements cannot be modified after creation.
- Tuple Packing groups multiple values into a Tuple.
- Tuple Unpacking assigns Tuple elements to separate variables.
- Tuples support indexing and slicing like Lists.
- Only `count()` and `index()` methods are available.
- Tuples are slightly faster and more memory-efficient than Lists.
- Tuples are ideal for storing fixed or read-only data.

---

## Mistakes Corrected

- Corrected the typo from **"Fight Number"** to **"Flight Number"**.
- Improved user input handling using `.strip().title()` for cleaner comparisons.
- Reinforced the practice of choosing Tuples only for immutable data.

---

## Daily Coding Challenge

### Problem

Create a Tuple containing latitude and longitude, unpack it into separate variables, and print both values.

### Difficulty

⭐ Easy

### Pattern

Tuple Unpacking

### Time Complexity

O(1)

### Space Complexity

O(1)

### Optimization

Already optimal because unpacking a fixed-size Tuple takes constant time.

---

## Revision Coding Challenge

Revised concepts from:

- Variables
- User Input
- if-else
- Membership Operator (`in`)
- Tuples

---

## Tech Lead Feedback

Today's lesson focused on selecting the correct data structure based on business requirements rather than syntax.

Highlights:

- Strong understanding of Tuple immutability.
- Correct use of Tuple packing and unpacking.
- Improved descriptive variable naming.
- Good understanding of when to choose a Tuple instead of a List.
- Started thinking from a software engineering perspective by selecting immutable data for fixed business information.

---

## Interview Preparation

### Basic Interview Questions Covered

- What is a Tuple?
- List vs Tuple
- Tuple Packing
- Tuple Unpacking
- Single Element Tuple
- Tuple Methods
- Mutable vs Immutable Objects

### Senior Engineer Questions Covered

- When should you choose a Tuple over a List?
- Why are Tuples faster?
- Can Tuples contain mutable objects?
- Can Tuples be Dictionary keys?
- Choosing the correct data structure based on business requirements.
- Tuple use cases in production systems.

---

# Day 8 | 27 Jul 2026

## Sprint

Sprint 1 – Python Core

---

## Lesson

Day 8 – Dictionaries

---

## Completed

- Learned Dictionary fundamentals
- Created Dictionaries
- Accessed values using keys
- Added and updated key-value pairs
- Removed entries using `pop()` and `del`
- Used `keys()`, `values()` and `items()`
- Used `get()` for safe access
- Iterated through Dictionaries
- Learned Nested Dictionaries
- Compared Dictionary vs List vs Tuple
- Completed Hands-on Coding
- Completed Assignment
- Completed Daily Coding Challenge
- Completed Revision Coding Challenge
- Completed Quiz
- Senior Code Review Completed
- Tech Lead Review Completed

---

## Learnings

- Dictionaries store data as key-value pairs.
- Keys must be unique.
- Values can be duplicated.
- Dictionaries are mutable.
- `get()` is safer than direct indexing.
- Python Dictionaries use hash tables.
- Dictionary operations are O(1) on average.
- Dictionaries map directly to JSON objects returned by APIs.

---

## Mistakes Corrected

- Improved output formatting instead of directly printing `dict_items`.
- Reinforced using `get()` for optional user input.
- Learned to choose Dictionaries for named business data instead of Lists.

---

## Daily Coding Challenge

Created a student information Dictionary and safely retrieved values using `get()`.

Difficulty: ⭐ Easy

Concepts:
- Dictionary Creation
- User Input
- Safe Lookup

---

## Revision Coding Challenge

Revised:

- Variables
- if-else
- User Input
- Dictionary Lookup
- `get()` Method

---

## Tech Lead Feedback

Today's lesson marked an important transition from sequence-based data structures (Lists and Tuples) to key-based data modeling.

Highlights:

- Strong understanding of CRUD operations on Dictionaries.
- Correct use of `get()` for safer code.
- Good understanding of choosing Dictionaries for business entities.
- Ready to work with JSON responses from REST APIs.

---

## Interview Preparation

### Basic Questions Covered

- Dictionary Fundamentals
- CRUD Operations
- `get()` vs `[]`
- Dictionary Methods
- Time Complexity

### Senior Engineer Questions Covered

- Dictionaries vs Lists
- Hash Tables
- Dictionary Keys
- JSON Mapping
- Production Use Cases

---

# Day 9 | 29 Jul 2026

## Sprint

Sprint 1 – Python Core

---

## Lesson

Day 9 – Sets

---

## Completed

- Learned Set fundamentals
- Created Sets
- Understood automatic duplicate removal
- Added elements using `add()`
- Removed elements using `remove()` and `discard()`
- Used membership operator (`in`)
- Performed Union
- Performed Intersection
- Performed Difference
- Performed Symmetric Difference
- Completed Hands-on Coding
- Completed Assignment
- Completed Daily Coding Challenge
- Completed Revision Coding Challenge
- Completed Quiz
- Senior Code Review Completed
- Tech Lead Review Completed

---

## Learnings

- Sets store only unique values.
- Duplicate elements are removed automatically.
- Sets are unordered collections.
- Empty Sets are created using `set()`.
- `remove()` raises an error if an element doesn't exist.
- `discard()` safely removes an element without raising an error.
- Sets use Hash Tables internally.
- Membership checking in a Set is O(1) on average.
- Set operations simplify comparing collections.

---

## Mistakes Corrected

- Corrected the Set operator for Intersection (`&`) after initially confusing it with Union (`|`).
- Improved the Daily Coding Challenge solution by converting an existing List into a Set using `set(cities)` instead of manually creating another Set.

---

## Daily Coding Challenge

### Problem

Remove duplicate city names from a List using a Set.

### Difficulty

⭐ Easy

### Concepts

- Set Creation
- Duplicate Removal
- List to Set Conversion

### Time Complexity

O(n)

### Space Complexity

O(n)

---

## Revision Coding Challenge

Revised concepts:

- Variables
- User Input
- `if-else`
- Membership Operator (`in`)
- Sets

---

## Tech Lead Feedback

Today's lesson focused on selecting the correct data structure for business problems involving uniqueness and fast lookups.

Highlights:

- Strong understanding of duplicate removal.
- Good use of membership testing.
- Correct application of all four Set operations.
- Improved coding style with meaningful variable names and clean user input handling.
- Demonstrated good understanding of when Sets are preferable to Lists.

---

## Interview Preparation

### Basic Questions Covered

- Set Fundamentals
- Creating Sets
- `remove()` vs `discard()`
- Set Operations
- Membership Testing
- Time Complexity

### Senior Engineer Questions Covered

- Hash Tables
- Set vs List
- Production Use Cases
- Choosing the Correct Data Structure
- Duplicate Removal Strategies

# Day 10 | 29 Jul 2026

## Sprint

Sprint 1 – Python Core

---

## Lesson

Day 10 – Functions (Part 1)

---

## Completed

- Learned why Functions are used
- Defined Functions using `def`
- Called Functions
- Learned Parameters and Arguments
- Used Return Statements
- Practiced Local Variables
- Practiced Global Variables
- Understood Variable Scope
- Completed Hands-on Coding
- Completed Assignment
- Completed Daily Coding Challenge
- Completed Revision Coding Challenge
- Completed Quiz
- Senior Code Review Completed
- Tech Lead Review Completed

---

## Learnings

- Functions are reusable blocks of code.
- Functions reduce duplicate code by following the DRY principle.
- Parameters are variables defined in the function declaration.
- Arguments are the actual values passed during a function call.
- `return` sends a value back to the caller.
- `print()` only displays output.
- Local variables exist only within a function.
- Global variables can be accessed throughout the program.
- Small, focused functions are easier to maintain and test.

---

## Mistakes Corrected

- Corrected the difference between **Parameters** and **Arguments**.
- Learned that `print(local_variable)` prints the function object, while `print(local_variable())` executes the function and prints its return value.
- Improved understanding of using `return` instead of `print()` when values need to be reused.

---

## Daily Coding Challenge

### Problem

Create a function `find_larger(a, b)` that returns the larger number.

### Difficulty

⭐ Easy

### Concepts

- Functions
- Parameters
- Return
- Conditional Statements

### Time Complexity

O(1)

### Space Complexity

O(1)

---

## Revision Coding Challenge

Revised concepts:

- Functions
- Sets
- Membership Operator (`in`)
- Return Values

---

## Tech Lead Feedback

Today's lesson introduced one of the most important software engineering concepts: **modular programming**.

Highlights:

- Good understanding of function creation and invocation.
- Appropriate use of `return` for reusable logic.
- Strong function naming overall.
- Good separation of responsibilities across functions.
- Developing clean coding habits by writing small, focused functions.

Areas to improve:

- Continue reinforcing the difference between Parameters and Arguments.
- Remember to execute functions using parentheses `()` when you need their return values.

---

## Interview Preparation

### Basic Questions Covered

- What is a Function?
- Function Syntax
- Parameters vs Arguments
- Return Statement
- Local vs Global Variables
- Variable Scope

### Senior Engineer Questions Covered

- DRY Principle
- Single Responsibility Principle
- Code Reusability
- Production Function Design
- `return` vs `print()`

---

# Day 11 | 30 Jul 2026

## Sprint

Sprint 1 – Python Core

---

## Lesson

Day 11 – Functions (Part 2)

---

## Completed

- Learned Default Parameters
- Learned Positional & Keyword Arguments
- Used `*args`
- Used `**kwargs`
- Created Lambda Functions
- Added Type Hints
- Wrote Docstrings
- Completed Hands-on Coding
- Completed Assignment
- Completed Daily Coding Challenge
- Completed Revision Coding Challenge
- Completed Quiz
- Senior Code Review Completed
- Tech Lead Review Completed

---

## Learnings

- Default parameters simplify common function calls.
- Keyword arguments improve readability.
- `*args` stores positional arguments in a Tuple.
- `**kwargs` stores keyword arguments in a Dictionary.
- Lambda functions are useful for small operations.
- Type hints improve readability and IDE support.
- Docstrings document functions for future developers.

---

## Mistakes Corrected

- Corrected confusion between `*args` and `**kwargs`.
- Reinforced that keyword arguments reduce errors caused by argument order.
- Improved understanding of writing production-friendly function signatures.

---

## Daily Coding Challenge

### Problem

Create `find_max(*numbers)` without using `max()`.

### Difficulty

⭐ Easy

### Concepts

- `*args`
- Loops
- Conditional Statements
- Return Values

### Time Complexity

O(n)

### Space Complexity

O(1)

---

## Revision Coding Challenge

Revised Concepts:

- `*args`
- Sets
- Duplicate Removal
- Return Values

---

## Tech Lead Feedback

Today's lesson focused on writing flexible, maintainable, and scalable functions.

Highlights:

- Strong understanding of advanced function syntax.
- Good use of type hints and docstrings.
- Correct implementation of `*args` and `**kwargs`.
- Continued improvement in writing reusable, modular code.

Areas to Improve:

- Reinforce the distinction between `*args` (Tuple) and `**kwargs` (Dictionary).
- Prefer keyword arguments when functions have multiple parameters for improved readability.

---

## Interview Preparation

### Basic Questions Covered

- Default Parameters
- Positional vs Keyword Arguments
- `*args`
- `**kwargs`
- Lambda Functions
- Type Hints
- Docstrings

### Senior Engineer Questions Covered

- Designing Flexible APIs
- DRY Principle
- Type Hints in Production
- Docstring Best Practices
- Choosing Between Lambda and Normal Functions

## Lesson

Day 12 – Modules & File Handling

---

## Completed

- Learned Modules
- Imported Built-in Modules
- Created Custom Modules
- Learned Packages
- Read Files
- Wrote Files
- Appended Files
- Used Context Managers (`with`)
- Completed Hands-on Coding
- Completed Assignment
- Completed Daily Coding Challenge
- Completed Revision Coding Challenge
- Completed Quiz
- Senior Code Review Completed
- Tech Lead Review Completed

---

## Learnings

- A Module is a Python file.
- A Package is a folder containing multiple modules.
- `import` is used to include modules.
- `with` automatically closes files.
- `"w"` overwrites existing files.
- `"a"` appends new data.
- Modules improve project organization.
- File handling enables persistent storage.

---

## Mistakes Corrected

- Corrected Module vs Package.
- Learned why `with` is preferred over `close()`.
- Identified hard-coded paths as a maintainability issue.

---

## Daily Coding Challenge

### Problem

Append travel destinations to a text file.

### Difficulty

⭐ Easy

### Concepts

- File Handling
- Append Mode
- Functions

### Time Complexity

O(1) amortized

### Space Complexity

O(1)

---

## Revision Coding Challenge

Revised Concepts:

- Functions
- Sets
- File Reading
- Duplicate Removal

---

## Tech Lead Feedback

Today's lesson focused on organizing software into reusable modules and persisting data through file handling.

Highlights:

- Good understanding of module creation and imports.
- Strong use of context managers (`with`).
- Correct implementation of reusable utility functions.
- Good combination of file handling with sets.

Areas to Improve:

- Replace hard-coded paths with `pathlib`.
- Add exception handling when reading files.

---

## Interview Preparation

### Basic Questions Covered

- Modules
- Packages
- Import Statements
- File Modes
- Context Managers

### Senior Engineer Questions Covered

- Project Structure
- Utility Modules
- Cross-platform File Handling
- Resource Management

---

## Lesson

Day 13 – Exception Handling

---

## Completed

- Learned Python Exceptions
- Learned `try`
- Learned `except`
- Learned `else`
- Learned `finally`
- Learned `raise`
- Learned common Python exceptions
- Introduced Custom Exceptions
- Completed Hands-on Coding
- Completed Assignment
- Completed Daily Coding Challenge
- Completed Revision Coding Challenge
- Completed Interview Coding Problem
- Completed 5-Minute Revision
- Completed Quiz
- Senior Code Review Completed
- Tech Lead Review Completed

---

## Learnings

- Exceptions occur during program execution.
- `try` contains potentially risky code.
- `except` handles exceptions.
- `else` executes when no exception occurs.
- `finally` executes regardless of success or failure.
- `raise` is used to intentionally raise an exception.
- Specific exceptions should generally be caught instead of using a bare `except`.
- File handling can be combined with exception handling.
- Sets provide efficient average-case membership checks.
- A Set + List combination can remove duplicates while preserving order.

---

## Mistakes Corrected

### 1. Interview Problem

Initially attempted to remove duplicates by modifying the list while iterating.

Problem:

- Removing elements changes list indexes.
- Elements can be skipped.
- The original list is modified.

Improved approach:

- Use a Set to track seen elements.
- Use a List to preserve order.

Complexity:

- Time: O(n) average
- Space: O(n)

### 2. Exception Handling

Initially manually raised `ZeroDivisionError` after checking for zero.

Improved approach:

Allow Python to raise the exception naturally and handle it with `except ZeroDivisionError`.

---

## Daily Coding Challenge

### Problem

Create `safe_division(a, b)` that handles division by zero.

### Difficulty

⭐ Easy

### Concepts

- Functions
- `try`
- `except`
- `raise`
- Return values

---

## Revision Coding Challenge

### Problem

Create `load_packages()` that reads destinations from a file and returns a Set.

If the file does not exist, return an empty Set.

### Concepts

- Functions
- Sets
- File Handling
- Context Managers
- Exception Handling

---

## Interview Problem

### Problem

Remove duplicate destinations while preserving their original order.

### Pattern

Set + List

### Difficulty

⭐ Easy

### Result

Solved with review required.

### Optimal Complexity

Time: O(n) average

Space: O(n)

### Key Learning

Use a Set for fast membership checks and a List for maintaining output order.

---

## Quiz

Score: **5/5**

---

## Code Review

### Strengths

- Good understanding of specific exceptions.
- Correct use of `try`, `except`, `else`, and `finally`.
- Good combination of file handling and exception handling.
- Successfully used `raise` for validation.
- Good understanding of Sets from previous lessons.

### Areas to Improve

- Avoid modifying collections while iterating.
- Prefer meaningful exception messages.
- Keep `try` blocks focused and small.
- Continue improving interview-style solution explanations.

---

## Interview Preparation

### Basic Questions Covered

- Exceptions
- `try`
- `except`
- `else`
- `finally`
- `raise`
- Common Python exceptions

### Senior Engineer Questions Covered

- Specific vs bare exception handling
- When to use `raise`
- Validation vs exceptions
- Keeping `try` blocks small
- Appropriate use of `finally`

---

# LEARNING LOG

## Day 14 — Expense Tracker Mini Project

### Status

Completed ✅

---

# Objective

Build a command-line Expense Tracker application by integrating the Python concepts learned during the previous lessons.

The goal was to move from isolated coding exercises toward building a complete application.

---

# Features Implemented

## 1. Add Expense

Implemented functionality to:

* Accept description.
* Accept category.
* Accept amount.
* Validate amount.
* Reject invalid input.
* Reject zero and negative amounts.
* Store the expense as a dictionary.
* Add the expense to the expenses list.

---

## 2. View Expenses

Implemented functionality to:

* Display all expenses.
* Handle the case where no expenses are available.

---

## 3. Calculate Total Expenses

Implemented a function that loops through all expenses and calculates the total.

Complexity:

Time: O(n)

Space: O(1)

---

## 4. Search by Category

Implemented category-based searching.

The program:

1. Accepts a category.
2. Loops through the expenses.
3. Displays matching expenses.
4. Displays a message if no category matches.

---

## 5. File Persistence

Implemented:

* Saving expenses to a text file.
* Loading expenses when the application starts.
* Reconstructing dictionaries from saved text.

File format:

Description|Category|Amount

---

## 6. Menu-Driven Application

Implemented a continuous application loop using:

while True

Implemented:

* `continue` for invalid menu input.
* `break` when the user selects Exit.

---

# Code Review Learning

The first version of the project had several issues.

## Issue 1 — Unsafe `eval()`

Initial approach used:

eval()

Problem:

`eval()` can execute arbitrary Python code.

Improvement:

Used a structured text format and:

split("|")

to reconstruct the expense data.

---

## Issue 2 — Application Ran Only Once

Initial menu executed only once.

Improvement:

Wrapped the menu inside:

while True

This allowed users to perform multiple operations.

---

## Issue 3 — Invalid Input Handling

Improved invalid menu input handling using:

try
except ValueError
continue

---

## Issue 4 — File Not Found

Initially, `load_expenses()` could return `None`.

Improvement:

Return an empty list when the file does not exist.

This guarantees that the caller receives a predictable list.

---

## Issue 5 — Expense Validation

Added validation to ensure the amount is:

* An integer.
* Greater than 0.

The application continues asking for input until valid data is entered.

---

## Issue 6 — Category Total Algorithm

Initial approach used nested loops.

Improved approach:

Use a dictionary to store category totals while looping through expenses once.

Concept:

For each expense:

If category exists:
Add amount

Otherwise:
Create category

Complexity:

Time: O(n)

Space: O(k)

---

# Important Concepts Reinforced

* Lists
* Dictionaries
* Sets
* Functions
* Return values
* Loops
* `while True`
* `break`
* `continue`
* Exception handling
* File handling
* Data persistence
* Input validation
* Dictionary membership
* Time complexity
* Space complexity
* Code organization

---

# Key Takeaway

Day 14 demonstrated how individual Python concepts work together in a real application.

The project flow was:

User Input
↓
Validation
↓
Business Logic
↓
Data Storage
↓
File Persistence

The most important improvement was learning to iterate on code after review instead of considering the first working solution as the final solution.

---

# Senior Engineer Perspective

Important lessons from this project:

* Working code is not automatically good code.
* Input validation is necessary.
* Functions should have clear responsibilities.
* Return types should be predictable.
* Unsafe shortcuts such as `eval()` should be avoided.
* Data structures should be selected based on the problem.
* Algorithm efficiency matters.
* Nested loops should be questioned when a single-pass solution is possible.
* Code should be improved through review and iteration.

# LEARNING LOG

# Day 15 — Object-Oriented Programming

## Status

✅ Completed

---

# 🎯 Objective

Learn the fundamentals of Object-Oriented Programming and understand how classes and objects can be used to model real-world entities.

The lesson also continued the coding-problem track with an optimized Two Sum implementation.

---

# 🧠 Concepts Learned

## Classes

A class acts as a blueprint/template for creating objects.

---

## Objects

Objects are instances of classes.

One class can create many objects.

Example:

Traveler class
↓
traveler1
traveler2
traveler3

---

## `__init__()`

Learned how `__init__()` is used to initialize an object's attributes when the object is created.

Java comparison:

Python `__init__()` ≈ Java constructor.

---

## `self`

Learned that `self` refers to the current instance.

Important distinction:

name

→ parameter/local variable

self.name

→ instance attribute

---

## Attributes

Attributes represent object state/data.

Examples:

* name
* age
* country
* price
* destination

---

## Methods

Methods represent object behavior.

Examples:

* display_profile()
* check_international_eligibility()
* calculate_discount()
* is_luxury()

---

## Class vs Instance Attributes

Learned that:

Instance attributes belong to individual objects.

Class attributes belong to the class and are generally shared by instances.

---

# 💻 Practical Work

## Traveler Class

Created a `Traveler` class with:

* name
* age
* country
* passport availability

Implemented:

* `display_profile()`
* `check_international_eligibility()`

---

## TravelPackage Class

Created a `TravelPackage` class with:

* destination
* price
* days

Implemented:

* `display_package()`
* `calculate_discount()`
* `is_luxury()`

---

## Rectangle Class

Created a Rectangle class with:

* length
* width

Implemented:

* `calculate_area()`
* `calculate_perimeter()`

---

## PackageAnalyzer Class

Created a `PackageAnalyzer` class that receives package data.

Implemented:

`get_luxury_packages()`

Important code review lesson:

When object state is stored as:

self.packages

methods should use:

self.packages

rather than relying on a global variable.

---

# 🔥 Coding Problem — Two Sum

## Brute Force Approach

Used nested loops to compare pairs.

Complexity:

Time: O(n²)

Space: O(1), excluding output.

---

## Optimized Approach

Used a dictionary to store:

number → index

For each number:

required = target - current_number

Then check whether the required value already exists.

Complexity:

Time: O(n)

Space: O(n)

---

# 🧑‍💻 Code Review Learnings

## Learning 1

A working solution isn't necessarily the most efficient solution.

The initial Two Sum solution worked but only checked adjacent elements.

The correct brute-force solution checks every possible pair.

---

## Learning 2

Using a dictionary does not automatically make an algorithm O(n).

If we use another loop/search to find information inside the dictionary, we may lose the expected performance benefit.

The optimized solution must use direct dictionary lookup.

---

## Learning 3

Objects should operate on their own state.

Prefer:

self.packages

over an unrelated global:

packages

---

## Learning 4

Don't automatically replace dictionaries with classes.

Use OOP where classes provide meaningful structure, state, behavior, or business rules.

---

# 🎤 Interview Preparation

Covered:

* OOP definition
* Class vs object
* `__init__`
* `self`
* Instance attributes
* Instance methods
* Class attributes
* Class vs instance attributes
* Data and behavior together
* Dictionary vs class
* OOP in Expense Tracker
* Two Sum complexity
* Dictionary-based optimization
* Separation of responsibilities

---

# 🌍 Wanderlust Wings Connection

OOP can eventually model domain entities such as:

Traveler
TravelPackage
Booking
Flight
Hotel
Itinerary

This provides a foundation for building more structured application components as Wanderlust Wings evolves.

---

# 🏆 Day 15 Achievement

Successfully completed:

* OOP fundamentals
* Multiple class implementations
* Object creation
* Instance state
* Instance behavior
* Class/instance attribute concepts
* Algorithm optimization
* Two Sum O(n) solution
* Senior Engineer code review

---

# 📌 Next

Day 16

Continue Python Core/OOP and problem-solving practice.

The learning workflow continues to follow:

Theory
↓
Hands-on Coding
↓
Coding Challenge
↓
Revision
↓
Interview Questions
↓
Code Review
↓
Wanderlust Wings Application



