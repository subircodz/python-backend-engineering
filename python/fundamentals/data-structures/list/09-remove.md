# `remove()`

`remove(value)` removes the **first matching occurrence by value**.

```python
numbers = [10, 20, 30, 20, 40]
numbers.remove(20)
```

Result:

```python
[10, 30, 20, 40]
```

Only the first `20` is removed.

## Important Distinction

`remove()` works by **value**, not by index.

```python
numbers.remove(1)
```

means “remove the value `1`”, not “remove the element at index `1`”.

If the value does not exist, Python raises `ValueError` and the list is unchanged.
