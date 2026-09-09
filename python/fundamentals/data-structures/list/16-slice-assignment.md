# List Slice Assignment

## Mental Model

A normal slice creates a new list containing references to the selected elements:

```python
numbers = [10, 20, 30, 40, 50]
part = numbers[1:4]
```

But assigning to a slice modifies the existing list in place:

```python
numbers[1:4] = [99, 88, 77]
# [10, 99, 88, 77, 50]
```

The replacement can contain a different number of elements, so slice assignment can grow or shrink a list.

```python
numbers[1:4] = [99]
# [10, 99, 50]
```

```python
numbers[1:2] = [20, 30, 40]
# [10, 20, 30, 40, 30, 40, 50]
```

The right-hand side can be any iterable, not only a list:

```python
items = ["A", "B", "C", "D"]
items[1:3] = "XYZ"
# ["A", "X", "Y", "Z", "D"]
```

## Replacing All Contents

```python
numbers[:] = [100, 200, 300]
```

This replaces all elements while preserving the existing list object.

## Engineering Priority

Understand the difference between creating a slice and assigning to a slice. Slice assignment is an in-place mutation.
