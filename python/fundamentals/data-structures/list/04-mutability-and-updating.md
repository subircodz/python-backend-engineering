# List Mutability and Updating

A list is **mutable**, so the existing list object can be changed after creation.

```python
users = ["Alice", "Bob", "Charlie"]
users[1] = "Subir"
```

The list becomes:

```python
["Alice", "Subir", "Charlie"]
```

## What Python changes

This statement:

```python
users[1] = "Subir"
```

changes the object stored in index `1`.

It does not insert a new element, so the list length stays the same.

The important distinction is:

```text
users
  ↓
list object
  ├── index 0 → "Alice"
  ├── index 1 → "Subir"   ← changed
  └── index 2 → "Charlie"
```

The list object itself remains the same object.

## Mutation vs rebinding

Changing a list through an operation such as index assignment is a **mutation** of the list.

Changing what a variable name refers to is **rebinding**.

```python
users[1] = "Subir"   # mutate the list

users = ["New"]      # rebind the name `users`
```

These are different operations.

## Why this matters

Many Python bugs become easier to understand when you first ask:

> Did the existing object change, or did the variable start referring to another object?

For lists, this distinction is especially important when the same list is referenced from more than one place.
