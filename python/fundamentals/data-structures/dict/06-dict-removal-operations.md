# Dictionary Removal Operations

Several operations remove dictionary data. They are not interchangeable.

## `del`

Use `del` when you only need to remove a known key.

```python
del user["age"]
```

It does not return the removed value. A missing key raises `KeyError`.

## `pop()`

Use `pop()` when you need the removed value.

```python
age = user.pop("age")
```

The key is removed and its value is returned.

A default can be supplied:

```python
age = user.pop("age", None)
```

If the key is missing, the default is returned instead of raising `KeyError`.

## `popitem()`

`popitem()` removes and returns one key-value pair.

```python
key, value = user.popitem()
```

In modern Python, this removes the last inserted pair.

The returned object is a tuple:

```python
(key, value)
```

## `clear()`

`clear()` removes all mappings from the existing dictionary.

```python
user.clear()
```

It mutates the dictionary and returns `None`.

This is different from:

```python
user = {}
```

The second statement rebinds `user` to a new dictionary.

## Quick choice

| Operation | Removes | Returns |
|---|---|---|
| `del d[key]` | one known key | nothing useful |
| `d.pop(key)` | one known key | removed value |
| `d.popitem()` | one pair | `(key, value)` |
| `d.clear()` | everything | `None` |

Choose the operation that matches the intent of the code.