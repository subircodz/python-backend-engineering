# Updating a List by Index

Use index assignment when an existing list element needs to be replaced.

```python
users = ["Alice", "Bob", "Charlie"]

users[1] = "Subir"
```

The list becomes:

```python
["Alice", "Subir", "Charlie"]
```

## What changes

Index assignment changes the object stored in one existing list slot.

- The list object stays the same.
- The list length stays the same.
- The old object at that index is replaced.

It does **not** add a new element.

## Compare with `insert()`

`insert()` adds an element and shifts existing elements.

```python
users = ["Alice", "Bob", "Charlie"]
users.insert(1, "Subir")
```

Now the list has four elements:

```python
["Alice", "Subir", "Bob", "Charlie"]
```

So the decision is simple:

- Replace an existing position → index assignment.
- Add a new element at a position → `insert()`.

## Engineering mental model

`users[1] = "Subir"` does not rebind the name `users`. It changes what the list stores at index `1`.