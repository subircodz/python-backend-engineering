# `defaultdict`

`defaultdict` is a dictionary type from Python's `collections` module.

```python
from collections import defaultdict
```

It changes what happens when a missing key is accessed.

A normal dictionary raises `KeyError`:

```python
orders = {}
orders[101]
```

A `defaultdict` can create a default value automatically:

```python
orders = defaultdict(list)
orders[101]
```

The missing key gets an empty list.

## How the default is created

The argument passed to `defaultdict` is a factory. Python calls it when a missing key needs a value.

```python
numbers = defaultdict(int)
```

For a missing key, Python uses:

```python
int()
```

which produces `0`.

Similarly:

```python
defaultdict(list)
```

uses `list()` to produce `[]`.

```python
defaultdict(set)
```

uses `set()` to produce `set()`.

## Grouping data

A common use is grouping several values under one key.

```python
from collections import defaultdict

orders = defaultdict(list)

orders[101].append("order-1")
orders[101].append("order-2")
orders[102].append("order-3")
```

The result behaves like:

```python
{
    101: ["order-1", "order-2"],
    102: ["order-3"],
}
```

The first access to `orders[101]` creates an empty list. The order is then appended to that list.

## Counting data

`defaultdict(int)` is useful for counters.

```python
counts = defaultdict(int)

counts["python"] += 1
counts["python"] += 1
counts["sql"] += 1
```

The result is:

```python
{
    "python": 2,
    "sql": 1,
}
```

The first access to `counts["python"]` creates `0`, then `+= 1` changes it to `1`.

## Missing-key access changes the dictionary

This is an important difference from `get()`.

```python
data = defaultdict(list)

print(data)
# defaultdict(<class 'list'>, {})

data["items"]

print(data)
# defaultdict(<class 'list'>, {'items': []})
```

Simply accessing the missing key created an entry.

Therefore, do not treat `defaultdict[key]` as a read-only lookup when the key may be missing.

## `dict` vs `defaultdict`

A normal dictionary:

```python
data = {}
data["items"]
```

raises `KeyError` when the key is missing.

A `defaultdict`:

```python
data = defaultdict(list)
data["items"]
```

creates the missing value using its factory.

This difference should be an intentional design choice.

## `setdefault()` vs `defaultdict`

Both can help with missing keys, but they are used differently.

With `setdefault()`:

```python
orders = {}
orders.setdefault(101, []).append("order-1")
```

The default behaviour is chosen at the individual operation.

With `defaultdict`:

```python
orders = defaultdict(list)
orders[101].append("order-1")
```

The default behaviour is part of the dictionary's design.

A useful rule:

- Use `setdefault()` when default insertion is needed only at particular points.
- Use `defaultdict` when missing keys should consistently create the same kind of value.

## Engineering mental model

`defaultdict(factory)` is a dictionary with a defined missing-key policy.

```text
normal dict
missing key → KeyError

defaultdict(factory)
missing key → factory() → store value → return value
```

Use it when that automatic creation is correct for the data model. Do not replace normal dictionaries with `defaultdict` just to avoid handling errors.
