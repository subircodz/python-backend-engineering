# `pop()`

`pop(index)` removes the element at the specified index **and returns the removed object**.

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

## Default Behaviour

Calling `pop()` without an index removes and returns the last element.

```python
items = ["A", "B", "C"]
removed = items.pop()
```

Result:

```python
items   # ["A", "B"]
removed # "C"
```

## Errors

- Invalid index → `IndexError`
- Empty list with `pop()` → `IndexError`

## Mental Model

`pop()` is useful when the removed value itself is needed by the program.
