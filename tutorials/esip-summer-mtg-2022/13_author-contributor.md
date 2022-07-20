# 13. Improving Authors / Contributors 

#### Lesson
> - Re-using the identifier "pattern"
> - Using schema.org website to find additional properties


**Guidelines:** 
[Identifier](/guides/Dataset.md#roles-of-people)

**Source:**
[Lines L27-L34](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt#L27-L34)

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
  },
  "contributor": {
    "@list":[
      {
        "@type": "Person",
        "name": "Makoto Saito"
      }
    ]
  }
}
```

### Adding ORCiDs to People

- Re-use the [Identifier pattern](03_identifiers.md) from Section #3
- Identifiers.org defines ORCiD: `https://registry.identifiers.org/registry/orcid`

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

### Improve search by person name 

> There are more fields defined at schema.org to improve descriptions of "things".

#### Schema.org Person

- [`Person`](https://schema.org/Person)
    - <strong>`familyName`
    - `givenName`</strong>
    - `additionalName`
    - `affiliation`
    -  and more ...

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

### Updated Markup - Author/Contributor

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
    "CTD profiler",
    "Gas Chromatograph",
    {
      "@type": "DefinedTerm",
      "name": "CTD",
      "url": "http://vocab.nerc.ac.uk/collection/L05/current/130/",
      "inDefinedTermSet": {
        "@id": "http://vocab.nerc.ac.uk/collection/L05/current/",
        "@type" : "DefinedTermSet",
        "name": "SeaDataNet device categories"
      }
    },
    {
      "@type": "DefinedTerm",
      "name": "gas chromatographs",
      "url": "http://vocab.nerc.ac.uk/collection/L05/current/LAB02/",
      "inDefinedTermSet": {
        "@id": "http://vocab.nerc.ac.uk/collection/L05/current/"
      },
      "termCode": "LAB02"
    }
  ],
  "license": ["https://spdx.org/licenses/CC-BY-4.0", "https://creativecommons.org/licenses/by/4.0/"],
  "identifier": {
    "@id": "https://doi.org/10.26008/1912/bco-dmo.775849.1",
    "@type": "PropertyValue",
    "propertyID": "https://registry.identifiers.org/registry/doi",
    "value": "doi:10.26008/1912/bco-dmo.775849.1",
    "url": "https://doi.org/10.26008/1912/bco-dmo.775849.1"
  },
  "sameAs": "https://doi.org/10.26008/1912/bco-dmo.775849.1",
  "publisher": {
    "@type": "Organization",
    "legalName": "Biological and Chemical Data Management Office",
    "url": "https://www.bco-dmo.org"
  },
  <strong>"creator": {
    "@list":[
      {
        "@type": "Person",
        "name": "Alyson E. Santoro",
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
        "identifier": {
          "@id": "https://orcid.org/0000-0001-6040-9295",
          "@type": "PropertyValue",
          "propertyID": "https://registry.identifiers.org/registry/orcid",
          "url": "https://orcid.org/0000-0001-6040-9295",
          "value": "orcid:0000-0001-6040-9295"
        }
      }
    ]
  },</strong>
  "temporalCoverage": "2016-01-17/2016-02-04",
  "spatialCoverage": {
    "@type": "Place",
    "geo": {
      "@type": "GeoShape",
      "polygon": "-10.563,139.8 17,139.8 17,156 -10.563,156 -10.563,139.8"
    },
    "additionalProperty": {
      "@type": "PropertyValue",
      "propertyID":"http://dbpedia.org/resource/Spatial_reference_system",
      "value": "http://www.w3.org/2003/01/geo/wgs84_pos#lat_long"
    }
  },
  "distribution": [
    {
      "@type": "DataDownload",
      "contentUrl": "https://darchive.mblwhoilibrary.org/bitstream/1912/28977/1/dataset-775849_proteomz-nitrous-oxide-data__v1.tsv",
      "encodingFormat": "text/tab-separated-values",
      "contentSize": "15077 bytes"
    }
  ]
}
</pre>

<hr/>

[Section #14: Adding a Provider >>](14_provider.md)

<hr/>

### Resources
- **Source:** [ProteOMZ nitrous oxide data](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt) (example metadata)
- **Testing:** [Google Rich Results Tool](https://search.google.com/test/rich-results)
