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

The trailing `if` controls which items are included. The expression before `for` controls what is placed into the new list.

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

## Conditional Expressions

A conditional expression can change the value produced for each item:

```python
labels = [
    "even" if num % 2 == 0 else "odd"
    for num in numbers
]
```

This is different from a trailing filter.

### Trailing `if` — Filtering

```python
[num for num in numbers if num % 2 == 0]
```

Only even numbers are included.

### `if ... else` — Conditional Transformation

```python
["even" if num % 2 == 0 else "odd" for num in numbers]
```

Every number is included, but the produced value changes based on the condition.

### Filtering + Conditional Transformation

Both can be used together:

```python
[
    (record["name"], "adult")
    if record["age"] >= 18
    else (record["name"], "minor")
    for record in users
    if record["active"]
]
```

The conceptual flow is:

```text
iterate -> filter -> conditionally transform -> collect
```

## Nested List Comprehensions

A nested comprehension represents nested loops.

Normal nested loops:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

result = []

for row in matrix:
    for number in row:
        result.append(number)
```

Equivalent nested comprehension:

```python
result = [
    number
    for row in matrix
    for number in row
]
```

Mental model:

> For each `row` in `matrix`, for each `number` in `row`, produce `number`.

The order of the `for` clauses follows the same order as the normal nested loops.

### Nested Filtering

A condition can be applied to the innermost iteration:

```python
result = [
    number
    for row in matrix
    for number in row
    if number % 2 == 0
]
```

This produces only the even numbers from all rows.

### Nested Records

Nested comprehensions are also useful when records are grouped inside another collection:

```python
users = [
    [
        {"name": "Subir", "active": True},
        {"name": "Rahul", "active": False},
    ],
    [
        {"name": "Amit", "active": True},
        {"name": "Priya", "active": True},
    ],
]

active_names = [
    record["name"]
    for group in users
    for record in group
    if record["active"]
]
```

The conceptual flow is:

```text
outer iteration -> inner iteration -> filter -> transform -> collect
```

### Engineering Judgement

Nested comprehensions are not automatically better than nested loops.

Use them when the iteration and transformation remain easy to read. Prefer normal loops when there are multiple business decisions, complex branching, detailed error handling, or enough nesting that the reader has to mentally decode the expression.

The goal is readable Python, not the fewest possible lines.

## Engineering Judgement

A comprehension is not automatically better than a normal loop.

Use a comprehension when the operation is simple and readable. Prefer a normal loop when the logic becomes complex, contains multiple business decisions, requires detailed error handling, or becomes difficult to understand as a single expression.

Do not optimise for fewer lines at the expense of readability.

PEP 8 readability is part of the implementation standard throughout the roadmap.

## Evaluation Behaviour

List comprehensions are eager. The resulting list is built immediately when the comprehension is evaluated.

This will later be contrasted with generator expressions, which are lazy.

## Current Learning Boundary

Covered here:

- list comprehension syntax
- transformation
- value extraction
- filtering with trailing `if`
- filtering + transformation
- conditional expressions inside comprehensions
- filtering + conditional transformation
- nested list comprehensions
- nested iteration and nested filtering
- basic readability/engineering judgement
- eager evaluation

Not covered yet:

- set comprehensions
- dictionary comprehensions
- generator expressions

## Practice Completed

1. Square each number in a list.
2. Extract names from a list of user dictionaries.
3. Filter active user records.
4. Filter active users and extract their names.
5. Filter active users and produce `(name, "adult"/"minor")` tuples using a conditional expression.
6. Flatten a nested list with a nested comprehension.
7. Flatten a nested list and keep only even numbers.
8. Extract active names from nested user groups.
9. Filter nested employee records by salary and extract their names.
10. Filter nested employee records by salary and produce formatted strings.
11. Apply a string method as the transformation in a nested comprehension.

All completed exercises were correct after the active-user filtering requirement was added to the final exercise.
