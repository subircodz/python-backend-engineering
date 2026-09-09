# Function Parameter Binding — Retrieval Exercises

## Purpose

Retrieval exercises for normal parameters, `*args`, `**kwargs`, keyword-only parameters, positional-only parameters, `/`, bare `*`, and mixed signatures.

## Exercise 1 — Normal + `*args` + `**kwargs`

```python
def process(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)

process("Subir", 10, 20, role="Developer", experience=10)
```

**Question:** Predict all three outputs.

**Solution:**

```text
Subir
(10, 20)
{'role': 'Developer', 'experience': 10}
```

Binding: `name → "Subir"`, `args → (10, 20)`, `kwargs → {"role": "Developer", "experience": 10}`.

---

## Exercise 2 — Keyword Binding

```python
def process(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)

process(name="Subir", role="Developer", experience=10)
```

**Question:** Predict the outputs.

**Solution:**

```text
Subir
()
{'role': 'Developer', 'experience': 10}
```

There are no positional arguments, so `args` is an empty tuple. `name` receives its value by keyword; the remaining keywords go to `kwargs`.

---

## Exercise 3 — Keyword-Only Parameter

```python
def save(data, *args, overwrite=False):
    print(data)
    print(args)
    print(overwrite)

save("users.csv", 10, 20, overwrite=True)
```

**Question:** Predict all three outputs.

**Solution:**

```text
users.csv
(10, 20)
True
```

`data → "users.csv"`, `args → (10, 20)`, `overwrite → True`. `overwrite` is keyword-only because it follows the bare `*`.

---

## Exercise 4 — Default Keyword-Only Value

```python
def save(data, *args, overwrite=False):
    print(data)
    print(args)
    print(overwrite)

save("users.csv", 10, 20)
```

**Question:** What happens to `overwrite`?

**Solution:**

```text
users.csv
(10, 20)
False
```

The caller does not provide `overwrite`, so its default value `False` is used.

---

## Exercise 5 — Bare `*`

```python
def connect(host, *, port, timeout=30):
    print(host)
    print(port)
    print(timeout)

connect("localhost", port=5432)
```

**Question:** Predict the outputs.

**Solution:**

```text
localhost
5432
30
```

`host` is positional-capable. `port` and `timeout` are keyword-only. `timeout` uses its default.

---

## Exercise 6 — Invalid Keyword-Only Binding

```python
def connect(host, *, port, timeout=30):
    print(host, port, timeout)

connect("localhost", 5432, 60)
```

**Question:** Does this execute? If not, is it `SyntaxError` or `TypeError`, and why?

**Solution:** It does not execute. The error is **`TypeError`** because `port` and `timeout` are keyword-only but were supplied positionally. The function definition itself is valid syntax, so this is not a `SyntaxError`.

---

## Exercise 7 — Positional-Only Parameters

```python
def connect(host, port, /, timeout=30):
    print(host)
    print(port)
    print(timeout)

connect("localhost", 5432, 60)
```

**Question:** Predict the output.

**Solution:**

```text
localhost
5432
60
```

`host` and `port` are positional-only because they appear before `/`. `timeout` receives `60` positionally.

---

## Exercise 8 — Invalid Positional-Only Binding

```python
def connect(host, port, /, timeout=30):
    print(host, port, timeout)

connect(host="localhost", port=5432)
```

**Question:** Does this execute? Explain exactly what `/` does here.

**Solution:** It does not execute. The error is **`TypeError`**. `/` means every parameter before it is positional-only, so `host` and `port` cannot be supplied by keyword.

---

## Exercise 9 — Full Mixed Signature

```python
def request(method, url, /, *args, timeout=30, verify=True, **kwargs):
    print("method:", method)
    print("url:", url)
    print("args:", args)
    print("timeout:", timeout)
    print("verify:", verify)
    print("kwargs:", kwargs)

request(
    "GET", "/users", 10, 20,
    timeout=5, verify=False, retry=True,
)
```

**Question:** Predict every output.

**Solution:**

```text
method: GET
url: /users
args: (10, 20)
timeout: 5
verify: False
kwargs: {'retry': True}
```

Binding: `method → "GET"`, `url → "/users"`, `args → (10, 20)`, `timeout → 5`, `verify → False`, `kwargs → {"retry": True}`.

---

## Exercise 10 — Mixed Signature with a Trap

```python
def request(method, url, /, *args, timeout=30, verify=True, **kwargs):
    print(method, url, args, timeout, verify, kwargs)

request("GET", "/users", timeout=10, method="POST")
```

**Question:** Does this work? If not, explain which parameter receives the first `"GET"` and why the later `method="POST"` causes a problem.

**Solution:** It does not execute. The first `"GET"` is bound to `method`. However, `method` is positional-only because it appears before `/`. Therefore `method="POST"` is invalid. The problem is **not** ordinary duplicate binding; a positional-only parameter cannot be supplied by keyword. The result is **`TypeError`**.

---

## Exercise 11 — Binding Everything

```python
def configure(name, /, *args, debug=False, **kwargs):
    print("name:", name)
    print("args:", args)
    print("debug:", debug)
    print("kwargs:", kwargs)

configure(
    "app", 10, 20,
    debug=True,
    version="1.0",
    environment="production",
)
```

**Question:** Predict all outputs.

**Solution:**

```text
name: app
args: (10, 20)
debug: True
kwargs: {'version': '1.0', 'environment': 'production'}
```

Binding: `name` is positional-only, `args` collects remaining positional arguments, `debug` is keyword-only, and the remaining keywords go to `kwargs`.

---

## Exercise 12 — Final Challenge

```python
def api_call(method, url, /, *args, timeout=30, verify=True, **kwargs):
    print("method:", method)
    print("url:", url)
    print("args:", args)
    print("timeout:", timeout)
    print("verify:", verify)
    print("kwargs:", kwargs)

api_call(
    "POST", "/users", {"name": "Subir"},
    timeout=10, verify=False,
    retry=3, cache=True,
)
```

**Question:** Do not execute until you have completely reasoned through it. Predict every output.

**Solution:**

```text
method: POST
url: /users
args: ({'name': 'Subir'},)
timeout: 10
verify: False
kwargs: {'retry': 3, 'cache': True}
```

The dictionary is one positional argument, so `args` is a one-element tuple containing that dictionary: `({"name": "Subir"},)`.

Binding: `method → "POST"`, `url → "/users"`, `args → ({"name": "Subir"},)`, `timeout → 10`, `verify → False`, `kwargs → {"retry": 3, "cache": True}`.

---

## Retrieval Summary

```text
/        → parameters before it are positional-only
*args    → collects remaining positional arguments into a tuple
bare *   → parameters after it are keyword-only
**kwargs → collects remaining keyword arguments into a dictionary
```

Preferred workflow: **predict → check → explain why the binding occurs that way**.
