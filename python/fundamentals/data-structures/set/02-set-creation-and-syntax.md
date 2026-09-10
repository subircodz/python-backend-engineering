# Set Creation and Syntax

## 1. Set Literal

A set can be created directly with curly braces when the values are already known:

```python
numbers = {10, 20, 30}
```

Duplicate values are stored only once:

```python
numbers = {10, 20, 10, 30, 20}
# {10, 20, 30} conceptually
```

A set is about **uniqueness and membership**, not positional order.

---

## 2. Empty Set vs Empty Dictionary

```python
{}
```

creates an empty dictionary, not an empty set.

Use:

```python
set()
```

to create an empty set.

```python
empty_dict = {}
empty_set = set()
```

### Important rule

- `{}` → empty `dict`
- `{10}` → one-element `set`
- `{10, 20}` → set
- `set()` → empty set

---

## 3. The `set()` Constructor

`set()` can consume an iterable and construct a new set from its elements.

```python
values = [10, 20, 10, 30, 20]
numbers = set(values)
```

Conceptually:

```text
values -> iterable -> set() -> new set containing unique values
```

The original iterable is not modified.

```python
values = [10, 20, 10]
numbers = set(values)

# values remains [10, 20, 10]
# numbers contains {10, 20}
```

### Common iterable inputs

```python
set([10, 20, 20, 30])
set((10, 20, 20, 30))
set("hello")
```

The constructor iterates over its input iterable and uses those objects as candidate set elements.

---

## 4. Literal vs Constructor

Use a **set literal** naturally when the values are already known in the source code:

```python
allowed_methods = {"GET", "POST", "PUT"}
```

Use the **constructor** naturally when you already have an iterable and want a set from it:

```python
methods = ["GET", "POST", "GET", "PUT"]
allowed_methods = set(methods)
```

The important distinction is not whether you know the values. The constructor is especially useful for converting an existing iterable into a set.

---

## 5. Set Elements Must Be Hashable

Every object stored **directly as an element of a set** must be hashable.

Common hashable types include:

```python
{10, "python", 3.14}
```

Tuples can also be set elements when their own elements are hashable:

```python
{(10, 20), (30, 40)}
```

Lists, dictionaries, and ordinary sets are unhashable and cannot be direct set elements:

```python
{[10, 20]}       # TypeError
{{10, 20}}       # TypeError
```

### Important mental model

Do not think about set element positions or indexes. Think:

> **Is each object I am directly trying to store in the set hashable?**

A tuple containing only hashable objects can be hashable. A tuple containing an unhashable list cannot be used as a set element.

```python
{(10, 20)}          # valid
{([10, 20], 30)}    # invalid
```

---

## 6. Parentheses Do Not Automatically Create Tuples

The comma creates tuple structure; parentheses alone can simply provide grouping.

```python
([10, 20])
```

is still a list, not a tuple.

Therefore:

```python
set([([10, 20]), ([30, 40])])
```

is effectively attempting to put lists into a set and fails because lists are unhashable.

Compare:

```python
set([(10, 20), (30, 40)])
```

which is valid because the direct set elements are tuples containing hashable integers.

---

## 7. Strings and the `set()` Constructor

A string is iterable character by character.

Therefore:

```python
set("banana")
```

contains the unique characters:

```python
{"b", "a", "n"}
```

But:

```python
set(["banana"])
```

contains one element: the complete string `"banana"`.

The constructor iterates over its **input iterable**. It does not recursively break down every object inside it.

### Important comparison

```python
set("ABC")
# {"A", "B", "C"}

set(["ABC"])
# {"ABC"}
```

---

## 8. `set()` Removes Duplicates, But Does Not Convert Types

`set()` removes duplicate/equal values; it does not convert strings into integers or otherwise change element types.

```python
values = ["10", "20", "10", "30"]
unique_values = set(values)
```

The result contains string objects:

```python
{"10", "20", "30"}
```

It does **not** become:

```python
{10, 20, 30}
```

### Mixed types

```python
data = ["10", 20, "10", 20, 30]
result = set(data)
```

Conceptually:

```python
{"10", 20, 30}
```

`"10"` and `10` are different values because one is a `str` and the other is an `int`.

```python
"10" != 10
```

---

## 9. Set Has No Positional Indexing or Slicing

A set is not a sequence and does not support positional access:

```python
numbers = {10, 20, 30}

numbers[0]      # TypeError
numbers[1:3]    # TypeError
```

Do not depend on the order in which a set is displayed or iterated.

The useful properties are:

- uniqueness
- membership testing
- set relationships and operations

---

## 10. Production Mental Model

Think of set creation as:

```text
INPUT ITERABLE
      |
      v
 iterate over elements
      |
      v
 keep unique/equal values
      |
      v
 NEW SET OBJECT
```

The original iterable is not modified by `set()`.

When deciding between syntax:

```python
{...}
```

means: **I am explicitly defining these set members here.**

```python
set(iterable)
```

means: **I have an iterable and want to construct a set from its elements.**

---

## Definition of Done

You should be able to explain without running Python:

1. Why `{}` is an empty dictionary rather than an empty set.
2. Why `{10}` is a set.
3. What `set(iterable)` does.
4. Why `set(iterable)` does not modify the original iterable.
5. Why lists cannot be direct set elements.
6. Why a tuple of hashable elements can be a set element.
7. Why a tuple containing a list cannot be a set element.
8. Why `set("ABC")` and `set(["ABC"])` produce different sets.
9. Why `set()` removes duplicates but does not convert element types.
10. Why set elements must be hashable and why positional indexing is not part of the set model.
