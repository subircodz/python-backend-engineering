# Python Backend Engineering Roadmap

## Mission

Become employable as a **Python Backend / Automation Engineer** by turning existing software-engineering knowledge into demonstrable Python engineering ability.

This roadmap is deliberately finite and job-focused. It is not intended to make the learner an expert in every Python technology before applying for work.

---

## Phase 0 — Baseline Assessment

**Status: IN PROGRESS**

Before teaching new Python material, assess the current ability in:

- Python fundamentals
- functions and scope
- data structures
- OOP
- exceptions
- modules/packages
- iterators/generators
- decorators/context managers
- typing
- filesystem/data handling
- HTTP/API usage
- testing
- debugging

### Completed / established

- functions and scope
- closures
- mutation vs rebinding
- OOP fundamentals, inheritance, overriding, `super()`, and MRO
- exception handling with `try/except/else/finally`
- modules, namespaces, and import forms
- packages, subpackages, `__init__.py`, package-level exports, and relative imports
- import resolution, `sys.path`, and `sys.modules`
- normal module execution and repeated-import behavior
- function parameter binding: `*args`, `**kwargs`, keyword-only parameters, and positional-only parameters
- higher-order functions, functions as first-class objects, `map()`, `filter()`, `reduce()`, `sorted(key=...)`, and lambda usage
- Python List model and operations, including mutation/rebinding and shallow-copy reference behavior
- fundamental `for` loop model, including iteration, loop-variable rebinding, post-loop binding, mutation through the loop variable, and effects of modifying a list during iteration
- Python Tuple fundamentals, including ordered access, immutability vs rebinding, mutable objects stored inside tuples, and basic unpacking
- Python Tuple creation and syntax, including comma-based tuple creation, single-element tuples, empty tuples, nested tuples, and `tuple()` construction
- Python Tuple packing and unpacking, including extended unpacking with `*`, function-call unpacking with `*`, argument collection with `*args`, keyword unpacking/collection with `**kwargs`, swapping, and reference behavior with mutable objects
- Python Tuple methods and operations, including `count()`, `index()`, concatenation, repetition, membership, indexing, slicing, `len()`, numeric built-ins, comparisons, `+=` rebinding, and mutable objects stored inside tuples
- Python Set fundamentals, including uniqueness, mutability, lack of positional indexing, hashable element requirements, set creation, empty-set syntax, membership testing, and the set-vs-list/tuple mental model
- Python Set creation and syntax, including set literals, empty-set syntax, `set()` construction from iterables, hashable element requirements, string/iterable behavior, literal-vs-constructor choice, and type preservation
- Python Set methods and operations, including `add()`, `update()`, `remove()`, `discard()`, `pop()`, `clear()`, union, intersection, difference, symmetric difference, in-place set operators, subset, superset, disjoint checks, mutation vs rebinding, and practical production use cases
- Python Dictionary fundamentals, including the key → value mapping model, unique keys, mutability vs rebinding, key-based lookup, `KeyError`, hashable key requirements, mutable/unhashable values, and mapping updates

### Exit condition

We know what is already solid, what is weak, and what should be skipped.

---

# Phase 1 — Python Engineering Core

**Goal:** Write maintainable Python without depending on tutorial patterns.

### 1.1 Language and runtime model

- [x] objects and references
- [x] mutability and identity
- [x] namespaces and scope
- [x] imports and module loading — import forms, package boundaries, import resolution, `sys.path`, `sys.modules`, and repeated imports covered
- [x] execution model — normal module execution and function-definition vs function-call behavior covered

### 1.2 Functions

- [x] parameters and arguments
- [x] positional/keyword arguments
- [x] default values
- [x] `*args` and `**kwargs` — collection, unpacking, and tuple/dictionary behavior covered
- [x] parameter binding rules — normal parameters, `*args`, keyword-only parameters, positional-only parameters, and `**kwargs`
- [x] closures
- [x] higher-order functions — function objects, passing/returning functions, `map()`, `filter()`, `reduce()`, `sorted(key=...)`, lambda, and production-oriented lambda vs `def` choice
- [x] function design

### 1.3 Data structures

- [x] list — **COMPLETE**; covered ordered/mutable model, positive/negative indexing, index assignment, aliasing, `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `clear()`, slicing and slice assignment, `len()`, membership, shallow copy, `index()`, `count()`, `reverse()`, `sort()`/`sorted()`, `reversed()`, `del`, `+`, repetition with shared-reference edge cases, and `+=`. Completed final 30-question retrieval revision; see `python/fundamentals/data-structures/list/28-list-revision-30-questions.md`.
- [x] fundamental `for` loops — **COMPLETE**; covered iteration over lists, loop-variable rebinding and post-loop binding, mutation vs rebinding, nested-object mutation, `+=` vs `+`, and mutation of the iterated list including skipped elements. See `python/fundamentals/for-loops/01-for-loop-fundamentals.md`.
- [x] tuple — **COMPLETE: fundamentals**; covered ordered access, immutability vs rebinding, mutable objects stored inside tuples, and basic unpacking. See `python/fundamentals/data-structures/tuple/01-tuple-fundamentals.md`.
- [x] tuple creation and syntax — **COMPLETE**; covered comma-based tuple creation, single-element tuple syntax, empty/nested tuples, and `tuple()` construction. See `python/fundamentals/data-structures/tuple/02-tuple-creation-and-syntax.md`.
- [x] tuple packing and unpacking — **COMPLETE**; covered tuple packing, iterable unpacking, extended unpacking with `*`, starred-target list behavior, `_` as a conventional throwaway binding, `func(*values)`, `*args`, `**kwargs`, swapping, and mutable-object reference behavior. See `python/fundamentals/data-structures/tuple/03-tuple-packing-and-unpacking.md`.
- [x] tuple methods and operations — **COMPLETE**; covered `count()`, `index()`, `+`, `*`, `in`/`not in`, indexing, slicing, `len()`, `min()`/`max()`/`sum()`, lexicographical ordering, equality, `+=` as new-tuple creation plus rebinding, and mutable objects stored inside tuples. See `python/fundamentals/data-structures/tuple/04-tuple-methods-and-operations.md`.
- [x] set — **COMPLETE**; covered set fundamentals, creation and syntax, set literals, empty-set syntax, `set()` construction from iterables, hashable element requirements, string/iterable behavior, literal-vs-constructor choice, type preservation, methods and operations, set relationships, in-place operations, mutation vs rebinding, and practical production use cases. See `python/fundamentals/data-structures/set/01-set-fundamentals.md`, `02-set-creation-and-syntax.md`, and `03-set-methods-and-operations.md`.
- [ ] dict — **IN PROGRESS**; fundamentals and the key → value mental model covered. See `python/fundamentals/data-structures/dict/01-dict-fundamentals.md`.
- [ ] comprehensions
- [ ] `collections`
- [ ] choosing the appropriate structure
- [ ] common performance characteristics

### 1.4 OOP

- [x] classes and instances
- [ ] instance/class/static methods
- [x] inheritance
- [x] method overriding
- [x] `super()`
- [x] MRO
- [ ] composition
- [ ] abstraction
- [ ] protocols/duck typing
- [ ] dataclasses

### 1.5 Error handling

- [x] exception hierarchy
- [ ] raising exceptions
- [ ] custom exceptions
- [ ] exception boundaries
- [x] `try/except/else/finally`
- [ ] resource safety

### 1.6 Python iteration model

- [ ] iterable vs iterator
- [ ] `iter()` / `next()`
- [ ] generators
- [ ] generator expressions
- [ ] lazy evaluation

### 1.7 Decorators

- [ ] functions as objects
- [ ] closures in decorators
- [ ] preserving metadata
- [ ] practical decorator patterns

### 1.8 Context managers

- [ ] `with`
- [ ] context manager protocol
- [ ] `contextlib`
- [ ] resource lifecycle management

### 1.9 Typing and data modelling

- [ ] type hints
- [ ] `Optional` / unions
- [ ] collections typing
- [ ] `Protocol`
- [ ] `TypedDict`
- [ ] dataclasses
- [ ] practical static type checking

### 1.10 Standard library for engineering

- [ ] `pathlib`
- [ ] `os` / `sys`
- [ ] `json`
- [ ] `csv`
- [ ] `datetime`
- [ ] `re`
- [ ] `collections`
- [ ] `itertools`
- [ ] `functools`
- [ ] `subprocess`
- [ ] `argparse`

### Exit condition

Can implement a small Python component from a specification, choose reasonable abstractions, handle failures, and write tests for it.

---

# Phase 2 — Python Packaging and Application Structure

**Goal:** Turn Python code into maintainable applications.

- [ ] virtual environments
- [ ] dependency management
- [ ] `pyproject.toml`
- [x] package layout
- [x] imports and package boundaries — package hierarchy, `__init__.py`, package exports, and relative imports covered
- [ ] configuration
- [ ] environment variables
- [ ] secrets handling
- [ ] entry points / CLI basics
- [ ] logging
- [ ] application settings

### Exit condition

Can create a clean Python application with reproducible dependencies and sensible configuration.

---

# Phase 3 — HTTP and APIs

**Goal:** Understand the web layer before hiding it behind a framework.

- [ ] client/server model
- [ ] HTTP methods
- [ ] status codes
- [ ] headers
- [ ] JSON
- [ ] authentication concepts
- [ ] REST principles
- [ ] idempotency
- [ ] pagination
- [ ] error responses
- [ ] API versioning basics
- [ ] consuming APIs from Python

### Exit condition

Can explain and consume a REST API confidently and design a basic API contract.

---

# Phase 4 — FastAPI Backend Development

**Goal:** Build production-style Python APIs.

- [ ] FastAPI application structure
- [ ] routing
- [ ] path/query parameters
- [ ] request bodies
- [ ] Pydantic models
- [ ] response models
- [ ] validation
- [ ] dependency injection
- [ ] error handling
- [ ] middleware basics
- [ ] authentication/authorization
- [ ] API documentation
- [ ] background work
- [ ] testing FastAPI applications

### Exit condition

Can independently build a documented, validated and tested REST API.

---

# Phase 5 — SQL and PostgreSQL

**Goal:** Build database-backed applications.

### SQL

- SELECT/filtering
- joins
- grouping/aggregation
- subqueries
- CTEs
- window functions
- transactions
- constraints
- indexes
- query reasoning

### PostgreSQL

- database/schema/table design
- data types
- constraints
- indexes
- transactions
- practical performance basics

### SQLAlchemy

- engine/session model
- models
- relationships
- queries
- transactions
- migrations concepts

### Exit condition

Can design a small relational schema and build a Python service that safely reads/writes PostgreSQL data.

---

# Phase 6 — Testing and Quality

**Goal:** Demonstrate that the code works and remains maintainable.

- pytest
- fixtures
- parametrization
- mocking
- unit tests
- integration tests
- API tests
- database tests
- test boundaries
- testable design
- coverage as a signal, not a target
- linting/formatting
- static checking

### Exit condition

Can design a sensible test strategy and diagnose a failing test rather than simply adding assertions until CI passes.

---

# Phase 7 — Docker and CI/CD

**Goal:** Move from “works on my machine” toward reproducible software delivery.

- Docker fundamentals
- Dockerfile
- image/container model
- environment configuration
- Docker Compose basics
- application + database locally
- GitHub Actions
- test automation
- linting in CI
- build verification

### Exit condition

A project can be cloned, tested and run consistently by another developer.

---

# Phase 8 — Production Engineering Basics

**Goal:** Understand the problems that appear after the happy path works.

- structured logging
- configuration separation
- graceful failure
- retries and timeouts
- validation at boundaries
- health checks
- security basics
- dependency updates
- debugging production failures
- basic performance reasoning
- API reliability

### Exit condition

Can identify and address common reliability problems in a backend service.

---

# Phase 9 — Automation Engineering

**Goal:** Use Python to automate real business and engineering workflows.

- API automation
- file/data automation
- database automation
- subprocess/system integration
- scheduled jobs
- background workers
- browser automation where appropriate
- retries/timeouts
- idempotent automation
- logging and auditability

### Exit condition

Can build a reliable automation workflow rather than a one-off script.

---

# Phase 10 — Portfolio Projects

Projects are evidence, not decoration.

## Project 01 — Python Service

Demonstrate:

- clean Python structure
- domain/service separation
- exceptions
- logging
- configuration
- tests
- packaging

## Project 02 — Backend API

Demonstrate:

- FastAPI
- PostgreSQL
- SQLAlchemy
- authentication
- validation
- error handling
- pytest
- Docker
- GitHub Actions
- documentation

## Project 03 — Automation System

Demonstrate:

- external API integration
- data processing
- persistence
- scheduled/background execution
- retries/timeouts
- logging
- tests
- failure recovery

### Exit condition

At least one project should be strong enough to discuss deeply in an interview, including architecture, trade-offs, testing and failure scenarios.

---

# Phase 11 — Interview Readiness

This phase starts **before** the roadmap is complete.

### Python

- language fundamentals
- OOP
- exceptions
- iterators/generators
- decorators
- context managers
- typing
- debugging

### Backend

- HTTP
- REST
- FastAPI
- authentication
- databases
- transactions
- API design

### SQL

- joins
- grouping
- subqueries
- CTEs
- window functions

### DSA

Only the level justified by target job postings:

- arrays/strings
- hash maps/sets
- stacks/queues
- linked lists
- trees
- sorting/searching
- complexity

### Project interview

Be able to answer:

- Why did you structure it this way?
- What happens when the database is unavailable?
- How did you test it?
- Where can it fail?
- How would you scale it?
- What would you change in the next version?

---

# Phase 12 — Job Application Loop

**This does not wait for roadmap completion.**

```text
Learn
  ↓
Build
  ↓
Publish evidence
  ↓
Apply
  ↓
Interview
  ↓
Record gaps
  ↓
Close gaps
  ↓
Apply again
```

Target titles will be selected from actual vacancies rather than from the label “Python Developer” alone.

Possible target families:

- Junior Python Developer
- Python Backend Developer
- Backend Developer (Python)
- Python Automation Engineer
- Automation Developer
- QA/Automation Engineer with Python
- Python API Developer
- AI/Automation Developer when the foundation is ready

---

# Deferred Topics

These are intentionally **not prerequisites for the first job**:

- advanced distributed systems
- Kubernetes
- deep cloud architecture
- microservices at scale
- Kafka-heavy architectures
- advanced DevOps
- machine learning theory
- deep learning
- advanced LLM engineering
- RAG/vector databases
- autonomous agents

They can be introduced when a target role requires them or after employability is established.

---

# Definition of Job Ready

The repository is not “complete” because every folder has files.

The first job-ready milestone is reached when the learner can:

1. write maintainable Python
2. explain the Python concepts used
3. build a REST API with FastAPI
4. work with SQL/PostgreSQL
5. use SQLAlchemy appropriately
6. write meaningful pytest tests
7. use Git confidently
8. run the application with Docker
9. automate testing with CI
10. debug failures
11. explain a substantial project end-to-end
12. solve common interview-level Python/SQL problems
13. apply to relevant vacancies with credible evidence

## Guiding Rule

> **If a topic does not materially improve our ability to get, perform, or interview for a target job, it is not automatically part of the roadmap.**
