# `append()`

`append(object)` adds **one object** to the end of the existing list.

```python
users = ["Alice", "Bob"]
users.append("Charlie")
```

The same list object is changed:

```python
["Alice", "Bob", "Charlie"]
```

## What matters

`append()` adds the object you pass. It does **not** open that object and add its elements.

For example:

```python
users = ["Alice", "Bob"]
users.append(["Charlie", "David"])
```

Result:

```python
["Alice", "Bob", ["Charlie", "David"]]
```

The inner list is one element of `users`.

## `append()` and mutation

`append()` mutates the existing list. It does not create a new outer list for the operation.

This matters when another name refers to the same list:

```python
users = ["Alice"]
other = users
users.append("Bob")
```

Both names now see:

```python
["Alice", "Bob"]
```

## Use it when

Use `append()` when one new object should become one new list element.
