# Tuple Packing and Unpacking

## 1. Packing

Packing means combining multiple values into a single tuple.

The comma is what creates the tuple. Parentheses are commonly used for readability or grouping.

```python
employee = "Subir", 101, "Developer"

print(employee)
# ('Subir', 101, 'Developer')
```

Explicit parentheses also work:

```python
employee = ("Subir", 101, "Developer")
```

Both create the same kind of object: a tuple.

### Single-element tuple

A trailing comma is required:

```python
value = (10,)   # tuple
value = (10)    # int
```

---

## 2. Unpacking

Unpacking means taking elements from an iterable and assigning them to target names.

```python
employee = ("Subir", 101, "Developer")

name, employee_id, role = employee
```

Conceptually:

```text
name       -> "Subir"
employee_id -> 101
role       -> "Developer"
```

The original tuple is not changed.

Unpacking works with other iterables too:

```python
numbers = [10, 20, 30]
a, b, c = numbers

letters = "ABC"
x, y, z = letters
```

The important idea is:

> Python takes elements from the iterable and assigns them to the target names.

---

## 3. Number of Targets Normally Must Match

```python
numbers = (10, 20, 30)
a, b = numbers
```

This raises:

```text
ValueError
```

There are three values but only two targets.

Likewise:

```python
numbers = (10, 20, 30)
a, b, c, d = numbers
```

also raises `ValueError` because there are not enough values.

---

## 4. Extended Unpacking with `*`

A starred target collects the remaining elements.

```python
numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers
```

Result:

```text
first  -> 10
middle -> [20, 30, 40]
last   -> 50
```

### Important: starred target becomes a list

Even when the source is a tuple, the starred target is a **list**:

```python
print(type(middle))
# <class 'list'>
```

More examples:

```python
first, *rest = numbers
# first = 10
# rest = [20, 30, 40, 50]
```

```python
*start, last = numbers
# start = [10, 20, 30, 40]
# last = 50
```

The `*` means:

> Collect all remaining elements into this target as a list.

---

## 5. Only One Starred Target

A normal unpacking assignment can have only one starred target because Python must have one clear place to collect the remaining elements.

```python
first, *middle, last = numbers
```

is valid.

Trying to use two starred targets is invalid:

```python
first, *middle, *rest = numbers
```

This is a `SyntaxError`.

---

## 6. Using `_` for Values You Intend to Ignore

`_` is commonly used as a throwaway name.

```python
response = (200, "OK", {"user_id": 101}, "request-id-123")

status_code, *_, request_id = response
```

Result:

```text
status_code -> 200
_           -> ["OK", {"user_id": 101}]
request_id  -> "request-id-123"
```

`_` is still a normal Python name. The convention simply tells readers that the value is not important for later use.

---

## 7. Packing and Unpacking in Function Calls

The `*` syntax also appears in function calls, but its meaning depends on where it is used.

### `*values` in a function call

Here an iterable is unpacked into separate positional arguments:

```python
values = (10, 20, 30)

add(*values)
```

This is equivalent to:

```python
add(10, 20, 30)
```

More precisely, `*values` unpacks the iterable into positional arguments, which are then bound to the function's parameters.

### `*args` in a function definition

Here the function collects positional arguments into a tuple:

```python
def show(*args):
    print(args)

show(10, 20, 30)
```

Inside the function:

```python
args == (10, 20, 30)
```

So these two uses are opposite operations:

```text
function call:       *values  -> unpack iterable into arguments
function definition: *args    -> collect arguments into tuple
```

---

## 8. Connection with `**kwargs`

The same general idea applies to keyword arguments.

```python
def create_user(**kwargs):
    print(kwargs)

create_user(name="Subir", role="Developer")
```

Inside the function, `kwargs` is a dictionary:

```python
{"name": "Subir", "role": "Developer"}
```

A dictionary can be unpacked into keyword arguments with `**`:

```python
user_data = {"name": "Subir", "role": "Developer"}

create_user(**user_data)
```

Mental model:

```text
*  -> positional argument unpacking / collection
** -> keyword argument unpacking / collection
```

---

## 9. Swapping Variables

Packing and unpacking make Python variable swapping concise:

```python
a = 10
b = 20

a, b = b, a
```

Conceptually:

1. The right-hand side is evaluated first.
2. `b, a` packs the current values into a tuple `(20, 10)`.
3. The left-hand side unpacks that tuple.
4. `a` becomes `20` and `b` becomes `10`.

The important point is that the old value of `a` is not lost before the right-hand side has been evaluated.

---

## 10. Mutable Objects and Unpacking

Unpacking does not deep-copy the objects inside the iterable.

```python
items = ([10, 20], [30, 40], [50, 60])

first, *middle = items
middle[0].append(99)
```

After this:

```python
items
# ([10, 20], [30, 40, 99], [50, 60])

middle
# [[30, 40, 99], [50, 60]]
```

Why?

- `middle` is a new list created by starred unpacking.
- Its elements are references to the same inner list objects.
- `middle[0]` and `items[1]` therefore refer to the same inner list.
- `append()` mutates that shared inner list.

Unpacking creates the new container required by the assignment; it does not recursively clone nested mutable objects.

---

## 11. Packing vs Unpacking

### Packing

Multiple values become one tuple:

```python
x = 10, 20, 30
```

Conceptually:

```text
10, 20, 30 -> (10, 20, 30)
```

### Unpacking

One iterable is split into individual bindings:

```python
x, y, z = (10, 20, 30)
```

Conceptually:

```text
(10, 20, 30) -> x=10, y=20, z=30
```

### Important distinction

Packing and unpacking are about how values are grouped or assigned. They do not imply copying the underlying objects.

---

## 12. Production Use Cases

Packing and unpacking are common in real Python code.

### Returning multiple values

```python
def get_user():
    return "Subir", 101, "Developer"

name, user_id, role = get_user()
```

Python packs the returned values into a tuple, then the caller can unpack them.

### Processing structured records

```python
for name, employee_id, role in employees:
    print(name, employee_id, role)
```

Each record is unpacked into meaningful names.

### Keeping the first and last item

```python
first, *middle, last = values
```

Useful when the number of middle values can vary.

### Passing stored arguments

```python
arguments = (10, 20)
result = add(*arguments)
```

This is useful when arguments are already stored in an iterable.

---

## 13. Mental Model to Retain

Remember these four patterns:

```python
# Packing
x = 10, 20, 30
```

```python
# Unpacking
x, y, z = values
```

```python
# Extended unpacking
first, *middle, last = values
```

```python
# Function-call unpacking
func(*values)
```

And distinguish them from:

```python
def func(*args):
    # collects positional arguments into a tuple
    ...
```

The same `*` symbol is used in different contexts, so always look at **where it appears** and ask whether Python is collecting or unpacking.
