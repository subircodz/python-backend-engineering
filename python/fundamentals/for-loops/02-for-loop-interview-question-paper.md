# Python `for` Loops — Interview Question Paper

**Level:** Interview / junior-to-mid Python engineering

**Total Marks:** 100

**Scope:** Only the fundamental `for` loop model already taught here. `range()`, `enumerate()`, `break`, `continue`, nested loops, comprehensions, and generators are intentionally excluded until taught.

## Section A — Iteration Model (20 marks)

### Q1 — Core model (5 marks)
Explain what Python does conceptually when executing:
```python
numbers = [10, 20, 30]
for number in numbers:
    print(number)
```
Your answer must distinguish the list object, iterable traversal, and the loop-variable name.

### Q2 — Loop variable (5 marks)
Is `number` a copy of each list element, or a name bound to the current object? Explain precisely.

### Q3 — Post-loop binding (5 marks)
Predict:
```python
items = ["A", "B", "C"]
for item in items:
    print(item)
print(item)
```
Why does the final `print()` work?

### Q4 — Empty iterable (5 marks)
What should you expect about the loop variable after a `for` loop whose iterable contains no elements? Explain why this differs from a loop that executes at least once.

## Section B — Rebinding vs Mutation (30 marks)

### Q5 — Rebinding a scalar loop variable (5 marks)
Predict:
```python
numbers = [10, 20, 30]
for number in numbers:
    number = number * 2
print(numbers)
print(number)
```
Explain why the list is unchanged.

### Q6 — Mutating through the loop variable (5 marks)
Predict:
```python
numbers = [[10], [20], [30]]
for number in numbers:
    number.append(5)
print(numbers)
```
Explain why this changes the outer list's observed contents.

### Q7 — Mutation followed by rebinding (5 marks)
Trace:
```python
numbers = [[10], [20], [30]]
for number in numbers:
    number.append(5)
    number = [100]
print(numbers)
print(number)
```
Give the exact output and explain both operations separately.

### Q8 — Index assignment through loop variable (5 marks)
Why does this mutate the nested lists?
```python
numbers = [[10], [20], [30]]
for number in numbers:
    number[0] = 99
```
Contrast `number[0] = 99` with `number = [99]`.

### Q9 — `+` versus `+=` (5 marks)
Explain the difference in these two loop bodies:
```python
number = number + [5]
```
and
```python
number += [5]
```
Why do they produce different effects for a list object?

### Q10 — Outer-list mutation vs current binding (5 marks)
Predict:
```python
numbers = [10, 20, 30]
for number in numbers:
    numbers[0] = 99
    print(number)
print(numbers)
```
Why does the first printed value remain `10`?

## Section C — Mutating the Iterated List (30 marks)

### Q11 — Append while iterating (6 marks)
Consider:
```python
numbers = [10, 20, 30]
for number in numbers:
    numbers.append(40)
    print(number)
```
Will this necessarily terminate? Explain the iterator/list interaction and the engineering risk.

### Q12 — Pop while iterating (6 marks)
Trace:
```python
numbers = [10, 20, 30]
for number in numbers:
    print(number)
    numbers.pop()
print(numbers)
```
Give the exact output and final list.

### Q13 — Remove current value (6 marks)
Trace:
```python
numbers = [10, 20, 30]
for number in numbers:
    numbers.remove(number)
print(numbers)
```
Why is `20` left behind?

### Q14 — Engineering decision (6 marks)
A developer writes a loop that removes selected items from the same list being iterated. Explain why this is dangerous and give a safer high-level strategy without using constructs that have not yet been taught.

### Q15 — Reference reasoning (6 marks)
Explain why modifying the outer list can affect future iteration while rebinding the loop variable generally does not modify the outer list.

## Section D — Integrated Interview Tracing (20 marks)

### Q16 — Combined mutation/rebinding (5 marks)
Predict:
```python
numbers = [[10], [20], [30]]
for number in numbers:
    number.append(5)
    number = [100]
    print(number)
print(numbers)
```

### Q17 — List element replacement during iteration (5 marks)
Predict:
```python
numbers = [10, 20, 30]
for number in numbers:
    numbers[0] = 99
    number = 500
print(numbers)
print(number)
```
Explain why the two assignments affect different things.

### Q18 — Identify the bug (5 marks)
A production script uses:
```python
for item in items:
    if some_condition(item):
        items.remove(item)
```
Explain the failure mode in terms of iteration position and changing list indexes. Would you consider this safe by default?

### Q19 — Mental-model explanation (5 marks)
Complete this rule in your own words:
> `name = value` ________ a name; `name.method()` may ________ an object.
Then give one example of each using a list loop.

## Scoring Standard

- **90–100:** Strong interview-level understanding of fundamental `for` loops.
- **80–89:** Good understanding; review edge cases involving mutation.
- **70–79:** Basic syntax is usable but execution/reference reasoning needs work.
- **Below 70:** Re-study the loop note and repeat later.

Full marks require correct reasoning, not just correct output.
