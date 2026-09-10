# Python Data Structures — Interview Question Paper

**Level:** Interview / junior-to-mid Python engineering

**Total Marks:** 100

**Purpose:** Cross-topic retrieval across the List, Tuple, and Set material currently taught.

## Section A — Choosing the Structure (30 marks)

### Q1 (6 marks)
You need an ordered, mutable collection of tasks where items may be added, removed, and updated by position. Which structure would you choose and why?

### Q2 (6 marks)
You need a fixed ordered record such as `(employee_name, employee_id, role)`. Which structure is natural and why?

### Q3 (6 marks)
You repeatedly need to answer whether a permission string exists in a collection, and uniqueness matters. Which structure is a strong candidate and why?

### Q4 (6 marks)
Explain why choosing a set merely because it “removes duplicates” can be wrong when the original ordering has business meaning.

### Q5 (6 marks)
Compare List, Tuple, and Set on ordering, mutability, positional access, and uniqueness.

## Section B — Mutation and References (30 marks)

### Q6 (6 marks)
Explain the difference between mutating a list and rebinding a name that refers to a list. Give one example of each.

### Q7 (6 marks)
Why can a tuple be immutable while containing a mutable list? Explain the difference between the tuple's structure and the referenced object.

### Q8 (6 marks)
Explain what happens when two names refer to the same list and one name calls `append()`.

### Q9 (6 marks)
Why does list `+=` normally mutate the existing list while tuple `+=` creates a new tuple and rebinds the name?

### Q10 (6 marks)
Explain why shallow copying a nested list does not isolate nested mutable objects.

## Section C — Operations and Reasoning (20 marks)

### Q11 (5 marks)
Compare `list.index()`, `list.count()`, and `in`. What question does each answer and what exception can `index()` raise?

### Q12 (5 marks)
Compare list `sort()` with built-in `sorted()`, and list `reverse()` with built-in `reversed()`.

### Q13 (5 marks)
Explain tuple `count()`, `index()`, slicing, concatenation, and repetition. Which operations create new tuples rather than mutate them?

### Q14 (5 marks)
Explain why a set does not support indexing and why code should not depend on its iteration/display order.

## Section D — Integrated Interview Scenario (20 marks)

### Q15 (10 marks)
An API receives a list of requested permission names. The system must remove duplicates, then later preserve the user's original order for an audit response. Explain why blindly converting the input to a set and returning it is not sufficient. Propose a better high-level design.

### Q16 (10 marks)
A developer reports that “copying the list fixed the shared-state bug,” but nested dictionaries are still changing in both the original and backup. Explain why this can happen and what “shallow copy” means.

## Scoring Standard

- **90–100:** Strong cross-structure interview reasoning.
- **80–89:** Good; review structure-selection trade-offs.
- **70–79:** Basic understanding with gaps in references/mutation.
- **Below 70:** Re-study the individual structure papers.
