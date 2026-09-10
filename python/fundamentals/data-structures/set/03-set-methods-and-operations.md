# Set Methods and Operations

## 1. `add()` — Add One Element

`add()` adds **one object** to an existing set.

```python
skills = {"Python", "SQL"}
skills.add("Git")
```

The set is mutated in place.

Adding a duplicate does nothing because sets keep unique values:

```python
skills.add("Python")
```

### Important mental model

```text
add(x)
  ↓
add THIS ONE object as an element
```

The argument can itself be a compound hashable object:

```python
skills.add(("Git", "Docker"))
```

The tuple is added as **one set element**.

---

## 2. `update()` — Add Multiple Elements

`update()` takes an iterable and adds its elements to the set.

```python
skills = {"Python"}
skills.update(["Git", "Docker", "Linux"])
```

Conceptually:

```text
iterable
   ↓
iterate over its elements
   ↓
add each element to the set
```

Compare:

```python
skills.add(("Git", "Docker"))
# adds one tuple element

skills.update(("Git", "Docker"))
# adds "Git" and "Docker" separately
```

This is the key distinction:

> `add()` adds one object. `update()` iterates over an iterable and adds its elements.

Because strings are iterable, this also matters:

```python
skills.update("Git")
```

adds `"G"`, `"i"`, and `"t"` as separate elements.

---

## 3. `remove()` — Remove a Specific Element

```python
skills = {"Python", "SQL", "Docker"}
skills.remove("SQL")
```

The specified element is removed from the set.

If the element does not exist, `remove()` raises `KeyError`.

```python
skills.remove("Java")
# KeyError
```

### Production mental model

Use `remove()` when absence represents an unexpected or invalid state.

---

## 4. `discard()` — Remove If Present

```python
skills.discard("SQL")
```

If the element exists, it is removed.

If it does not exist, nothing happens and no exception is raised:

```python
skills.discard("Java")
# no error
```

### `remove()` vs `discard()`

| Method | Element present | Element missing |
|---|---|---|
| `remove(x)` | removes it | raises `KeyError` |
| `discard(x)` | removes it | does nothing |

Use `discard()` when the intent is simply:

> Make sure this value is not in the set.

---

## 5. `pop()` — Remove and Return an Arbitrary Element

```python
skills = {"Python", "SQL", "Docker"}
removed = skills.pop()
```

`pop()`:

1. removes an element from the set
2. returns the removed element
3. leaves the set with one fewer element

Because sets do not provide positional order, the removed element is **arbitrary**. Do not write code that depends on which value is returned.

```python
removed = skills.pop()
```

You can guarantee that `removed` was an element of the set before the operation, but you cannot reliably predict which one.

For an empty set:

```python
set().pop()
# KeyError
```

### Contrast with list

A list has positional behavior, so `list.pop()` can remove by position. A set has no positional indexing, so set `pop()` removes an arbitrary element.

---

## 6. `clear()` — Empty the Existing Set

```python
skills = {"Python", "SQL"}
alias = skills

skills.clear()
```

`clear()` mutates the existing set object.

Both names still refer to the same set object, which is now empty:

```text
skills ──┐
         ├──> existing set: {}
alias  ──┘
```

This differs from rebinding:

```python
skills = {"Python", "SQL"}
alias = skills

skills = set()
```

Now `skills` refers to a **new** empty set, while `alias` still refers to the original set containing `{"Python", "SQL"}`.

### Core engineering distinction

```text
clear()
→ mutation of existing object

skills = set()
→ new object + rebinding of the name
```

---

# Set Combination Operations

Use these sets:

```python
backend = {"Python", "SQL", "Docker"}
devops = {"Docker", "Linux", "Git"}
```

These operations normally return a **new set** and do not mutate the operands.

---

## 7. Union — `|` / `union()`

Union contains every unique element from both sets.

```python
result = backend | devops
```

Equivalent method:

```python
result = backend.union(devops)
```

Conceptually:

```python
{"Python", "SQL", "Docker", "Linux", "Git"}
```

Neither original set is changed.

### Mental model

> Union = everything from A or B, with duplicates collapsed.

---

## 8. Intersection — `&` / `intersection()`

Intersection contains only elements present in **both** sets.

```python
result = backend & devops
```

Equivalent:

```python
result = backend.intersection(devops)
```

Result:

```python
{"Docker"}
```

### Mental model

> Intersection = shared elements.

---

## 9. Difference — `-` / `difference()`

Difference contains elements that belong to the **first set but not the second**.

```python
backend - devops
# {"Python", "SQL"}
```

Equivalent:

```python
backend.difference(devops)
```

Direction matters:

```python
devops - backend
# {"Linux", "Git"}
```

### Mental model

> `A - B` = everything in A that is not in B.

Do not think of difference as a symmetric operation. Swapping the operands can change the result.

---

## 10. Symmetric Difference — `^` / `symmetric_difference()`

Symmetric difference contains elements that appear in either set, but **not in both**.

```python
result = backend ^ devops
```

Equivalent:

```python
result = backend.symmetric_difference(devops)
```

Result:

```python
{"Python", "SQL", "Linux", "Git"}
```

`"Docker"` is excluded because it appears in both sets.

### Mental model

> Symmetric difference = everything unique to either side; remove shared elements.

---

# Operator and Method Equivalents

| Operator | Method | Meaning |
|---|---|---|
| `a \| b` | `a.union(b)` | all unique elements |
| `a & b` | `a.intersection(b)` | shared elements |
| `a - b` | `a.difference(b)` | elements in `a` but not `b` |
| `a ^ b` | `a.symmetric_difference(b)` | elements in either, but not both |

These operations return a new set rather than changing the original operands.

---

# In-Place Set Operations

Set operators also have in-place forms:

```python
a |= b
a &= b
a -= b
a ^= b
```

They mutate the existing set referenced by `a`.

### `|=` — union into `a`

```python
a |= b
```

Equivalent in intent to adding all elements of `b` into `a` in place.

### `&=` — keep intersection

```python
a &= b
```

`a` becomes the intersection of the original `a` and `b`.

### `-=` — remove elements

```python
a -= b
```

Elements found in `b` are removed from `a`.

### `^=` — symmetric difference into `a`

```python
a ^= b
```

`a` becomes the symmetric difference of the original `a` and `b`.

---

## In-Place Mutation vs Rebinding

Compare:

```python
a |= b
```

with:

```python
a = a | b
```

The first performs an in-place update of the existing set.

The second creates the result of `a | b` as a new set and then rebinds `a` to that new object.

This matters when another name refers to the original object:

```python
a = {"Python"}
alias = a

a |= {"SQL"}
```

Both `a` and `alias` observe the mutation.

But:

```python
a = {"Python"}
alias = a

a = a | {"SQL"}
```

`a` is rebound to a new set. `alias` continues referring to the original set.

This is the same core mutation-vs-rebinding model used throughout Python.

---

# Set Relationship Operations

## 11. Subset — `<=` / `issubset()`

Given:

```python
required = {"Python", "SQL"}
skills = {"Python", "SQL", "Docker", "Git"}
```

```python
required <= skills
required.issubset(skills)
```

both return `True`.

A set is a **subset** when every element in it is also present in the other set.

### Mental model

> `required` asks: "Are all my elements available in `skills`?"

---

## 12. Superset — `>=` / `issuperset()`

```python
skills >= required
skills.issuperset(required)
```

both return `True`.

A set is a **superset** when it contains every element of another set.

### Mental model

> A superset contains all members of the smaller/required set, and may contain additional members.

Subset and superset describe the same relationship from opposite sides.

---

## 13. Disjoint — `isdisjoint()`

Two sets are disjoint when they have **no elements in common**.

```python
frontend = {"HTML", "CSS", "JavaScript"}
backend = {"Python", "SQL", "Docker"}

frontend.isdisjoint(backend)
# True
```

If one shared element is introduced:

```python
backend.add("JavaScript")

frontend.isdisjoint(backend)
# False
```

### Mental model

> `isdisjoint()` asks: "Do these two sets have zero shared elements?"

It returns:

- `True` → no common elements
- `False` → at least one common element

---

# Production Use Cases

Sets are especially useful when the problem is about **membership, uniqueness, or relationships between groups**.

### 1. Fast membership checks

```python
allowed_methods = {"GET", "POST", "PUT"}

if method in allowed_methods:
    ...
```

### 2. Removing duplicates

```python
unique_user_ids = set(user_ids)
```

### 3. Comparing permissions

```python
required_permissions <= user_permissions
```

This can express whether a user has every permission required by an operation.

### 4. Finding overlap

```python
customer_tags & campaign_tags
```

Useful when finding shared categories, permissions, capabilities, IDs, or features.

### 5. Finding missing/exclusive values

```python
required_ids - available_ids
```

This directly expresses which required IDs are unavailable.

### 6. Detecting completely separate groups

```python
set_a.isdisjoint(set_b)
```

Useful when groups must have no overlap.

---

# Common Mistakes

### Mistake 1 — Treating `add()` like `update()`

```python
skills.add(("Git", "Docker"))
```

adds one tuple object.

### Mistake 2 — Forgetting that strings are iterables

```python
skills.update("Git")
```

adds individual characters.

### Mistake 3 — Assuming `pop()` means "last element"

Sets have no positional last element. Set `pop()` removes an arbitrary element.

### Mistake 4 — Confusing `remove()` and `discard()`

The important difference is behavior when the target is missing.

### Mistake 5 — Forgetting difference direction

```python
a - b
```

is not generally the same as:

```python
b - a
```

### Mistake 6 — Confusing mutation with rebinding

```python
a |= b       # mutate existing set

a = a | b    # new set + rebind a
```

### Mistake 7 — Treating sets as ordered sequences

Do not depend on which element `pop()` removes or on displayed/iteration order.

---

# Quick Mental Map

```text
MODIFY ONE
    add()

MODIFY MANY
    update()

REMOVE
    remove()      -> error if missing
    discard()     -> ignore if missing
    pop()         -> arbitrary element + return it
    clear()       -> empty existing set

COMBINE / COMPARE
    |             -> union
    &             -> intersection
    -             -> difference
    ^             -> symmetric difference

IN-PLACE
    |=            -> union into existing set
    &=            -> intersection into existing set
    -=            -> difference into existing set
    ^=            -> symmetric difference into existing set

RELATIONSHIPS
    <=            -> subset
    >=            -> superset
    isdisjoint()  -> no common elements
```

# Production Mental Model

A set should make you think:

```text
                SET
                 |
       +---------+---------+
       |                   |
   MEMBERSHIP           UNIQUENESS
       |                   |
       +---------+---------+
                 |
          RELATIONSHIPS
                 |
     +-----------+-----------+
     |           |           |
   union    intersection  difference
```

The core question is not "What is element 0?" but:

> **What membership or relationship am I trying to express?**

For mutation, always distinguish:

```text
mutate existing set
        vs
create new set + rebind a name
```

This distinction becomes important when multiple names reference the same set object.

# Definition of Done

You should be able to explain and predict without running Python:

1. Why `add()` and `update()` behave differently.
2. Why `add(("Git", "Docker"))` adds one element while `update(("Git", "Docker"))` adds two.
3. Why `update("Git")` adds characters.
4. The difference between `remove()` and `discard()`.
5. Why set `pop()` returns an arbitrary element.
6. The difference between `clear()` and rebinding with `set()`.
7. What union, intersection, difference, and symmetric difference mean.
8. Why difference is directional.
9. The difference between in-place operators and creating a new set with an operator expression.
10. How subset, superset, and disjoint relationships work.
11. Appropriate production situations for using sets.
12. How mutation vs rebinding affects aliases to the same set object.
