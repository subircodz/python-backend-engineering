# For Loop Fundamentals

## Core Mental Model

A Python `for` loop takes objects from an iterable one at a time and executes the loop body for each object.

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

Mental model:

```text
numbers ──► [10, 20, 30]

Iteration 1:
number ──► 10

Iteration 2:
number ──► 20

Iteration 3:
number ──► 30
```

The loop variable `number` is a **name**. Each iteration rebinds that name to the next object supplied by the iterable.

The loop does not create copies of the objects merely because they are assigned to the loop variable.

## Loop Variable Remains After the Loop

Python does not create a separate block scope for a normal `for` loop.

```python
items = ["A", "B", "C"]

for item in items:
    print(item)

print(item)
```

Output:

```text
A
B
C
C
```

After the loop, `item` is still bound to the last object processed, `"C"`, provided the loop executed at least once.

## Rebinding the Loop Variable Does Not Change the List

```python
numbers = [10, 20, 30]

for number in numbers:
    number = number * 2
    print(number)

print(numbers)
```

Output:

```text
20
40
60
[10, 20, 30]
```

Why?

```text
Iteration 1:
number ──► 10
number = number * 2
number ──► 20
```

The assignment rebinds the name `number`. It does not replace the element stored in `numbers`.

## Rebinding After Mutation

These two operations can happen in the same iteration:

```python
numbers = [[10], [20], [30]]

for number in numbers:
    number.append(5)
    number = [100]

print(numbers)
print(number)
```

Output:

```text
[[10, 5], [20, 5], [30, 5]]
[100]
```

Execution for one iteration:

```text
number ──► [10]

number.append(5)
        ↓
number ──► [10, 5]
```

The inner list is mutated, so `numbers` changes.

Then:

```python
number = [100]
```

creates a new list and rebinds `number` to it. The original `[10, 5]` remains inside `numbers`.

## Mutating Through the Loop Variable

```python
numbers = [[10], [20], [30]]

for number in numbers:
    number[0] = 99

print(numbers)
```

Output:

```text
[[99], [99], [99]]
```

`number[0] = 99` mutates the inner list object currently referenced by `number`.

Important distinction:

```python
number = [99]       # rebinds number
number[0] = 99      # mutates the inner list
```

## `+=` With Lists

For lists, `+=` performs in-place addition and mutates the existing list.

```python
numbers = [[10], [20], [30]]

for number in numbers:
    number += [5]

print(numbers)
```

Output:

```text
[[10, 5], [20, 5], [30, 5]]
```

Compare:

```python
number = number + [5]   # creates a new list, then rebinds number
number += [5]           # mutates the existing list in place
```

## Changing the Outer List Does Not Retroactively Change `number`

```python
numbers = [10, 20, 30]

for number in numbers:
    numbers[0] = 99
    print(number)

print(numbers)
```

Output:

```text
10
20
30
[99, 20, 30]
```

During the first iteration:

```text
numbers ──► [10, 20, 30]
number  ──► 10
```

After:

```python
numbers[0] = 99
```

the list becomes `[99, 20, 30]`, but `number` is still bound to the `10` object for that iteration.

Changing an element of the list does not retroactively change an earlier binding of `number`.

## Modifying a List While Iterating

A `for` loop over a list does not necessarily iterate over a frozen copy. Mutating the same list during iteration can change which elements are visited.

### Appending While Iterating

```python
numbers = [10, 20, 30]

for number in numbers:
    numbers.append(40)
    print(number)
```

The appended elements can be observed by the iterator. This can make the loop continue growing the list and fail to terminate normally.

### Popping While Iterating

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
    numbers.pop()
```

Output:

```text
10
20
```

Final list:

```text
[10]
```

The list shrinks while the iterator advances, so the changing indexes can cause elements to be skipped.

### Removing the Current Value

```python
numbers = [10, 20, 30]

for number in numbers:
    numbers.remove(number)

print(numbers)
```

Final value:

```text
[20]
```

Trace:

```text
Start: [10, 20, 30]

number = 10
remove(10)
→ [20, 30]

Iterator advances to the next index.

number = 30
remove(30)
→ [20]

The remaining 20 was skipped.
```

**Engineering rule:** avoid modifying a list while iterating over that same list unless the behavior is deliberately understood and required. Prefer constructing a new result or iterating over a separate snapshot when appropriate.

## Summary: The Critical Distinctions

```text
number = ...
    ↓
rebinds the name `number`

number.append(...)
    ↓
mutates the list object referenced by `number`

number[0] = ...
    ↓
mutates the list object referenced by `number`

number = number + [...]
    ↓
creates a new list and rebinds `number`

number += [...]
    ↓
mutates the existing list in place
```

The most important question when tracing a `for` loop is:

> **Am I rebinding the loop variable, or am I mutating an object that the loop variable currently refers to?**
