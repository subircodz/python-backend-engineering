# List `sort()` vs `sorted()`

## `sort()`

`sort()` is a list method. It sorts the existing list **in place** and returns `None`.

```python
numbers = [4, 1, 3, 2]
result = numbers.sort()

numbers # [1, 2, 3, 4]
result  # None
```

## `sorted()`

`sorted()` is a built-in function. It does not mutate the original list; it returns a new list.

```python
numbers = [4, 1, 3, 2]
result = sorted(numbers)

numbers # [4, 1, 3, 2]
result  # [1, 2, 3, 4]
```

Both support `key=` and `reverse=`.

## Engineering Priority

The important distinction is mutation versus a new result:

- `list.sort()` → mutate this list, return `None`
- `sorted(iterable)` → create and return a new list
