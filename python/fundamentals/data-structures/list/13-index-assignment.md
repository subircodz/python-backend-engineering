# Updating a List by Index

An existing element can be replaced by assigning to its index.

```python
users = ["Alice", "Bob", "Charlie"]
users[1] = "Subir"
```

Result:

```python
["Alice", "Subir", "Charlie"]
```

## Mental Model

Index assignment **rebinds the slot at that index** to another object.

It does not insert an additional element:

- the list object remains the same
- the list length remains unchanged
- the object previously stored at that index is replaced in that slot

This is different from `insert()`, which adds a new element and shifts existing elements.
