# Requirements and Capabilities

## Purpose

The repository currently provides excellent traceability from legislation to rules, concepts, and processes.

The next logical evolution is **not** to add more legal content, but to provide a bridge between legislation and implementation.

Two complementary knowledge objects can provide this bridge:

- **Requirements** – what must be fulfilled.
- **Capabilities** – what an organisation must be able to do.

Neither replaces existing Rule Cards or Processes. Instead, they provide additional perspectives for architects, business analysts, project managers, and system developers.

---

# Why?

Legislation rarely specifies how something should be implemented.

Instead, legislation creates obligations.

Those obligations eventually become:

- business requirements
- organisational capabilities
- information requirements
- system requirements

Making these relationships explicit increases the value of the repository without changing its legal focus.

---

# Capability

## Definition

A **Capability** describes something that a competent authority must be able to perform in order to comply with the legislation.

A capability describes **what** the organisation must be able to do.

It intentionally does **not** describe:

- how the work is performed
- organisational responsibilities
- IT solutions
- implementation details

Capabilities are stable over time, while processes and systems may change.

---

## Example

```text
CAP-REG-001

Register Application

Purpose

Create a legally valid registered application.

Supported by

Registration Process

Implements

RULE-APR-027-001

Produces

Registered Application

Related Concepts

Application
Registration
Applicant
```

---

## Suggested Structure

```text
ID

Name

Purpose

Implements

Supported By

Produces

Consumes

Related Concepts

Related Rules
```

---

## Repository Placement

```
shared/
    capabilities/
```

or

```
capabilities/
```

depending on whether capabilities are considered reusable across domains.

---

# Requirement

## Definition

A **Requirement** expresses an obligation derived from one or more legal rules.

Requirements translate legal obligations into implementation-neutral statements.

They are **not** software requirements.

They are implementation-independent requirements that any compliant organisation must satisfy.

---

## Example

```text
REQ-APR-027-001

The registration date shall be recorded.

Derived From

RULE-APR-027-001

Purpose

Support legal time limits.

Related Concepts

Registration Date

Supported By

Register Application
```

---

## Suggested Structure

```text
ID

Statement

Purpose

Derived From

Related Concepts

Supported By

Notes
```

---

## Repository Placement

```
shared/
    requirements/
```

---

# Relationship to Existing Knowledge Objects

Current traceability:

```
Article

↓

Rule

↓

Process
```

Possible future traceability:

```
Article

↓

Rule

↓

Requirement

↓

Capability

↓

Process
```

This creates a clear bridge between legislation and implementation while keeping each knowledge object focused on a single purpose.

---

# Why Both?

Requirements and Capabilities answer different questions.

| Question | Knowledge Object |
|-----------|------------------|
| What does the law require? | Rule |
| What obligation follows? | Requirement |
| What must the organisation be able to do? | Capability |
| How is it performed? | Process |

These perspectives complement rather than duplicate one another.

---

# Naming

The English term **Capability** is well established within Enterprise Architecture (TOGAF, ArchiMate, and similar frameworks).

Possible Swedish translations include:

- Förmåga
- Verksamhetsförmåga
- Kapabilitet

Recommendation:

Use **Capability** as the repository object name.

It is internationally recognised and aligns with common architecture terminology.

When Swedish terminology is needed, **Verksamhetsförmåga** is probably the most accurate translation.

---

# Scope

Requirements and Capabilities should remain intentionally lightweight.

They should not become:

- business process documentation
- software specifications
- solution designs
- user manuals

Their purpose is to make the transition from legislation to implementation explicit while preserving the repository's legal focus.

---

# Recommendation

The current architecture should remain unchanged.

Requirements and Capabilities should be introduced only if there is a clear implementation perspective that benefits from them.

If introduced, they should be treated as complementary knowledge objects alongside:

- Articles
- Rules
- Concepts
- Processes
- Diagrams
- Interpretations
- Open Questions

rather than replacing or restructuring any existing part of the repository.

This preserves the repository's simplicity while significantly increasing its usefulness for business analysts, enterprise architects, solution architects, and implementation teams.