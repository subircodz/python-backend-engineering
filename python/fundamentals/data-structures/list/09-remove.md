# `remove()`

`remove(value)` removes the **first matching object by value** from the list.

```python
numbers = [10, 20, 30, 20, 40]
numbers.remove(20)
```

Result:

```python
[10, 30, 20, 40]
```

Only the first `20` is removed.

## Value, not index

`remove()` searches for a matching value. It does not treat its argument as a position.

```python
numbers = [10, 20, 30]
numbers.remove(1)
```

This means:

> Find the value `1` and remove its first occurrence.

It does **not** mean “remove the object at index `1`”.

For position-based removal, use `pop(index)` or `del` when appropriate.

## If the value is missing

```python
numbers = [10, 20, 30]
numbers.remove(99)
```

Python raises `ValueError` and the list remains unchanged.

## Duplicate values

Only the first matching occurrence is removed:

```python
items = ["A", "B", "A", "C", "A"]
items.remove("A")
```

Result:

```python
["B", "A", "C", "A"]
```

`remove()` does not return the removed object. If the removed value is needed, `pop()` is usually the better operation when removal can be expressed by position.
