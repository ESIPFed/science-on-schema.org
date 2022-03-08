# Provide funding using the inverse of fundedItem with @reverse

Discussion: https://github.com/ESIPFed/science-on-schema.org/issues/109

## Status ##

__Accepted__

## Decision ##

Provide funding information about one or more grants through the `schema:MonetaryGrant`, linking it to `schema:Dataset` using the `schema:funding` property that can now be used from a schema:CreativeWork.

## Context ##

Before the `schema:funding` property existed, the `schema:MonetaryGrant` could only be linked to started from a `Dataset` by using the  JSON-LD `@reverse` keyword on the `Grant` property called `fundedItem`. `schema.org` has now created a `funding` property and defined it as the `inverseOf` the `fundedItem`. See https://github.com/schemaorg/schemaorg/issues/3056.

## Consequences ##

- With the `funding` property accepted into the core schema.org vocabulary, there are no consequences to no longer using the JSON-LD `@reverse` keyword.
