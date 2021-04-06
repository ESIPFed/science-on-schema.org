# Use PROV-O, isBasedOn, and ProvONE for provenance information

Discussion: https://github.com/ESIPFed/science-on-schema.org/issues/72

## Status ##

__Accepted__

## Decision ##

Provide provenance information about data processing workflows, data derivation relationships, and versioning information using PROV-O, ProvONE, and schema.org predicates.

- [`schema:isBasedOn`](https://schema.org/isBasedOn).
- `PROV-O` namespace (http://www.w3.org/ns/prov#) predicates, including `prov:wasDerivedFrom`, `prov:wasRevisionOf`, `prov:used`, and `prov:generatedBy`
- [ProvONE](https://purl.dataone.org/provone-v1-dev), which specializes PROV for reproducible software workflows, can be used to specify `provone:Program` and `provone:Execution` that create derived products

## Context ##
High level relationships that link datasets based on their processing workflows and versioning relationships are critical for consumers to differentiate versions of a [schema:Dataset](https://schema.org/Dataset), to clarify when a dataset is derived from one or more source Datasets, and to specify linkages to the software that created these derived Datasets. The [PROV-O](https://www.w3.org/TR/prov-o/) recommendation provides the widely-adopted vocabulary for representing this type of information, and should be used within Dataset descriptions, as most relevant properties are missing from schema.org. The main exception is [`schema:isBasedOn`](https://schema.org/isBasedOn), which provides a predicate for indicating that a Dataset was derived from one or more source Datasets. Producers and consumers should interpret `schema:isBasedOn` to be an equivalent property to `prov:wasDerivedFrom` (in the `owl:equivalentProperty` sense). Either is acceptable for representing derivation relationships, but there is utility in expressing the relationship with both predicates. When other `PROV` predicates are used, it is preferred to use `prov:wasDerivedFrom`. Workflow relationships among processing software and both source and derived data files shoudl be described with `prov:used` and `prov:generatedBy` predicates, and by using workflow classes from ProvONE.

## Consequences ##

- Versioning and derivation relationships will be clearer
- Aggregators and search systems should use these properties to cluster versions of Datasets, and to provide bi-directional linkages to derived data products
- Software processing and other processing relationships can be provided via linkages to `prov:Activity`, and particularly `provone:Execution` and `provone:Program` for specifying software processes that create derived products. However, these relationships get complicated as multi-step software workflows can be complex. Providing these relationships is useful when researchers strive to describe reproducible research through software workflows.
