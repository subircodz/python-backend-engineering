# `len()`

`len()` returns the number of elements currently stored in a list.

```python
items = ["A", "B", "C", "D", "E"]

len(items)
# 5
```

## Length vs index

Length tells you **how many elements** the list has. An index tells you **which position** to access.

For five elements:

```text
index:  0   1   2   3   4
value:  A   B   C   D   E
```

Therefore:

```python
len(items)       # 5
items[4]         # "E"
len(items) - 1   # 4, the last valid positive index
```

## Empty list

An empty list has length `0` and has no valid index.

```python
items = []

len(items)  # 0
```

Trying `items[0]` raises `IndexError`.

## Engineering mental model

For a non-empty list:

> number of elements = `len(items)`
>
> last positive index = `len(items) - 1`

`len()` reads the current size of the list. It does not change the list.