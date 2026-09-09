# `len()`

`len()` returns the number of elements currently contained in a list.

```python
items = ["A", "B", "C", "D", "E"]

len(items)
# 5
```

## Length vs Index

Length counts elements; indexing identifies a position.

For five elements:

```text
index:  0   1   2   3   4
value:  A   B   C   D   E
```

Therefore:

```python
len(items)       # 5
items[4]         # "E"
len(items) - 1   # 4, the last index
```

## Mental Model

For a non-empty list, the last valid positive index is `len(list) - 1`.
