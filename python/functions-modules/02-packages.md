# Packages

## Purpose

A package provides a way to organize related Python modules into a hierarchical namespace.

This note covers packages, subpackages, `__init__.py`, package-level names, and relative imports.

## Package vs Module

A module is a unit of Python code that provides a namespace. A package groups related modules.

```text
Package
├── Module
├── Module
└── Module
```

Example:

```text
project/
├── main.py
└── users/
    ├── __init__.py
    ├── models.py
    └── service.py
```

Here:

- `users` is a package.
- `models.py` is a module.
- `service.py` is a module.

A package can also contain subpackages:

```text
project/
└── backend/
    ├── users/
    │   ├── models.py
    │   └── service.py
    └── orders/
        ├── models.py
        └── service.py
```

Here `backend` is a package, and `users` and `orders` are subpackages of `backend`.

## Import Hierarchy

A package and its modules form a hierarchy.

```python
from backend.users.models import User
```

Read this as:

```text
backend → package
users   → subpackage
models  → module
User    → name inside models
```

The hierarchy can be expressed as:

```text
package → subpackage → module → name
```

## `__init__.py`

`__init__.py` is the initialization module of a package. It can contain code that is executed when the package is imported.

Example:

```text
users/
├── __init__.py
├── models.py
└── service.py
```

```python
# users/__init__.py
print("Users package initialized")
```

Then:

```python
import users
```

can execute the code in `users/__init__.py`.

### Is `__init__.py` required?

No. Modern Python also supports namespace packages that do not contain `__init__.py`.

Therefore, avoid the incomplete rule:

> `__init__.py` is always required to make a directory a package.

For normal application packages, however, `__init__.py` is commonly used for package initialization and package-level exports.

## Exposing Names at Package Level

A package can expose selected names through its `__init__.py`.

Suppose:

```text
users/
├── __init__.py
└── models.py
```

`models.py`:

```python
class User:
    pass
```

Normally we can write:

```python
from users.models import User
```

If `users/__init__.py` contains:

```python
from .models import User
```

we can also write:

```python
from users import User
```

The class is still defined in `models.py`. `__init__.py` makes the name available from the package level as well.

Therefore both can refer to the same class:

```text
users.models.User → original location
users.User        → package-level access exposed by __init__.py
```

This can be used to provide a cleaner public interface for a package.

## Importing a Module Through a Package

Given:

```text
users/
├── __init__.py
└── models.py
```

this import:

```python
import users.models
```

does not import all names from `models.py` into the current namespace.

If `models.py` contains:

```python
class User:
    pass
```

then this is not direct access:

```python
User()  # NameError
```

The module is accessed through the package:

```python
users.models.User()
```

The important mental model is:

```text
import users.models
        ↓
qualified access through users.models
        ↓
users.models.User
```

## What Name Does `import users.models` Bind?

With:

```python
import users.models
```

the top-level package name `users` is available in the current namespace.

Therefore:

```python
print(users)         # works
print(users.models)  # works
print(models)        # NameError
```

`models` is accessed as an attribute of the imported package:

```python
users.models
```

This is different from:

```python
from users.models import User
```

which binds `User` directly in the current namespace.

## Relative Imports

Relative imports refer to modules using the current package hierarchy.

A single dot means the current package:

```python
from .models import User
```

Meaning:

```text
. → current package
models → module in the current package
User → name in models
```

Two dots mean the parent package:

```python
from ..database import connect
```

For example:

```text
backend/
├── __init__.py
├── database.py
└── users/
    ├── __init__.py
    └── service.py
```

Inside `users/service.py`:

```python
from ..database import connect
```

means:

```text
current package: users
        ↓
.. → parent package: backend
        ↓
database → module
        ↓
connect → name inside database
```

Use the package hierarchy as the mental model rather than thinking only in terms of filesystem directories.

## Core Mental Models

1. **Module** → a unit of Python code with its own namespace.
2. **Package** → groups related modules and provides hierarchical organization.
3. **Subpackage** → a package nested inside another package.
4. **`__init__.py`** → package initialization module; it can also expose selected package-level names.
5. **`import users.models`** → access the module through `users.models`; it does not put every module name into the current namespace.
6. **`from users.models import User`** → binds `User` directly in the current namespace.
7. **`.`** → current package in a relative import.
8. **`..`** → parent package in a relative import.

## Learning Boundary

This note intentionally does not cover advanced import machinery such as import hooks, custom finders/loaders, or `__all__`. Those belong to a later level if they become relevant to production work.
