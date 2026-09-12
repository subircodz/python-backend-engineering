# TypedDict — Engineering Notes

`TypedDict` is useful when a dictionary is being used as a **structured record** and we want static type checkers to understand the expected keys and value types.

It does **not** create a new runtime dictionary type.

```python
from typing import TypedDict


class Product(TypedDict):
    product_id: str
    name: str
    category: str
    price: float
    stock: int
    active: bool
```

A value using that shape is still a normal `dict` at runtime:

```python
product: Product = {
    "product_id": "P001",
    "name": "Keyboard",
    "category": "Electronics",
    "price": 1200.0,
    "stock": 15,
    "active": True,
}
```

## Why use it?

Without `TypedDict`, this:

```python
product: dict = {
    "product_id": "P001",
    "stock": 15,
}
```

tells a type checker very little about the record's intended structure.

With `TypedDict`:

```python
product: Product = {
    "product_id": "P001",
    "name": "Keyboard",
    "category": "Electronics",
    "price": 1200.0,
    "stock": 15,
    "active": True,
}
```

the intended schema is explicit.

This becomes useful when dictionaries cross method boundaries, move between modules, or represent records returned by application code.

## Important mental model

Keep these three things separate:

```text
TypedDict definition
        ↓
describes the expected dictionary shape
        ↓
actual object is still a normal dict
```

`TypedDict` is primarily a **static typing tool**. It does not provide runtime validation by itself.

For example, defining:

```python
class Product(TypedDict):
    stock: int
```

does not automatically stop this at runtime:

```python
product = {"stock": "fifteen"}
```

A static type checker can report the mismatch, but Python itself does not turn the dictionary into a validated `Product` object.

## TypedDict vs class

A `TypedDict` is still dictionary-shaped data:

```python
product["stock"]
```

A normal class instance uses attributes:

```python
product.stock
```

Use `TypedDict` when the data naturally needs to remain dictionary-like. Use a class when behaviour and object identity are central to the design.

Do not choose `TypedDict` simply because it looks more structured. Choose it because the application is already working with dictionary records.

## TypedDict vs `dict[str, object]`

This:

```python
product: dict[str, object]
```

says roughly:

> This is a dictionary with string keys and values of various types.

It does not describe which keys are expected.

`TypedDict` can describe that record explicitly:

```python
class Product(TypedDict):
    product_id: str
    price: float
    stock: int
```

The second form communicates much more about the application's data contract to a type checker and to another engineer reading the code.

## Useful pattern for record-based code

For a manager that stores product records:

```python
from typing import TypedDict


class Product(TypedDict):
    product_id: str
    name: str
    category: str
    price: float
    stock: int
    active: bool


class InventoryManager:
    def __init__(self):
        self.products: list[Product] = []
```

The manager still stores ordinary dictionaries. `Product` communicates what each dictionary is supposed to contain.

Another valid storage design is:

```python
class InventoryManager:
    def __init__(self):
        self.products: dict[str, Product] = {}
```

The choice between `list[Product]` and `dict[str, Product]` is a **data-structure/design decision**. `TypedDict` does not make that decision for you.

## Required keys are the default

In a normal `TypedDict`, declared keys are expected to be present:

```python
class Product(TypedDict):
    product_id: str
    stock: int
```

So this is not the complete expected shape:

```python
product: Product = {
    "product_id": "P001",
}
```

If a record genuinely has optional keys, `TypedDict` has features for modelling that. Learn those deliberately when the application actually needs them rather than adding them pre-emptively.

## What TypedDict does NOT do

Do not treat `TypedDict` as:

- runtime validation
- a replacement for input validation
- a database schema
- a class with methods
- a runtime wrapper around `dict`
- protection against bad external data

If data comes from an API, file, database, or user input, the application may still need runtime validation before trusting it.

## Engineering rule

Use `TypedDict` when all of these are true:

1. The data is naturally dictionary-shaped.
2. The record has a known set of fields.
3. Static tooling benefits from knowing those fields and their types.
4. You do not need the dictionary itself to gain behaviour through methods.

If those conditions do not hold, a plain dictionary or a different data model may be simpler.

## Current learning boundary

This note is intentionally an **engineering reference**, not a full typing lesson.

For now, the important working knowledge is:

```text
TypedDict = describe the expected shape of a dictionary for static type checking.

It does not change the fact that the runtime object is a dict.
```

Features such as optional/total keys, inheritance between `TypedDict`s, `Required`, `NotRequired`, and more advanced typing patterns should be learned separately when they become relevant.
