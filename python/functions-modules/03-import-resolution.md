# Import Resolution

## Purpose

Import resolution explains how Python finds a module or package when an import statement is executed.

This note covers the import search path, `sys.path`, search order, `sys.modules`, and module reuse.

## What Happens During an Import?

When Python encounters:

```python
import calculator
```

Python must first resolve the name `calculator`.

A simplified mental model is:

```text
import calculator
        ↓
resolve the module name
        ↓
search import locations
        ↓
check whether the module is already loaded
        ↓
load and initialize it if necessary
        ↓
make the module available to the importing code
```

The actual import system is more sophisticated, but this model is sufficient for normal application development.

## `sys.path`

Python maintains an ordered collection of locations used when resolving imports. It is exposed through `sys.path`.

```python
import sys

for path in sys.path:
    print(path)
```

A typical environment may contain locations such as:

```text
project directory
Python standard-library locations
virtual-environment site-packages
other configured import locations
```

The important mental model is:

> `sys.path` contains locations Python can search when resolving imports.

A module file itself is not an entry in `sys.path`. The directory containing the module is an entry.

For example, if:

```text
project/
├── main.py
└── helper.py
```

and the project directory is available through the import search path, then:

```python
import helper
```

can resolve `helper.py`.

## Python Does Not Recursively Search the Project

Consider:

```text
project/
├── main.py
└── tools/
    └── calculator.py
```

This does not mean that:

```python
import calculator
```

will recursively search every directory inside `project/`.

Python searches its configured import locations. It does not simply walk the entire project tree looking for a matching filename.

The package hierarchy provides structured access:

```python
from tools import calculator
```

or:

```python
from tools.calculator import add
```

## Search Order Matters

`sys.path` is ordered.

Conceptually, if:

```text
path_1
path_2
path_3
```

are search locations and both `path_1` and `path_3` contain a matching module, the earlier matching location can determine which module is resolved.

Therefore, import resolution can be affected by the order of entries in the import search path.

This is one reason that accidentally naming a local file after a standard-library or third-party package can cause confusing import behavior.

## `sys.path` Is Not Simply the Current Shell Directory

Do not use the incomplete rule:

> `sys.path` is whatever directory I am currently in after running `cd`.

How Python is launched affects the import path. For example, when a script is executed directly, the script's directory is commonly made available as an import location.

The reliable way to understand the active environment is to inspect:

```python
import sys

print(sys.path)
```

## `sys.modules`

Python also maintains a cache of modules that have already been loaded. This cache is available through:

```python
import sys

print(sys.modules)
```

After:

```python
import calculator
```

we can check:

```python
print("calculator" in sys.modules)
```

which will normally be:

```text
True
```

A simplified model is:

```text
import calculator
        ↓
resolve calculator
        ↓
is calculator already loaded?
        ↓
   ┌────┴────┐
   │         │
  No        Yes
   │         │
   ▼         ▼
load and   reuse the
initialize existing module
   │
   ▼
store in sys.modules
```

## Repeated Imports Reuse the Module

Suppose:

```python
# calculator.py
print("Calculator loaded")

x = 10
```

and:

```python
# main.py
import calculator
import calculator

print(calculator.x)
```

The module-level print is normally executed once:

```text
Calculator loaded
10
```

The second import reuses the already-loaded module rather than executing the module from scratch again.

## Module Identity and References

Because the already-loaded module is reused, two imports can refer to the same module object.

For example:

```python
import calculator
import calculator as calc

print(calculator is calc)
```

The result is:

```text
True
```

The alias `calc` does not create another copy of the module. It is another name referring to the same module object.

The mental model connects directly to Python's object/reference model:

```text
                 ┌─────────────────────┐
calculator ─────►│                     │
                 │  calculator module  │
calc ───────────►│       x = 10        │
                 │                     │
                 └─────────────────────┘
                         ▲
                         │
                    sys.modules
```

## `sys.path` vs `sys.modules`

These solve different problems:

| Mechanism | Main purpose |
|---|---|
| `sys.path` | Locations Python can search for imports |
| `sys.modules` | Modules already loaded in the current Python process |

A useful mental model is:

```text
sys.path
    ↓
Where can Python find it?

sys.modules
    ↓
Have I already loaded it?
```

## Import Name Binding

Import resolution and name binding are related but distinct.

With:

```python
import calculator
```

Python resolves and loads the module, then the name `calculator` is available in the importing module.

With:

```python
from calculator import add
```

Python resolves the module and obtains `add`, then `add` is bound directly in the importing module.

The distinction remains:

```text
import calculator
    → name `calculator` refers to the module

from calculator import add
    → name `add` refers to the imported object
```

## Core Mental Models

1. **Import resolution** → the process of finding and loading an importable module or package.
2. **`sys.path`** → ordered import search locations; directories, not individual module files.
3. **Search order matters** → an earlier matching import location can determine which module is resolved.
4. **No recursive project search** → Python does not simply walk every directory inside a project.
5. **`sys.modules`** → cache/registry of modules already loaded in the current Python process.
6. **Repeated imports** → normally reuse the already-loaded module instead of executing it again.
7. **Module identity** → different names such as `calculator` and `calc` can refer to the same module object.
8. **Search vs cache** → `sys.path` helps answer “where can Python find it?” while `sys.modules` helps answer “has it already been loaded?”

## Learning Boundary

This note intentionally does not cover advanced import machinery such as custom import hooks, finders, loaders, importlib internals, or namespace-package internals. Those can be introduced later if they become relevant to production work.
