# `reversed()`

## Mental Model

`reversed()` is a built-in function that does **not** mutate the original list. It returns a reverse iterator.

```python
numbers = [1, 2, 3, 4]
result = reversed(numbers)

numbers            # [1, 2, 3, 4]
list(result)       # [4, 3, 2, 1]
```

## `reverse()` vs `reversed()`

- `reverse()` → list method, mutates the list, returns `None`
- `reversed()` → built-in, leaves the original unchanged, returns an iterator

## Engineering Priority

Recognize that `reversed()` produces a lazy iterator rather than a new list. Convert it with `list()` when an actual list is required.
