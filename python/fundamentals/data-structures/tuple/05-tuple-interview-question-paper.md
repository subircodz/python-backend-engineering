# Python Tuple — Interview Question Paper

**Level:** Interview / junior-to-mid Python engineering

**Total Marks:** 100

**Scope:** All Tuple topics taught in the preceding Tuple notes: fundamentals, creation/syntax, packing/unpacking, methods, operations, immutability, references, and comparisons.

## Section A — Fundamentals and Creation (25 marks)

### Q1 — Tuple model (5 marks)
What does it mean to say a tuple is immutable? Explain what is immutable and what can still be changed when a tuple contains a mutable object.

### Q2 — Indexing (4 marks)
For `numbers = (10, 20, 30, 40, 50)`, give the results of `numbers[0]`, `numbers[-1]`, and `numbers[-3]`.

### Q3 — Immutability vs rebinding (4 marks)
Why does `numbers[0] = 99` raise an error while `numbers = (99, 20, 30)` works? Explain the difference between mutation and rebinding.

### Q4 — Comma creates the tuple (4 marks)
Classify each expression:
```python
(10)
(10,)
10, 20, 30
()
```
Explain why parentheses alone are not what fundamentally create a tuple.

### Q5 — Constructor (4 marks)
What does `tuple([10, 20, 10, 30])` do? Does it mutate the original list?

### Q6 — Mixed/nested values (4 marks)
Can a tuple contain different types and mutable objects? Give a production-relevant example and explain the reference implication.

## Section B — Packing and Unpacking (25 marks)

### Q7 — Basic unpacking (5 marks)
Trace:
```python
employee = ("Subir", 101, "Developer")
name, employee_id, role = employee
```
What is bound to each name? Does `employee` change?

### Q8 — Count mismatch (4 marks)
What exception should you expect if a tuple has three elements but you provide only two unpacking targets? Why?

### Q9 — Extended unpacking (5 marks)
Predict:
```python
numbers = (10, 20, 30, 40, 50)
first, *middle, last = numbers
```
Give the values and types of `first`, `middle`, and `last`.

### Q10 — Starred target (3 marks)
Why is the value captured by `*middle` a list even though the source is a tuple?

### Q11 — One starred target (4 marks)
What happens if an unpacking assignment contains two starred targets? Explain why Python cannot determine an unambiguous split.

### Q12 — Throwaway `_` (4 marks)
Explain the convention behind `_` in:
```python
name, _, role = employee
```
Is `_` a special keyword that prevents binding?

## Section C — Function Argument Packing/Unpacking (20 marks)

### Q13 — Call-site `*` (5 marks)
Explain:
```python
values = (10, 20, 30)
func(*values)
```
What is `*` doing at the call site?

### Q14 — Definition-site `*args` (5 marks)
Explain:
```python
def show(*args):
    print(args)
```
What type is `args` inside the function, and how is this different from `func(*values)`?

### Q15 — `**kwargs` (5 marks)
Explain the difference between collecting keyword arguments with `**kwargs` and unpacking a mapping with `func(**mapping)`.

### Q16 — Swapping (5 marks)
Explain why this works without a temporary variable:
```python
a = 10
b = 20
a, b = b, a
```
Describe the RHS-first evaluation model.

## Section D — Methods and Operations (20 marks)

### Q17 — `count()` and `index()` (4 marks)
For `numbers = (10, 20, 10, 30, 20)`, give the results of `numbers.count(20)` and `numbers.index(20)`. What happens for `numbers.index(99)`?

### Q18 — Concatenation (4 marks)
Explain what happens here:
```python
a = (10, 20)
b = (30, 40)
c = a + b
```
Are `a` and `b` mutated? Is `c` a new tuple?

### Q19 — Repetition (4 marks)
Predict:
```python
numbers = (10, 20)
result = numbers * 3
```
Explain what operation `*` performs on a tuple in this context.

### Q20 — Membership and slicing (4 marks)
Explain the results and whether either operation mutates the tuple:
```python
20 in numbers
numbers[1:4]
numbers[::-1]
```

### Q21 — `len`, `min`, `max`, `sum` (4 marks)
Which of these are tuple methods and which are built-ins? Explain the distinction.

## Section E — Comparisons and Reference Behaviour (10 marks)

### Q22 — Equality vs ordering (5 marks)
Explain the results:
```python
(10, 20) == (10, 20)
(10, 20) == (20, 10)
(10, 20, 30) < (10, 20, 40)
```
What does lexicographical comparison mean?

### Q23 — Tuple `+=` (5 marks)
Trace:
```python
numbers = (10, 20, 30)
old = numbers
numbers += (40,)
```
Are `old` and `numbers` still referring to the same tuple? Explain why tuple `+=` works despite tuple immutability.

## Section F — Nested Mutable Objects (10 marks)

### Q24 — Mutable object inside tuple (5 marks)
Predict:
```python
data = ([10, 20], [30, 40])
data[0].append(99)
print(data)
```
Why is this allowed even though the tuple itself is immutable?

### Q25 — Reference mental model (5 marks)
Explain this statement precisely:
> A tuple prevents changing which objects its slots refer to, but it does not make the referenced objects themselves immutable.

Use a nested list example.

## Scoring Standard

- **90–100:** Interview-ready on the Tuple concepts taught.
- **80–89:** Strong; review the missed edge cases.
- **70–79:** Usable knowledge but weak points remain.
- **Below 70:** Re-study the relevant Tuple notes and repeat later.

Correct output without correct reasoning receives reduced credit.
