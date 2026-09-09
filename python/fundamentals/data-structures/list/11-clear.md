# `clear()`

`clear()` removes all elements from the existing list object.

```python
items = ["A", "B"]
other = items
items.clear()
```

Both variables now observe the same emptied list:

```python
items  # []
other  # []
```

## Mental Model

`clear()` **mutates** the existing list.

This differs from:

```python
items = []
```

which rebinds `items` to a new list object. It does not clear the old object that another variable may still reference.
