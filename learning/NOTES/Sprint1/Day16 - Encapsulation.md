📘 Day 16 — OOP Deep Dive
🎯 Business Requirement

In Wanderlust Wings, we'll eventually have thousands of travelers and travel packages.

A simple class such as:

class Traveler:

    def __init__(self, name, age):
        self.name = name
        self.age = age

allows us to model travelers, but it doesn't protect the object's state.

For example:

traveler.age = -500

would currently be possible.

We therefore need a way to:

Keep data and related behavior together
Protect important object state
Validate values when they change
Calculate derived values without unnecessarily storing them

This leads us to encapsulation and properties.

🧠 1. Instance Attributes vs Class Attributes
Instance Attribute

An instance attribute belongs to a particular object.

class Traveler:

    def __init__(self, name, age):
        self.name = name
        self.age = age

If we create:

traveler1 = Traveler("Tushar", 30)
traveler2 = Traveler("Rahul", 25)

then:

traveler1.name → Tushar
traveler2.name → Rahul

Each object maintains its own state.

Rule

Instance attribute → belongs to an individual object.

Class Attribute

A class attribute belongs to the class and is normally shared by its instances.

class Traveler:

    platform = "Wanderlust Wings"

    def __init__(self, name):
        self.name = name

Both:

traveler1.platform
traveler2.platform

can access:

Wanderlust Wings
Java comparison

A Python class attribute is conceptually similar to a Java static field.

static String platform = "Wanderlust Wings";
🧠 2. Encapsulation

Encapsulation means keeping data and the behavior that operates on that data together while controlling how the object's state is accessed or modified.

Instead of allowing arbitrary changes:

Object
  ↓
Anyone changes state
  ↓
Potentially invalid object

we want:

Object
  ↓
Controlled access
  ↓
Validation
  ↓
Valid state
Why is it useful?

It helps:

Maintain valid object state
Reduce accidental modification
Improve maintainability
Keep related logic together
Make classes easier to reason about
🧠 3. Python Access Conventions

Python doesn't enforce access modifiers in exactly the same way as Java.

Public
self.name

A normal attribute is intended to be publicly accessible.

Single Underscore
self._age

A single underscore communicates:

This attribute is intended for internal use.

It is a convention, not strict access protection.

Python technically still allows:

traveler._age = 30
Double Underscore
self.__age

This triggers name mangling.

Python internally changes the name to reduce accidental access and naming conflicts.

This should not simply be considered the exact equivalent of Java's private.

🧠 4. @property

A property allows us to expose method behavior through attribute-style access.

Without a property:

traveler.get_age()

With a property:

traveler.age

Example:

class Traveler:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

Now:

print(traveler.age)

looks like normal attribute access, but Python is actually executing the property method.

🧠 5. Property Getter

This:

@property
def age(self):
    return self._age

is the getter.

It controls how the value is retrieved.

Conceptually:

traveler.age
      ↓
@property
      ↓
return self._age
🧠 6. Property Setter

A setter allows us to control what happens when an attribute is changed.

class Traveler:

    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):

        if value < 0:
            raise ValueError("Age cannot be negative")

        self._age = value

Now:

traveler.age = 31

goes through the setter.

If:

traveler.age = -10

the setter rejects it.

Key idea
traveler.age
      ↓
Getter


traveler.age = 30
      ↓
Setter
☕ Java Comparison

In Java, you might commonly write:

traveler.getAge();
traveler.setAge(30);

Python properties allow a cleaner interface:

traveler.age
traveler.age = 30

while still allowing validation and other behavior behind the scenes.

🧠 7. Read-Only Properties

A property without a setter is effectively read-only through that interface.

Example:

class Booking:

    @property
    def booking_summary(self):
        return f"{self.traveler_name} booked {self.destination}"

We can do:

booking.booking_summary

but we haven't defined:

@booking_summary.setter

So the caller cannot normally assign a new value through that property.

🧠 8. Computed Properties

Sometimes a value depends on other attributes.

Example:

class TravelPackage:

    def __init__(self, price, discount):
        self.price = price
        self.discount = discount

    @property
    def final_price(self):
        return self.price - self.discount

Now:

package.final_price

calculates the value.

We don't need:

self.final_price = self.price - self.discount
⭐ Why Not Store final_price?

Suppose:

price = 50,000
discount = 5,000
final_price = 45,000

Later:

package.price = 60_000

If final_price was separately stored, it could become stale.

A computed property:

@property
def final_price(self):
    return self.price - self.discount

always uses the current values.

Senior Engineer principle

Don't unnecessarily store data that can safely and cheaply be derived from existing state.

🧠 9. Object Invariants

An invariant is a condition that should remain true for a valid object.

For example:

Traveler.age >= 0

TravelPackage.price > 0

TravelPackage.days > 0

TravelPackage.discount >= 0

If we allow:

package.price = -5000

we have broken the object's valid state.

Good class design tries to protect important invariants.

🧠 10. Where Should Validation Live?

Validation can exist at different layers.

For example:

API Layer
    ↓
Domain/Object Validation
    ↓
Business/Service Logic

These layers can have different responsibilities.

API layer

Could validate:

Is age an integer?
Is required field present?
Is request format correct?
Domain/class

Could enforce:

Age cannot be negative
Price must be greater than zero
Service/business layer

Could enforce rules such as:

Is this traveler eligible for this particular package?
Can this package be booked under this business rule?

This distinction becomes increasingly important when we reach FastAPI + Pydantic + service architecture.

🧠 11. Too Much Logic in a Domain Class

A domain class should have a clear responsibility.

We don't want:

Traveler
 ├── Traveler validation
 ├── Database queries
 ├── HTTP requests
 ├── Email sending
 ├── Payment processing
 ├── File operations
 └── Booking system

This creates:

Tight coupling
Harder testing
Difficult maintenance
Larger classes
Difficult debugging
Principle

Keep responsibilities focused.

This will become important when we start designing the actual Wanderlust Wings backend.

💻 12. Example — Validated TravelPackage

A clean implementation looks like:

class TravelPackage:

    def __init__(self, destination, price, discount, days):
        self.destination = destination
        self.price = price
        self.discount = discount
        self.days = days

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, destination):
        if destination == "":
            raise ValueError("Destination can't be empty")

        self._destination = destination

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price <= 0:
            raise ValueError("Price must be greater than zero")

        self._price = price

    @property
    def days(self):
        return self._days

    @days.setter
    def days(self, days):
        if days <= 0:
            raise ValueError("Days must be greater than zero")

        self._days = days

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        if discount < 0:
            raise ValueError("Discount can't be negative")

        self._discount = discount

    @property
    def final_price(self):
        return self.price - self.discount

Notice that:

package.discount = -500

cannot create an invalid state.

And:

package.final_price

is calculated dynamically.

🧩 13. Sets + Duplicate Detection

We also revisited an important collection pattern.

Given:

destinations = [
    "Goa",
    "Thailand",
    "Goa",
    "Japan",
    "Thailand",
    "Dubai"
]

we can find duplicates efficiently:

seen = set()
duplicates = set()

for destination in destinations:

    if destination in seen:
        duplicates.add(destination)
    else:
        seen.add(destination)
Complexity

Average:

Time  → O(n)
Space → O(n)

This is significantly better than comparing every element with every other element using nested loops.

🧠 14. Stack — Valid Parentheses

We also introduced the Stack pattern.

A stack follows:

LIFO — Last In, First Out

Example:

push "("
push "["
push "{"

       ↓

     "{"
     "["
     "("

The most recently added item is removed first.

In Python, a list can act as a stack:

stack = []

stack.append("(")
stack.append("[")
stack.pop()
Valid Parentheses Algorithm

For:

"([{}])"

we:

Push opening brackets.
When a closing bracket appears:
Check whether the stack is empty.
Check whether the top matches.
Pop if it matches.
At the end, the stack should be empty.

Target complexity:

Time  → O(n)
Space → O(n)
🎯 Day 16 Key Concepts
Instance Attribute
        ↓
Individual object state

Class Attribute
        ↓
Shared class-level state

Encapsulation
        ↓
Controlled object state

@property
        ↓
Attribute-style access to behavior

@property + setter
        ↓
Validation + controlled mutation

Read-only property
        ↓
No setter

Computed property
        ↓
Value derived from existing state

Invariant
        ↓
Condition that must remain true

Set
        ↓
Efficient uniqueness/membership

Stack
        ↓
LIFO processing
🎤 Interview Questions & Answers
Q1. What is encapsulation?

Answer:
Encapsulation means keeping data and the behavior that operates on that data together while controlling how the object's state is accessed or modified.

Q2. Why is unrestricted modification of object state dangerous?

Answer:
It can allow invalid data or invalid types to enter an object and break assumptions made elsewhere in the application.

Q3. What does _age mean in Python?

Answer:
A single underscore indicates that an attribute is intended for internal use. It is a convention rather than strict access protection.

Q4. What happens when we use __age?

Answer:
Python applies name mangling, which changes the internal attribute name to reduce accidental access and naming conflicts.

Q5. What is @property?

Answer:
@property allows a method to be accessed using attribute-style syntax and can be used for controlled access, validation, or computed values.

Q6. What is the purpose of a property setter?

Answer:
A setter allows us to control and validate values when an attribute is assigned or modified.

Q7. What is the difference between traveler.age and traveler.get_age()?

Answer:
traveler.age uses attribute/property access, while traveler.get_age() explicitly calls a method.

Q8. What is a read-only property?

Answer:
A property that has a getter but no setter, meaning the value can be retrieved but cannot be assigned through that property.

Q9. Why might final_price be better represented as a property?

Answer:
Because it depends on price and discount. A computed property ensures the value always reflects the current state instead of becoming stale.

Q10. What does it mean for an object to maintain a valid state?

Answer:
It means the object's attributes always satisfy the rules or invariants required for that object to be valid.

👨‍💻 Senior Engineer Interview Questions & Answers
Q11. Would you use properties for every attribute?

Answer:
No. Properties should be used when they provide value, such as validation, transformation, controlled access, or computation. Simple attributes don't need unnecessary getters and setters.

Q12. Should all validation belong inside the class?

Answer:
No. Validation can exist at multiple layers. Domain invariants should generally be protected by the domain object, while request-format validation belongs at the API boundary and broader business rules may belong in services.

Q13. What is the downside of putting too much logic inside a domain class?

Answer:
The class can become tightly coupled and difficult to test and maintain. It may end up handling unrelated responsibilities such as database access, HTTP calls, payments, and notifications.

Q14. Why are global variables dangerous in a class-based application?

Answer:
Global state is shared across unrelated objects and can be modified unexpectedly. Individual objects should generally maintain their own state.

Q15. Should final_price be stored?

Answer:
Usually no, if it is cheap to calculate from price and discount. A computed property avoids duplicated state and prevents the value from becoming stale.

☕ Java → Python Mapping
Java	Python
this	self
Class	Class
Object	Object
Instance field	Instance attribute
static field	Class attribute
Getter	@property
Setter	@property.setter
private convention	_attribute / name mangling with __attribute__
ArrayList	list
HashSet	set
HashMap	dict
Stack implementation	list
✅ Code Review Checklist

Before considering an OOP class complete:

 Class has a clear responsibility
 Instance state uses self
 No unnecessary global dependencies
 Important invariants are protected
 Properties are used only when useful
 Setters validate state where required
 Derived values aren't unnecessarily duplicated
 Methods have clear responsibilities
 Edge cases are considered
 Time and space complexity are understood
⭐ Best Practices
1. Don't blindly copy Java patterns

You don't need:

get_age()
set_age()

for every attribute.

Python properties provide a more natural interface.

2. Validate at the right boundary

Don't validate the same thing everywhere without reason.

Think:

API format
     ↓
Domain invariant
     ↓
Business rule
3. Protect important invariants

If:

price > 0

must always be true, design the class so invalid prices cannot easily enter the object.

4. Don't duplicate derived state

Prefer:

@property
def final_price(self):
    return self.price - self.discount

over storing another mutable final_price attribute when there is no need to.

5. Think about responsibility

Before adding a method to a class, ask:

Does this behavior logically belong to this object?

That question will become increasingly important as we move from basic OOP toward production backend architecture.

🏁 Day 16 Status

Day 16 — OOP Deep Dive: ✅ COMPLETE

You have now moved beyond simply creating classes and objects and started learning how to design objects that protect their state and maintain valid behavior.

This is an important foundation for the next stage of the journey: Inheritance, polymorphism, abstraction, and eventually applying OOP concepts to the Wanderlust Wings backend.