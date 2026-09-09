# List Repetition with `*`

## Mental Model

For lists, repetition with `*` creates a **new outer list** containing repeated references to the existing element objects.

```python
items = ["A", "B"]
result = items * 3

result # ["A", "B", "A", "B", "A", "B"]
items  # ["A", "B"]
```

The original list is unchanged.

## Important Mutable-Object Edge Case

```python
items = [[]] * 3
items[0].append("A")
```

Result:

```python
[["A"], ["A"], ["A"]]
```

There is **one inner list object**, and all three positions reference that same object.

Likewise:

```python
items = [["A"]] * 3
items[0].append("B")
# [["A", "B"], ["A", "B"], ["A", "B"]]
```

This is not because empty or nested lists are singletons. It happens because list repetition repeats references to the existing element object.

## Engineering Priority

Remember:

> `*` creates a new container but repeats references to the existing elements.

This matters especially when the repeated elements are mutable objects.
