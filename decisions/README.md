# Lightweight Architecture Decision Records #

## Status ##
*Proposed*

## Context ##
*Lightweight Architecture Decision Records (ADRs)* are a technique for capturing important architectural decisions along with their context and consequences stored in a version control system for the benefit of future team members as well as for external oversight. Storing ADRs in version control systems are recommended as opposed to Wikis or a website so that they remain in sync with the code itself. 

* See: https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records
* See: https://github.com/joelparkerhenderson/architecture_decision_record

## Decision ##
When a design decision is made about how to implement schema.org properly, an ADR will be stored in this repository in the decisions directory. Discussion may happen across pull requests and Github Issues, but these will be boiled down to the essentials of the decision and its context to expedite onboarding of new members.

## Consequences ##

As views on certain topics change over time, it will be difficult without ADRs to reflect on the context for a decision as it changes with respect to the code. In the past, this meant wadin through Github issues that speider web off into different directions to related issues, but make if difficult to follow the progression of thought across a single idea.

------------

### Sections of an ADR: ###

* **Title**: short present tense imperative phrase, less than 50 characters, like a git commit message.

* **Status**: Proposed, Accepted, Rejected, Deprecated, Superseded, etc.

* **Context**: what is the issue that we're seeing that is motivating this decision or change.

* **Decision**: what is the change that we're actually proposing or doing.

* **Consequences**: what becomes easier or more difficult to do because of this change.
