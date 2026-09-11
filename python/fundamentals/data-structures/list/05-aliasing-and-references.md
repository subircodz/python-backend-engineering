# List Aliasing and References

Consider this code:

```python
users = ["Alice", "Bob", "Charlie"]
other = users

users[1] = "Subir"
```

`users` and `other` now refer to the **same list object**.

```text
users ──┐
        ├──> ["Alice", "Subir", "Charlie"]
other ──┘
```

So both names see the change:

```python
users
# ["Alice", "Subir", "Charlie"]

other
# ["Alice", "Subir", "Charlie"]
```

## Assignment does not copy the list

This:

```python
other = users
```

does not create another list. It creates another reference to the existing list.

If the list is mutated through either name, the change is visible through the other name as well.

## Why this matters

Shared mutable objects can be useful, but they can also cause unexpected changes when different parts of an application hold references to the same object.

When reviewing code, ask:

> Are these two names referring to the same mutable object, or are they referring to separate objects?

That question is often more useful than simply saying that a variable “contains a list.”
