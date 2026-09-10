# Set Fundamentals

## What is a Set?

A `set` is a mutable Python collection that stores **unique, hashable elements**.

```python
numbers = {10, 20, 10, 30, 20}
```

The set contains the unique values:

```text
{10, 20, 30}
```

Duplicate values are not stored multiple times.

---

## 1. Sets Store Unique Elements

A set is useful when the meaning of the data is uniqueness rather than preserving duplicates.

```python
user_ids = [101, 102, 101, 103, 102, 104]

unique_user_ids = set(user_ids)
```

`unique_user_ids` contains each ID once.

---

## 2. Sets Have No Positional Indexing

Lists and tuples provide positional access:

```python
numbers = [10, 20, 30]
numbers[0]  # 10
```

A set does not provide positional indexing:

```python
numbers = {10, 20, 30}
numbers[0]  # TypeError
```

A set is **unordered/unindexed** for the purposes of its data model. Do not rely on the order in which a set prints or iterates.

Sets are therefore appropriate when we care about:

- uniqueness
- membership

and not about:

- position
- sequence order

---

## 3. Sets Are Mutable

A normal `set` can be changed after creation.

```python
numbers = {10, 20, 30}
```

Elements can later be added or removed. Set mutation methods are covered in the next lesson.

The important distinction is:

```text
tuple -> immutable structure
set   -> mutable structure
```

---

## 4. Set Elements Must Be Hashable

Every element stored in a set must be **hashable**.

Common hashable values include:

```python
10
"hello"
3.14
(10, 20)
```

For example:

```python
data = {10, "hello", (20, 30)}
```

works.

Mutable containers such as lists, dictionaries, and sets cannot normally be set elements:

```python
data = {[10, 20]}
```

This raises:

```text
TypeError: unhashable type: 'list'
```

### Important distinction

Do not confuse:

> The set is mutable

with:

> The elements inside the set must be hashable.

The set itself can change, while each object stored inside it must satisfy the hashing requirement.

---

## 5. Creating a Set

### Set literal

```python
numbers = {10, 20, 30}
```

### `set()` constructor

`set()` can construct a set from an iterable:

```python
numbers = set([10, 20, 10, 30])
```

Duplicates are removed.

A string is also iterable:

```python
letters = set("hello")
```

This creates a set containing the unique characters `h`, `e`, `l`, and `o`.

Do not rely on the displayed order.

---

## 6. Empty Set Syntax

This is an important Python syntax distinction:

```python
{}
```

creates an empty **dictionary**, not an empty set.

Use:

```python
empty = set()
```

to create an empty set.

Therefore:

```python
type({})       # dict
type(set())    # set
```

---

## 7. Membership Testing

Sets are especially useful for checking whether a value is a member of a collection.

```python
allowed_roles = {"admin", "developer", "manager"}

"admin" in allowed_roles   # True
"guest" in allowed_roles   # False
```

This matches a common backend requirement:

> Is this value one of the allowed values?

For example:

```python
allowed_methods = {"GET", "POST", "PUT"}

if method in allowed_methods:
    ...
```

Set membership is typically efficient because sets are hash-based.

---

## Set vs List vs Tuple

| Property | List | Tuple | Set |
|---|---|---|---|
| Positional sequence | Yes | Yes | No |
| Duplicates | Yes | Yes | No |
| Mutable | Yes | No | Yes |
| Indexing | Yes | Yes | No |
| Slicing | Yes | Yes | No |
| Main use | Sequence of items | Fixed sequence | Uniqueness + membership |

Do not choose a set simply because it may be faster. Choose it when the **meaning of the data** fits a set.

Good reasons include:

```text
"I need unique values."
"I need to test membership."
"I do not care about positions."
```

---

## Core Mental Model

Remember these points:

1. A set stores unique elements.
2. A set is mutable.
3. A set has no positional indexing or slicing.
4. Set elements must be hashable.
5. Sets are especially useful for uniqueness and membership testing.
6. `{}` is an empty dictionary; `set()` is an empty set.
7. Do not rely on set iteration or display order.

Set mutation methods and set operations will be covered separately.
