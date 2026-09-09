# List `+=`

## Mental Model

For lists, `+=` extends the existing list in place.

```python
a = [1, 2]
b = [3, 4]

a += b
# a == [1, 2, 3, 4]
```

This is importantly different from list concatenation with `+`:

```python
a = [1, 2]
b = a

a += [3, 4]
```

Both `a` and `b` observe `[1, 2, 3, 4]` because the existing list was mutated.

By contrast:

```python
a = [1, 2]
b = a

a = a + [3, 4]
```

creates a new list and rebinds `a`; `b` still refers to `[1, 2]`.

## Key Distinction

For lists:

- `a + b` → creates a new list
- `a += b` → mutates the existing list
- `a.extend(b)` → mutates the existing list

## Engineering Priority

When aliases exist, distinguish mutation (`+=`, `extend()`) from creating a new list (`+`).
