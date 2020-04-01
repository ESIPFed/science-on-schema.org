# schema.org/additionalType vs. re-using '@type' #

Discussion: https://github.com/ESIPFed/science-on-schema.org/issues/74 

## Status ##
*Adopted*

## Decision ##
We will recommend the use of '@type' (or rdf:type) when typing resources to classes outside of the core schema.org vocabulary.

## Context ##
* schema.org/additionalType does not provide the semantics that using '@type' or rdf:type does. '@type' or rdf:type provides proper RDF typing making RDF querying across these data easier withot having to mix checking for rdf:type and schema/additionalType without forcing the harvester to pre-process schema.org/additionalType.
* schema.org/additionalType is defined as a URL and not an RDF resource making the use of prefixed URIs problematic. Prefixed URIs in schema.org/additionalType will not expand to the full URI when harvested. This might be problematic where different publishers use different prefixes ( e.g. a typical issue when prefixing Dublin Core, Dublin Core Terms, DCAT with 'dc', 'dct', 'dcterms' getting mixed usage across publishers)


## Consequences ##

* Google Structured Data Testing Tool throws errors for anything that isn't using the schema.org vocabulary, and this may cause questions for some schema.org publishers
* Benefit to using proper typing makes querying easier by not having to check two fields each time a class type is mentioned in a query.
