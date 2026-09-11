# Dictionary Interview Question Paper

**Total: 100 marks**

Answer from your own understanding. Do not search for answers while attempting the paper.

The paper checks both Python behaviour and engineering reasoning.

## Section A — Core behaviour (20 marks)

### 1. (5 marks)
What is the difference between dictionary key-based access and list position-based access? Give one example of each.

### 2. (5 marks)
Explain why this dictionary contains only one `name` entry:

```python
user = {
    "name": "Subir",
    "name": "Rahul",
}
```

What value will `user["name"]` return, and why?

### 3. (5 marks)
What happens when this code runs?

```python
user = {"name": "Subir"}
print(user["age"])
```

Name the exception and explain why it occurs.

### 4. (5 marks)
Explain the difference between mutation and rebinding with dictionaries.

Use one code example for each.

## Section B — Access and mutation (20 marks)

### 5. (5 marks)
Compare these two operations:

```python
user["email"]
user.get("email")
```

What happens when `email` is missing?

### 6. (5 marks)
What is the difference between:

```python
user.get("city", "Guwahati")
```

and:

```python
user.setdefault("city", "Guwahati")
```

Focus on what happens to the dictionary when `city` is missing.

### 7. (5 marks)
Explain what each operation does:

```python
user.pop("age")
del user["age"]
user.popitem()
user.clear()
```

Mention what each operation returns where relevant.

### 8. (5 marks)
What does `"name" in user` check? Does it check dictionary values? Explain how you would check for a value and for a key-value pair.

## Section C — Views, iteration and transformation (20 marks)

### 9. (5 marks)
What are the differences between:

```python
user.keys()
user.values()
user.items()
```

Also explain what one individual item from `user.items()` is.

### 10. (5 marks)
Why does this work?

```python
for key, value in user.items():
    print(key, value)
```

Explain the role of the tuple returned for each item and tuple unpacking.

### 11. (5 marks)
Why can this code raise `RuntimeError`?

```python
for user_id in users:
    del users[user_id]
```

Explain the difference between changing an existing value and changing the dictionary structure during iteration.

### 12. (5 marks)
You have a dictionary of product prices. You need to create another dictionary containing only products priced at or above 5000.

Write the code and explain whether the original dictionary is changed.

## Section D — Nested dictionaries (15 marks)

### 13. (5 marks)
Given:

```python
user = {
    "name": "Subir",
    "address": {
        "city": "Guwahati",
        "state": "Assam",
    },
}
```

Explain exactly what Python does when evaluating:

```python
user["address"]["city"]
```

### 14. (5 marks)
Write code to change the nested `city` value to `Jorhat` and add a nested `country` value of `India`.

Explain which dictionary is being changed by each statement.

### 15. (5 marks)
When can this pattern be useful?

```python
city = user.get("address", {}).get("city")
```

Why should it not be used blindly for required data?

## Section E — `update()`, `setdefault()` and `defaultdict` (25 marks)

### 16. (5 marks)
Explain what happens when this runs:

```python
user = {"name": "Subir", "age": 38}
user.update({"age": 39, "city": "Guwahati"})
```

Which key is added? Which key is changed?

### 17. (5 marks)
Write a short example where `setdefault()` is useful for grouping values under a key.

Explain why the first access can create the collection.

### 18. (5 marks)
What is `defaultdict`? Where does it come from?

Explain what this means:

```python
from collections import defaultdict
orders = defaultdict(list)
```

### 19. (5 marks)
Explain the difference between these two designs:

```python
orders = {}
orders.setdefault(101, []).append("order-1")
```

and:

```python
orders = defaultdict(list)
orders[101].append("order-1")
```

Focus on where the missing-key behaviour is defined.

### 20. (5 marks)
Consider:

```python
counts = defaultdict(int)

counts["python"] += 1
counts["python"] += 1
counts["sql"] += 1
```

Explain step by step why the final counts are what they are.

## Engineering judgement

While answering, do not focus only on memorising method names. For each question, explain what Python actually does and why the behaviour matters in real code.

Important areas to watch:

- key lookup vs position lookup
- mutation vs rebinding
- missing-key behaviour
- dictionary views vs individual tuples
- changing values vs changing dictionary structure
- nested ownership
- `get()` vs `setdefault()` vs `defaultdict`
- choosing automatic defaults only when they match the data model
