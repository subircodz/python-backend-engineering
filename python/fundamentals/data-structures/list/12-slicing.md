# List Slicing

Slicing follows:

```python
sequence[start:stop:step]
```

Core rules:

- `start` is included
- `stop` is excluded
- `step` controls movement
- positive step moves forward
- negative step moves backward

Example:

```python
numbers = [10, 20, 30, 40, 50]

numbers[1:4]  # [20, 30, 40]
numbers[:3]   # [10, 20, 30]
numbers[2:]   # [30, 40, 50]
numbers[:]    # [10, 20, 30, 40, 50]
```

With a step:

```python
numbers = [0, 1, 2, 3, 4, 5, 6]
numbers[1:6:2]
# [1, 3, 5]
```

## Negative Step

```python
numbers[::-1]
# reversed order
```

A negative step means movement is backward. Reversal is the resulting behaviour when the slice covers the sequence in that direction.

Example:

```python
numbers = [10, 20, 30, 40, 50, 60]
numbers[4:1:-1]   # [50, 40, 30]
numbers[5:1:-2]   # [60, 40]
```

## Mental Model

> `start` = where to begin, `stop` = where to stop (excluded), `step` = how far to move.

A normal slice creates a new list containing references to the selected elements.
