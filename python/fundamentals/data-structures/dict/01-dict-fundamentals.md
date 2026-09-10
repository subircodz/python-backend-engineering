# Python Dictionary Fundamentals

## 1. What is a dictionary?

A Python dictionary is a **mutable mapping of keys to values**.

```python
user = {
    "name": "Subir",
    "age": 38,
    "role": "Python Developer",
}
```

Mental model:

```text
"name" → "Subir"
"age"  → 38
"role" → "Python Developer"
```

A dictionary is not primarily about positions. It is about **mapping a key to an object**.

---

## 2. Keys are unique

A dictionary cannot keep two values under the same key.

```python
user = {
    "name": "Subir",
    "name": "John",
}
```

The resulting dictionary contains only one `"name"` entry:

```python
{"name": "John"}
```

The later assignment replaces the earlier mapping.

---

## 3. Dictionaries are mutable

An existing dictionary can be changed.

```python
user = {"name": "Subir", "age": 38}

user["age"] = 39
```

The dictionary object is mutated. The name `user` still refers to the same dictionary object.

This is different from rebinding:

```python
user = {"name": "Subir"}
user = {"name": "John"}
```

Here the name `user` is rebound to another dictionary object.

---

## 4. Dictionary access is key-based

```python
user = {"name": "Subir", "age": 38}

name = user["name"]
```

`user["name"]` means: look up the value mapped to the key `"name"`.

If the key does not exist, direct indexing raises `KeyError`:

```python
user["email"]  # KeyError
```

Compare:

```text
list  → position → object
       missing position → IndexError

dict  → key      → object
       missing key      → KeyError
```

---

## 5. Keys must be hashable

Dictionary keys must be hashable because Python uses the key's hash to support efficient lookup.

Common valid keys:

```python
{"name": "Subir"}
{10: "ten"}
{3.14: "pi"}
{(1, 2): "point"}
```

A list cannot be a dictionary key:

```python
{[1, 2]: "value"}  # TypeError
```

Lists are mutable and therefore unhashable.

### Values do not have to be hashable

```python
user = {
    "name": "Subir",
    "skills": ["Python", "SQL"],
    "profile": {"active": True},
}
```

The list and nested dictionary are valid values.

---

## 6. A key maps to an object

A useful mental model is:

```text
key ───────→ object
```

For example:

```python
user = {"age": 38}
```

The dictionary maps `"age"` to the integer object `38`.

When we write:

```python
user["age"] = 39
```

we are not mutating integer `38` into `39`. Integers are immutable. We are changing the dictionary's mapping so that `"age"` now maps to the integer object `39`.

---

## 7. Dictionary vs other core structures

| Structure | Main idea |
|---|---|
| List | ordered collection accessed by position |
| Tuple | ordered immutable collection |
| Set | unique objects / membership |
| Dictionary | key → value mapping |

The important question is not just **“which syntax do I remember?”** but **“what relationship does my data have?”**

If the data naturally has an identifier associated with another object, a dictionary is often a strong candidate.

---

## 8. Production mental model

Suppose a backend service needs to represent configuration:

```python
config = {
    "host": "localhost",
    "port": 8000,
    "debug": False,
}
```

The keys describe what each value means. We do not need to remember that `8000` is at position `1`; we ask for `config["port"]`.

This is one reason dictionaries are fundamental in Python backend development: structured data frequently has **named fields or identifiers** rather than meaningful numeric positions.

---

## Key takeaways

- A dictionary is a mutable mapping of keys to values.
- Keys are unique.
- Dictionary lookup is key-based, not position-based.
- Missing direct lookup raises `KeyError`.
- Keys must be hashable.
- Values can be mutable or unhashable.
- Updating `d[key]` changes the mapping; it does not mutate an immutable value object.
- Think **key → object**, not **position → object**.
