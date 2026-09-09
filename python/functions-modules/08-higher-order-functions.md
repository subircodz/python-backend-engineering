# Higher-Order Functions — Functions as First-Class Objects

## Purpose

Understand how Python treats functions as objects and how higher-order functions use functions as values.

## Functions Are First-Class Objects

A function is an object/value in Python. A reference to a function can be:

- assigned to a variable
- passed as an argument
- returned from another function

The important distinction is between a function object and calling the function:

```python
def greet():
    return "Hello"

operation = greet      # function object
result = greet()       # return value
```

`greet` refers to the function object. `greet()` calls the function and produces its return value.

## Passing a Function as an Argument

```python
def double(x):
    return x * 2


def apply(operation, value):
    return operation(value)

result = apply(double, 10)
```

Flow:

```text
double
  ↓
function object passed to apply
  ↓
operation refers to the same function object
  ↓
operation(value) → double(10)
  ↓
returns 20
  ↓
apply returns 20
  ↓
result refers to int object 20
```

`apply()` does not need to know what operation it received. The behavior is supplied by the caller.

## Returning a Function

A function can also return another function object:

```python
def make_operation():
    return square
```

Then:

```python
operation = make_operation()
```

`operation` refers to the `square` function object. `square` is returned, not called.

Calling the returned function happens separately:

```python
result = operation(5)
```

## Higher-Order Functions

A higher-order function (HOF) is a function that **takes a function as an argument and/or returns a function**.

Example:

```python
def apply(operation, value):
    return operation(value)
```

`apply` is a higher-order function because it accepts a function as an argument.

A function does **not** have to be a closure to be a higher-order function.

## HOF vs Closure

These are different concepts.

### Higher-order function

Concerned with functions being passed around as values:

```python
def apply(operation, value):
    return operation(value)
```

### Closure

A function retains access to variables from its enclosing scope after the enclosing function has finished:

```python
def multiplier(n):
    def multiply(x):
        return x * n

    return multiply
```

Here `multiplier` is a higher-order function because it returns a function. The returned `multiply` function is a closure because it retains access to `n`.

## Multiple Closures

Each call to `multiplier()` creates a returned function object with its own closure state:

```python
double = multiplier(2)
triple = multiplier(3)
```

Conceptually:

```text
double → multiply function + remembered n = 2
triple → multiply function + remembered n = 3
```

Therefore:

```python
double(10)  # 20
triple(10)  # 30
```

The function code is the same, but each closure retains a different `n` value.

## Why Higher-Order Functions Are Useful

Higher-order functions separate **what operation should happen** from **how the operation is applied**.

Instead of creating separate functions such as `apply_double()` and `apply_triple()`, one generic function can accept the required behavior:

```python
def apply(operation, value):
    return operation(value)

apply(double, 10)
apply(triple, 10)
```

This makes code more reusable because behavior can be supplied from outside.

## `map()` — Transforming Items

`map()` is a built-in higher-order function. It accepts a function and an iterable, then applies the function to each item.

```python
def double(x):
    return x * 2

numbers = [1, 2, 3, 4]
result = map(double, numbers)
```

The function object `double` is passed to `map()` without calling it. `map()` calls it for each element.

In Python 3, `map()` returns a lazy `map` object rather than immediately creating a list.

```python
values = list(result)
# [2, 4, 6, 8]
```

Mental model:

```text
function object + iterable
        ↓
      map()
        ↓
apply function to every item
        ↓
lazy map object
        ↓
list(...) consumes it
```

## `filter()` — Selecting Items

`filter()` is another built-in higher-order function. It applies a predicate function to items and keeps the items for which the predicate returns a truthy value.

```python
def is_positive(x):
    return x > 0

numbers = [-2, 5, -1, 8]
result = filter(is_positive, numbers)
```

Like `map()`, `filter()` returns a lazy `filter` object in Python 3.

```python
values = list(result)
# [5, 8]
```

Mental model:

```text
predicate function + iterable
        ↓
     filter()
        ↓
keep items where predicate is truthy
        ↓
lazy filter object
        ↓
list(...) consumes it
```

### `map()` vs `filter()`

- `map()` → transforms every item
- `filter()` → decides which items to keep

For example:

```python
list(map(lambda x: x * 2, [1, 2, 3]))
# [2, 4, 6]

list(filter(lambda x: x > 0, [-2, 5, -1, 8]))
# [5, 8]
```

## Why `double` and Not `double()`?

When passing a function to a higher-order function, pass the function object:

```python
map(double, numbers)
```

not the result of calling it:

```python
map(double(), numbers)  # wrong for this purpose
```

Mental model:

```text
double    → function object
double()  → function call → return value
```

`map()` needs the function object because it is responsible for calling the function for each element.

## Lambda Functions

A `lambda` creates a function object using a compact expression:

```python
lambda x: x * 2
```

It is commonly useful for short, simple, local behavior, especially when the function is needed only at the point where it is used.

Example:

```python
numbers = [1, 2, 3, 4]
result = list(map(lambda x: x + 5, numbers))
# [6, 7, 8, 9]
```

The lambda expression represents a function object. `map()` receives that function object and calls it for each element.

### Lambda vs `def`

Do not use the rule **"one line means lambda and multiple lines mean `def`"** as an absolute rule.

Prefer `lambda` when the behavior is:

- short
- simple
- local/throwaway
- naturally expressed as one expression

Prefer `def` when the behavior:

- has a meaningful name
- is reusable
- represents business/domain logic
- may need documentation
- should be tested independently
- is complex enough that a named function improves readability

For example, even though this function is only one line, `def` is clearer because the calculation has a meaningful purpose:

```python
def calculate_tax(amount):
    return amount * 0.18
```

Whereas a small local transformation may be clearer inline:

```python
result = list(map(lambda x: x * 2, numbers))
```

## Mental Model

```text
Function object
    ↓
can be assigned
can be passed
can be returned
    ↓
Higher-order functions use functions as values
    ↓
map() transforms items
filter() selects items
lambda creates compact function objects
    ↓
Closures are a separate concept
    ↓
A HOF may be a closure-related pattern, but it does not have to be a closure
```

## Retrieval Summary

- `function_name` → refers to the function object.
- `function_name()` → calls the function and produces its return value.
- Functions can be assigned, passed, and returned because functions are objects.
- A higher-order function takes a function as an argument and/or returns a function.
- A closure retains access to variables from an enclosing scope.
- Higher-order function and closure are different concepts.
- Each invocation of a closure-producing function can create a separate closure with its own retained values.
- `map()` applies a function to every item and returns a lazy `map` object.
- `filter()` applies a predicate and keeps items where the predicate is truthy, returning a lazy `filter` object.
- Pass `double`, not `double()`, when a higher-order function needs the function object.
- `lambda` is useful for short, simple, local behavior.
- `def` is preferable when behavior has a meaningful name, reuse, documentation, testing needs, or greater complexity.

Preferred workflow: **predict → explain the object/reference flow → check → correct the mental model**.
