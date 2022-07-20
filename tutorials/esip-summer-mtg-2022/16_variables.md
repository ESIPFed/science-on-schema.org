# 16. Variables

#### Lesson
> - Describing variables in detail with `PropertyValue`
> - Using external vocabulary URIs to describe a variable with `propertyID`
> - Describing units with `PropertyValue`

**Guidelines:** 
[Variables](/guides/Dataset.md#variables)

**Source:**
[Line 93-155](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt#L93-L155)

> Abbreviated list of variables from the source data for brevity

```
parameters:
  - 
    name: "ISO_DateTime_UTC"
    description: "Date time time of cast following ISO 8601 convention in UTC"
    format: "YYYY-MM-DDTHH:MM:SS[.xx]Z"
    identifier:
      uri: "http://vocab.nerc.ac.uk/collection/P01/current/DTUT8601/"
  ...
  -  
    name: "cast"
    description: "CTD cast number"
  ...
  - 
    name: "temperature"
    description: "Temperature from CTD"
    identifier:
      name: "water temperature"
      uri: "http://vocab.nerc.ac.uk/collection/P01/current/TEMPP901/"
    units:
      name: "Celsius (C)"
      uri: "https://qudt.org/vocab/unit/DEG_C"
  ...
```

### Schema.org Variables

- [`variableMeasured`](https://schema.org/variableMeasured)
    - Text
    - PropertyValue

#### Variables as Text - Good

Similar to [Keywords in Section 3](03_keywords.md)

<pre>
{
  "@context": "https://schema.org/",
  <strong>"variableMeasured": [
    "ISO_DateTime_UTC", 
    "cast", 
    "temperature"
  ]</strong>
}
</pre>

#### Variables as PropertyValue - Better

<pre>
{
  "@context": "https://schema.org/",
  <strong>"variableMeasured": [
    {
      "@type": "PropertyValue",
      "name": "cast",
      "description": "CTD cast number"
    }</strong>
  ]
}
</pre>

#### Variables as PropertyValue w. propertyID - Best

<pre>
{
  "@context": "https://schema.org/",
  "variableMeasured": [
    {
      "@type": "PropertyValue",
      "name": "ISO_DateTime_UTC",
      "description": "Date time time of cast following ISO 8601 convention in UTC",
      <strong>"propertyID": "http://vocab.nerc.ac.uk/collection/P01/current/DTUT8601/",</strong>
    },
    {
      "@type": "PropertyValue",
      "name": "cast",
      "description": "CTD cast number"
    }
  ]
}
</pre>

### Variables with Units

#### Schema.org PropertyValue + Units

- `variableMeasured` >> [`PropertyValue`](https://schema.org/PropertyValue)
    - <strong>`unitText`</strong> - a unit description.
    - <strong>`unitCode`</strong> - Can be text or URL. We recommend a URI from a controlled vocabulary like [QUDT](https://www.qudt.org/2.1/catalog/qudt-catalog.html)
    - 
<pre>
{
  "@context": "https://schema.org/",
  "variableMeasured": [
    {
      "@type": "PropertyValue",
      "name": "temperature",
      "description": "Temperature from CTD",
      "propertyID": "http://vocab.nerc.ac.uk/collection/P01/current/TEMPP901/",
      <strong>"unitText": "Celsius (C)",
      "unitCode": "https://qudt.org/vocab/unit/DEG_C"</strong>
    }
  ]
}
</pre>

### Updated Markup - Variables

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
      "termCode": "LAB02",
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
  "provider": { "@id": "https://www.bco-dmo.org" },
  "creator": {
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
  },
  "funding": [
    {
      "@type": "MonetaryGrant",
      "name": "R/V Falkor 160115 SOI ProteOMZ Expedition",
      "url": "https://www.bco-dmo.org/award/685695",
      "funder": {
        "@type": "Organization",
        "name": "Schmidt Ocean Institute"
      }
    },
    {
      "@type": "MonetaryGrant",
      "name": "FG-2016-7129",
      "url": "https://www.bco-dmo.org/award/875341",
      "funder": {
        "@type": "Organization",
        "name": "Sloan Foundation",
        "identifier": {
          @id": "https://doi.org/10.13039/100000879",
          "@type": "PropertyValue",
          "propertyID": "https://registry.identifiers.org/registry/doi",
          "value": "doi:10.13039/100000879",
          "url": "https://doi.org/10.13039/100000879"
        }
      }
    }
  ],
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
  ],
  <strong>"variableMeasured": [
    {
      "@type": "PropertyValue",
      "name": "ISO_DateTime_UTC",
      "description": "Date time time of cast following ISO 8601 convention in UTC",
      <strong>"propertyID": "http://vocab.nerc.ac.uk/collection/P01/current/DTUT8601/",</strong>
    },
    {
      "@type": "PropertyValue",
      "name": "cast",
      "description": "CTD cast number"
    },
    {
      "@type": "PropertyValue",
      "name": "temperature",
      "description": "Temperature from CTD",
      "propertyID": "http://vocab.nerc.ac.uk/collection/P01/current/TEMPP901/",
      <strong>"unitText": "Celsius (C)",
      "unitCode": "https://qudt.org/vocab/unit/DEG_C"</strong>
    }
  ]</strong>
} 
</pre>

<hr/>

[Section #17: Metadata Records >>](17_metadata-records.md)

<hr/>

### Resources
- **Source:** [ProteOMZ nitrous oxide data](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt) (example metadata)
- **Testing:** [Google Rich Results Tool](https://search.google.com/test/rich-results)
