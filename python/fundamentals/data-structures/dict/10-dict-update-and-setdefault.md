# Dictionary `update()` and `setdefault()`

Two useful dictionary methods are `update()` and `setdefault()`. They solve different problems.

## `update()`

`update()` adds or changes multiple key-value mappings in an existing dictionary.

```python
user = {
    "name": "Subir",
    "age": 38,
}

user.update({
    "age": 39,
    "city": "Guwahati",
})
```

The result is:

```python
{
    "name": "Subir",
    "age": 39,
    "city": "Guwahati",
}
```

If a key already exists, its value is replaced. If the key does not exist, it is added.

## `update()` mutates the existing dictionary

```python
user = {"name": "Subir"}
user.update({"age": 38})
```

The existing dictionary object is changed.

This is different from assigning a new dictionary:

```python
user = {"name": "Subir"}
user = {"name": "Subir", "age": 38}
```

The first operation is mutation. The second is rebinding `user` to another dictionary object.

## `update()` with keyword arguments

For keys that are valid Python identifiers, keyword arguments are also convenient:

```python
user.update(
    age=38,
    city="Guwahati",
)
```

Dictionary syntax is still needed for keys such as `"first-name"` that are not valid Python identifiers.

## `setdefault()`

`setdefault(key, default)` checks a key and creates it with the default value only when the key is missing.

```python
user = {"name": "Subir"}

city = user.setdefault("city", "Guwahati")
```

Now the dictionary contains `city`, and `city` contains `"Guwahati"`.

If the key already exists, the existing value is kept:

```python
user = {
    "name": "Subir",
    "city": "Jorhat",
}

city = user.setdefault("city", "Guwahati")
```

The value remains `"Jorhat"`.

`setdefault()` also returns the value associated with the key.

## `get()` vs `setdefault()`

The important difference is whether the dictionary should change when the key is missing.

```python
city = user.get("city", "Guwahati")
```

`get()` returns the fallback value but does not add the key.

```python
city = user.setdefault("city", "Guwahati")
```

`setdefault()` returns the value and adds the key if it was missing.

Mental model:

```text
get()
    read + fallback

setdefault()
    read + fallback + possibly insert
```

## A common grouping pattern

`setdefault()` can create a collection when a group does not exist yet.

```python
orders = {}

orders.setdefault(101, []).append("order-1")
orders.setdefault(101, []).append("order-2")
orders.setdefault(102, []).append("order-3")
```

Result:

```python
{
    101: ["order-1", "order-2"],
    102: ["order-3"],
}
```

The missing customer key gets an empty list. Later items are appended to that list.

This pattern is useful, but `defaultdict` is often a cleaner choice when this missing-key behaviour is needed repeatedly.

## Engineering mental model

Use the operation that matches the intended state change:

- `update()` → apply several mappings to an existing dictionary.
- `get()` → read a value with an optional fallback without changing the dictionary.
- `setdefault()` → read a value and create the key with a default when missing.

Do not use `setdefault()` just because it avoids an `if`. First decide whether creating the missing key is actually correct behaviour.
