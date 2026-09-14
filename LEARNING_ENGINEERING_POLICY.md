# Learning & Engineering Policy

This document defines how the Python Backend Engineering track is taught and how practical exercises are evaluated.

## 1. Job-First Objective

The purpose of this track is to become employable as a **Python Backend / Automation Engineer**, not to complete an endless Python syllabus.

The target roles are:

- Junior Python Backend Developer
- Python Backend Developer
- Python Automation Engineer
- Python Software Engineer where Python is the primary language

Topics and depth should be justified by real job requirements, interview expectations, and the ability to demonstrate working software.

This repository is intentionally separate from the Python Engineering track. Python Engineering develops the underlying Python capability; this track answers:

> **Can I use Python to build, test, debug, maintain, and improve backend systems and reliable automation?**

## 2. AI-Resilient Engineering Standard

AI can generate large amounts of backend boilerplate. Therefore, progress is **not** measured mainly by how much code the learner can type manually.

Training should build the ability to understand and control:

- requirements
- API contracts
- application architecture
- data flow
- business logic
- failure modes
- databases
- authentication and authorization
- validation
- testing
- observability
- deployment
- security
- performance
- maintainability

The target capability is:

> Understand the system, build a component, explain the design, test it, debug it, improve it, and use AI to accelerate the work without blindly depending on AI.

## 3. Teach Before Retrieval

New material is taught first. Retrieval practice is used later for consolidation when requested or when appropriate.

A learner should not be blocked from learning a new concept simply because a retrieval quiz has not happened yet.

## 4. Requirement → Design → Implementation Cycle

Practical work should progressively follow this engineering loop:

```text
Requirement
    ↓
Design
    ↓
Learner attempts
    ↓
Implementation
    ↓
Test / verify
    ↓
Failure analysis
    ↓
Refactor
    ↓
AI comparison
    ↓
Production hardening
```

The exact depth depends on the current learning stage. Fundamentals should not be overloaded with architecture that has not yet been taught.

## 5. Specification Before Design

When an exercise is intended to develop engineering judgment, the exercise should specify:

- scenario/context
- required behaviour
- constraints
- expected results
- important rules and boundaries

It should **not** prescribe the internal design unless the design itself is the lesson.

The learner should decide things such as:

- data structure
- abstraction
- method boundaries
- control flow
- mutation vs creation of new results
- return shape
- reuse of existing methods
- appropriate use of exceptions

The instructor should not reveal these decisions before the learner has attempted the problem.

## 6. Review the Reasoning, Not Just the Output

A solution is reviewed for:

1. Python logic and correctness
2. behaviour/contract and documentation
3. type hints appropriate to the current learning stage
4. test-case thinking
5. design reasoning and trade-offs
6. readability and maintainability

Review findings should distinguish actual defects from improvements:

- **❌ Logic/behaviour bug** — the implementation is incorrect or violates the requirement.
- **⚠️ Style/readability issue** — the implementation works but is harder to read or maintain.
- **🔧 Engineering improvement** — a reasonable production improvement that is not required for correctness.
- **💡 Optional optimisation** — a context-dependent improvement, not automatically better.

If the implementation works but the design is weak, explain the weakness and correct the reasoning rather than simply replacing the learner's solution.

## 7. Interview-Style Development

The expected interview pattern is increasingly:

```text
Requirement
    ↓
Choose an approach
    ↓
Implement
    ↓
Run / verify
    ↓
Explain design decisions
    ↓
Discuss edge cases and failures
    ↓
Discuss alternatives and trade-offs
```

The learner is therefore trained to answer not only **"Does it work?"**, but also:

- Why did you choose this approach?
- What assumptions did you make?
- What happens at the boundaries?
- What could fail?
- What would you change if the requirements changed?
- What are the trade-offs of another approach?
- How would you test this?
- How would you debug it if it failed in production?

Interview preparation should be connected to actual engineering work rather than disconnected trivia.

## 8. Real-World Failure Training

Exercises and projects should increasingly include realistic failure modes, including:

- invalid requests
- missing fields
- malformed input
- database unavailability
- timeouts
- duplicate requests
- partial failures
- authentication failures
- authorization failures
- race conditions
- bad configuration
- dependency failures
- unexpected data
- API contract changes

The learner should be trained to reason about what happens when the happy path breaks.

## 9. Scenario-Based Completion

A topic is not considered practically complete merely because syntax and isolated examples are understood.

The final stage of a topic should normally contain one or two realistic scenario-based exercises that combine the concepts covered in that section and earlier roadmap material.

The exercises should be specification-driven and should leave meaningful implementation decisions to the learner.

## 10. Test-Case Thinking Before pytest

Formal pytest and testing strategy are taught later in the roadmap. However, test-case thinking starts during ordinary implementation work.

For each practical, consider at least:

- normal/success case
- boundary case
- empty case
- missing/unknown item
- invalid input where the specification permits it
- duplicate/conflicting state
- mutation side effects
- expected failure

This is preparation for formal testing, not a replacement for the later testing phase.

## 11. Do Not Add Premature Complexity

Engineering practices should be introduced when they support the current concept.

Do not turn a Python fundamentals exercise into an architecture exercise by adding frameworks, databases, APIs, advanced typing, infrastructure, or patterns that have not yet been taught.

The goal is to develop engineering judgment progressively.

## 12. Framework and Database Teaching Standard

Frameworks must be taught as engineering tools, not button-clicking exercises. For an important framework feature, explain the problem it solves, the useful internal model, how it should be tested, common mistakes, and relevant production considerations.

Backend development should include practical database knowledge, especially PostgreSQL and SQL. Database concepts should be introduced when backend systems require them rather than turned into an unrelated database curriculum.

Important backend/database areas include:

- HTTP and request/response lifecycle
- REST and API contracts
- authentication and authorization
- validation and error handling
- PostgreSQL and SQL
- schema design and constraints
- indexes and query behaviour
- transactions and isolation concepts
- safe parameterized queries
- connection handling and pooling
- migrations

## 13. Deliberate AI Use

AI is a development accelerator, not a technical authority.

The learner should be trained to:

- convert requirements into precise prompts
- ask AI for architecture proposals
- generate boilerplate when useful
- inspect generated code
- detect security and correctness problems
- verify framework/API behaviour
- write tests around generated code
- debug generated code
- refactor generated code
- compare alternative implementations
- explain accepted generated code independently

**"AI says so" is never sufficient technical justification.**

If AI-generated code is used in a project, the learner must understand enough to explain its behaviour, assumptions, risks, and trade-offs in an interview.

## 14. Production-Style Project Standard

Projects are evidence of engineering ability, not decoration.

Avoid creating many repetitive toy CRUD applications. Prefer fewer projects with increasing complexity.

A meaningful backend project should progressively demonstrate:

- clear structure
- API design
- validation
- database integration
- error handling
- logging
- tests
- configuration
- documentation
- Git
- CI where appropriate
- security basics
- realistic failure handling

At least one project should eventually be strong enough to discuss deeply in an interview, including architecture, trade-offs, testing, debugging, and failure scenarios.

## 15. Repository Discipline

Before changing repository content:

1. inspect `README.md`
2. inspect `ROADMAP.md`
3. inspect `TODO.md` if present
4. inspect relevant notes
5. check the latest commit
6. determine the exact current learning checkpoint

Never duplicate material unnecessarily.

Update roadmap/TODO tracking after completed milestones. Commit meaningful completed work.

If a referenced tracking file such as `TODO.md` does not exist, do not invent it merely because the policy mentions it; first verify the repository state and then decide whether a new tracking file is actually useful.

## 16. Definition of Done

A topic is complete when the learner can:

- use the concept correctly
- explain the underlying mental model
- implement it without copying a tutorial
- make reasonable design decisions from a specification
- discuss important edge cases
- complete the final scenario-based practical(s)
- explain the resulting code in an interview-style discussion

Roadmap checkboxes should be marked complete only when this practical standard has been met.
