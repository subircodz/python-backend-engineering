# Python Set — Interview Question Paper

**Level:** Interview / junior-to-mid Python engineering

**Total Marks:** 100

**Scope:** Set fundamentals and creation/syntax taught so far. Set methods and set algebra will be added to this paper when those topics are taught.

## Section A — Set Mental Model (25 marks)

### Q1 — Core model (5 marks)
What problem is a Python set designed to solve better than a list? Explain uniqueness, membership testing, ordering, and mutability.

### Q2 — Duplicate values (5 marks)
Predict:
```python
numbers = {10, 20, 10, 30, 20}
print(len(numbers))
```
Why is the result not `5`?

### Q3 — Hashable elements (5 marks)
Why can integers and strings normally be set elements while lists and dictionaries cannot? Explain the requirement in terms of hashability.

### Q4 — Ordering and indexing (5 marks)
Why is this invalid?
```python
numbers = {10, 20, 30}
print(numbers[0])
```
What mental model should you use instead of positional access?

### Q5 — Set vs sequence (5 marks)
A function only needs to answer “is this user ID allowed?”. Explain why a set may be a better data structure than a list for that requirement.

## Section B — Creation and Syntax (25 marks)

### Q6 — Literal vs constructor (5 marks)
Explain the difference between:
```python
allowed = {"GET", "POST", "PUT"}
```
and
```python
allowed = set(["GET", "POST", "PUT"])
```
When is each syntax natural?

### Q7 — Empty collections (5 marks)
Classify:
```python
{}
set()
```
Why does Python use `{}` for an empty dictionary rather than an empty set?

### Q8 — Constructor from iterable (5 marks)
Trace:
```python
values = [10, 20, 10, 30, 20]
numbers = set(values)
```
What does the constructor do? Is `values` modified?

### Q9 — String conversion (5 marks)
What is the purpose of:
```python
unique_chars = set("hello")
```
What properties of the resulting collection should your code avoid depending on?

### Q10 — Nested set syntax (5 marks)
Why does a set containing another ordinary set fail? What property of the inner set prevents it from being a set element? Name the immutable set-like type that exists for this purpose, without relying on its methods yet.

## Section C — Interview Tracing (25 marks)

### Q11 — Equality and duplicates (5 marks)
If a set receives values `10` and another equal `10`, why does it retain only one logical value? Explain the role of equality and hashing at a high level.

### Q12 — Conversion pipeline (5 marks)
A list contains repeated employee IDs. Write a short Python expression that produces unique IDs using the `set()` constructor. Explain each stage.

### Q13 — Invalid positional thinking (5 marks)
A developer writes `users_set[0]` because they want “the first user”. Explain why this is a design smell for a set and what requirement should be clarified before choosing a data structure.

### Q14 — Hashability diagnosis (5 marks)
What exception would you expect from:
```python
values = {[1, 2], [3, 4]}
```
Explain the underlying reason rather than only naming the exception.

### Q15 — Production choice (5 marks)
You receive 100,000 permission strings and repeatedly need membership checks. Explain why a set is a natural candidate. Also state one reason you should not use a set if the application requirement is to preserve a meaningful sequence position.

## Section D — Design and Explanation (25 marks)

### Q16 — API validation design (5 marks)
An API receives a requested HTTP method and must validate it against `GET`, `POST`, and `PUT`. Propose a suitable set declaration and explain why it communicates the requirement clearly.

### Q17 — Deduplication trade-off (5 marks)
You convert a list to a set to remove duplicates. What information may you lose by doing so? Explain why this matters when order is meaningful.

### Q18 — Set and mutable values (5 marks)
Why is “the set is mutable” not a contradiction with “set elements must be hashable”? Distinguish mutability of the container from hashability of its elements.

### Q19 — Constructor reasoning (5 marks)
Compare these requirements:
1. “I already know the unique allowed values and want to declare them clearly.”
2. “I have an existing iterable and want a set containing its unique values.”
Which syntax would you choose for each and why?

### Q20 — Mental model test (5 marks)
Explain this statement in your own words:
> A set is primarily a uniqueness-and-membership data structure, not a positional sequence.

## Scoring Standard

- **90–100:** Strong interview-level understanding of the Set concepts taught so far.
- **80–89:** Strong but review the missed edge cases.
- **70–79:** Basic model is present but design reasoning needs work.
- **Below 70:** Re-study Set fundamentals and creation/syntax before repeating.

This paper will be extended, not rewritten, when Set Methods and Operations are taught.
