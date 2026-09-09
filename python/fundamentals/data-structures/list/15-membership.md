# List Membership

## Mental Model

The `in` and `not in` operators test whether an object is present among the elements of a list.

```python
users = ["Alice", "Bob", "Charlie"]

"Bob" in users        # True
"David" in users      # False
"David" not in users  # True
```

## Key Distinction

Membership is different from indexing:

- `"Bob" in users` asks whether the object exists in the list.
- `users[1]` retrieves the object at position `1`.

## Engineering Priority

Membership checks are useful for validating whether a value or permission exists before performing an operation.
