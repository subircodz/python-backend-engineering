# Negative Indexing

Python lists support indexing from the **right side** using negative numbers.

```python
users = ["Alice", "Bob", "Charlie"]
```

```python
users[-1]   # "Charlie"
users[-2]   # "Bob"
users[-3]   # "Alice"
```

## Mental Model

`-1` means the last object.

Then Python moves left as the number becomes more negative:

```text
-3      -2      -1
 ↓       ↓       ↓
Alice   Bob    Charlie
```

Negative indexing is useful when the code cares about a position relative to the end of the list.

## Invalid index

If the negative index goes beyond the start of the list, Python raises `IndexError`.

```python
users[-4]
# IndexError
```

## Why this matters

Negative indexing avoids calculating the last position manually.

> `-1` → last object
>
> `-2` → second-last object
