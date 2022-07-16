# Basic Dataset

**Source:** [ProteOMZ nitrous oxide data](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt) (example metadata)

**Testing:** [Google Rich Results Tool](https://search.google.com/test/rich-results)

## 3. Identifiers

**Guidelines:** 
[Identifier](/guides/Dataset.md#identifier)

**Source:**
[Line 5](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt#L5)

#### Identifiers as Text - Good

```
{
  "@context": "https://schema.org/",
  "identifier": "doi:10.26008/1912/bco-dmo.775849.1"
}
```

#### Identifiers as URL - Better

```
{
  "@context": "https://schema.org/",
  "identifier": "https://doi.org/10.26008/1912/bco-dmo.775849.1"
}
```

#### Using Identifiers.org - Best

https://registry.identifiers.org/registry

DOI: https://registry.identifiers.org/registry/doi

```
{
  "@context": "https://schema.org/",
  "identifier": {
    "@id": "https://doi.org/10.26008/1912/bco-dmo.775849.1",
    "@type": "PropertyValue",
    "propertyID": "https://registry.identifiers.org/registry/doi",
    "value": "doi:10.26008/1912/bco-dmo.775849.1",
    "url": "https://doi.org/10.26008/1912/bco-dmo.775849.1"
  }
}
```

##### Other Common Identifiers.org Types

- ARK: https://registry.identifiers.org/registry/ark
- PubMed: https://registry.identifiers.org/registry/pubmed
- PaleoDB: https://registry.identifiers.org/registry/paleodb
- Protein Data Bank: https://registry.identifiers.org/registry/pdb



### Updated Markup - Identifiers

<pre>
{
  "@context": "https://schema.org/",
  "@type": "Dataset",
  "name": "Nitrous oxide concentrations from the R/V Falkor expedition FK160115 in the Central Pacific from January to February 2016",
  "description": "Dissolved N2O concentrations from were measured in discrete samples on a research expedition to the Equatorial Pacific. Water samples were collected using a 24 bottle Niskin rosette equipped with a CTD. N₂O concentrations were measured using a headspace equilibration method and analyzed on a SRI Greenhouse Gas Monitoring Gas Chromatograph.",
  "url": "https://www.bco-dmo.org/dataset/775849",
  "version": "1",
  "isAccessibleForFree": "true",
  "dateCreated": "2019-08-22",
  "dateModified": "2019-08-22",
  "datePublished": "2022-06-08",
  "keywords": [
    "nitrous oxide", 
    "Central Pacific", 
    "headspace equilibration", 
    "SRI Greenhouse Gas Monitoring Gas Chromatograph",
    {
      "@type": "DefinedTerm",
      "name": "CTD",
      "inDefinedTermSet": "http://vocab.nerc.ac.uk/collection/L05/current/",
      "url": "http://vocab.nerc.ac.uk/collection/L05/current/130/"
    },
    {
      "@type": "DefinedTerm",
      "name": "CTD",
      "inDefinedTermSet": "http://vocab.nerc.ac.uk/collection/L05/current/",
      "url": "http://vocab.nerc.ac.uk/collection/L05/current/LAB02/",
      "termCode": "LAB02"
    }
  ],
  <strong>"identifier": {
    "@id": "https://doi.org/10.26008/1912/bco-dmo.775849.1",
    "@type": "PropertyValue",
    "propertyID": "https://registry.identifiers.org/registry/doi",
    "value": "doi:10.26008/1912/bco-dmo.775849.1",
    "url": "https://doi.org/10.26008/1912/bco-dmo.775849.1"
  }</strong>
}
</pre>

[Section #4: Publisher/Provider >>](04_publisher-provider.md)
