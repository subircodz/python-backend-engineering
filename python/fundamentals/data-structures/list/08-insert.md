# `insert()`

`insert(index, object)` inserts one object at a specified position and shifts existing elements to the right.

```python
numbers = [10, 30, 40]
numbers.insert(1, 20)
```

Result:

```python
[10, 20, 30, 40]
```

## Mental Model

Unlike index assignment, `insert()` changes the structure of the list:

- a new element is added
- elements at and after the insertion point shift right
- list length increases by one

`append()` is the specialized case for adding at the end.
