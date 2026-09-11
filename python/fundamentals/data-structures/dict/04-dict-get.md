# Dictionary `get()`

## Why `get()` exists

Direct access with `[]` expects the key to exist.

```python
email = user["email"]
```

A missing key raises `KeyError`.

`get()` is useful when a missing key is allowed.

```python
email = user.get("email")
```

If `email` is missing, this returns `None` instead of raising `KeyError`.

## Default value

A fallback can be supplied.

```python
role = user.get("role", "user")
```

If `role` exists, its value is returned. If it does not exist, `"user"` is returned.

## `[]` vs `get()`

Use `[]` when the field is required and missing data should be treated as an error.

```python
user_id = request_data["user_id"]
```

Use `get()` when the field is optional or a fallback is valid.

```python
page = request_data.get("page", 1)
```

## `get()` does not mutate the dictionary

```python
user.get("email")
```

This only reads the mapping. It does not add `email` to the dictionary.

## `None` can be a real value

This distinction matters:

```python
user = {"email": None}
```

Here the key exists, but its value is `None`.

```python
user.get("email")
```

also returns `None` when the key is absent.

If the code must distinguish these cases, check membership:

```python
if "email" in user:
    ...
```

## Engineering rule

Ask what the code expects:

- required key → `data[key]`
- optional key → `data.get(key)`
- optional key with fallback → `data.get(key, default)`
- need to distinguish missing from stored `None` → membership check