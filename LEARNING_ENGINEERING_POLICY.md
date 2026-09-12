# Learning & Engineering Policy

This document defines how the Python Backend Engineering track is taught and how practical exercises are evaluated.

## 1. Job-First Objective

The purpose of this track is to become employable within a practical job-search timeframe, not to complete an endless Python syllabus.

The target is Python Backend / Automation work. Topics and depth should be justified by real job requirements, interview expectations, and the ability to demonstrate working software.

## 2. Teach Before Retrieval

New material is taught first. Retrieval practice is used later for consolidation when requested or when appropriate.

A learner should not be blocked from learning a new concept simply because a retrieval quiz has not happened yet.

## 3. Specification Before Design

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

## 4. Review the Reasoning, Not Just the Output

A solution is reviewed for:

1. Python logic and correctness
2. behaviour/contract and documentation
3. type hints appropriate to the current learning stage
4. test-case thinking
5. design reasoning and trade-offs

If the implementation works but the design is weak, the weakness should be explained and corrected through reasoning rather than simply replacing the learner's solution.

## 5. Interview-Style Development

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

## 6. Scenario-Based Completion

A topic is not considered practically complete merely because syntax and isolated examples are understood.

The final stage of a topic should normally contain one or two realistic scenario-based exercises that combine the concepts covered in that section and earlier roadmap material.

The exercises should be specification-driven and should leave meaningful implementation decisions to the learner.

## 7. Test-Case Thinking Before pytest

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

## 8. Do Not Add Premature Complexity

Engineering practices should be introduced when they support the current concept.

Do not turn a Python fundamentals exercise into an architecture exercise by adding frameworks, databases, APIs, advanced typing, infrastructure, or patterns that have not yet been taught.

The goal is to develop engineering judgment progressively.

## 9. Record New Decisions

The methodology is allowed to evolve.

When a useful design principle, interview expectation, recurring mistake, or new teaching decision emerges during the track, record it in the appropriate repository documentation rather than relying only on conversation history.

## 10. Definition of Done

A topic is complete when the learner can:

- use the concept correctly
- explain the underlying mental model
- implement it without copying a tutorial
- make reasonable design decisions from a specification
- discuss important edge cases
- complete the final scenario-based practical(s)
- explain the resulting code in an interview-style discussion

Roadmap checkboxes should be marked complete only when this practical standard has been met.
