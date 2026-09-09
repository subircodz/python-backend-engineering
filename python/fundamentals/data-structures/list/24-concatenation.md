# List Concatenation with `+`

## Mental Model

The `+` operator concatenates two lists by creating a **new list**.

```python
a = [1, 2]
b = [3, 4]
c = a + b
```

Result:

```python
a # [1, 2]
b # [3, 4]
c # [1, 2, 3, 4]
```

The original operands are not mutated.

## Contrast with `extend()`

```python
a.extend(b)
```

mutates `a` in place, whereas `a + b` creates a new list.

## Engineering Priority

Use `+` when a new combined list is wanted; use `extend()` when mutating the existing list is intended.
