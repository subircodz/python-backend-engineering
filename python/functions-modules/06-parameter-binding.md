# Function Parameter Binding

## Purpose

Understand how Python binds positional and keyword arguments to function parameters, including `*args`, `**kwargs`, keyword-only parameters, and positional-only parameters.

## Normal Parameters

A normal parameter can receive a value positionally or by keyword.

```python
def show(name):
    print(name)

show("Subir")
show(name="Subir")
```

Both calls bind `"Subir"` to `name`.

A parameter cannot receive two values. For example:

```python
show("Subir", name="Developer")
```

raises `TypeError` because `name` was already bound positionally.

## `*args` with Normal Parameters

```python
def show(name, *args):
    print(name)
    print(args)

show("Subir", 10, 20)
```

Binding:

```text
name → "Subir"
args → (10, 20)
```

The normal parameter is bound first; remaining positional arguments are collected by `*args`.

If there are no remaining positional arguments:

```text
args → ()
```

`args` is always a tuple when `*args` is used.

## Keyword Arguments and `**kwargs`

```python
def show(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)

show(name="Subir", age=38, role="Developer")
```

Binding:

```text
name   → "Subir"
args   → ()
kwargs → {"age": 38, "role": "Developer"}
```

A normal parameter can receive its value by keyword. `**kwargs` collects remaining keyword arguments.

A keyword argument that tries to bind a parameter that already received a value causes `TypeError`:

```python
def show(name, *args, **kwargs):
    ...

show(10, 20, name="Subir")
```

`name` already received `10`, so the second value for `name` is invalid.

## Keyword-Only Parameters

A bare `*` makes every parameter after it keyword-only.

```python
def connect(host, *, port, timeout):
    ...
```

Binding:

```text
host    → normal parameter
port    → keyword-only
 timeout → keyword-only
```

This is valid:

```python
connect("localhost", port=5432, timeout=10)
```

This is invalid:

```python
connect("localhost", 5432, 10)
```

A bare `*` does not collect arguments. It creates a boundary in the signature.

## Keyword-Only Parameters with Defaults

```python
def save_data(data, *args, overwrite=False):
    ...
```

Binding:

```text
data      → normal parameter
args       → remaining positional arguments → tuple
overwrite  → keyword-only parameter, default False
```

For example:

```python
save_data("file.csv", 10, 20)
```

produces:

```text
data      → "file.csv"
args       → (10, 20)
overwrite  → False
```

And:

```python
save_data("file.csv", 10, overwrite=True)
```

produces:

```text
data      → "file.csv"
args       → (10,)
overwrite  → True
```

The default value is used only when the caller does not provide another value.

## Positional-Only Parameters

A `/` makes every parameter before it positional-only.

```python
def connect(host, port, /, timeout=30):
    ...
```

Binding rules:

```text
host    → positional-only
port    → positional-only
timeout → normal parameter, default 30
```

This is valid:

```python
connect("localhost", 5432, timeout=60)
```

This is invalid:

```python
connect(host="localhost", port=5432)
```

because `host` and `port` are positional-only.

## Combining `/` and `*`

```python
def request(method, url, /, *, timeout=30, verify=True):
    ...
```

The parameters are divided into three groups:

```text
method, url       → positional-only
                 /
timeout, verify   → keyword-only
```

So this is valid:

```python
request("GET", "/users", timeout=10, verify=False)
```

The `/` and bare `*` are signature boundaries. They do not collect values.

## `*args` vs Bare `*`

These are different:

```python
def show(*args):
    ...
```

`*args` collects remaining positional arguments into a tuple.

```python
def show(name, *, timeout):
    ...
```

Bare `*` does not collect anything. It makes parameters after it keyword-only.

## Complete Mental Model

```text
Normal parameter
    → can receive positional or keyword argument

*args
    → collects remaining positional arguments → tuple

bare *
    → makes following parameters keyword-only

keyword-only parameter
    → must receive its value by keyword

**kwargs
    → collects remaining keyword arguments → dictionary

/
    → makes preceding parameters positional-only
```

### Signature boundaries

```python
def example(positional_only, /, normal, *args, keyword_only=True, **kwargs):
    ...
```

Conceptually:

```text
before /       → positional-only
between / and *args → normal parameters
*args          → remaining positional arguments
following named parameters → keyword-only
**kwargs       → remaining keyword arguments
```

## Current Learning Boundary

Covered:

- normal parameter binding
- positional and keyword arguments
- `*args` with normal parameters
- `**kwargs` with normal parameters
- duplicate argument binding errors
- bare `*` and keyword-only parameters
- keyword-only parameters with defaults
- `/` and positional-only parameters
- combining positional-only and keyword-only parameters

Advanced signature inspection and less common parameter-binding edge cases are intentionally deferred until needed.
