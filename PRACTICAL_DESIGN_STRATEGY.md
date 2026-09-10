# Practical Design Strategy

## Purpose

When a practical scenario feels difficult, do not try to invent a perfect architecture immediately.

The goal is to build a repeatable engineering thinking process. With practice, the process becomes faster and more natural.

---

## The Core Process

For every practical problem, work through these steps before writing the code:

```text
PROBLEM
   ↓
NOUNS
   ↓
DATA / OWNERSHIP
   ↓
VERBS
   ↓
STATE CHANGES
   ↓
INVALID CASES
   ↓
DATA STRUCTURES
   ↓
IMPLEMENT
   ↓
TEST
```

---

## 1. Understand the Problem

Read the specification and identify exactly what the system must do.

Do not design yet.

Ask:

- What is the system supposed to achieve?
- What operations must it support?
- What information must it remember?
- What rules must always be true?

Avoid adding features that the specification did not ask for.

---

## 2. Nouns → Classes / Objects

Look for important nouns in the problem statement.

For example:

```text
Shopping Cart
Product
Customer
Order
```

Possible objects:

```python
Product
Cart
Customer
Order
```

Not every noun needs to become a class. A noun becomes a candidate class when it has meaningful identity, state, or behaviour.

### Rule

> Do not create classes just because classes are available. Create them when they represent a useful domain concept.

---

## 3. Data → Ownership

For every piece of data, ask:

> Who should own this data?

Example:

```text
Product
- name
- price

Cart
- products
```

The `Cart` owns the collection of products because the cart manages what has been added to it.

This question prevents random attributes from being placed on the wrong class.

### Useful question

> If this object disappears, which data should disappear with it?

---

## 4. Verbs → Methods

Look for actions in the specification.

Examples:

```text
add product
remove product
clear cart
mark server down
mark server up
```

These become candidate methods:

```python
cart.add_product(...)
cart.remove_product(...)
cart.clear_cart()

monitor.mark_down(...)
monitor.mark_up(...)
```

### Rule

> Methods should represent meaningful operations on the object or the data it manages.

---

## 5. Identify State Changes

Ask:

> What changes when this operation runs?

For example:

```python
server.status = Status.DOWN
```

The server's state changes.

Or:

```python
self.products.append(product)
```

The cart's collection changes.

Always distinguish:

- mutation of an existing object
- rebinding a name to another object
- creation of a new object

This is especially important in Python.

---

## 6. Identify Invalid Cases

Do not only design the happy path.

Ask:

- What if the object does not exist?
- What if it already exists?
- What if the operation is repeated?
- What if the input is invalid?
- What if the state does not allow the operation?

Example:

```text
add server
→ Is the server already registered?

mark server DOWN
→ Is the server registered?
→ Is it already DOWN?
```

These rules become part of the design, not something to discover accidentally while coding.

---

## 7. Choose the Data Structure

Only after understanding the data should you choose how to store it.

Ask what the system needs:

```text
Need order?              → list
Need uniqueness?         → set
Need key → value lookup? → dict
Need immutable sequence? → tuple
```

Do not choose a data structure just because it is familiar.

Choose it because its behaviour matches the requirement.

Example:

If a monitor must prevent duplicate server names, a set may be useful because membership and uniqueness are central requirements.

---

## 8. Keep the First Design Small

The first implementation does not need to solve every possible future problem.

Start with:

- the required classes
- the required state
- the required methods
- the required validation
- the simplest appropriate data structures

Do not prematurely add:

- factories
- abstract base classes
- repositories
- dependency injection frameworks
- design patterns
- databases
- configuration systems

unless the specification actually requires them.

### Rule

> Build the smallest design that correctly represents the problem.

Then improve it when a real requirement justifies the improvement.

---

## 9. Test the Design Mentally Before Coding

Before running the program, walk through a few scenarios.

### Happy path

```text
Create object
→ perform operation
→ verify state
```

### Duplicate case

```text
Add same object again
→ verify the rule is enforced
```

### Missing object

```text
Operate on unknown object
→ verify expected behaviour
```

### Repeated operation

```text
Perform same operation twice
→ verify state remains correct
```

This catches many design mistakes before they become code mistakes.

---

## 10. After Coding: Review the Mental Model

Do not only ask:

> Does the output look correct?

Also ask:

- Who owns this data?
- Why is this a class?
- Why is this method on this class?
- Why did I choose this data structure?
- What object is being mutated?
- What name is being rebound?
- What happens if this operation fails?
- Can another developer understand the design?

Correct output with an incorrect mental model is not considered complete learning.

---

# Quick Template

Use this template when starting a practical:

```text
PROBLEM:
What exactly must the system do?

NOUNS:
What are the important domain objects?

DATA / OWNERSHIP:
What data belongs to each object?

VERBS:
What operations must the system perform?

STATE:
What changes after each operation?

INVALID CASES:
What can go wrong or violate the rules?

DATA STRUCTURES:
Why list / set / tuple / dict?

IMPLEMENT:
What is the smallest clean design?

TEST:
Happy path + invalid path + repeated operations.
```

---

# Important Reminder

Feeling that you cannot "think of the design" immediately does not mean you cannot learn software engineering.

Design thinking is a skill built through repeated exposure to problems.

At the beginning, consciously walk through the checklist. Over time, the questions become automatic.

The objective is **not** to predict the perfect architecture.

The objective is to make a reasonable design, understand why it works, test it, and improve it when new requirements expose a weakness.

> **Think systematically, not perfectly.**
