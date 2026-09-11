# `insert()`

`insert(index, object)` adds one object at a specific position in the list.

```python
numbers = [10, 30, 40]
numbers.insert(1, 20)
```

Result:

```python
[10, 20, 30, 40]
```

## What Python changes

`insert()` changes the structure of the existing list:

1. A new element is added.
2. The element currently at that position, and the elements after it, move one position to the right.
3. The list length increases by one.

So this:

```python
[10, 30, 40]
```

becomes:

```text
index:   0   1   2
value:  10  30  40
```

After `insert(1, 20)`:

```text
index:   0   1   2   3
value:  10  20  30  40
```

## `insert()` vs index assignment

These operations are different:

```python
numbers[1] = 20
```

replaces the object already stored at index `1`. The list length does not change.

```python
numbers.insert(1, 20)
```

adds a new element and shifts existing elements. The list length increases.

## `append()` connection

`append()` is effectively the normal way to add an element at the end of a list. Use `insert()` when the position itself matters.
