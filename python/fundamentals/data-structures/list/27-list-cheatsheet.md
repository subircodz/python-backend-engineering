# Python List Cheatsheet

A practical reference for Python lists covered in this learning path.

## 1. Core Mental Model

A list is:

- **Ordered** — elements have defined positions/indexes.
- **Mutable** — the existing list object can be changed.
- **Indexed** — positions start at `0`.
- **Heterogeneous** — a list can contain different object types.
- **A container of references** — list slots refer to objects; copying a list does not automatically copy nested objects.

```python
items = ["A", "B", "C"]
```

```text
index:    0      1      2
value:   "A"    "B"    "C"
```

**Ordered does not mean sorted.**

---

## 2. Indexing

```python
items[0]      # first element
items[1]      # second element
items[-1]     # last element
items[-2]     # second last element
```

For a list of length `n`, positive indexes are `0` through `n - 1`.

```python
last_index = len(items) - 1
```

---

## 3. Replace an Element

```python
items[1] = "X"
```

This **mutates the existing list** by replacing the object stored at index `1`.

It does not insert a new element and does not create a new list.

---

## 4. Aliasing

```python
items = ["A", "B"]
other = items
```

`items` and `other` refer to the **same list object**.

```python
items.append("C")
```

Both names now observe:

```python
["A", "B", "C"]
```

Mental model:

> Assignment copies the reference, not the list.

---

## 5. Adding Elements

### `append()` — add one object

```python
items.append("C")
```

Adds the supplied object as **one element**.

```python
items = ["A"]
items.append(["B", "C"])
# ["A", ["B", "C"]]
```

### `extend()` — add elements from an iterable

```python
items.extend(["B", "C"])
# ["A", "B", "C"]
```

`extend()` iterates over its argument and adds each element individually.

```python
items.extend((1, 2, 3))
items.extend("ABC")
items.extend({"name": "Subir", "age": 38})  # adds keys
```

An `int` is not iterable:

```python
items.extend(10)  # TypeError
```

### `insert()` — add at a position

```python
items.insert(1, "X")
```

Inserts at the specified index and shifts later elements to the right.

---

## 6. Removing Elements

| Operation | Removes by | Returns | Missing target |
|---|---|---|---|
| `remove(value)` | value | `None` | `ValueError` |
| `pop(index)` | index | removed object | `IndexError` |
| `pop()` | last element | removed object | `IndexError` on empty list |
| `del items[index]` | index | nothing | `IndexError` |
| `clear()` | all elements | `None` | — |

### `remove()`

```python
items.remove("B")
```

Removes the **first matching occurrence**.

### `pop()`

```python
removed = items.pop()
```

Removes and returns the last element.

```python
removed = items.pop(2)
```

Removes and returns the element at index `2`.

### `del`

```python
del items[1]
del items[1:4]
```

Can remove an element or a slice.

### `clear()`

```python
items.clear()
```

Removes all elements from the **existing list object**.

Compare:

```python
items.clear()  # mutate existing list
items = []     # rebind name to a new list
```

---

## 7. Slicing

General form:

```python
sequence[start:stop:step]
```

- `start` — where to begin; included.
- `stop` — where to stop; **excluded**.
- `step` — how far to move each time.

```python
numbers = [10, 20, 30, 40, 50, 60]

numbers[1:4]    # [20, 30, 40]
numbers[:3]     # [10, 20, 30]
numbers[2:]     # [30, 40, 50, 60]
numbers[:]      # shallow copy of the outer list
numbers[::2]    # [10, 30, 50]
numbers[::-1]   # reverse order
```

Negative step moves backward:

```python
numbers[4:1:-1]   # [50, 40, 30]
numbers[5:1:-2]   # [60, 40]
```

### Slice assignment

```python
numbers[1:4] = [99]
```

Modifies the existing list and can change its length.

The right-hand side can be any iterable:

```python
items[1:3] = "XYZ"
# ["A", "X", "Y", "Z", "D"]
```

Full-list replacement while preserving the same outer list object:

```python
items[:] = [100, 200, 300]
```

---

## 8. Length and Membership

### `len()`

```python
len(items)
```

Returns the number of elements.

> Length counts elements; indexing identifies a position.

### `in` / `not in`

```python
"Bob" in users
"Admin" not in users
```

These test membership, not position.

---

## 9. Searching

### `index()`

```python
items.index("B")
```

Returns the index of the **first matching value**.

Missing value:

```python
items.index("X")  # ValueError
```

### `count()`

```python
items.count("B")
```

Returns the number of occurrences.

Missing value:

```python
items.count("X")  # 0
```

Quick distinction:

```text
value in items     -> Does it exist?
items.index(value) -> Where is the first one?
items.count(value) -> How many are there?
```

---

## 10. Copying — Shallow Copy

```python
items = ["A", "B", "C"]
other = items.copy()
```

Creates a **new outer list object**.

```text
items  -> ["A", "B", "C"]
other  -> ["A", "B", "C"]
```

The outer containers are different, but their element references are initially shared.

### Outer replacement is independent

```python
items[0] = "X"
```

`other[0]` remains `"A"`.

### Nested mutation is shared

```python
items = [["A", "B"], ["C", "D"]]
other = items.copy()

items[0].append("X")
```

Both lists observe the changed inner list because the inner list object is shared.

Mental model:

> A shallow copy copies the outer container, not the objects inside it.

---

## 11. `reverse()` vs `reversed()`

### `reverse()`

```python
result = items.reverse()
```

- List method.
- Mutates the existing list.
- Returns `None`.

### `reversed()`

```python
result = reversed(items)
```

- Built-in function.
- Does not mutate the list.
- Returns a reverse iterator.

To materialize a new list:

```python
result = list(reversed(items))
```

Mental model:

> `reverse()` → mutate this list.
>
> `reversed()` → give me an iterator that goes backward.

---

## 12. `sort()` vs `sorted()`

### `sort()`

```python
result = numbers.sort()
```

- List method.
- Mutates the existing list.
- Returns `None`.

### `sorted()`

```python
result = sorted(numbers)
```

- Built-in function.
- Does not mutate the original.
- Returns a new list.
- Works with any iterable.

Both support `key=` and `reverse=`.

```python
sorted(employees, key=lambda employee: employee["salary"])
```

---

## 13. Concatenation: `+`

```python
a = [1, 2]
b = [3, 4]
c = a + b
```

Result:

```python
c == [1, 2, 3, 4]
```

`a` and `b` are unchanged. `+` creates a **new outer list**.

---

## 14. Repetition: `*`

```python
items = ["A", "B"]
result = items * 3
```

Result:

```python
["A", "B", "A", "B", "A", "B"]
```

A new outer list is created, but element references are repeated; the elements are not automatically deep-copied.

### Shared-reference trap

```python
items = [[]] * 3
items[0].append("A")
```

Result:

```python
[["A"], ["A"], ["A"]]
```

There is **one inner list object referenced three times**.

---

## 15. `+` vs `+=` vs `extend()`

```python
a = [1, 2]
b = [3, 4]
```

### `+`

```python
c = a + b
```

Creates a new list.

### `+=`

```python
a += b
```

For lists, mutates the existing list in place.

### `extend()`

```python
a.extend(b)
```

Mutates the existing list in place.

Quick comparison:

| Operation | Existing list mutated? | New outer list produced? |
|---|---:|---:|
| `a + b` | No | Yes |
| `a += b` | Yes | No, for normal list in-place operation |
| `a.extend(b)` | Yes | No |

---

## 16. Common Traps

### Trap 1 — `remove()` does not mean index

```python
items.remove(1)
```

Means: remove the **value `1`**, not index `1`.

### Trap 2 — `pop()` returns something

```python
removed = items.pop()
```

`removed` receives the removed object.

### Trap 3 — `reverse()` returns `None`

```python
result = items.reverse()
# result is None
```

### Trap 4 — `sort()` returns `None`

```python
result = items.sort()
# result is None
```

### Trap 5 — `sorted()` does not mutate the original

```python
result = sorted(items)
```

### Trap 6 — `clear()` vs `items = []`

`clear()` mutates the existing list; rebinding with `=` points the variable at another list.

### Trap 7 — shallow copy is not deep copy

```python
other = items.copy()
```

Nested mutable objects may still be shared.

### Trap 8 — `*` can repeat shared references

```python
items = [[]] * 3
```

The three positions refer to the same inner list.

### Trap 9 — `count()` does not raise for a missing value

```python
items.count("X")  # 0
```

### Trap 10 — `index()` does raise for a missing value

```python
items.index("X")  # ValueError
```

---

## 17. Mutation vs Rebinding — Core Mental Model

### Mutation

Changes an existing object.

```python
items.append("X")
items[0] = "Y"
items.clear()
items.extend(other)
```

Aliases to the same object observe the mutation.

### Rebinding

Changes what a variable name refers to.

```python
items = []
```

The old list object is not modified by this assignment.

### Nested mutation

```python
items[0]["name"] = "Subir"
```

If the nested dictionary is shared, other references to that dictionary observe the change.

---

## 18. Method/Operation Quick Reference

| Syntax | Purpose | Mutates original? | Main result |
|---|---|---:|---|
| `items[i]` | access by index | No | element |
| `items[i] = x` | replace element | Yes | `None` |
| `items.append(x)` | add one object | Yes | `None` |
| `items.extend(x)` | add elements from iterable | Yes | `None` |
| `items.insert(i, x)` | insert at index | Yes | `None` |
| `items.remove(x)` | remove first matching value | Yes | `None` |
| `items.pop(i)` | remove by index | Yes | removed object |
| `items.pop()` | remove last | Yes | removed object |
| `items.clear()` | remove all | Yes | `None` |
| `items[i:j]` | create slice | No | new list |
| `items[i:j] = x` | replace slice | Yes | `None` |
| `len(items)` | count elements | No | integer |
| `x in items` | membership | No | boolean |
| `items.index(x)` | first matching position | No | integer / `ValueError` |
| `items.count(x)` | occurrence count | No | integer |
| `items.copy()` | shallow copy | No | new list |
| `items.reverse()` | reverse in place | Yes | `None` |
| `reversed(items)` | reverse iterator | No | iterator |
| `items.sort()` | sort in place | Yes | `None` |
| `sorted(items)` | create sorted list | No | new list |
| `del items[i]` | delete by index | Yes | no returned value |
| `a + b` | concatenate | No | new list |
| `a * n` | repeat | No | new list |
| `a += b` | in-place concatenation | Yes | updated `a` |

---

## 19. One-Line Mental Models

```text
List             -> ordered, mutable container of object references
Index            -> access a position
Negative index   -> count from the right; -1 is last
append           -> add one object
extend           -> iterate and add elements individually
insert           -> add at a position
remove           -> remove first matching value
pop              -> remove by index and return the object
clear            -> empty the existing list
slice            -> select a range and create a new list
slice assignment -> replace a range in the existing list
len              -> number of elements
in               -> membership check
index            -> first matching position
count            -> number of matches
copy             -> new outer list, shared nested objects
reverse          -> mutate list, return None
reversed         -> reverse iterator, original unchanged
sort             -> mutate list, return None
sorted           -> new sorted list
+                -> new concatenated list
*                -> new outer list with repeated element references
+=               -> mutate list in place
```

## 20. Engineering Rule

When reasoning about a list, ask three questions:

1. **Which list object am I referring to?**
2. **Am I mutating that object or rebinding a name?**
3. **Are any nested mutable objects shared?**

Those three questions explain most list-related behavior that matters in real Python code.
