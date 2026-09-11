# `clear()`

`clear()` removes all elements from the **existing list object**.

```python
items = ["A", "B"]
other = items

items.clear()
```

Both names still point to the same list object, so both now see:

```python
items  # []
other  # []
```

## Mutation vs rebinding

The important difference is between clearing the existing object and assigning a new object.

```python
items = ["A", "B"]
other = items

items.clear()
```

`clear()` mutates the list. `other` sees that mutation because it references the same list.

Compare it with:

```python
items = ["A", "B"]
other = items

items = []
```

Here `items = []` creates a new list and rebinds the name `items` to it. The old list is still referenced by `other`.

```python
items  # []
other  # ["A", "B"]
```

## Engineering use

Use `clear()` when the existing list object must be emptied and other references should observe that change.

If the intention is to make one name point to a new list without changing the old list, use assignment instead.