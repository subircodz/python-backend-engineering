# List — 30-Question Revision Notes

This document records the final revision test for Python Lists.

The purpose is not only to remember outputs, but to verify the mental model of **objects, references, mutation, rebinding, indexing, and nested references**.

---

## 1. Aliasing + `append()`

```python
items = ["A", "B", "C"]
other = items

items.append("D")
```

### Correct answer

```python
items  # ["A", "B", "C", "D"]
other  # ["A", "B", "C", "D"]
```

### Explanation

`other = items` does not create another list. Both names refer to the same list object.

`append()` mutates that existing list object, so both names observe the change.

> Assignment copies the reference, not the list.

---

## 2. Index assignment

```python
users = ["Alice", "Bob", "Charlie"]
users[1] = "Subir"
```

### Correct answer

```python
users  # ["Alice", "Subir", "Charlie"]
```

No new list is created.

### Explanation

Index assignment changes the object reference stored in slot `1` of the existing list.

The list object remains the same and its length does not change.

> `items[index] = value` replaces what that slot refers to; it does not insert a new element.

---

## 3. Positive and negative indexing

```python
numbers = [10, 20, 30, 40, 50]
```

### Correct answer

```python
numbers[0]   # 10
numbers[2]   # 30
numbers[-1]  # 50
numbers[-3]  # 30
```

### Explanation

Positive indexing starts at `0` from the left.

Negative indexing counts from the right:

```text
-1 -> last
-2 -> second last
-3 -> third last
```

---

## 4. `append()` vs `extend()`

```python
items = ["A"]
items.append(["B", "C"])

items2 = ["A"]
items2.extend(["B", "C"])
```

### Correct answer

```python
items   # ["A", ["B", "C"]]
items2  # ["A", "B", "C"]
```

### Explanation

`append()` adds exactly **one object** as one element.

`extend()` iterates over an iterable and adds its elements individually.

> `append(x)` -> add `x` as one element.
>
> `extend(x)` -> iterate over `x` and add its elements.

---

## 5. `extend()` with a string

```python
items = ["A"]
items.extend("BC")
```

### Correct answer

```python
items  # ["A", "B", "C"]
```

### Explanation

A string is iterable. `extend()` therefore processes its characters one at a time.

---

## 6. `extend()` with a dictionary

```python
items = ["A"]
data = {"name": "Subir", "age": 38}
items.extend(data)
```

### Correct answer

```python
items  # ["A", "name", "age"]
```

### Explanation

Iterating over a dictionary produces its keys by default. Therefore `extend()` adds the dictionary keys.

---

## 7. `insert()`

```python
numbers = [10, 30, 40]
numbers.insert(1, 20)
```

### Correct answer

```python
numbers  # [10, 20, 30, 40]
```

### Explanation

`insert(index, value)` places the value at the requested position. Existing elements at that position and after it shift to the right.

---

## 8. `remove()` with duplicates

```python
items = ["A", "B", "A", "C", "A"]
items.remove("A")
```

### Correct answer

```python
items  # ["B", "A", "C", "A"]
```

Two `"A"` values remain.

### Explanation

`remove(value)` removes the **first matching occurrence by value**.

If the value is absent, `remove()` raises `ValueError`.

---

## 9. `pop()`

```python
tasks = ["task1", "task2", "task3"]
last_task = tasks.pop()
```

### Correct answer

```python
tasks       # ["task1", "task2"]
last_task   # "task3"
```

### Explanation

With no argument, `pop()` removes the last element and **returns the removed object itself**.

It does not return a one-element list.

```python
removed = items.pop(2)
```

With an index, it removes and returns the object at that index.

---

## 10. `clear()` vs rebinding

### Case 1

```python
items = ["A", "B"]
other = items
items.clear()
```

### Correct answer

Both names refer to the same now-empty list:

```python
items  # []
other  # []
```

### Case 2

```python
items = ["A", "B"]
other = items
items = []
```

### Correct answer

```python
items  # []
other  # ["A", "B"]
```

### Explanation

`clear()` mutates the existing list object.

`items = []` creates a new empty list object and rebinds `items` to it. `other` still refers to the original list.

> Mutation changes the object. Rebinding changes what a name refers to.

---

## 11. Basic slicing

```python
numbers = [10, 20, 30, 40, 50, 60]
```

### Correct answer

```python
numbers[1:4]  # [20, 30, 40]
numbers[:3]   # [10, 20, 30]
numbers[2:]   # [30, 40, 50, 60]
numbers[:]    # [10, 20, 30, 40, 50, 60]
```

### Explanation

The general form is:

```python
sequence[start:stop:step]
```

`start` is included and `stop` is excluded.

`numbers[:]` creates a shallow copy of the outer list.

---

## 12. Slicing with `step`

```python
numbers = [0, 1, 2, 3, 4, 5, 6]
```

### Correct answer

```python
numbers[1:6:2]  # [1, 3, 5]
numbers[::2]     # [0, 2, 4, 6]
```

### Explanation

`step` determines how far slicing moves between selected positions.

For `numbers[1:6:2]`:

```text
index 1 -> take 1
move 2 -> take 3
move 2 -> take 5
stop before index 6
```

---

## 13. Negative-step slicing

```python
numbers = [10, 20, 30, 40, 50, 60]
```

### Correct answer

```python
numbers[::-1]     # [60, 50, 40, 30, 20, 10]
numbers[4:1:-1]   # [50, 40, 30]
numbers[5:1:-2]   # [60, 40]
```

### Explanation

A negative step makes slicing traverse from right to left.

The same start-inclusive / stop-exclusive rule still applies.

> Negative `step` means move backward through the sequence.

---

## 14. Slice assignment

```python
numbers = [10, 20, 30, 40, 50]
numbers[1:4] = [99]
```

### Correct answer

```python
numbers  # [10, 99, 50]
```

### Explanation

Slice assignment mutates the existing list.

The replacement does not have to contain the same number of elements as the slice being replaced. Therefore a list can grow or shrink.

---

## 15. Slice assignment with a string

```python
items = ["A", "B", "C", "D"]
items[1:3] = "XYZ"
```

### Correct answer

```python
items  # ["A", "X", "Y", "Z", "D"]
```

### Explanation

The right-hand side is an iterable. A string is iterable over its characters, so the slice is replaced with `X`, `Y`, and `Z` individually.

---

## 16. `len()` vs index

```python
items = ["A", "B", "C", "D", "E"]
```

### Correct answer

```python
len(items)  # 5
items[4]    # "E"
```

### Explanation

`len()` returns the **number of elements**.

The last valid positive index is:

```python
len(items) - 1
```

So for length `5`, the last valid positive index is `4`.

---

## 17. Membership

```python
permissions = ["read", "write", "delete"]
```

### Correct answer

```python
"write" in permissions   # True
"admin" in permissions   # False
"admin" not in permissions  # True
```

### Explanation

`in` and `not in` test whether a value is a member of the collection. They answer an existence question, not a position question.

---

## 18. Shallow copy — replacing an outer element

```python
items = [["A", "B"], ["C", "D"]]
other = items.copy()
items[0] = ["X", "Y"]
```

### Correct answer

```python
items  # [["X", "Y"], ["C", "D"]]
other  # [["A", "B"], ["C", "D"]]
```

### Explanation

`items.copy()` creates a new outer list, but initially copies the references stored in its slots.

`items[0] = ["X", "Y"]` replaces the reference in slot `0` of `items`. It does not mutate the old inner list.

Therefore `other[0]` still refers to `["A", "B"]`.

---

## 19. Shallow copy — mutating a nested object

```python
items = [["A", "B"], ["C", "D"]]
other = items.copy()
items[0].append("X")
```

### Correct answer

```python
items  # [["A", "B", "X"], ["C", "D"]]
other  # [["A", "B", "X"], ["C", "D"]]
```

### Explanation

The outer lists are different, but their slot `0` references initially point to the same inner list.

`items[0].append("X")` mutates that shared inner list, so both outer lists observe the change.

> Shallow copy copies the outer container, not nested mutable objects.

---

## 20. Shallow copy with dictionaries

```python
users = [
    {"name": "Alice"},
    {"name": "Bob"}
]

backup = users.copy()
users[0]["name"] = "Subir"
```

### Correct answer

```python
users = [
    {"name": "Subir"},
    {"name": "Bob"}
]

backup = [
    {"name": "Subir"},
    {"name": "Bob"}
]
```

### Explanation

The first dictionary object is shared between the two outer lists.

`users[0]["name"] = "Subir"` mutates that dictionary rather than replacing `users[0]` with a different dictionary.

Therefore both lists observe the mutation.

---

## 21. `index()` vs `count()` vs `in`

```python
items = ["A", "B", "C", "B", "D", "B"]
```

### Correct answer

```python
items.index("B")  # 1
items.count("B")   # 3
"X" in items       # False
```

For:

```python
items.index("X")
```

the result is:

```text
ValueError
```

### Explanation

- `index(value)` -> first matching position.
- `count(value)` -> number of occurrences.
- `in` -> membership check.

`index()` raises `ValueError` when the requested value is not present.

Do not confuse this with invalid positional access such as `items[10]`, which raises `IndexError`.

---

## 22. `reverse()`

```python
numbers = [1, 2, 3, 4]
result = numbers.reverse()
```

### Correct answer

```python
numbers  # [4, 3, 2, 1]
result   # None
```

### Explanation

`reverse()` is a list method that mutates the existing list in place.

It returns `None`.

---

## 23. `sort()` vs `sorted()`

```python
numbers = [5, 2, 4, 1, 3]

a = numbers.sort()
b = sorted(numbers)
```

### Correct answer

```python
numbers  # [1, 2, 3, 4, 5]
a        # None
b        # [1, 2, 3, 4, 5]
```

### Explanation

`sort()` is a **list method**. It mutates the existing list and returns `None`.

`sorted()` is a **built-in function**. It does not mutate the original and returns a new sorted list. It can accept any iterable.

Both support `key=` and `reverse=`.

---

## 24. `reversed()`

```python
numbers = [10, 20, 30, 40]
result = reversed(numbers)
```

### Correct answer

```python
numbers       # [10, 20, 30, 40]
list(result)  # [40, 30, 20, 10]
```

### Explanation

`reversed()` does not mutate the original list. It returns a reverse iterator.

The iterator can then be consumed or materialized into a new list with `list(result)`.

Compare:

```python
numbers.reverse()  # mutates list
reversed(numbers)  # returns reverse iterator
```

---

## 25. `del`

```python
items = ["A", "B", "C", "D", "E"]
del items[1:4]
```

### Correct answer

```python
items  # ["A", "E"]
```

### Explanation

`del` can remove an element by index or a range by slice.

Compare the three removal operations:

```text
remove(value) -> remove by value; first match; returns None
pop(index)    -> remove by index; returns removed object
 del index    -> remove by index/slice; no returned value
```

`remove()` and `pop()` are methods. `del` is a Python statement.

---

## 26. List concatenation with `+`

```python
a = [1, 2]
b = [3, 4]
c = a + b
```

### Correct answer

```python
a  # [1, 2]
b  # [3, 4]
c  # [1, 2, 3, 4]
```

### Explanation

`+` creates a new outer list. It does not mutate `a` or `b`.

---

## 27. List repetition with `*`

```python
items = ["A", "B"]
result = items * 3
```

### Correct answer

```python
items   # ["A", "B"]
result  # ["A", "B", "A", "B", "A", "B"]
```

### Explanation

A new outer list is created, but the references to the existing element objects are repeated.

The elements are not automatically deep-copied.

---

## 28. Shared-reference trap

```python
items = [[]] * 3
items[0].append("A")
```

### Correct answer

```python
items  # [["A"], ["A"], ["A"]]
```

### Explanation

The repetition operation creates one outer list containing three references to the **same inner list object**.

Conceptually:

```text
slot 0 ─┐
slot 1 ─┼──> same inner list []
slot 2 ─┘
```

Appending through any slot mutates that same shared inner list.

---

## 29. `+=` vs `+`

```python
a = [1, 2]
b = a

a += [3, 4]

c = a + [5, 6]
```

### Correct answer

```python
a  # [1, 2, 3, 4]
b  # [1, 2, 3, 4]
c  # [1, 2, 3, 4, 5, 6]
```

### Explanation

For lists, `+=` performs in-place concatenation and mutates the existing list. Because `b` refers to the same list, `b` observes the mutation.

`a + [5, 6]` creates a new list. The assignment to `c` then binds `c` to that new list.

Important:

> `=` itself does not create a list. `+` creates the new list; `=` binds the name to it.

---

## 30. Final mixed mental model

```python
items = ["A", ["B", "C"], "D"]

other = items.copy()

items.append("E")
items[1].append("X")
other[0] = "Z"
```

### Correct answer

```python
items
# ["A", ["B", "C", "X"], "D", "E"]

other
# ["Z", ["B", "C", "X"], "D"]
```

### Which object is shared?

The inner list:

```python
["B", "C", "X"]
```

is shared between `items[1]` and `other[1]`.

The two outer lists are different objects because `copy()` created a new outer list.

### Which operation affects only `items`?

```python
items.append("E")
```

This mutates the outer `items` list. `other` is a different outer list, so it does not change.

### Which operation affects both lists?

```python
items[1].append("X")
```

This mutates the shared inner list object. Both outer lists contain a reference to that same inner object.

### Which operation affects only `other`?

```python
other[0] = "Z"
```

This replaces the reference stored in slot `0` of `other`. It does not mutate the shared inner list and does not modify `items[0]`.

### Final mental model

```text
items  ──> outer list A
             ├── slot 0 -> "A"
             ├── slot 1 ───────┐
             │                 ↓
             │             ["B", "C", "X"]  <- shared inner list
             │                 ↑
             │                 │
other  ──> outer list B       slot 1
             └── slot 0 -> "Z"

items also has slot 3 -> "E"
```

The key distinction is:

> Mutating an object affects every reference to that object. Replacing a slot affects only the container whose slot was replaced.

---

# Final List Completion Check

The 30-question revision covered:

- ordered and mutable list model
- indexing and negative indexing
- mutation vs rebinding
- aliasing
- `append()` / `extend()` / `insert()`
- `remove()` / `pop()` / `clear()` / `del`
- slicing and slice assignment
- `len()` and membership
- `index()` / `count()`
- shallow copying
- nested mutable references
- `reverse()` / `reversed()`
- `sort()` / `sorted()`
- `+` / `*` / `+=`
- shared-reference traps
- `ValueError` vs `IndexError`

## Definition of Done

**List: COMPLETE.**

The learner can reason about list behavior using the object/reference model rather than relying only on memorized method outputs.
