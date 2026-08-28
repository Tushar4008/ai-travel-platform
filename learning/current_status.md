# CURRENT STATUS — AI Full Stack Journey

## Project

Wanderlust Wings — AI-Powered Travel Platform

## Current Sprint

Sprint 1 — Python Foundations & Problem-Solving Fundamentals

## Current Progress

### Day 14 — COMPLETED ✅

Completed an integrated Python mini project:

# Expense Tracker CLI

The project combined concepts learned during Days 1–13.

## Features Completed

* Add Expense
* View Expenses
* Calculate Total Expenses
* Search Expenses by Category
* Validate expense amount
* Handle invalid user input
* Load saved expenses from a file
* Save expenses before exiting
* Menu-driven application using `while True`
* Graceful handling of invalid menu selections

## Concepts Applied

### Python Fundamentals

* Variables
* Strings
* Type conversion
* Input/output
* Conditions
* Loops

### Collections

* Lists
* Dictionaries
* Sets

### Functions

* Function definitions
* Parameters
* Return values
* Separation of responsibilities

### Exception Handling

* `try`
* `except`
* `FileNotFoundError`
* `ValueError`

### File Handling

* Read mode
* Write mode
* Context managers
* Data serialization using a custom delimiter format
* Loading file data back into Python objects

### Problem-Solving

Implemented category-wise expense aggregation.

Initial approach:

Nested loops

Improved approach:

Single loop + Dictionary

Complexity:

Time: O(n)

Space: O(k)

---

# Key Engineering Improvements Made During Code Review

* Replaced unsafe `eval()` usage.
* Added a continuous menu loop.
* Used `continue` for invalid menu input.
* Used `break` for application exit.
* Separated saving logic from adding expense logic.
* Ensured `load_expenses()` returns an empty list if no file exists.
* Added positive amount validation.
* Optimized category total calculation from a nested-loop approach to a single-pass dictionary-based approach.
* Improved separation of responsibilities.

---

# Current Skill Level

## Python Fundamentals

Strong foundation established.

Comfortable with:

* Variables
* Strings
* Input/output
* Type conversion
* Conditions
* Loops

## Collections

Comfortable with:

* Lists
* Tuples
* Dictionaries
* Sets

Understands basic use cases and average time complexity for common membership operations.

## Functions

Comfortable with:

* Parameters
* Return values
* Default arguments
* `*args`
* `**kwargs`
* Lambda functions
* Type hints
* Docstrings

## File Handling

Understands:

* Reading files
* Writing files
* Appending files
* Using `with open()`
* Loading data from files

## Exception Handling

Understands:

* `try`
* `except`
* `else`
* `finally`
* `raise`

## Problem Solving

Current focus:

* Strengthening coding logic.
* Revising previously learned concepts through coding problems.
* Understanding time and space complexity.
* Choosing appropriate data structures.
* Optimizing naive solutions.

---

# Mini Projects Completed

## 1. Travel Package Programs

Applied:

* Strings
* Input handling
* Conditions
* Loops
* Collections
* Functions

## 2. Expense Tracker CLI

Applied:

* Lists
* Dictionaries
* Sets
* Functions
* Loops
* Exception handling
* File handling
* Algorithm optimization

---

# Current Learning Approach

Each lesson follows:

Business Requirement
↓
Theory
↓
Hands-on Coding
↓
Daily Coding Challenge
↓
Revision Challenge
↓
Coding / Interview Problem
↓
Wanderlust Wings Connection
↓
Code Review
↓
Best Practices

The learning approach now also includes continuous problem-solving practice using previously learned concepts.

---

# Current Position

Day 14 Completed ✅

Next:

# Day 15

Focus will continue toward completing the remaining Sprint 1 concepts while strengthening:

* Problem-solving
* Code quality
* Complexity analysis
* Python project structure
* Revision of previous topics

---

# Sprint Goal

Build a strong foundation in:

Python Fundamentals
+
Problem Solving
+
Data Structures
+
Functions
+
File Handling
+
Exception Handling
+
Code Organization

Before moving deeper into backend and AI Full Stack development for Wanderlust Wings.
