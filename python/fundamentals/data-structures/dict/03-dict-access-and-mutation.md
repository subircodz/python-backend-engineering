# Dictionary Access and Mutation

## Read a value

Use the key inside `[]`.

```python
user = {"name": "Subir", "age": 38}

name = user["name"]
```

The expression returns the value mapped to that key.

## Missing key

If the key does not exist, `[]` raises `KeyError`.

```python
user["email"]
```

This fails because `email` is not present.

## Add a key

Assignment adds a new mapping when the key is not already present.

```python
user["email"] = "subir@example.com"
```

## Change a key

The same syntax changes an existing mapping.

```python
user["age"] = 39
```

So this operation has two possible results:

```text
key absent  → add mapping
key present → replace value
```

## Mutation vs rebinding

This changes the existing dictionary:

```python
user["age"] = 39
```

The dictionary object is mutated.

This is different:

```python
user = {"name": "Rahul"}
```

Here the variable is rebound to another dictionary object.

Keep the two ideas separate because other references to the original dictionary behave differently.

## Delete a key

```python
del user["age"]
```

This removes the mapping for `age`.

If the key does not exist, `del` raises `KeyError`.

## Engineering mental model

Think of a dictionary as mappings that can change:

```text
user["age"]       → lookup
user["age"] = 39  → add or replace mapping
del user["age"]   → remove mapping
```

The syntax is simple, but the important part is understanding whether the code is reading, adding, replacing, or removing a mapping.