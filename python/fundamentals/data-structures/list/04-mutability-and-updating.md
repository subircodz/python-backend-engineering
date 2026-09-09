# List Mutability and Updating

Lists are mutable: an existing list object can be changed after creation.

```python
users = ["Alice", "Bob", "Charlie"]
users[1] = "Subir"
```

Result:

```python
["Alice", "Subir", "Charlie"]
```

## Mental Model

Index assignment does not insert a new element. It **rebinds the slot at that index** to the new object.

The list object remains the same list, and its length does not change.

This connects two core ideas:

- indexing identifies a position
- mutability allows the object stored at that position to be changed
