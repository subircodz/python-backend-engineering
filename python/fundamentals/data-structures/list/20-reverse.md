# List `reverse()`

## Mental Model

`reverse()` reverses the existing list **in place**.

```python
items = ["A", "B", "C", "D"]
result = items.reverse()
```

After the call:

```python
items  # ["D", "C", "B", "A"]
result # None
```

`reverse()` mutates the list and returns `None`.

## Engineering Priority

Do not expect `reverse()` to return a reversed list. Use it when in-place mutation is intended.
