# Design Review

This document summarizes observations and recommendations after reviewing the current repository structure and domain model.

The purpose is to identify areas for improvement while preserving the current architecture.

---

# Overall Assessment

The repository has reached a mature and consistent architecture.

The current model based on:

- Articles
- Concepts
- Rules
- Processes
- Interpretations
- Open Questions

is considered sufficiently stable to continue developing content.

The focus should now shift from architectural design to expanding and refining the knowledge base.

---

# Strengths

## Consistent domain structure

All domains follow the same layout, making navigation predictable and reducing cognitive load.

## Strong traceability

The relationship between legislation, rules and processes is clear.

```
Article
    ↓
Rule
    ↓
Process
    ↓
Diagram
```

## Good separation of reusable capabilities

The distinction between domain-specific knowledge and shared capabilities is well defined.

## Rule Cards

Rule Cards provide an excellent bridge between legal requirements and operational processes.

---

# Recommendations

## 1. Strengthen relationships between domains

Domains currently describe themselves well but provide limited context about where they fit in the overall asylum procedure.

Each domain README should describe:

- Previous domain(s)
- Next domain(s)
- Entry criteria
- Exit criteria

Example:

```
Previous

Screening

↓

Registration

↓

Responsibility determination
```

---

## 2. Introduce an end-to-end case lifecycle

The repository lacks a simple overview of how an asylum case progresses through the Pact.

Recommended new document:

```
CASE_LIFECYCLE.md
```

Example lifecycle:

```
Person seeks protection

↓

Screening

↓

Registration

↓

Eurodac

↓

Responsibility determination

↓

Regular procedure
or
Border procedure

↓

Decision

↓

Appeal / Return / Protection
```

This document should act as the primary navigation aid for new readers.

---

## 3. Continue consolidating shared concepts

Several concepts appear across multiple domains.

Examples include:

- Applicant
- Identity
- Documents
- Family member
- Minor
- Vulnerability
- Security checks

Where appropriate, these should be maintained in `shared/` and referenced rather than duplicated.

---

## 4. Expand cross-domain references

As additional content is added, increase explicit references between:

- Articles
- Rules
- Processes
- Shared capabilities
- Related domains

The repository should gradually evolve into a connected knowledge graph.

---

## 5. Explain the purpose of each domain

Several domains describe *what* they contain.

Consider also describing *why* the domain exists within the legal framework.

This provides important context for readers unfamiliar with asylum law.

---

# Recommendations for future work

The following activities are recommended before introducing additional architectural concepts.

## Complete the Registration pilot

Continue expanding:

- Articles
- Rule Cards
- Processes
- Diagrams

Evaluate the architecture only after the Registration domain is considered complete.

---

## Expand remaining domains

Follow the same pattern established by Registration.

Avoid introducing domain-specific structures unless a clear need emerges.

---

## Review architecture after multiple domains are complete

Architectural changes should be driven by practical experience rather than anticipated future complexity.

---

# Avoid unnecessary complexity

The current review does **not** recommend introducing additional object types such as:

- Events
- State objects
- Decision objects
- Milestone folders

These concepts can currently be represented effectively within existing process and rule documentation.

---

# Guiding Principle

The repository should remain:

- understandable for non-lawyers,
- traceable to legislation,
- reusable by architects and developers,
- easy for AI systems to navigate,
- maintainable over time.

Whenever design decisions are considered, preference should be given to readability over abstraction.

> Model second. Explain first.