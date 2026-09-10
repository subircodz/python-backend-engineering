# Tuple Fundamentals

## 1. What is a tuple?

A tuple is an ordered Python collection whose own structure is immutable.

```python
numbers = (10, 20, 30)
```

`numbers` is a name referring to a tuple object.

The important difference from a list is not simply `()` versus `[]`:

- list → mutable
- tuple → immutable

---

## 2. Tuple indexing

Tuples support positional access just like lists.

```python
person = ("Subir", 38, "Python")

person[0]   # "Subir"
person[1]   # 38
person[-1]  # "Python"
```

Reading an element does not modify the tuple.

---

## 3. Tuple element assignment is not allowed

```python
numbers = (10, 20, 30)
numbers[0] = 99
```

This raises `TypeError` because the tuple's structure cannot be mutated.

The tuple remains:

```python
(10, 20, 30)
```

---

## 4. Immutability does not prevent rebinding

This is allowed:

```python
numbers = (10, 20, 30)
numbers = (99, 20, 30)
```

The existing tuple was not changed. A new tuple was created and the name `numbers` was rebound to it.

Mental model:

```text
Before:
numbers ─────→ (10, 20, 30)

After:
numbers ─────→ (99, 20, 30)
```

So:

```python
numbers[0] = 99       # mutation → not allowed
numbers = (99, 20, 30) # rebinding → allowed
```

---

## 5. Tuples can contain different types

```python
employee = ("Subir", 101, 60000, True)
```

A tuple can contain objects of different types. There is no requirement that all elements have the same type.

---

## 6. Immutable tuple containing mutable objects

Tuple immutability applies to the tuple's own structure. It does not automatically make contained objects immutable.

```python
data = ([10, 20], [30, 40])
```

This is not allowed:

```python
data[0] = [100, 200]
```

because it tries to replace an element of the tuple.

But this is allowed:

```python
data[0].append(99)
```

because the operation mutates the list object stored inside the tuple.

Result:

```python
([10, 20, 99], [30, 40])
```

Important rule:

> A tuple being immutable does not make the objects stored inside it immutable.

---

## 7. Why tuples are useful

Use a tuple when values form a fixed ordered group and the structure should not be changed.

Examples:

```python
coordinates = (10, 20)
rgb = (255, 128, 0)
employee = ("Subir", 101, "Developer")
```

The engineering reason is often structural intent: the collection itself represents a fixed set of positions.

Do not reduce the choice to "tuple is faster than list". Mutability and intended data semantics are usually more important design considerations.

---

## 8. Tuple unpacking

A tuple can be unpacked into multiple names:

```python
employee = ("Subir", 101, "Developer")

name, employee_id, role = employee
```

After unpacking:

```text
name        → "Subir"
employee_id → 101
role        → "Developer"
```

This is called tuple unpacking. The detailed binding rules will be studied separately.

---

## Core mental model

```python
items = (10, 20, 30)
```

### Read

```python
items[0]
```

Allowed.

### Mutate tuple structure

```python
items[0] = 99
```

Not allowed.

### Rebind the name

```python
items = (99, 20, 30)
```

Allowed.

### Mutate a mutable object stored inside

```python
items = ([10, 20], [30, 40])
items[0].append(99)
```

Allowed because the list object is being mutated, not the tuple structure.

## Summary

- Tuple is ordered.
- Tuple supports indexing and negative indexing.
- Tuple's own structure is immutable.
- Rebinding a name that refers to a tuple is still allowed.
- A tuple can contain objects of different types.
- A tuple can contain mutable objects such as lists.
- Mutating a contained mutable object is different from mutating the tuple structure.
- Tuple unpacking binds multiple names from tuple elements.
