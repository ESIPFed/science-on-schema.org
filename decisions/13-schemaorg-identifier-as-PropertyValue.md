# Represent persistent identifiers (schema:identifier) using schema:PropertyValue instead of Text or URL #

Discussion: https://github.com/ESIPFed/science-on-schema.org/issues/13

## Status ##
_Proposed_

## Decision ##
We will encourage the use of [schema.org/PropertyValue](https://schema.org/PropertyValue) when describing persistent identifiers (PIDs).

## Context ##
* PropertyValue is more expressive than the Text or URL, and this is helpful when trying to query across data publishers for the same PID. 
For example, while schema.org/identifier does force the [value to be a resource](https://json-ld.org/playground/#startTab=tab-nquads&json-ld=%7B%22%40context%22%3A%22http%3A%2F%2Fschema.org%2F%22%2C%22%40type%22%3A%22Dataset%22%2C%22name%22%3A%22Test%20Dataset%22%2C%22identifier%22%3A%22https%3A%2F%2Fdoi.org%2F10.1234%2F56789%22%7D&frame=%7B%7D&context=%7B%7D) (see N-Quads tab at the JSON-LD Playground), there isn't consistent use of the same resource URI to define a PID. For example, https://doi.org/<value>, http://dx.doi.org/<value>, http://doi.org/<value> are all valid RDF Resource URIs for the same DOI. But in RDF linked data space, these resource URIs are different making querying for linkages and relationships problematic. To encourage this approach would mean that harvesters would need to recognize PIDs and normalize those PIDs for appropriate, effective querying.
Using a PropertyValue enables publishers to express the identifier scheme and the value separately while also expressing them together if desired.

### 1) We recognize that most identifiers have common properties ###

- a **value**, 
- a **domain** or **scheme** (in which the value is guaranteed to be unique),
- (optionally) a **resolvable URL** (where the thing being identified can be found),
- (optionally) a **domain prefix** (a token string of characters succeeded by a colon ':' that represents the domain or scheme).

### 2) The identifiers.org Registry is a comprehensive and good resource for disambiguating the identifier scheme ###

With almost 700 different registered URIs, identifiers.org does a great job of explaining the values of the fields above. Some examples:

- DOI: https://registry.identifiers.org/registry/doi
- ARK: https://registry.identifiers.org/registry/ark
- PubMed: https://registry.identifiers.org/registry/pubmed
- PaleoDB: https://registry.identifiers.org/registry/paleodb
- Protein Data Bank: https://registry.identifiers.org/registry/pdb

### 3) These map to `schema:PropertyValue` fields as:

- **value** - `schema:value` as the identifier value, 
- **scheme** - `schema:propertyID` as a URI for the identifier scheme,
- **resolvable URL** - `schema:url` as a resolvable url for that identifier,
- no good standalone field for the **prefix**.

### 4) Include the **prefix** of an identifier in `schema:value` to help disambiguate the identifier in a single field. ###

2a) Most researchers recognize identifiers that are preceeded by its well known prefix
- a DOI of value `10.5066/F7VX0DMQ` is more readily recognized as `doi:10.5066/F7VX0DMQ`. 

2b) URLs do not do a good job of uniquely disambiguating an identifier - multiple working variants from the resolving service, and publishers may mistakenly use the resulting redirect URL instead of the desired resolving URL.

### Example ###

<pre>
"identifier": [
      {
        "@type": "PropertyValue",
        "propertyID": "https://registry.identifiers.org/registry/ark",
        "name": "ARK: 13030/c7833mx7t",
        "value": "ark:13030/c7833mx7t",
        "url": "https://n2t.net/ark:13030/c7833mx7t"
      },{
        "@type": "PropertyValue",
        "propertyID": "https://registry.identifiers.org/registry/pubmed",
        "name": "Pubmed ID #16333295",
        "value": "pubmed:16333295",
        "url": "http://www.ncbi.nlm.nih.gov/pubmed/16333295"
      },
     {
        "@type": "PropertyValue",
        "propertyID": "https://registry.identifiers.org/registry/paleodb",
        "name": "Paleo Database ID #83088",
        "value": "paleodb:83088",
        "url": "https://identifiers.org/paleodb:83088"
      },
     {
        "@type": "PropertyValue",
        "propertyID": "https://registry.identifiers.org/registry/pdb",
        "name": "Protein Data Bank 2gc4",
        "value": "pdb:2gc4",
        "url": "https://identifiers.org/pdb:2gc4"
      }
]
</pre>

## Consequences ##
* Without the identifier scheme, it is difficult to accurately query how identifiers are used and linked across repositories and resources.

