# ESIP Summer Meeting 2022

## Agenda

1. [Intro to Schema.org](#intro)
2. [Walkthrough - Build a basic schema.org entry (goal: it's not complicated)](#walkthrough-basic)
3. [Walkthrough - 2nd pass - improving the record](#walkthrough-improve)
4. [Wrap-up (not hands-on) Extend it with more complicated stuff](#advanced-techniques)

<a name="intro"></a>
### Intro to Schema.org

1. What is Schema.org?
2. What is actionable content?
3. Science-on-schema.org guidelines

<a name="walkthrough-basic"></a>
### Walkthrough - Basic Dataset

1. Context (basic) - explain downloading the schema file to define all the terms
2. Basic Fields (title, description, isAccess….)
3. Keywords (lesson - strings)
4. License (lesson - CC BY 0)
5. Identifiers (lesson - simple - good & better)
    b. SameAs (same dataset in different locations)
6. Publisher - single publisher
7. Authors / Contributors - (1 author; 1 contributor)
8. Space/Time - (simple - WKT correctly)

<a name="walkthrough-improve"></a>
### Walkthrough - Improving the Dataset
1. Keywords (lesson - DefinedTerm)
2. License (lesson - expressivity of RDF)
3. Identifiers - (lesson - Identifiers.org - best)
4. Publisher/Provider (lesson - using `@id`; specifying a different org - reuse of a dataset)
5. Authors / Contributors - (lesson - `@list`; more structured name fields for improved searching)
6. Funding & Awards
7. Data Distributions
8. Metadata Records
9. Checksums
10. Validate - SHACL Playground: https://shacl-playground.zazuko.com/ 

<a name="advanced-techniques"></a>
### Advanced Techniques

1. Variables (using external vocabs)
2. Provenance (extending the context)
3. Geologic Time
