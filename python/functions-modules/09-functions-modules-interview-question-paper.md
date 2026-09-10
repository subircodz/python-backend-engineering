# Python Functions, Modules and Packages — Interview Question Paper

**Level:** Interview / junior-to-mid Python engineering

**Total Marks:** 100

**Scope:** All functions/modules topics already taught in this directory: modules and namespaces, packages and relative imports, import resolution, `sys.path`, `sys.modules`, module execution/caching, `*args`/`**kwargs`, parameter binding, closures, higher-order functions, first-class functions, `map`, `filter`, `reduce`, `sorted(key=...)`, and lambda usage.

## Section A — Modules, Namespaces and Imports (25 marks)

### Q1 — Module mental model (4 marks)
What is a Python module? Explain what namespace a module provides and why modules help prevent unrelated names from colliding.

### Q2 — Import forms (4 marks)
Explain the practical difference between:
```python
import math
```
and
```python
from math import sqrt
```
What names become available in the importing module?

### Q3 — Namespace lookup (4 marks)
Why does `math.sqrt(16)` work after `import math`, while `sqrt(16)` does not necessarily work? Explain the name-binding model.

### Q4 — Package hierarchy (4 marks)
Given:
```text
backend/
    users/
        models.py
```
Explain what `backend.users.models.User` represents if `User` is defined in `models.py`.

### Q5 — Relative imports (5 marks)
Explain the meaning of `.` and `..` in a relative import. When would you use a relative import inside a package?

### Q6 — Package exports (4 marks)
What role can `__init__.py` play in a package? Explain package-level exports without assuming that every package must re-export everything.

## Section B — Import Resolution and Execution (25 marks)

### Q7 — `sys.path` (5 marks)
What is `sys.path` used for during an import? Explain at a high level how Python uses it to locate importable modules/packages.

### Q8 — `sys.modules` (5 marks)
What is stored in `sys.modules`? Why is it important for repeated imports in the same Python process?

### Q9 — Repeated import (5 marks)
Suppose `example.py` contains:
```python
print("module executed")
```
Then another module executes:
```python
import example
import example
```
How many times should the top-level print normally execute in that process? Explain the role of import caching.

### Q10 — Module execution order (5 marks)
Does `import module_name` merely make names visible, or can it execute top-level module code? Explain the normal module-loading sequence at a conceptual level.

### Q11 — Import debugging (5 marks)
An application raises `ModuleNotFoundError` for a module that exists on disk. What should you investigate about the import search path and package structure before randomly changing imports?

## Section C — Function Parameters and Binding (25 marks)

### Q12 — `*args` collection (5 marks)
Explain:
```python
def show(*args):
    print(args)

show(10, 20, 30)
```
What is `args` and what type does it have?

### Q13 — Call-site unpacking (5 marks)
Explain:
```python
values = (10, 20, 30)
show(*values)
```
How is this different from defining `def show(*args)`?

### Q14 — `**kwargs` (5 marks)
Explain both:
```python
def configure(**kwargs):
    ...
```
and
```python
settings = {"host": "localhost", "port": 8000}
configure(**settings)
```
Distinguish collection from unpacking.

### Q15 — Keyword-only parameters (5 marks)
Why would an API designer use:
```python
def create_user(name, *, is_admin=False):
    ...
```
What calls should be accepted or rejected, and what design benefit does this provide?

### Q16 — Positional-only parameters (5 marks)
Explain the purpose of `/` in a function signature such as:
```python
def calculate(amount, /, tax):
    ...
```
What calling restriction does it impose on `amount`?

## Section D — Closures and First-Class Functions (15 marks)

### Q17 — Function object vs function call (5 marks)
Explain the difference between:
```python
operation = add
```
and
```python
result = add(10, 20)
```
What does each name refer to?

### Q18 — Passing a function (5 marks)
Trace conceptually:
```python
def execute(operation, value):
    return operation(value)

result = execute(double, 10)
```
What is passed to `execute`, what happens inside, and what is returned?

### Q19 — Closure (5 marks)
Explain how a nested function can remember a variable from its enclosing function after the enclosing function has returned. Use the term closure correctly and distinguish the captured variable from the returned function object.

## Section E — Higher-Order Functions and Pythonic Design (10 marks)

### Q20 — `map()` (3 marks)
What does `map()` conceptually do? Explain the difference between passing a function object and calling the function before passing it.

### Q21 — `filter()` (3 marks)
What does `filter()` expect from its function argument? Explain what determines whether an element is retained.

### Q22 — `reduce()` (2 marks)
At a high level, what problem does `reduce()` solve? Give one example where it could combine many values into one result.

### Q23 — `sorted(key=...)` and lambda (2 marks)
Explain why this is useful:
```python
users = [{"name": "A", "age": 30}, {"name": "B", "age": 20}]
sorted(users, key=lambda user: user["age"])
```
What does `key` receive and what does it return?

## Scoring Standard

- **90–100:** Strong interview-level understanding of the functions/modules material taught.
- **80–89:** Strong, with some areas requiring retrieval practice.
- **70–79:** Working knowledge but important runtime/binding gaps remain.
- **Below 70:** Re-study the relevant topic notes and repeat after a delay.

**Full-credit principle:** A memorized definition is not enough. For tracing questions, explain what object is created, what name is bound, what gets called, and what gets returned.
