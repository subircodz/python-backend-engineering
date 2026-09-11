# List Membership

Use `in` and `not in` to check whether an object is present among the elements of a list.

```python
users = ["Alice", "Bob", "Charlie"]

"Bob" in users        # True
"David" in users      # False
"David" not in users  # True
```

## Membership vs indexing

These operations answer different questions.

```python
"Bob" in users
```

asks:

> Is `"Bob"` present in the list?

While:

```python
users[1]
```

asks:

> What object is stored at index `1`?

Membership does not give you the position. It gives a boolean result: `True` or `False`.

## Engineering use

Membership checks are useful before an operation when the code needs to know whether a value already exists.

```python
if user in allowed_users:
    grant_access()
```

## Important behaviour

For a list, membership checks examine the elements of the list. If the list is large and membership checks happen frequently, choosing a different data structure such as a `set` may be more suitable.

The choice depends on the required behaviour, not only on the syntax.