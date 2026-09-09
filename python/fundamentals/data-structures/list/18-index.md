# List `index()`

## Mental Model

`index(value)` searches a list and returns the index of the **first matching occurrence**.

```python
items = ["A", "B", "C", "B", "D"]
items.index("B")  # 1
```

If the value is absent, `index()` raises `ValueError`.

## Related Operations

- `items.index(value)` → first position; absent value raises `ValueError`
- `value in items` → membership; absent value returns `False`
- `items.count(value)` → number of occurrences

## Engineering Priority

Use `index()` when the position of the first matching value is required. Do not confuse it with a membership check.
