# Dictionary Membership

## `in` checks keys

For a dictionary, `in` checks keys by default.

```python
user = {
    "name": "Subir",
    "age": 38,
}

"name" in user
```

This is `True` because `name` is a key.

A value is not checked by default:

```python
"Subir" in user
```

This is `False` because `Subir` is a value, not a key.

## Check values

Use `values()` when the requirement is to search values.

```python
"Subir" in user.values()
```

## Check a key-value pair

Use `items()` when both the key and value matter.

```python
("name", "Subir") in user.items()
```

## Practical validation

A common backend pattern is checking required fields.

```python
required_fields = {"username", "email"}

for field in required_fields:
    if field not in request_data:
        print(f"Missing field: {field}")
```

The code is asking whether each required key exists.

## `in` vs `get()`

These answer different questions:

```python
"email" in user
```

asks:

> Does this key exist?

Whereas:

```python
user.get("email")
```

asks:

> What value is mapped to this key, if it exists?

If `None` is a valid stored value, membership is especially useful because it separates a missing key from a present key whose value is `None`.

## Mental model

For a dictionary:

```text
in            → key existence
in d.values() → value existence
in d.items()  → pair existence
```

This follows the main purpose of a dictionary: key-based lookup.