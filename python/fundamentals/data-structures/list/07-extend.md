# `extend()`

`extend(iterable)` iterates over the supplied iterable and adds its elements individually to the existing list.

```python
users = ["Alice", "Bob"]
users.extend(["Charlie", "David"])
```

Result:

```python
["Alice", "Bob", "Charlie", "David"]
```

## Mental Model

> `extend()` asks the supplied object for its elements by iterating over it, then adds those elements to the list.

It accepts an **iterable**, not specifically a list.

Examples:

```python
items.extend([1, 2, 3])       # list
items.extend((1, 2, 3))       # tuple
items.extend({1, 2, 3})       # set; do not rely on order
items.extend("subir")        # individual characters
items.extend({"name": "Subir", "age": 38})  # dictionary keys
```

An integer is not iterable:

```python
items.extend(10)  # TypeError
```

## `append()` vs `extend()`

- `append(x)` adds `x` as one element.
- `extend(iterable)` adds the iterable's elements individually.
