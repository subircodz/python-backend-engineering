# Python Fundamentals — Interview Question Bank

**Purpose:** A recurring master paper for the Python fundamentals currently taught in this directory.

**Current coverage:** Lists, fundamental `for` loops, Tuples, and Sets.

**Rule:** The individual topic papers are the primary papers. This file is for mixed retrieval so that knowledge is tested without being grouped by concept.

## Mixed Interview Paper — 100 Marks

### Q1 (5 marks)
Explain the difference between mutation and rebinding using a list example.

### Q2 (5 marks)
Why does `items = other` not copy a list? Explain aliasing.

### Q3 (5 marks)
Predict the result of a list `pop()` operation and explain what value the method returns.

### Q4 (5 marks)
Explain why `items[10]` and `items.index(10)` can raise different exception types when `10` is unavailable.

### Q5 (5 marks)
Explain why `items[:]` is a shallow copy rather than a deep copy.

### Q6 (5 marks)
Predict and explain a `for` loop where the loop variable is rebound inside the body. Does the source list change?

### Q7 (5 marks)
Predict and explain a `for` loop where the loop variable calls `append()` on a nested list.

### Q8 (5 marks)
Explain why modifying the same list being iterated can cause skipped elements or non-termination.

### Q9 (5 marks)
Explain why `(10)` is not a one-element tuple but `(10,)` is.

### Q10 (5 marks)
Explain tuple immutability versus rebinding and give one example where rebinding is valid.

### Q11 (5 marks)
Predict extended tuple unpacking with `first, *middle, last` and state the type of `middle`.

### Q12 (5 marks)
Explain the difference between `func(*values)`, `def func(*args)`, and `func(**mapping)` at a conceptual level.

### Q13 (5 marks)
Explain tuple lexicographical comparison and distinguish it from equality comparison.

### Q14 (5 marks)
Explain why `tuple += tuple_value` can work even though tuples are immutable.

### Q15 (5 marks)
Explain why a set is useful for uniqueness and membership but not positional access.

### Q16 (5 marks)
Explain the difference between `{}` and `set()` and why both are not empty sets.

### Q17 (5 marks)
Explain what `set(iterable)` does and whether it mutates the source iterable.

### Q18 (5 marks)
Explain why a list cannot normally be a set element. Use the term “hashable” correctly.

### Q19 (5 marks)
Choose List, Tuple, or Set for each of three realistic requirements and justify each choice using properties rather than memorized slogans.

### Q20 (5 marks)
A candidate gives correct outputs for all questions but repeatedly says “the variable contains a copy of the object” when Python actually only rebinds a name. Explain why this mental-model error matters in production code.

## Scoring Standard

- **90–100:** Strong mixed retrieval across current fundamentals.
- **80–89:** Good retention; repeat weak topics separately.
- **70–79:** Knowledge is present but not yet reliable under mixed questioning.
- **Below 70:** Return to the topic notes before repeating.

Scores from this paper should be tracked over time. Improvement in explanation quality matters as much as the numerical score.
