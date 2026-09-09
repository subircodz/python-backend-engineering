# Modules, Namespaces and Imports

## Purpose

This document explains how Python organizes code across files and namespaces using modules and imports.

The goal is to understand the runtime model behind:

- modules
- module namespaces
- `import`
- `from ... import ...`
- name resolution
- name conflicts between modules

---

## 1. What is a Module?

A **module** is a Python module object that provides a namespace containing names such as:

- variables
- functions
- classes
- other imported names

A `.py` file is commonly used as the source from which Python creates a module when it is imported.

For example:

```python
# calculator.py

x = 10

def add(a, b):
    return a + b
```

When another Python file imports `calculator`, Python makes the module available through the name `calculator`.

```python
# main.py

import calculator

print(calculator.x)
print(calculator.add(2, 3))
```

Output:

```text
10
5
```

Here, `calculator` refers to the imported module.

---

## 2. A Module Has Its Own Namespace

A module provides its own namespace.

For example:

```python
# calculator.py

x = 10
```

```python
# main.py

import calculator

x = 100

print(x)
print(calculator.x)
```

Output:

```text
100
10
```

There is no conflict between the two `x` names.

Conceptually:

```text
main namespace
----------------
x = 100
calculator -> module


calculator namespace
--------------------
x = 10
```

Therefore:

```python
x
```

refers to `x` in the current namespace.

Whereas:

```python
calculator.x
```

means:

> Find the module referenced by `calculator`, then find `x` inside that module.

This is an important distinction from local, enclosing and global scope. A module itself is also a namespace in which names are defined.

---

## 3. `import module`

The basic form is:

```python
import calculator
```

This makes the name `calculator` available in the current namespace.

The names defined inside the module are accessed through that name:

```python
calculator.x
calculator.add(2, 3)
```

The module name acts as the qualifier.

Example:

```python
# calculator.py

x = 10

def add(a, b):
    return a + b
```

```python
# main.py

import calculator

print(calculator.x)
print(calculator.add(5, 3))
```

Output:

```text
10
8
```

The current namespace contains the name:

```text
calculator
```

not direct names such as `x` and `add`.

---

## 4. `from module import name`

Python also allows a specific name to be imported:

```python
from calculator import add
```

Now `add` is available directly in the current namespace.

```python
print(add(5, 3))
```

The module does not need to be referenced explicitly in the call.

Conceptually:

```text
main namespace
----------------
add -> calculator.add
```

This is different from:

```python
import calculator
```

where the current namespace contains:

```text
calculator -> calculator module
```

---

## 5. Importing One Name Does Not Import Every Name Into the Current Namespace

Consider:

```python
# calculator.py

x = 10

def add(a, b):
    return a + b
```

```python
# main.py

from calculator import add

print(add(2, 3))
print(x)
```

The first statement works:

```text
5
```

But `x` is not available as a direct name in `main.py`.

The result is:

```text
NameError
```

The reason is that:

```python
from calculator import add
```

introduces `add` into the current namespace, not `x`.

Conceptually:

```text
main namespace
----------------
add -> calculator.add
x   -> not defined
```

The `calculator` module may have `x`, but `main.py` does not have a direct name `x`.

---

## 6. `NameError` vs `AttributeError`

These two errors are important when working with modules.

### NameError

A `NameError` occurs when Python cannot find the requested name in the relevant namespace.

Example:

```python
print(x)
```

If `x` has not been defined or imported into the current namespace:

```text
NameError
```

### AttributeError

An `AttributeError` occurs when an object exists, but the requested attribute does not exist on that object.

Example:

```python
import calculator

print(calculator.y)
```

If `calculator` exists but has no `y`:

```text
AttributeError
```

The distinction is:

```text
NameError
    "I cannot find this name."

AttributeError
    "I found the object, but it does not have this attribute."
```

---

## 7. Imported Names Can Be Rebound

Consider:

```python
# calculator.py

def add(a, b):
    return a + b
```

```python
# main.py

from calculator import add

def add(a, b):
    return a * b

print(add(2, 3))
```

Output:

```text
6
```

The imported `add` initially creates the name `add` in `main.py`.

Then:

```python
def add(a, b):
    return a * b
```

binds the name `add` to a new function in `main.py`.

The name has therefore been **rebound**.

This does not modify the original function in `calculator`.

Conceptually:

```text
calculator namespace
--------------------
add -> addition function


main namespace
--------------
add -> multiplication function
```

The two names exist independently.

This is another reason qualified access can sometimes make code clearer:

```python
import calculator

calculator.add(2, 3)
```

The origin of `add` is explicit.

---

## 8. Import Forms and the Names They Introduce

### `import calculator`

```python
import calculator
```

Introduces:

```text
calculator
```

into the current namespace.

Access:

```python
calculator.add(...)
calculator.x
```

---

### `from calculator import add`

```python
from calculator import add
```

Introduces:

```text
add
```

into the current namespace.

Access:

```python
add(...)
```

---

## 9. Namespace Mental Model

A useful mental model is to think of namespaces as mappings between names and objects.

For example:

```text
main.py

x          -> integer object
calculator -> calculator module
add        -> function object
```

And inside `calculator`:

```text
calculator module

x   -> integer object
add -> function object
```

The same name can exist in multiple namespaces.

For example:

```text
main.x         -> 100
calculator.x   -> 10
```

The name itself is not globally unique.

Its meaning depends on **which namespace Python is looking in**.

---

## 10. Why Modules Matter

Modules allow a Python application to divide code into separate responsibilities.

Instead of putting everything into one file:

```text
main.py
    database code
    validation code
    API code
    logging code
    business logic
    utility functions
```

we can separate responsibilities:

```text
project/
    main.py
    database.py
    validation.py
    api.py
    services.py
```

Each module can provide its own namespace.

This helps with:

- separation of responsibilities
- code organization
- reuse
- avoiding unnecessary name conflicts
- maintaining larger applications

Modules therefore provide both an **organizational boundary** and a **namespace boundary**.

---

## 11. Key Mental Models

### Module

A module is a Python module object containing names in its own namespace.

A `.py` file is commonly the source used to create that module.

### Namespace

A namespace is where names are associated with objects.

Different namespaces can contain the same name without those names referring to the same object.

### `import`

```python
import calculator
```

makes the module available through the name `calculator`.

### `from ... import ...`

```python
from calculator import add
```

binds the selected name, `add`, directly into the current namespace.

### Qualified access

```python
calculator.add
```

means that `add` is being looked up inside the namespace associated with `calculator`.

### Rebinding

If a name is assigned a new object:

```python
add = another_function
```

the name now refers to the new object in that namespace. This does not automatically change a similarly named object in another namespace.

---

## 12. Current Learning Boundary

This document covers:

- modules
- module namespaces
- importing modules
- importing specific names
- qualified names
- name resolution at the module level
- name conflicts and rebinding

The next topic is **packages**.

Packages build on modules by providing a way to organize related modules into a larger importable structure.
