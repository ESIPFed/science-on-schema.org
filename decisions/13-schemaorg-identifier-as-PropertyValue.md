# schema.org/identifier as schema.org/PropertyValue over Text/URL #

Discussion: https://github.com/ESIPFed/science-on-schema.org/issues/13

## Status ##
_Proposed_

## Decision ##
We will encourage the use of [schema.org/PropertyValue](https://schema.org/PropertyValue) when describing persistent identifiers (PIDs).

## Context ##
* PropertyValue is more expressive than the Text or URL, and this is helpful when trying to query across data publishers for the same PID. 
For example, while schema.org/identifier does force the [value to be a resource](https://json-ld.org/playground/#startTab=tab-nquads&json-ld=%7B%22%40context%22%3A%22http%3A%2F%2Fschema.org%2F%22%2C%22%40type%22%3A%22Dataset%22%2C%22name%22%3A%22Test%20Dataset%22%2C%22identifier%22%3A%22https%3A%2F%2Fdoi.org%2F10.1234%2F56789%22%7D&frame=%7B%7D&context=%7B%7D) (see N-Quads tab at the JSON-LD Playground), there isn't consistent use of the same resource URI to define a PID. For example, https://doi.org/<value>, http://dx.doi.org/<value>, http://doi.org/<value> are all valid RDF Resource URIs for the same DOI. But in RDF linked data space, these resource URIs are different making querying for linkages and relationships problematic. To encourage this approach would mean that harvesters would need to recognize PIDs and normalize those PIDs for appropriate, effective querying.
Using a PropertyValue enables publishers to express the identifier scheme and the value separately while also expressing them together if desired.
* The DataCite Metadata kernel splits the scheme from the identifier when referring to a PID.

* See: [DataCite Ontology](https://sparontologies.github.io/datacite/current/datacite.html)
* See: https://blog.datacite.org/dc2ap-and-dc2rdf-webinar/


## Consequences ##
* Without the identifier scheme, it is difficult to accurately query how identifiers are used and linked across repositories and resources.

Example:

<pre>
{ 
  "@context": "https://schema.org/",
  "@type": "Dataset",
  "name": "Example Dataset",
  "identifier": "doi:10.1234/56789"
}
</pre>
is the same as
<pre>
{ 
  "@context": "https://schema.org/",
  "@type": "Dataset",
  "name": "Example Dataset",
  "identifier": "https://doi.org/10.1234/56789"
}
</pre>
is the same as
<pre>
{ 
  "@context": {
    "@vocab": "https://schema.org/",
    "datacite": "http://purl.org/spar/datacite/"
  },
  "@type": "Dataset",
  "name": "Example Dataset",
  "identifier": {
    "@id": "https://doi.org/10.1234/56789",
    "@type": ["PropertyValue", "datacite:ResourceIdentifier"],
    "datacite:usesIdentifierScheme": { "@id": "datacite:doi" },
    "value": "10.1234/56789",
    "propertyID": "DOI",
    "url": "https://doi.org/10.1234/56789"
  }
}
</pre>

Given a DOI, "10.1234/56789", a SPARQL query that resolves all three as the same is difficult w/o pre-processing on harvest.
