# List Basics

## Mental Model

A Python list is a **mutable, ordered collection of objects**.

- **Ordered** means each element has a defined position in the sequence.
- It does **not** mean the elements are sorted.
- **Mutable** means the existing list object can be changed after creation.
- A list can contain objects of different types.

Example:

```python
items = [10, 5000, 2, "Subir"]
```

The elements are not sorted, but they are ordered because each element has a defined position.

## Key Distinction

- Ordered → positional sequence
- Sorted → arranged according to a comparison or criterion

## Engineering Priority

This mental model is important because indexing, mutation, iteration, and list operations all depend on the idea that a list stores objects in defined positions.
