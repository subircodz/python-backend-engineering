# List Basics

A Python list is a **mutable, ordered collection of objects**.

```python
items = [10, 5000, 2, "Subir"]
```

## What “ordered” means

Each object has a position in the list.

```text
10      → position 0
5000    → position 1
2       → position 2
"Subir" → position 3
```

Ordered does **not** mean sorted.

The example above is ordered because every item has a position. It is not sorted because the values are not arranged by a sorting rule.

## What “mutable” means

The same list object can be changed after it is created.

```python
items[0] = 99
```

The list now contains `99` at position `0`.

The list object was changed; a new list was not required.

## Lists store objects

A list can contain objects of different types:

```python
items = [10, "Subir", [1, 2], None]
```

The important point is that a list stores references to objects. The objects themselves do not have to be the same type.

## Ordered vs sorted

- **Ordered** → elements have positions.
- **Sorted** → elements are arranged using a sorting rule.

Do not use these words as if they mean the same thing.

## Why this matters

Indexing, iteration, mutation, slicing, and list methods all depend on this basic model:

> A list is one mutable object containing objects at defined positions.
