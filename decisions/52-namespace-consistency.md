# Namespace Consistency for http://schema.org/

Discussion:
  - https://github.com/ESIPFed/science-on-schema.org/issues/52
  - https://github.com/ESIPFed/science-on-schema.org/issues/151

## Status ##
_Pick one of:_ Proposed, Accepted, Rejected, Deprecated, Superseded

Accepted

## Decision ##
We recommend that the namespace URI for the schema.org vocabulary be consistently set to the value `http://schema.org/`.

## Context ##
While the schema.org vocabulary is resolvable at both the original http address and the newer `https` address, changing the namespace to https references would also effectively change the namespace of the terms to a new namespace. While schema.org maintainers have clarified that both namespaces have been actively recommended for 5 years, and are considered synonomous,
the official context file that is retrieved from both `https://schema.org/` and `http://schema.org` define the namespace URI for the vocabulary as `http://schema.org/`. See the discussion and pointers in issue #151. For consistency, we recommend using a `http`-based namespace so that term URIs stay comparable over time, but also that harvesters consumers treat the http and https namespaced terms as logical synonyms. In some cases, importing the aligment axioms from schema.org-provided files (like OWL files) may provide sufficient rules for determining that equivalence.

One consistent mechanism to use the `http`-based namespace is to load the context from the context file maintained by schema.org. This can be accomplished using:

```json
{
    "@context": "https://schema.org/",
    "@type": "Dataset",
    "name": "Example dataset title"
}
```

While the context is loaded from the `https` address above, the resulting JSON-LD fragment uses the `http` namespace when it is expanded:

```json
[
  {
    "@type": [
      "http://schema.org/Dataset"
    ],
    "http://schema.org/name": [
      {
        "@value": "Example dataset title"
      }
    ]
  }
]
```

In addition to the `http`, we also need the trailing slash to be consistently applied, so that term URIs that are constructed become properly expanded. For example, `schema:Dataset` should expand to `http://schema.org/Dataset`. Without the trailing slash, it would expand to the incorrect `http://schema.orgDataset`.

## Consequences ##

- Providers should modify documents to use the https-based URI with a trailing slash for retrieving the context document
- The actual namespace used is precisely `http://schema.org/`
- Harvesters should treat the http and https-based namespaces as equivalent
