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

### Next Lesson

Day 5 – Loops (`for` & `while`)