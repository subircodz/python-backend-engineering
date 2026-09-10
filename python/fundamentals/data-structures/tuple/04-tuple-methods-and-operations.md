# Tuple Methods and Operations

## Overview

A tuple is an immutable ordered sequence. Its own structure cannot be changed, but many operations can read it or create a new tuple.

Tuple provides only two main methods: `count()` and `index()`. Other common operations are implemented through operators, built-ins, or sequence behavior.

---

## 1. `count()`

`count(value)` returns how many times a value occurs in the tuple.

```python
numbers = (10, 20, 10, 30, 10)

result = numbers.count(10)

print(result)  # 3
```

- Returns an integer.
- Does not mutate the tuple.

Mental model:

> `count()` asks: **How many occurrences are there?**

---

## 2. `index()`

`index(value)` returns the position of the **first occurrence** of a value.

```python
numbers = (10, 20, 30, 20, 40)

result = numbers.index(20)

print(result)  # 1
```

If the value is not found, `index()` raises `ValueError`.

Mental model:

> `index()` asks: **Where is the first occurrence?**

---

## 3. Tuple concatenation with `+`

`+` creates a new tuple by joining tuples.

```python
first = (10, 20)
second = (30, 40)

result = first + second

print(result)  # (10, 20, 30, 40)
```

The original tuples are unchanged.

Tuple and list cannot be concatenated directly:

```python
(10, 20) + [30, 40]  # TypeError
```

---

## 4. Tuple repetition with `*`

`*` creates a new tuple containing repeated elements.

```python
numbers = (10, 20)

result = numbers * 3

print(result)  # (10, 20, 10, 20, 10, 20)
```

The original tuple is unchanged.

Important: repetition repeats references to contained objects; it does not deep-copy nested mutable objects.

---

## 5. `+=` with tuples

Tuple `+=` **does work**, but it does not mutate the existing tuple.

```python
numbers = (10, 20, 30)
numbers += (40,)

print(numbers)  # (10, 20, 30, 40)
```

Conceptually, this is similar to:

```python
numbers = numbers + (40,)
```

A new tuple is created and `numbers` is rebound to it. The old tuple becomes unreachable if no other reference exists.

The operand must be a tuple for tuple concatenation:

```python
numbers += [40]   # TypeError
numbers += (40,)  # works
```

Contrast with lists:

```python
numbers = [10, 20, 30]
numbers += [40]
```

For a list, `+=` normally mutates the existing list in place.

---

## 6. Membership: `in` and `not in`

Membership testing returns a Boolean and does not mutate the tuple.

```python
numbers = (10, 20, 30, 40)

print(30 in numbers)      # True
print(50 not in numbers)  # True
```

Mental model:

> Membership asks whether a value is present; it does not modify the sequence.

---

## 7. Indexing

Tuples support normal and negative indexing.

```python
numbers = (10, 20, 30, 40)

numbers[0]   # 10
numbers[-1]  # 40
```

Attempting to assign through an index raises `TypeError` because the tuple is immutable:

```python
numbers[0] = 99  # TypeError
```

---

## 8. Slicing

Tuples support slicing. A slice produces a new tuple.

```python
numbers = (10, 20, 30, 40, 50)

numbers[1:4]  # (20, 30, 40)
numbers[-3:]  # (30, 40, 50)
numbers[::2]  # (10, 30, 50)
```

Rules:

- start is included
- stop is excluded
- omitted start means begin from the appropriate end
- omitted stop means continue to the end
- `step` controls how elements are selected

`::2` means take every second element.

Slicing does not mutate the original tuple.

---

## 9. `len()`

`len()` is a built-in function, not a tuple method.

```python
numbers = (10, 20, 30)

len(numbers)  # 3
```

It returns the number of elements in the tuple.

---

## 10. `min()`, `max()`, and `sum()`

These are built-in functions, not tuple methods.

```python
numbers = (10, 20, 30)

min(numbers)  # 10
max(numbers)  # 30
sum(numbers)  # 60
```

Their use depends on the contained values being appropriate for the operation.

---

## 11. Tuple comparison

Tuple equality compares corresponding elements in order.

```python
(10, 20) == (10, 20)  # True
(10, 20) == (20, 10)  # False
```

For ordering operators such as `<` and `>`, tuples use lexicographical comparison: compare from left to right and stop at the first pair of unequal elements.

```python
(10, 20, 30) < (10, 20, 40)  # True
```

The comparison works like this:

```text
10 == 10  -> continue
20 == 20  -> continue
30 < 40   -> True
```

Python does not need to compare later elements once the first unequal pair determines the result.

Do not treat `==` and ordering operators as exactly the same operation: equality checks corresponding values for equality, while ordering uses lexicographical ordering.

---

## 12. Immutability reminder: operations can create new tuples

An operation that appears to change a tuple usually creates a new tuple and may rebind the name.

```python
numbers = (10, 20, 30)
numbers = numbers + (40,)
```

The original tuple was not mutated. `numbers` now refers to a new tuple.

Similarly:

```python
numbers += (40,)
```

creates a new tuple and rebinds `numbers`.

---

## 13. Mutable objects inside tuples

Tuple immutability does not make contained objects recursively immutable.

```python
record = ("Subir", 101, ["Python", "SQL"])

record[2].append("FastAPI")

print(record)
# ('Subir', 101, ['Python', 'SQL', 'FastAPI'])
```

The tuple still contains the same three object references. The list object at position `2` was mutated.

This is illegal:

```python
record[2] = ["Python", "SQL", "FastAPI"]  # TypeError
```

Mental model:

> Tuple immutability applies to the tuple's own structure/references. It does not recursively freeze mutable objects stored inside it.

---

## 14. Tuple vs list: methods and operations

A tuple mainly provides:

- `count()`
- `index()`

Common tuple operations include:

- `+`
- `*`
- `in` / `not in`
- indexing
- slicing
- `len()`
- `min()` / `max()` / `sum()` where appropriate
- comparisons
- `+=` (new tuple + rebinding)

Lists have many mutation methods such as `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `clear()`, `reverse()`, and `sort()`.

---

## Production mental model

> **A tuple is an immutable ordered sequence. `count()` and `index()` read it. Operators and slicing can create new tuples. `+=` on a tuple creates a new tuple and rebinds the name; it does not mutate the existing tuple. Objects stored inside the tuple can still be mutable and can be mutated independently.**
