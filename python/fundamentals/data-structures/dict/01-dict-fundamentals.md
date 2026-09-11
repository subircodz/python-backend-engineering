# Dictionary Fundamentals

## What a dictionary is

A dictionary (`dict`) stores data as **key → value** mappings.

```python
user = {
    "name": "Subir",
    "age": 38,
    "role": "Python Developer",
}
```

Here:

- `"name"`, `"age"`, and `"role"` are keys.
- `"Subir"`, `38`, and `"Python Developer"` are values.

The important idea is that a dictionary is accessed by **key**, not by position.

```python
user["name"]
# "Subir"
```

This is different from a list:

```python
users = ["Subir", "Rahul", "Amit"]
users[0]
```

A list uses a position. A dictionary uses a key.

---

## A dictionary is mutable

A dictionary object can be changed after it is created.

```python
user = {"name": "Subir", "age": 38}

user["age"] = 39
```

The dictionary is changed in place.

```python
print(user)
# {'name': 'Subir', 'age': 39}
```

This is mutation. The dictionary object remains the same object; its mapping changes.

This is different from rebinding the variable:

```python
user = {"name": "Subir"}

user = {"name": "Rahul"}
```

Here `user` is made to refer to a different dictionary object.

Keep these two ideas separate:

- **Mutation** → change the existing dictionary object.
- **Rebinding** → make the variable refer to another object.

---

## Keys are unique

A dictionary cannot keep two different values for the same key.

```python
user = {
    "name": "Subir",
    "name": "Rahul",
}
```

The later value replaces the earlier one:

```python
print(user)
# {'name': 'Rahul'}
```

This matters when building dictionaries from data. If the same key is inserted again, the old value is replaced.

---

## Keys must be hashable

Dictionary keys must be **hashable**. In simple terms, Python needs to be able to calculate a stable hash value for the key so it can find the mapping efficiently.

Common valid keys:

```python
user = {
    "name": "Subir",
    101: "active",
    (10, 20): "location",
}
```

A list cannot be used directly as a key because a list is mutable and therefore not hashable.

```python
# This raises TypeError
user = {
    ["name"]: "Subir"
}
```

A useful rule is:

> Dictionary keys must be hashable. Dictionary values do not have this restriction.

For example, a list can be a value:

```python
user = {
    "skills": ["Python", "SQL"]
}
```

---

## Values can be mutable

There is no requirement for dictionary values to be immutable.

```python
user = {
    "name": "Subir",
    "skills": ["Python", "SQL"],
}
```

The list stored as the value can be changed:

```python
user["skills"].append("Git")
```

Now the existing list object has been mutated.

This becomes important when dictionaries contain lists, dictionaries, or other mutable objects. Changing the nested object is still a mutation of that object.

---

## Missing keys

Using `[]` with a key that does not exist raises `KeyError`.

```python
user = {"name": "Subir"}

user["age"]
```

Result:

```text
KeyError: 'age'
```

This is different from a missing list position:

```python
users = ["Subir"]
users[5]
```

That raises `IndexError` because the list position does not exist.

The error tells you what kind of lookup failed:

- dictionary key lookup → `KeyError`
- list position lookup → `IndexError`

---

## Dictionary vs other basic data structures

Use the structure based on what the code needs to do.

| Structure | Main access / behaviour | Typical use |
|---|---|---|
| `list` | position | ordered collection of items |
| `tuple` | position | ordered collection that should not be changed |
| `set` | membership / uniqueness | unique items and fast membership checks |
| `dict` | key | mapping one piece of data to another |

Examples:

```python
users = ["Subir", "Rahul"]
```

Use a list when position/order is important.

```python
user = {"name": "Subir", "age": 38}
```

Use a dictionary when you need named fields or a key-based lookup.

```python
roles = {"admin", "developer", "support"}
```

Use a set when uniqueness and membership are the main requirements.

---

## Common backend uses

Dictionaries are used heavily in backend code because many systems work with key-value data.

### Configuration

```python
config = {
    "host": "localhost",
    "port": 8000,
    "debug": True,
}
```

### API data

JSON objects are commonly represented as Python dictionaries after parsing.

```python
response = {
    "id": 101,
    "name": "Subir",
    "active": True,
}
```

### Database transformation

A database row can be represented as a dictionary so application code can work with named fields.

```python
row = {
    "product_id": 101,
    "price": 250.0,
}
```

### Lookup tables

```python
status_codes = {
    200: "OK",
    404: "Not Found",
    500: "Server Error",
}
```

The key gives direct access to the corresponding value.

### Caches and indexes

A dictionary can map an identifier to an object or result:

```python
users_by_id = {
    101: "Subir",
    102: "Rahul",
}
```

Then application code can look up a user by ID instead of scanning a list every time.

---

## Core mental model

Think of a dictionary as a collection of mappings:

```text
key  →  value
```

For example:

```text
"name"  →  "Subir"
"age"   →  38
"role"  →  "Python Developer"
```

When Python evaluates:

```python
user["age"]
```

it performs a key-based lookup and returns the value mapped to `"age"`.

When Python evaluates:

```python
user["age"] = 39
```

it changes the mapping for that key.

That distinction — **lookup vs changing a mapping** — is the base for the next dictionary topics.

---

## Practical rules

1. Use a dictionary when data is naturally represented as key → value.
2. Dictionary keys must be hashable.
3. Dictionary values can be mutable or immutable.
4. Keys are unique. Assigning an existing key replaces its value.
5. `dict[key]` performs key-based lookup.
6. A missing key with `[]` raises `KeyError`.
7. Changing an existing dictionary is mutation; assigning a new dictionary is rebinding.
8. Choose `dict`, `list`, `set`, or `tuple` based on the operation the code needs most often.
