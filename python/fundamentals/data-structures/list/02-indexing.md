# List Indexing

List elements are accessed by their **position**, called an index.

```python
users = ["Alice", "Bob", "Charlie"]
```

| Index | Object |
|---:|---|
| `0` | `"Alice"` |
| `1` | `"Bob"` |
| `2` | `"Charlie"` |

```python
users[1]
# "Bob"
```

## Mental Model

Python uses **zero-based indexing**. The first position is `0`, not `1`.

When Python evaluates:

```python
users[1]
```

it looks at index `1` and gets the object currently stored there.

Indexing does not copy the list. It reads the object at that position.

## Invalid index

If the index is outside the valid range, Python raises `IndexError`.

```python
users[10]
# IndexError
```

## Why this matters

List indexing is positional access. This is different from a dictionary, where access is based on a key.

> **List → position → object**
