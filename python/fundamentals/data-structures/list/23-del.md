# `del` with Lists

## Mental Model

`del` is a Python statement that can remove a list element by index.

```python
items = ["A", "B", "C", "D"]
del items[1]
# ["A", "C", "D"]
```

It can also delete a slice:

```python
items = ["A", "B", "C", "D", "E"]
del items[1:4]
# ["A", "E"]
```

The existing list is mutated.

## Related Operations

- `remove(value)` → remove by value; returns `None`
- `pop(index)` → remove by index and return the removed object
- `del items[index]` → remove by index; no returned value

## Engineering Priority

Choose based on whether you need removal by value, removal by position with the removed object, or deletion without needing the removed object.
