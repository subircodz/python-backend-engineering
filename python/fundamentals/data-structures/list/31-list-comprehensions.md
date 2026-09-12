# List Comprehensions

## Overview

A list comprehension is a compact way to create a new list by iterating over an iterable and producing a value for each item.

Basic form:

```python
[expression for item in iterable]
```

Mental model:

> Create a list of `expression` for each `item` in `iterable`.

## Transformation

A normal loop:

```python
numbers = [2, 4, 6, 8, 10]
squares = []

for num in numbers:
    squares.append(num * num)
```

Equivalent comprehension:

```python
squares = [num * num for num in numbers]
```

Result:

```python
[4, 16, 36, 64, 100]
```

The comprehension creates a new list. It does not mutate the original list by itself.

## Extracting Values

Comprehensions are useful for extracting values from records:

```python
users = [
    {"name": "Subir", "active": True},
    {"name": "Rahul", "active": False},
    {"name": "Amit", "active": True},
]

names = [record["name"] for record in users]
```

Result:

```python
["Subir", "Rahul", "Amit"]
```

## Filtering

A condition can be added with `if`:

```python
active_users = [record for record in users if record["active"]]
```

The `if` controls which items are included. The expression before `for` controls what is placed into the new list.

## Filtering + Transformation

These two operations can be combined:

```python
active_names = [
    record["name"]
    for record in users
    if record["active"]
]
```

Result:

```python
["Subir", "Amit"]
```

Conceptually:

```text
iterate -> check condition -> produce expression -> collect
```

## Engineering Judgement

A comprehension is not automatically better than a normal loop.

Use a comprehension when the operation is simple and readable. Prefer a normal loop when the logic becomes complex, contains multiple business decisions, requires detailed error handling, or becomes difficult to understand as a single expression.

Do not optimise for fewer lines at the expense of readability.

## Evaluation Behaviour

List comprehensions are eager. The resulting list is built immediately when the comprehension is evaluated.

This will later be contrasted with generator expressions, which are lazy.

## Current Learning Boundary

Covered here:

- list comprehension syntax
- transformation
- value extraction
- filtering with `if`
- filtering + transformation
- basic readability/engineering judgement
- eager evaluation

Not covered yet:

- conditional expressions inside comprehensions
- nested comprehensions
- set comprehensions
- dictionary comprehensions
- generator expressions

## Practice Completed

1. Square each number in a list.
2. Extract names from a list of user dictionaries.
3. Filter active user records.
4. Filter active users and extract their names.

All four exercises were completed correctly.
