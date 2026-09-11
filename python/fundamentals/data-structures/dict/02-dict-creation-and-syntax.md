# Dictionary Creation and Syntax

## Dictionary literal

The normal way to create a dictionary is with `{}` and key-value pairs.

```python
user = {
    "name": "Subir",
    "age": 38,
}
```

The key comes before `:` and the value comes after it.

```text
key → value
```

## Empty dictionary

```python
user = {}
```

`{}` creates an empty dictionary.

Do not confuse it with an empty set. Use `set()` for an empty set.

```python
empty_dict = {}
empty_set = set()
```

## `dict()` constructor

A dictionary can also be created with `dict()`.

```python
user = dict(name="Subir", age=38)
```

This form is useful when the keys are valid Python keyword-style names.

For arbitrary keys, use a dictionary literal.

```python
user = {
    "user-name": "Subir",
    101: "active",
}
```

## Creating from pairs

`dict()` can also build a dictionary from pairs.

```python
pairs = [
    ("name", "Subir"),
    ("age", 38),
]

user = dict(pairs)
```

Each pair becomes one key-value mapping.

## Expressions can produce keys and values

Keys and values do not have to be written as fixed literals.

```python
field = "name"
age = 38

user = {
    field: "Subir",
    "age": age,
}
```

Python evaluates the expressions when creating the dictionary.

## Duplicate keys

A dictionary keeps one value for each key.

```python
user = {
    "name": "Subir",
    "name": "Rahul",
}
```

The later value wins:

```python
{"name": "Rahul"}
```

This matters when dictionaries are built from incoming data. A repeated key does not create a second entry.

## Backend use

Dictionary creation is common when preparing:

- API response data
- configuration
- database rows
- lookup tables
- data passed between functions

The main question is not which syntax looks shorter. The useful question is what key-value mapping the code needs to represent.