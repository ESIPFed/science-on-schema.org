# 12. Identifiers

#### Lesson
> - Introducing Identifiers.org Registry
> - Using the `PropertyValue` type

**Guidelines:** 
[Identifier](/guides/Dataset.md#identifier)

**Source:**
[Line 5](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt#L5)

```
doi: "10.26008/1912/bco-dmo.775849.1"
```

### Using Identifiers.org - Best

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

#### Other Common Identifiers.org Types

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
  <strong>"identifier": {
    "@id": "https://doi.org/10.26008/1912/bco-dmo.775849.1",
    "@type": "PropertyValue",
    "propertyID": "https://registry.identifiers.org/registry/doi",
    "value": "doi:10.26008/1912/bco-dmo.775849.1",
    "url": "https://doi.org/10.26008/1912/bco-dmo.775849.1"
  },</strong>
  "sameAs": "https://doi.org/10.26008/1912/bco-dmo.775849.1",
  "publisher": {
    "@type": "Organization",
    "legalName": "Biological and Chemical Data Management Office",
    "url": "https://www.bco-dmo.org"
  },
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
  },
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

[Section #13: Authors/Contributor w. ORCiD >>](13_author-contributor.md)

<hr/>

### Resources
- **Source:** [ProteOMZ nitrous oxide data](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt) (example metadata)
- **Testing:** [Google Rich Results Tool](https://search.google.com/test/rich-results)
