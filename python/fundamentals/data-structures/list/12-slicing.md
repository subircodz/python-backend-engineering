# List Slicing

List slicing selects part of a list using this form:

```python
sequence[start:stop:step]
```

The rules are:

- `start` is included.
- `stop` is excluded.
- `step` controls how the indexes are visited.
- A positive `step` moves forward.
- A negative `step` moves backward.

Example:

```python
numbers = [10, 20, 30, 40, 50]

numbers[1:4]  # [20, 30, 40]
numbers[:3]   # [10, 20, 30]
numbers[2:]   # [30, 40, 50]
numbers[:]    # [10, 20, 30, 40, 50]
```

## Step

`step` decides how far Python moves between selected indexes.

```python
numbers = [0, 1, 2, 3, 4, 5, 6]

numbers[1:6:2]
# [1, 3, 5]
```

Python starts at index `1`, stops before index `6`, and moves two positions at a time.

## Negative step

A negative step makes Python move from right to left.

```python
numbers = [10, 20, 30, 40, 50, 60]

numbers[::-1]
# [60, 50, 40, 30, 20, 10]

numbers[4:1:-1]
# [50, 40, 30]

numbers[5:1:-2]
# [60, 40]
```

## Object behaviour

A normal slice creates a **new list**. The new list contains references to the selected elements.

So slicing creates a new outer list, but it does not automatically deep-copy mutable objects inside it.

```python
items = [[1, 2], [3, 4]]
other = items[:]
```

`items` and `other` are different list objects, but their inner lists are shared.

## Engineering mental model

Think of a slice as:

> Start here → move using `step` → stop before `stop`.

For a normal slice, the original list is not changed.