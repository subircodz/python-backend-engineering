# `*args` and `**kwargs`

## Purpose

Understand how Python functions collect and unpack variable numbers of positional and keyword arguments.

## `*args`: collecting positional arguments

When `*args` appears in a function parameter list, Python collects the extra positional arguments into a tuple.

```python
def show(*args):
    print(args)

show(10, 20, 30)
```

Inside the function:

```text
args → (10, 20, 30)
```

Examples:

```text
show()           → ()
show(10)         → (10,)
show(10, 20)     → (10, 20)
show(10, 20, 30) → (10, 20, 30)
```

A one-element tuple needs a trailing comma: `(10,)`.

Because the collected value is a tuple, its elements cannot be changed:

```python
args[0] = 100
```

raises `TypeError` because tuples are immutable.

The local name `args` itself can still be rebound:

```python
args = (100, 20)
```

This is rebinding the name, not mutating the original tuple.

## `**kwargs`: collecting keyword arguments

When `**kwargs` appears in a function parameter list, Python collects the extra keyword arguments into a dictionary.

```python
def show(**kwargs):
    print(kwargs)

show(name="Subir", role="Developer")
```

Inside the function:

```python
{
    "name": "Subir",
    "role": "Developer"
}
```

Because the collected value is a dictionary, its contents can be changed:

```python
def show(**kwargs):
    kwargs["age"] = 38
```

Dictionaries are mutable.

## Using both

A function can collect both positional and keyword arguments:

```python
def show(*args, **kwargs):
    print(args)
    print(kwargs)

show(10, 20, role="Developer")
```

Result:

```text
args   → (10, 20)
kwargs → {"role": "Developer"}
```

The core distinction is:

```text
*args    → positional arguments → tuple
**kwargs → keyword arguments   → dictionary
```

## Unpacking at the function call

The same `*` and `**` syntax can also be used when calling a function. In that position, they mean **unpack**, not collect.

### `*` unpacks an iterable into positional arguments

```python
def show(a, b, c):
    print(a, b, c)

values = (10, 20, 30)
show(*values)
```

This is equivalent to:

```python
show(10, 20, 30)
```

### `**` unpacks a dictionary into keyword arguments

```python
def show(name, role):
    print(name, role)

data = {"name": "Subir", "role": "Developer"}
show(**data)
```

This is equivalent to:

```python
show(name="Subir", role="Developer")
```

## Mental model

There are two related but opposite operations:

```text
Function definition:
    *args     → collect positional arguments → tuple
    **kwargs  → collect keyword arguments   → dictionary

Function call:
    *values   → unpack iterable → positional arguments
    **data    → unpack dictionary → keyword arguments
```

The symbol has different behavior depending on where it appears: in a parameter list it collects; in a call it unpacks.

## Current learning boundary

Covered:

- collecting positional arguments with `*args`
- collecting keyword arguments with `**kwargs`
- tuple/dictionary behavior of collected arguments
- using `*args` and `**kwargs` together
- unpacking positional arguments with `*`
- unpacking keyword arguments with `**`

Parameter ordering rules, interactions with normal parameters, keyword-only parameters, positional-only parameters, and more advanced argument-signature behavior are intentionally deferred until they are taught.
