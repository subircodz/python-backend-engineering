# `append()`

`append(object)` adds exactly **one object** to the end of the existing list.

```python
users = ["Alice", "Bob"]
users.append("Charlie")
```

Result:

```python
["Alice", "Bob", "Charlie"]
```

The operation mutates the existing list.

## Important Edge Case

If the object passed to `append()` is itself a list, that list becomes one element:

```python
users = ["Alice", "Bob"]
users.append(["Charlie", "David"])
```

Result:

```python
["Alice", "Bob", ["Charlie", "David"]]
```

`append()` adds the supplied object itself; it does not iterate through it.
