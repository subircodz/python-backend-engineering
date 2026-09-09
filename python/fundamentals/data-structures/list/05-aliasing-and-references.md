# List Aliasing and References

Consider:

```python
users = ["Alice", "Bob", "Charlie"]
other = users
users[1] = "Subir"
```

Both `users` and `other` refer to the **same list object**.

Therefore:

```python
users
# ["Alice", "Subir", "Charlie"]

other
# ["Alice", "Subir", "Charlie"]
```

## Mental Model

Assignment of a list variable does not automatically copy the list. It creates another reference to the same object.

This matters whenever mutable objects are shared between parts of an application.
