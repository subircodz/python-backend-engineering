# Python List — Interview Question Paper

**Purpose:** Repeated retrieval practice for Python List knowledge already taught in this repository.

**Level:** Interview / junior-to-mid Python engineering

**Total Marks:** 100

**Rule:** Answer without looking at the notes. For output questions, give the exact output and explain why. For design questions, explain the object/reference/mutation behaviour, not only the final result.

## Section A — Core Model and Indexing (20 marks)

### Q1 — List model (4 marks)
What makes a Python list different from a tuple? Explain mutability, ordering, and what an assignment such as `items = other` does with respect to the list object.

### Q2 — Indexing (4 marks)
Given `items = [10, 20, 30, 40, 50]`, state the values of `items[0]`, `items[2]`, `items[-1]`, and `items[-3]`. Explain why negative indexing works.

### Q3 — Index assignment (4 marks)
Trace:
```python
users = ["Alice", "Bob", "Charlie"]
users[1] = "Subir"
```
What changes? Is a new outer list created? Explain the slot/reference model.

### Q4 — Invalid access (4 marks)
What exception does `items[10]` raise when `items = [1, 2, 3]`? Contrast this with `items.index(10)` when `10` is absent.

### Q5 — `len()` and last index (4 marks)
For a list of length `n`, what is the last valid positive index? Why is it `n - 1` rather than `n`?

## Section B — Mutation, Aliasing and Methods (30 marks)

### Q6 — Aliasing (5 marks)
Predict and explain:
```python
items = ["A", "B"]
other = items
items.append("C")
print(items)
print(other)
```

### Q7 — `append()` vs `extend()` (5 marks)
Predict both results and explain the difference:
```python
a = ["A"]
a.append(["B", "C"])

b = ["A"]
b.extend(["B", "C"])
```

### Q8 — `extend()` and iterables (4 marks)
What does this produce, and why?
```python
items = ["A"]
items.extend("BC")
```
What happens if the argument is a dictionary?

### Q9 — `insert()` and shifting (4 marks)
Explain exactly what happens to the existing elements here:
```python
numbers = [10, 30, 40]
numbers.insert(1, 20)
```

### Q10 — `remove()` (4 marks)
Given:
```python
items = ["A", "B", "A", "C", "A"]
items.remove("A")
```
What remains? Which occurrence is removed? What happens if the value does not exist?

### Q11 — `pop()` (4 marks)
Explain the difference between `remove()` and `pop()`. Include what `pop()` returns and what happens with `pop()` versus `pop(index)`.

### Q12 — `clear()` vs rebinding (4 marks)
Trace both cases and explain why `other` differs:
```python
items = ["A", "B"]
other = items
items.clear()
```
and
```python
items = ["A", "B"]
other = items
items = []
```

## Section C — Slicing and List Operations (20 marks)

### Q13 — Basic slicing (4 marks)
For `numbers = [10, 20, 30, 40, 50, 60]`, give the results of `numbers[1:4]`, `numbers[:3]`, `numbers[2:]`, and `numbers[:]`. Explain start-inclusive/stop-exclusive behaviour.

### Q14 — Step slicing (4 marks)
Predict:
```python
numbers = [0, 1, 2, 3, 4, 5, 6]
print(numbers[1:6:2])
print(numbers[::2])
```

### Q15 — Reverse slicing (4 marks)
Predict:
```python
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[::-1])
print(numbers[4:1:-1])
print(numbers[5:1:-2])
```
Explain how a negative step changes traversal.

### Q16 — Slice assignment (4 marks)
Predict and explain:
```python
numbers = [10, 20, 30, 40, 50]
numbers[1:4] = [99]
```
Why can slice assignment change the length of a list?

### Q17 — Concatenation and repetition (4 marks)
Explain whether the following mutate the originals:
```python
c = a + b
x = items * 3
```
What is the important reference-sharing edge case when the repeated element itself is mutable?

## Section D — Copying, Ordering and Built-ins (15 marks)

### Q18 — Shallow copy (5 marks)
Trace:
```python
items = [["A", "B"], ["C", "D"]]
other = items.copy()
items[0].append("X")
```
Give both lists and explain which objects are shared.

### Q19 — Replacement after shallow copy (4 marks)
Now trace:
```python
items = [["A", "B"], ["C", "D"]]
other = items.copy()
items[0] = ["X", "Y"]
```
Why does `other` not change this time?

### Q20 — `sort()` vs `sorted()` (3 marks)
Explain the difference between:
```python
result = numbers.sort()
result = sorted(numbers)
```
Include mutation and return value.

### Q21 — `reverse()` vs `reversed()` (3 marks)
Explain the difference between `items.reverse()` and `reversed(items)`. What does each return and what happens to the original list?

## Section E — Membership, Search and Deletion (10 marks)

### Q22 — Search operations (4 marks)
For:
```python
items = ["A", "B", "C", "B", "D", "B"]
```
Explain the purpose and result of `items.index("B")`, `items.count("B")`, and `"X" in items`. What exception does `items.index("X")` raise?

### Q23 — `del` (3 marks)
Predict:
```python
items = ["A", "B", "C", "D", "E"]
del items[1:4]
```
Contrast `del` with `remove()` and `pop()`.

### Q24 — Membership vs position (3 marks)
A production function only needs to know whether a permission exists. Why is `"write" in permissions` conceptually different from calling `permissions.index("write")`?

## Section F — Interview Tracing and Engineering Judgement (5 marks)

### Q25 — Mutation during iteration (5 marks)
Trace carefully:
```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
    numbers.pop()

print(numbers)
```
Give the output and final list. Explain why changing the list while iterating can cause elements to be skipped.

## Scoring Standard

- **90–100:** Interview-ready for the tested List concepts; mental model is reliable.
- **80–89:** Strong, but review the missed edge cases before relying on this topic in interviews.
- **70–79:** Functional knowledge, but important reasoning gaps remain.
- **Below 70:** Re-study the relevant notes and repeat the paper after a delay.

**Important:** A correct final output with an incorrect explanation does not receive full marks. The objective is to verify the mental model of objects, references, mutation, rebinding, iteration, and container operations.
