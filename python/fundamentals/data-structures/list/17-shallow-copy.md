# List Shallow Copy

## Mental Model

```python
items = ["A", "B", "C"]
copy_items = items.copy()
```

`copy()` creates a new outer list object. The element references are initially shared.

Replacing a slot in one list does not change the other:

```python
items[0] = "X"
```

For nested mutable objects, the inner objects are still shared:

```python
items = [["A", "B"], ["C", "D"]]
copy_items = items.copy()

items[0].append("X")
```

Both lists observe the changed inner list.

### Rebinding vs Mutation

These are different:

```python
items[0] = ["X", "Y"]
```

This replaces the outer list's slot, so a shallow copy is unaffected at that slot.

```python
items[0].append("X")
```

This mutates the shared inner list, so both lists observe the change.

## Important Example

```python
users = [{"name": "Alice"}, {"name": "Bob"}]
backup = users.copy()
users[0]["name"] = "Subir"
```

Both `users[0]` and `backup[0]` refer to the same dictionary, so both show `{"name": "Subir"}`.

## Engineering Priority

A shallow copy separates the outer container, not the nested mutable objects it contains. This distinction is critical when working with nested data structures.
