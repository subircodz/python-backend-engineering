# Module Execution

## Purpose

Understand what happens when Python executes a module, especially during `import`.

## Module execution during import

When Python imports a module, it does not simply make the `.py` file available. Python creates a module object, registers it in `sys.modules`, and then executes the module's top-level code.

Conceptually:

```text
Find module
    ↓
Create module object
    ↓
Put module in sys.modules
    ↓
Execute module code
    ↓
Import completed
```

A module can therefore be present in `sys.modules` before all of its code has finished executing. This is also why circular imports can encounter a partially initialized module.

## Top-level code executes during import

Given:

```python
# calculator.py

x = 10

def add(a, b):
    return a + b

print("calculator loaded")
```

When `calculator` is imported:

- `x = 10` executes.
- The `def add(...)` statement executes and creates the function object.
- The body of `add()` does **not** execute yet.
- `print("calculator loaded")` executes.

## Function definition vs function execution

A function definition creates a function object when the module is executed, but the function body runs only when the function is called.

Example:

```python
print("Start")

def add(a, b):
    print("Inside add")
    return a + b

print("End")
```

Importing this module produces:

```text
Start
End
```

The output from `Inside add` appears only when `add()` is actually called.

## Example

```python
# calculator.py
print("Start")

def add(a, b):
    print("Inside add")
    return a + b

print("End")
```

```python
# main.py
import calculator

print("Main")
calculator.add(2, 3)
```

Output:

```text
Start
End
Main
Inside add
5
```

### Why?

`import calculator` executes the top-level statements in `calculator.py`. The `def` statement creates `add`, but its body waits for a call.

Later:

```python
calculator.add(2, 3)
```

calls the function, so its body executes.

## Connection with `sys.modules`

A second import normally reuses the module already stored in `sys.modules` instead of executing the module from scratch again.

```python
import calculator
import calculator
```

Therefore, a top-level statement such as:

```python
print("calculator loaded")
```

normally runs only during the first import in that Python process.

## Core mental model

Keep these two ideas separate:

```text
Module import
    → executes module-level code
    → creates function/class objects

Function call
    → executes the function body
```

## Current learning boundary

At this stage, the goal is to understand normal module execution and its relationship with imports and `sys.modules`.

Python bytecode, compilation internals, import loaders, and other interpreter internals are intentionally deferred until they become useful for practical engineering work.
