# `extend()`

`extend(iterable)` takes elements from another **iterable** and adds them to the existing list one by one.

```python
users = ["Alice", "Bob"]
users.extend(["Charlie", "David"])
```

Result:

```python
["Alice", "Bob", "Charlie", "David"]
```

The existing list is mutated.

## Mental model

Think of `extend()` as:

> Iterate over the supplied object and append each element to this list.

The argument does not have to be a list.

```python
items.extend([1, 2, 3])
items.extend((1, 2, 3))
items.extend({1, 2, 3})
items.extend("subir")
items.extend({"name": "Subir", "age": 38})
```

These add list elements from a list, tuple, set, string, and dictionary respectively.

For a dictionary, iteration gives its **keys**, not its values.

A set does not provide a sequence order to rely on, so do not use `extend()` with a set when element order matters.

An object that is not iterable raises `TypeError`:

```python
items.extend(10)  # TypeError
```

## `append()` vs `extend()`

```python
items.append([1, 2])
# adds the list [1, 2] as one element

items.extend([1, 2])
# adds 1 and 2 as separate elements
```

The important question is: **Do I want to add this object, or the elements inside it?**
