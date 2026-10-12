# 📘 Day 17 — Inheritance, Method Overriding & `super()`

## 🎯 Objective

Understand how inheritance enables code reuse, how child classes customize parent behavior, and how to design reusable classes for Wanderlust Wings.

## 1. Business Requirement

Wanderlust Wings needs to represent different types of travelers and travel packages.

Examples:
- `Traveler`
- `InternationalTraveler`
- `DomesticTraveler`
- `TravelPackage`
- `PremiumPackage`
- `LuxuryPackage`

These entities share common behavior, but specialized entities need additional attributes or customized behavior.

Instead of duplicating common code, inheritance allows us to create a parent class and extend it through child classes.

## 2. What Is Inheritance?

Inheritance allows a child class to reuse attributes and methods from a parent class.

```python
class Traveler:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_profile(self):
        return f"Name: {self.name}, Age: {self.age}"


class InternationalTraveler(Traveler):
    def __init__(self, name, age, passport_number):
        super().__init__(name, age)
        self.passport_number = passport_number
```

`InternationalTraveler` inherits from `Traveler`.

It receives the common attributes `name` and `age` while adding `passport_number`.

### Terminology

- Parent class: Base class or superclass.
- Child class: Derived class or subclass.
- Inheritance: Reusing and extending a parent class.

### Java comparison

Python:

```python
class InternationalTraveler(Traveler):
    pass
```

Java:

```java
class InternationalTraveler extends Traveler {
}
```

Both express inheritance, although their language rules and implementation details differ.

## 3. The `super()` Function

`super()` lets a child class access behavior defined by its parent or the next class in Python's method resolution order.

```python
class InternationalTraveler(Traveler):
    def __init__(self, name, age, passport_number):
        super().__init__(name, age)
        self.passport_number = passport_number
```

Why use it?

1. Avoids repeating initialization logic.
2. Keeps common behavior in one place.
3. Makes future changes easier to maintain.
4. Supports cooperative multiple inheritance when used consistently.

Java comparison:

```java
super(name, age);
```

In Python, `super()` is not simply a fixed reference to the direct parent; it follows the method resolution order (MRO).

## 4. Method Overriding

Method overriding occurs when a child class provides its own implementation of an inherited method.

```python
class Traveler:
    def travel_message(self):
        return "Traveler is preparing for a trip."


class InternationalTraveler(Traveler):
    def travel_message(self):
        return "International traveler is preparing for a trip."
```

Calling `travel_message()` on an `InternationalTraveler` instance uses the child implementation.

This supports polymorphism: different object types can respond differently to the same method call.

### Overriding vs. overloading

- **Overriding:** A subclass customizes an inherited method.
- **Overloading:** A familiar Java concept in which methods share a name but have different parameter lists. Python does not support traditional signature-based method overloading in the same way as Java; alternatives include default arguments and dispatch mechanisms.

## 5. Extending Parent Behavior with `super()`

A child can reuse the parent's implementation and then add specialized behavior.

```python
class Traveler:
    def display_profile(self):
        return "Traveler profile"


class InternationalTraveler(Traveler):
    def display_profile(self):
        parent_info = super().display_profile()
        return f"{parent_info}, Passport required"
```

This avoids duplicating the parent method's logic.

**Best practice:** Use `super()` when you want to extend parent behavior rather than copy and maintain a separate version of the same logic.

## 6. Inheritance vs. Composition

### Inheritance — IS-A relationship

Use inheritance when one type genuinely is a specialized form of another.

Examples:
- An `InternationalTraveler` is a `Traveler`.
- A `PremiumPackage` is a type of `TravelPackage`.

### Composition — HAS-A relationship

Use composition when one object contains or uses another object.

Examples:
- A `Booking` has a `Traveler`.
- A `Booking` has a `TravelPackage`.
- An `Itinerary` has a collection of activities.

Composition often provides more flexibility when objects need to vary independently.

Avoid inheritance merely to reuse a few lines of code. A deep or complicated inheritance hierarchy can make behavior difficult to understand and change.

## 7. MRO, `isinstance()` and `issubclass()`

### Method Resolution Order (MRO)

MRO determines the order in which Python searches classes for methods and attributes, especially when multiple inheritance is involved.

Inspect it using:

```python
print(InternationalTraveler.mro())
```

### `isinstance()`

Checks whether an object is an instance of a class or its subclasses.

```python
traveler = InternationalTraveler("Alex", 30, "P123")

print(isinstance(traveler, Traveler))
```

Expected result:

```text
True
```

### `issubclass()`

Checks whether a class inherits from another class.

```python
print(issubclass(InternationalTraveler, Traveler))
```

Expected result:

```text
True
```

## 8. Wanderlust Wings Implementation

### Traveler hierarchy

```text
Traveler
├── InternationalTraveler
├── DomesticTraveler
└── PremiumTraveler
```

Possible shared behavior:
- Store common traveler details.
- Display a profile.
- Provide a generic travel message.

Possible specialized behavior:
- International travelers: passport information and international eligibility.
- Domestic travelers: domestic travel requirements.
- Premium travelers: additional service preferences.

### Travel package hierarchy

```text
TravelPackage
├── PremiumPackage
└── LuxuryPackage
```

A base `TravelPackage` can calculate the base price. A specialized package can add premium services or a luxury fee.

Example:

```python
class TravelPackage:
    def __init__(self, destination, price):
        self.destination = destination
        self.price = price

    def calculate_price(self):
        return self.price


class LuxuryPackage(TravelPackage):
    def __init__(self, destination, price, luxury_fee):
        super().__init__(destination, price)
        self.luxury_fee = luxury_fee

    def calculate_price(self):
        return super().calculate_price() + self.luxury_fee
```

This design reuses the base calculation instead of duplicating it.

## 9. Coding Challenge — Best Time to Buy and Sell Stock

Given stock prices, find the maximum profit from one buy followed by one sell. If no profitable trade exists, return `0`.

```python
prices = [7, 1, 5, 3, 6, 4]
```

Expected output:

```text
5
```

### Optimized approach

Maintain:
- `min_price`: the minimum price seen so far.
- `profit`: the best profit found so far.

For each price:
1. Update the minimum price if necessary.
2. Calculate potential profit by selling at the current price.
3. Update the best profit if the potential profit is greater.

Complexity:
- Time: **O(n)**
- Auxiliary space: **O(1)**

The original nested-loop approach is O(n²); tracking the minimum price removes the need to revisit earlier prices.

## 10. Code Review Learnings

- Use `super().__init__()` to initialize inherited state.
- Use `super().method()` to reuse parent behavior.
- Keep method return behavior consistent where practical.
- Prefer descriptive variable and class names.
- Use inheritance for genuine IS-A relationships.
- Prefer composition for HAS-A relationships.
- Avoid unnecessarily deep inheritance hierarchies.
- Test edge cases, including decreasing stock prices.
- Separate business logic from output formatting where appropriate.

## 11. Interview Preparation

Review these questions:

1. What is inheritance, and why is it useful?
2. What is the difference between a parent and a child class?
3. What does `super()` do?
4. What is method overriding?
5. How does overriding differ from overloading?
6. Explain IS-A and HAS-A relationships.
7. Why shouldn't inheritance be used only to avoid code duplication?
8. What does `super().__init__(name, age)` do?
9. What is the Method Resolution Order?
10. What is the difference between `isinstance()` and `issubclass()`?
11. What alternatives exist when an inheritance hierarchy becomes complicated?
12. Why is composition often preferred in large systems?
13. How would you decide whether `LuxuryPackage` should inherit from `TravelPackage`?

## 12. Key Takeaways

- Inheritance reuses and extends behavior.
- `super()` supports parent initialization and behavior reuse.
- Overriding enables specialized behavior and polymorphism.
- Composition models relationships between independent objects.
- Good object-oriented design focuses on clear responsibilities, not just code reuse.
- Algorithm optimization often comes from maintaining useful information rather than repeatedly recomputing it.

## Next

- Complete the remaining interview questions.
- Refine the package analyzer and luxury package implementation.
- Verify the stock solution and its edge cases.
- Apply inheritance and composition decisions to Wanderlust Wings.
