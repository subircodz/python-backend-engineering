# Dictionary Iteration and Transformation

Dictionaries are often processed by reading their entries, checking conditions, and building or updating data.

## Transforming data

```python
prices = {
    "laptop": 50000,
    "mouse": 1000,
    "keyboard": 2000,
}

updated_prices = {}

for product, price in prices.items():
    updated_prices[product] = price * 1.10
```

The original dictionary is kept unchanged. A new dictionary is built from it.

This pattern is useful when input data should remain unchanged while processed data is created separately.

## Filtering data

```python
expensive_products = {}

for product, price in prices.items():
    if price >= 5000:
        expensive_products[product] = price
```

The result contains only entries that pass the condition.

This is a common pattern when processing API responses, database rows, configuration data, or lookup data.

## Modifying values while iterating

Changing the value of an existing key does not change the number of keys.

```python
users = {
    "u1": "active",
    "u2": "active",
}

for user_id in users:
    users[user_id] = users[user_id].upper()
```

The dictionary structure stays the same. Existing values are replaced.

## Do not structurally change the dictionary during direct iteration

This is unsafe:

```python
for user_id, status in users.items():
    if status == "inactive":
        del users[user_id]
```

Removing a key changes the dictionary structure while the loop is walking through it. Python can raise:

```text
RuntimeError: dictionary changed size during iteration
```

The same principle applies when adding new keys during direct iteration.

## Safe removal pattern

If entries must be removed, iterate over a separate snapshot of the items.

```python
users = {
    "u1": "active",
    "u2": "inactive",
    "u3": "active",
}

for user_id, status in list(users.items()):
    if status == "inactive":
        del users[user_id]
```

`list(users.items())` creates a separate list for the loop. The original dictionary can then be changed safely.

## Engineering mental model

When processing a dictionary, ask:

1. Am I reading the existing data?
2. Am I changing values for existing keys?
3. Am I adding or removing keys?
4. Should I build a new dictionary instead?

The last question is often useful when the input represents raw or source data that should not be changed.

Comprehensions can make some of these transformations shorter. They are a separate topic and should not hide the underlying loop logic.