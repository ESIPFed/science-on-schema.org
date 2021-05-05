# Provide funding using the inverse of fundedItem with @reverse

Discussion: https://github.com/ESIPFed/science-on-schema.org/issues/109

## Status ##

__Proposed__

## Decision ##

Provide funding information about one or more grants through the `schema:MonetaryGrant, linking it to `schema:Dataset` using the JSON-LD `@reverse` keyword on the `schema:fundedItem` property.`

## Context ##

`schema:MonetaryGrant` privides the structured information we need, and is related to the items that a grant funds via the `schema:fundedItem` property. Howeverr, the inverse of that property (something like `fundedBy`) does not exist, and so its hard to make the linkage from Dataset to MonetaryGrant. The JSON-LD `@reverse` property enables one to reference an inverse property without naming it, thereby enabling us to point directly from Dataset (which we are describing) to the MonetaryGrant that it is fundedBy. schema.org is considering a `funding` or `fundedBy` property in https://github.com/schemaorg/schemaorg/pull/2618, but it does not yet exist. In the future, if such a prperty were defined, then people could easily switch to using it.

## Consequences ##

- `@reverse` allows linking directly from Dataset to Monetary grant
- Compliant JSON-LD parsers correctly interpret these and convert them to the correct set of RDF triples
- The Google tools do not at this time properly interpret @reverse, which needs to be reported
- Using `@reverse` is a little complex, but not as complex as the alternative, which is to build a `@graph` to hold the nodes

