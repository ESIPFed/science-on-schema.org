# Basic Dataset

**Source:** [ProteOMZ nitrous oxide data](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt) (example metadata)

**Testing:** [Google Rich Results Tool](https://search.google.com/test/rich-results)

## 5. Authors / Contributors

**Guidelines:** 
[Identifier](/guides/Dataset.md#roles-of-people)

**Source:**
[Lines L27-L34](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt#L27-L34)

#### Authors

```
{
  "@context": "https://schema.org/",
  "creator": {
    "@list":[
      {
        "@type": "Person",
        "name": "Alyson E. Santoro"
      },
      {
        "@type": "Person",
        "name": "Sarah Marie Laperriere"
      }
    ]
  }
}
```

#### Contributors

<pre>
{
  "@context": "https://schema.org/",
  <strong>"contributor":</strong> {
    "@list":[
      {
        "@type": "Person",
        "name": "Makoto Saito"
      }
    ]
  }
}
</pre>

##### Adding ORCiDs to People

- Re-use the [Identifier pattern](03_identifiers.md) from Section #3
- Identifiers.org defines ORCiD: `https://registry.identifiers.org/registry/orcid`
- 
<pre>
{
  "@context": "https://schema.org/",
  "creator": {
    "@list":[
      {
        "@type": "Person",
        "name": "Alyson E. Santoro",
        <strong>"identifier": {
          "@id": "https://orcid.org/0000-0003-2503-8219",
          "@type": "PropertyValue",
          "propertyID": "https://registry.identifiers.org/registry/orcid",
          "url": "https://orcid.org/0000-0003-2503-8219",
          "value": "orcid:0000-0003-2503-8219"
        }</strong>
      },
      {
        "@type": "Person",
        "name": "Sarah Marie Laperriere",
        <strong>"identifier": {
          "@id": "https://orcid.org/0000-0003-4691-8741",
          "@type": "PropertyValue",
          "propertyID": "https://registry.identifiers.org/registry/orcid",
          "url": "https://orcid.org/0000-0003-4691-8741",
          "value": "orcid:0000-0003-4691-8741"
        }</strong>
      }
    ]
  },
  "contributor": {
    "@list":[
      {
        "@type": "Person",
        "name": "Makoto Saito",
        <strong>"identifier": {
          "@id": "https://orcid.org/0000-0001-6040-9295",
          "@type": "PropertyValue",
          "propertyID": "https://registry.identifiers.org/registry/orcid",
          "url": "https://orcid.org/0000-0001-6040-9295",
          "value": "orcid:0000-0001-6040-9295"
        }</strong>
      }
    ]
  }
}
</pre>

##### Breaking down people names

<pre>
{
  "@context": "https://schema.org/",
  "creator": {
    "@list":[
      {
        "@type": "Person",
        "name": "Alyson E. Santoro",
        <strong>"givenName": "Alyson",
        "familyName": "Santoro",</strong>
      }
    ]
  }
}
</pre>

### Updated Markup - Authors / Contributors

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
  <strong>"creator": {
    "@list":[
      {
        "@type": "Person",
        "name": "Alyson E. Santoro",
        "givenName": "Alyson",
        "familyName": "Santoro",
        "identifier": {
          "@id": "https://orcid.org/0000-0003-2503-8219",
          "@type": "PropertyValue",
          "propertyID": "https://registry.identifiers.org/registry/orcid",
          "url": "https://orcid.org/0000-0003-2503-8219",
          "value": "orcid:0000-0003-2503-8219"
        }
      },
      {
        "@type": "Person",
        "name": "Sarah Marie Laperriere",
        "givenName": "Sarah Marie",
        "familyName": "Laperriere",
        "identifier": {
          "@id": "https://orcid.org/0000-0003-4691-8741",
          "@type": "PropertyValue",
          "propertyID": "https://registry.identifiers.org/registry/orcid",
          "url": "https://orcid.org/0000-0003-4691-8741",
          "value": "orcid:0000-0003-4691-8741"
        }
      }
    ]
  },
  "contributor": {
    "@list":[
      {
        "@type": "Person",
        "name": "Makoto Saito",
        "givenName": "Makoto",
        "familyName": "Saito",
        "identifier": {
          "@id": "https://orcid.org/0000-0001-6040-9295",
          "@type": "PropertyValue",
          "propertyID": "https://registry.identifiers.org/registry/orcid",
          "url": "https://orcid.org/0000-0001-6040-9295",
          "value": "orcid:0000-0001-6040-9295"
        }
      }
    ]
  }</strong>
}
</pre>

[Section #6: Files >>](06_Files.md)
