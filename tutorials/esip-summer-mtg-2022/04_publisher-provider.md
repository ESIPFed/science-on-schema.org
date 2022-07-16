# Basic Dataset

**Source:** [ProteOMZ nitrous oxide data](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt) (example metadata)

**Testing:** [Google Rich Results Tool](https://search.google.com/test/rich-results)

## 4. Publisher & Provider

**Guidelines:** 
[Publisher / Provider](/guides/Dataset.md#publisher--provider)

**Source:**
[Line 39-41](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt#L39-L41)

#### Publisher

```
{
  "@context": "https://schema.org/",
  "publisher": {
    "@type": "Organization",
    "legalName": "Biological and Chemical Data Management Office",
    "name": "BCO-DMO",
    "sameAs": "http://www.re3data.org/repository/r3dxxxxxxxxx",
    "url": "[https://www.sample-data-repository.org](https://www.bco-dmo.org)"
  }
}
```
#### Provider

```
{
  "@context": "https://schema.org/",
  "provider": {
    "@type": "Organization",
    "legalName": "Biological and Chemical Data Management Office",
    "name": "BCO-DMO",
    "sameAs": "http://www.re3data.org/repository/r3dxxxxxxxxx",
    "url": "[https://www.sample-data-repository.org](https://www.bco-dmo.org)"
  }
}

```
##### Using '@id'

<pre>
{
  "@context": "https://schema.org/",
  "publisher": {
    <strong>"@id": "https://www.bco-dmo.org",</strong>
    "@type": "Organization",
    "legalName": "Biological and Chemical Data Management Office",
    "name": "BCO-DMO",
    "sameAs": "http://www.re3data.org/repository/r3dxxxxxxxxx",
    "url": "[https://www.sample-data-repository.org](https://www.bco-dmo.org)"
  },
  <strong>"provider": {
    "@id": "https://www.bco-dmo.org"
  }</strong>
}
</pre>

### Updated Markup - Publisher/Provider

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
 "identifier": {
    "@id": "https://doi.org/10.26008/1912/bco-dmo.775849.1",
    "@type": "PropertyValue",
    "propertyID": "https://registry.identifiers.org/registry/doi",
    "value": "doi:10.26008/1912/bco-dmo.775849.1",
    "url": "https://doi.org/10.26008/1912/bco-dmo.775849.1"
  },
  <strong>"publisher": {
    <strong>"@id": "https://www.bco-dmo.org",</strong>
    "@type": "Organization",
    "legalName": "Biological and Chemical Data Management Office",
    "name": "BCO-DMO",
    "sameAs": "http://www.re3data.org/repository/r3dxxxxxxxxx",
    "url": "[https://www.sample-data-repository.org](https://www.bco-dmo.org)"
  },
  "provider": {
    "@id": "https://www.bco-dmo.org"
  }</strong>
}
</pre>

[Section 5. Authors/Contributors >>](05_authors-contributors.md)
