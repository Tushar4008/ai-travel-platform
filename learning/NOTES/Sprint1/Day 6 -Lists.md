📘 Sprint 1 – Python Core
📖 Day 6 – Lists
🎯 Learning Objectives

By the end of this lesson, I should be able to:

Understand what a List is.
Create Lists.
Access List elements using indexing.
Modify Lists.
Add and remove elements.
Use common List methods.
Iterate through Lists using loops.
Search for elements using the in operator.
Understand List mutability.
Analyze the time complexity of List operations.
💼 Business Requirement

Real-world applications rarely work with a single value.

In Wanderlust Wings, we need to manage collections such as:

Travel packages
Destinations
Hotels
Flights
Customer bookings
AI recommendations

Instead of creating hundreds of variables, we store related values inside a List, making our code scalable and easy to maintain.

📚 Theory Notes
1. What is a List?

A List is an ordered, mutable collection that can store multiple values.

Example:

packages = ["Thailand", "Bali", "Goa"]

Characteristics:

Ordered
Mutable
Allows duplicate values
Can store different data types
2. Creating Lists
cities = ["Delhi", "Mumbai", "Goa"]

Numbers

prices = [10000, 20000, 30000]

Mixed Data Types

details = ["Thailand", 50000, True]
3. Accessing Elements

Positive Index

packages[0]

Output

Thailand

Negative Index

packages[-1]

Output

Goa
4. Updating Lists

Lists are mutable.

packages[1] = "Maldives"

Output

["Thailand", "Maldives", "Goa"]
5. Adding Elements
append()

Adds an element to the end.

packages.append("Dubai")
insert()

Adds an element at a specific index.

packages.insert(1, "Singapore")
6. Removing Elements
remove()

Removes by value.

packages.remove("Goa")
pop()

Removes by index (or the last element if no index is provided).

packages.pop()

packages.pop(2)
7. Finding Length
len(packages)

Returns the total number of elements.

8. Membership Operator
if "Thailand" in packages:
    print("Available")

Checks whether an element exists in the list.

9. Looping Through Lists
for package in packages:
    print(package)

This is the preferred way to process every element in a list.

10. Nested Lists
travel_data = [
    ["Thailand", 50000],
    ["Bali", 40000]
]

Accessing an element:

travel_data[0][0]

Output

Thailand
☕ Java Developer's Perspective
Java	Python
ArrayList	List
add()	append()
add(index, value)	insert(index, value)
remove()	remove()
size()	len()
get(index)	list[index]

Python is much more concise and readable.

❌ Mistakes I Made
Mistake 1

I printed the package list twice even though it hadn't changed.

Instead of:

print(packages)

print(len(packages))

print(packages)

Only the first print is necessary.

Mistake 2

I used:

sum = 0

sum is a built-in Python function.

Better:

total = 0

or

total_sum = 0

Avoid overriding built-in function names.

Mistake 3

Package searches are case-sensitive.

If the list contains:

Thailand

and the user enters:

thailand

the search fails.

A better approach:

user_package = input("Which package are you searching? ").strip().title()

This makes the search more user-friendly.

⭐ Best Practices
Use Lists to store related values.
Use meaningful variable names.
Avoid overriding built-in functions like sum, list, or str.
Use loops instead of repeated code.
Prefer the in operator for membership checks.
Keep List operations simple and readable.
Normalize user input before comparison.
🎯 Interview Questions with Short Answers
1. What is a List?

A mutable, ordered collection that stores multiple values.

2. Why are Lists mutable?

Because elements can be modified after the List is created.

3. Difference between append() and insert()?
append() adds an element to the end.
insert() adds an element at a specified position.
4. Difference between remove() and pop()?
remove() removes an element by value.
pop() removes an element by index and returns it.
5. Difference between Lists and Strings?
Lists are mutable.
Strings are immutable.
6. What does len() return?

The total number of elements in the List.

7. Time Complexity of iterating through a List?

O(n)

8. Space Complexity of iterating through a List?

O(1)

🌍 Wanderlust Wings Connection

Lists will be used throughout the project to manage:

Travel packages
Destinations
Hotel options
Flight details
Customer bookings
Reviews
AI-generated recommendations
API response data

Almost every module in Wanderlust Wings will use Lists.

📝 One Minute Revision
Lists
│
├── Create
├── Indexing
├── Negative Indexing
├── Update
├── append()
├── insert()
├── remove()
├── pop()
├── len()
├── in
├── for loop
└── Nested Lists
🔑 Key Takeaways
Lists store multiple values in one variable.
Lists are ordered and mutable.
Use indexing to access elements.
Use append() and insert() to add data.
Use remove() and pop() to delete data.
Use len() to find the number of elements.
Use the in operator to search for values.
Lists are one of the most important Python data structures.
🔥 Common Interview Traps

❌ Confusing append() with insert()

Remember:

append() → End of the list
insert() → Specific position

❌ Confusing remove() with pop()

remove() → Removes by value
pop() → Removes by index

❌ Overriding built-in functions

Avoid:

sum = 0
list = []
str = ""

❌ Assuming List indexing starts at 1

Python indexing starts at 0.

🧠 Daily Coding Challenge
Problem

Find the sum of all numbers in a List without using sum().

numbers = [10, 20, 30, 40, 50]

Expected Output

150
Pattern

Iteration + Accumulator

Time Complexity

O(n)

Space Complexity

O(1)

🔁 Revision Coding Challenge
Problem

Create a List of cities.

Display:

Welcome to Delhi
Welcome to Goa
Welcome to Mumbai

Ask the user for their favourite city.

If it exists:

Great Choice!

Otherwise:

Let's add it soon!
Concepts Revised
Variables
Input
Strings
Loops
Conditional Statements
Lists
✅ Day 6 Summary

Today I learned how to work with Lists, Python's most commonly used collection data structure. I practiced creating Lists, accessing elements using positive and negative indexing, adding and removing items, checking membership, looping through Lists, and using built-in methods like append(), insert(), remove(), pop(), and len(). I also learned the importance of avoiding built-in function names such as sum and making user input more robust through normalization.