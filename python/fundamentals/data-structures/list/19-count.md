# List `count()`

## Mental Model

`count(value)` returns how many times a value occurs in the list.

```python
items = ["A", "B", "C", "B", "D", "B"]
items.count("B")  # 3
```

If the value is absent, `count()` returns `0`; it does not raise `ValueError`.

## Related Operations

- `items.index(value)` → where is the first occurrence?
- `items.count(value)` → how many occurrences?
- `value in items` → does it exist?

## Engineering Priority

Remember the different result contracts: `index()` may raise for an absent value, while `count()` safely returns zero.
