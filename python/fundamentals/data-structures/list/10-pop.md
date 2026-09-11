# `pop()`

`pop(index)` removes the object at a position and **returns the removed object**.

```python
items = ["A", "B", "C", "D"]
removed = items.pop(2)
```

After the operation:

```python
items
# ["A", "B", "D"]

removed
# "C"
```

The list is mutated, and the removed object is available to the caller.

## Without an index

`pop()` without an argument removes and returns the last element.

```python
items = ["A", "B", "C"]
removed = items.pop()
```

Now:

```python
items   # ["A", "B"]
removed # "C"
```

## `pop()` vs `remove()`

The two operations answer different questions:

- `remove(value)` → find the first matching value and remove it.
- `pop(index)` → remove the object at this position and return that object.
- `pop()` → remove the last object and return it.

This difference matters when the removed object must be used after removal.

## Errors

- Invalid index → `IndexError`
- `pop()` on an empty list → `IndexError`

## Engineering use

`pop()` is useful when a list is being used as a simple stack or when code needs to process an item and remove it from the list at the same time.
