# Repository Review – Increasing Detail and Sense-Making

Any text-diagram here should be represented by PlantUml-diagrams instead.

## Overall Assessment

The repository has reached a level of maturity where the architecture is no longer the primary area for improvement. The domain structure, traceability model, and navigation are coherent and scalable.

Future improvements should therefore focus on **knowledge richness** rather than **architectural complexity**.

The next phase is about helping readers answer not only **what the law says**, but also:

- Why does this rule exist?
- What changes when this step is completed?
- How is information reused?
- How do concepts relate to each other?
- How does this domain fit into the larger asylum system?

---

# Recommendation 1 – Enrich Rule Cards

Rule Cards are already the core knowledge objects of the repository.

They could become even more valuable by answering a consistent set of questions.

## Suggested template additions

```text
Purpose

Trigger

Legal Effect

Used By

Related Rules
```

Example:

```text
Purpose

Ensures that an application formally enters the asylum procedure.

Trigger

A third-country national expresses a wish to seek international protection.

Legal Effect

The Member State becomes obliged to register the application.

Used By

Registration Process

Related Rules

RULE-APR-027-002
RULE-APR-027-003
```

This transforms Rule Cards from legal extracts into reusable knowledge objects.

---

# Recommendation 2 – Visualize State Changes

Most domains are not primarily about activities.

They are about **changing the legal state**.

Each domain could explicitly describe:

```text
Before

↓

Action

↓

After
```

Example:

```text
Before

Application not registered

↓

Registration

↓

After

Application registered
```

This helps readers immediately understand why the domain exists.

---

# Recommendation 3 – Visualize Information Flow

Current diagrams primarily describe activities.

Another useful perspective is information movement.

Example:

```text
Applicant

↓

Identity

↓

Registration

↓

Eurodac

↓

Responsibility

↓

Procedure
```

This illustrates how information created in one domain is reused by later domains.

This perspective is especially useful for architects and system designers.

---

# Recommendation 4 – Expand Concepts

Concept pages could become true knowledge hubs.

Suggested structure:

```text
Definition

Purpose

Legal Basis

Where Used

Created By

Used By

Related Concepts

Related Rules
```

Rather than acting only as glossary entries, Concepts become navigation hubs throughout the repository.

---

# Recommendation 5 – Separate Legal and Operational Perspectives

Many legal requirements imply operational behaviour.

Example:

```text
Legal Requirement

↓

Operational Consequence

↓

System Implication
```

Example:

```text
Register within five days

↓

Authority records the application

↓

Case management system requires registration date
```

This makes the repository valuable for solution architects as well as legal experts.

---

# Recommendation 6 – Show Domain Dependencies

Dependencies currently exist but are mostly implicit.

Simple dependency diagrams could make them much clearer.

Example:

```text
Registration

depends on

Identity
Documents
Interpreter

↓

produces

Registered Application

↓

used by

Eurodac

Responsibility

Procedure
```

These diagrams explain how domains collaborate without describing process logic.

---

# Recommendation 7 – Explain Why Articles Exist

Every article could begin with a short purpose statement.

Example:

```text
Purpose

Ensures that every asylum application formally enters the asylum procedure.
```

Only one or two sentences are needed.

Readers often understand legislation much faster when they understand its objective before reading its requirements.

---

# Recommendation 8 – Define Scope Explicitly

Each domain could clearly state what it covers—and what it does not.

Example:

```text
Scope

Included

✓ Registration

✓ Deadlines

✓ Documentation

Not Included

✗ Examination

✗ Responsibility

✗ Decision
```

Explicit scope definitions reduce ambiguity and improve navigation.

---

# Recommendation 9 – Add Key Questions

Each domain could start with the questions it answers.

Example:

```text
This domain answers:

• When is an application registered?

• Who performs the registration?

• What information is recorded?

• What deadlines apply?

• What happens after registration?
```

Readers immediately know whether they are in the right place.

---

# Recommendation 10 – Present Three Complementary Views

Every domain could be understood through three perspectives.

## Legal View

```text
Articles

↓

Rules
```

Focus:

What the legislation requires.

---

## Operational View

```text
Activities

↓

Process
```

Focus:

How the work is performed.

---

## Information View

```text
Applicant

↓

Application

↓

Registration Record

↓

Documents
```

Focus:

How information is created, transformed, and reused.

These three perspectives complement each other without duplicating information.

---

# The Next Evolution

The repository already documents legislation exceptionally well.

The next step is not adding more folders or object types.

Instead, it is about making **relationships** increasingly visible.

Almost every page could answer questions such as:

- Created By
- Consumes
- Produces
- Used By
- Related Concepts
- Related Rules
- Related Processes

Over time, this naturally transforms the repository into a navigable knowledge graph without changing its underlying architecture.

---

# Prioritized Improvements

## 1. Enrich Rule Cards

Add:

- Purpose
- Trigger
- Legal Effect
- Used By
- Related Rules

---

## 2. Expand Concepts

Develop Concepts into reusable knowledge hubs by adding:

- Where Used
- Created By
- Used By
- Related Concepts

---

## 3. Introduce Additional Diagram Types

Complement existing process diagrams with:

- Legal Effects
- Information Flow
- Domain Dependencies
- State Transitions

These diagrams improve understanding without replacing existing PlantUML process diagrams.

---

## 4. Increase Relationship Visibility

Explicitly document:

- Created By
- Produces
- Consumes
- Used By

across Rules, Concepts, Processes, and Domains.

---

## 5. Improve Context

Add concise introductory sections to domains and articles:

- Purpose
- Scope
- Key Questions

These additions help readers understand not only *what* the legislation requires, but also *why* it exists and *how* it fits into the larger Migration and Asylum Pact.

---

# Final Observation

The architecture is now sufficiently mature that future improvements should focus on **depth rather than breadth**.

Rather than introducing additional object types or structural changes, future work should enrich the existing knowledge objects and strengthen the relationships between them.

The repository is evolving from structured documentation into a comprehensive legal knowledge base.

The next milestone is to make that knowledge increasingly self-explanatory.