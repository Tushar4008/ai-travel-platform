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

---

## Next Lesson

Day 12 – Modules & File Handling

Topics:

- Modules
- Packages
- File Handling
- Reading & Writing Files
- Context Managers
- Project Organization

