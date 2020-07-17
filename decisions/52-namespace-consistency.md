# Namespace Consistency for http://schema.org/

Discussion: https://github.com/ESIPFed/science-on-schema.org/issues/52

## Status ##
_Pick one of:_ Proposed, Accepted, Rejected, Deprecated, Superseded

Proposed

## Decision ##
We recommend that the namespace URI for the schema.org vocabulary be consistently set to the value `http://schema.org/`, typically in the `@vocab` property of the JSON-LD file.

## Context ##
While the schema.org vocabulary is resolvable at both the original http address and the newer `https` address, changing the @vocab references would also effectively change the namespace of the terms to a new namespace. Thus, for consistency, we need to maintain the original `http`-based namespace so that term URIs stay comparable over time.

In addition to the `http`, we also need the trailing slash to be consistently applied, so that term URIs that are constructed become properly expanded. For example, `schema:Dataset` should expand to `http://schema.org/Dataset`. Without the trailing slash, it would expand to the incorrect `http://schema.orgDataset`.

## Consequences ##
TODO: What becomes easier or more difficult to do because of this change?

TODO: discuss how to handle resolution at both http and https addresses while still keeping the http namespace fixed

TODO: Discuss consequences for reasoning and comparison of using different URIs
