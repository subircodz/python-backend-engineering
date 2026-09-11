# Nested Dictionaries

A dictionary value can itself be another dictionary.

This is common when data has groups of related fields.

```python
user = {
    "id": 101,
    "name": "Subir",
    "address": {
        "city": "Guwahati",
        "state": "Assam",
        "pincode": 781001,
    },
}
```

Here, `address` is a key in the outer dictionary. Its value is another dictionary.

## Accessing nested data

```python
user["address"]["city"]
```

Python first gets the value for `"address"`. That value is another dictionary. Then it gets `"city"` from that dictionary.

So this is simply two dictionary lookups:

```text
outer dictionary → address dictionary → city value
```

## Changing nested data

You can change a value inside the nested dictionary.

```python
user["address"]["city"] = "Jorhat"
```

This changes the existing nested dictionary.

You can also add a new key to the nested dictionary:

```python
user["address"]["country"] = "India"
```

This adds `country` inside `address`. It does not add it to the outer dictionary.

## Deeper nesting

Dictionaries can contain dictionaries at more than one level.

```python
company = {
    "name": "Example",
    "office": {
        "address": {
            "city": "Guwahati",
        }
    },
}
```

Accessing the city:

```python
company["office"]["address"]["city"]
```

Deep nesting is valid, but it becomes harder to read and increases the number of places where a key can be missing.

## Missing keys at different levels

Any missing lookup can raise `KeyError`.

```python
user["address"]["country"]
```

If `country` does not exist, the lookup fails.

If `address` itself does not exist, the first lookup fails.

Each level must contain the expected key before the next lookup can happen.

## Optional nested data

If a nested field is optional, `get()` can be used.

```python
city = user.get("address", {}).get("city")
```

If `address` is missing, `{}` is used for that lookup, so the code does not raise `KeyError` for that level.

Do not use this pattern automatically. If `address` is required by the application or API contract, silently treating it as missing may hide a data problem.

## Engineering mental model

A nested dictionary is not a special data structure. It is a dictionary containing another dictionary as a value.

When working with nested data, ask:

1. Which dictionary am I accessing?
2. Which key belongs to that dictionary?
3. Is the field required or optional?
4. Am I reading the nested object or changing it?
5. Is the nesting becoming too deep for the code to remain clear?

Nested dictionaries are common in API responses, configuration data, and structured application data. They are useful, but the code should still make ownership and missing-data behaviour clear.
