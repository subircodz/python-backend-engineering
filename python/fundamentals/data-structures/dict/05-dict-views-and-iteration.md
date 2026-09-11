# Dictionary Views and Iteration

## `keys()`, `values()`, and `items()`

A dictionary provides three useful views:

```python
user.keys()
user.values()
user.items()
```

They represent:

- `keys()` → keys
- `values()` → values
- `items()` → key-value pairs

## Direct iteration

Iterating directly over a dictionary gives keys.

```python
for key in user:
    print(key)
```

This is equivalent to iterating over `user.keys()` for normal use.

## Values

```python
for value in user.values():
    print(value)
```

Use this when the keys are not needed.

## Key-value pairs

```python
for key, value in user.items():
    print(key, value)
```

`items()` returns a dictionary view. Each individual item is a tuple containing the key and value.

For example:

```python
("name", "Subir")
```

The loop uses tuple unpacking:

```python
for key, value in user.items():
```

## Views are not normal lists

The result of `keys()`, `values()`, and `items()` is a dictionary view, not a new list of all elements.

The view is connected to the dictionary and reflects later changes to that dictionary.

## Engineering mental model

Choose the view based on what the code needs:

```text
keys()   → names/identifiers
values() → stored values
items()  → key + value together
```

For backend data processing, `items()` is often the most useful because transformation logic usually needs both the field name and its value.