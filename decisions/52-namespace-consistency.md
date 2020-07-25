# Namespace Consistency for http://schema.org/

Discussion: https://github.com/ESIPFed/science-on-schema.org/issues/52

## Status ##
_Pick one of:_ Proposed, Accepted, Rejected, Deprecated, Superseded

Accepted

## Decision ##
We recommend that the namespace URI for the schema.org vocabulary be consistently set to the value `https://schema.org/`, typically in the `@vocab` property of the JSON-LD file.

## Context ##
While the schema.org vocabulary is resolvable at both the original http address and the newer `https` address, changing the @vocab references would also effectively change the namespace of the terms to a new namespace. However, schema.org maintainers have clarified that both namespaces have been actively recommended for 5 years, and are considered synonomous. See the discussion and pointers in issue #52. Thus, for consistency, we recommend using a `https`-based namespace so that term URIs stay comparable over time, but also that harvesters consumers treat the http and https namespaced terms as logical synonyms. In some cases, importing the aligment axioms from schema.org-provided files (like OWL files) may provide sufficient rules for determining that equivalence.

In addition to the `http`, we also need the trailing slash to be consistently applied, so that term URIs that are constructed become properly expanded. For example, `schema:Dataset` should expand to `https://schema.org/Dataset`. Without the trailing slash, it would expand to the incorrect `https://schema.orgDataset`.

## Consequences ##

- Providers should modify documents to use the https-based URI with a trailing slash
- Consumers need to treat the http and https-based namespaces as equivalent
