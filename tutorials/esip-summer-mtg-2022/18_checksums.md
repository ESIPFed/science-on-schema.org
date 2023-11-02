# 18. Checksums for Data Files and Metadata Records


#### Lesson
> - Using external vocabularies within schema.org markup

**Guidelines:** 
[Checksums](/guides/Dataset.md#checksum)

**Source:**
[Line 70-92](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt#L70-L92)

> Abbreviated list of files from the source data for brevity. 
> The same concepts apply to all files

```
files:
  ...
metadata:
  - 
    url: "https://darchive.mblwhoilibrary.org/bitstream/1912/28977/4/NOAA_ISO19115-2.xml"
    bytesize: 64855
    mimetype: "application/xml"
    format: "http://www.isotc211.org/2005/gmd-noaa"
    md5: "77584383325794d3d9b7be42024687f6"
```

### Using External Vocabularies

- Schema.org Vocabulary doesn't have properties to describe checksums in detail
- The [SPDX vocabulary](https://spdx.org/rdf/terms/) `https://spdx.org/rdf/terms/` has terms describing checksum values and algorithms
- To use an external vocabulary, add its URI and a prefix to the `@context`
    1. Make `@context` an array
    2. Include a new JSON object with the prefix as a property and the URI of the vocabulary as the proeprty's value. 

<pre>
{
  "@context": [
    "https://schema.org/",
    <strong>{
      "spdx": "http://spdx.org/rdf/terms#"
    }</strong>
  ]
}
</pre>

### Using SPDX Checksum class and properties

- [`spdx:Checksum`](https://spdx.org/rdf/terms/#d4e1930)
    - [`spdx:checksumValue`](https://spdx.org/rdf/terms/#d4e1111)
    - [`spdx:algorithm`](https://spdx.org/rdf/terms/#d4e52) >> [`spdx:ChecksumAlgorithm`](https://spdx.org/rdf/terms/#d4e1968)
    
#### Specifying the `spdx:checksumValue`

<pre>
{
  "@context": [
    "https://schema.org/",
    {
      "spdx": "http://spdx.org/rdf/terms#"
    }
  ],
  "subjectOf": { 
    "@type": "DataDownload",
    "contentURL":"[https://example.com/metadata/eml-metadata.xml](https://darchive.mblwhoilibrary.org/bitstream/1912/28977/4/NOAA_ISO19115-2.xml)",
    "encodingFormat": ["application/xml", "http://www.isotc211.org/2005/gmd-noaa"],
    "contentSize": "64855 bytes",
    <strong>"spdx:checksum": {
      {
          "@type": "spdx:Checksum",
          "spdx:checksumValue": "77584383325794d3d9b7be42024687f6",
      }
    }</strong>
  }
}
</pre>

#### Specifying the `spdx:algorithm`

- The values of `spdx:algorithm` needs to be of type `spdx:ChecksumAlgorithm`. 
- SPDX gives us URIs that we can reuse for many common checksum algorithms.
- Using a URI form an external vocabulary requires that we use a JSON-LD object with an `@id` property for the URI

| Algorithm Type | SPDX ChecksumAlgorithm URI |
| -- | -- |
| MD2 | [`spdx:checksumAlgorithm_md2`](https://spdx.org/rdf/terms/#d4e3691) |
| MD4 | [`spdx:checksumAlgorithm_md4`](https://spdx.org/rdf/terms/#d4e3704) |
| MD5 | [`spdx:checksumAlgorithm_md5`](https://spdx.org/rdf/terms/#d4e3717) |
| MD6 | [`spdx:checksumAlgorithm_md6`](https://spdx.org/rdf/terms/#d4e3731) |
| SHA-1 | [`spdx:checksumAlgorithm_sha1`](https://spdx.org/rdf/terms/#d4e3744) |
| SHA224 | [`spdx:checksumAlgorithm_sha224`](https://spdx.org/rdf/terms/#d4e3757) |
| SHA256 | [`spdx:checksumAlgorithm_sha256`](https://spdx.org/rdf/terms/#d4e3771) |
| SHA384 | [`spdx:checksumAlgorithm_sha384`](https://spdx.org/rdf/terms/#d4e3784) |
| SHA512 | [`spdx:checksumAlgorithm_sha512`](https://spdx.org/rdf/terms/#d4e3797) |

<pre>
{
  "@context": [
    "https://schema.org/",
    {
      "spdx": "http://spdx.org/rdf/terms#"
    }
  ],
  "subjectOf": { 
    "@type": "DataDownload",
    "contentURL":"[https://example.com/metadata/eml-metadata.xml](https://darchive.mblwhoilibrary.org/bitstream/1912/28977/4/NOAA_ISO19115-2.xml)",
    "encodingFormat": ["application/xml", "http://www.isotc211.org/2005/gmd-noaa"],
    "contentSize": "64855 bytes",
    "spdx:checksum": {
      {
        "@type": "spdx:Checksum",
        "spdx:checksumValue": "77584383325794d3d9b7be42024687f6",
        <strong>"spdx:checksumAlgorithm": {
          "@id": "spdx:checksumAlgorithm_md5"
        }</strong>
      }
    }
  }
}
</pre>

### Updated Markup - Metadata Records

<pre>
{
  "@context": "https://schema.org/",
  <strong>"@id": "https://www.bco-dmo.org/dataset/775849",</strong>
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
  "variableMeasured": [
    {
      "@type": "PropertyValue",
      "name": "ISO_DateTime_UTC",
      "description": "Date time time of cast following ISO 8601 convention in UTC",
      "propertyID": "http://vocab.nerc.ac.uk/collection/P01/current/DTUT8601/",
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
      "unitText": "Celsius (C)",
      "unitCode": "https://qudt.org/vocab/unit/DEG_C"
    }
  ],
  "subjectOf": { 
    "@type": "DataDownload",
    "contentURL":"[https://example.com/metadata/eml-metadata.xml](https://darchive.mblwhoilibrary.org/bitstream/1912/28977/4/NOAA_ISO19115-2.xml)",
    "encodingFormat": ["application/xml", "http://www.isotc211.org/2005/gmd-noaa"],
    "contentSize": "64855 bytes",
    "about": { "@id": "https://www.bco-dmo.org/dataset/775849" },
    "dateModified": "2022-07-18T20:44:15Z",
    <strong>"spdx:checksum": {
      {
        "@type": "spdx:Checksum",
        "spdx:checksumValue": "77584383325794d3d9b7be42024687f6",
        "spdx:checksumAlgorithm": {
          "@id": "spdx:checksumAlgorithm_md5"
        }
      }
    }</strong>
  }
} 
</pre>

<hr/>

[Advanced Techniques >>](advanced-techniques.md)

<hr/>

### Resources
- **Source:** [ProteOMZ nitrous oxide data](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt) (example metadata)
- **Testing:** [Google Rich Results Tool](https://search.google.com/test/rich-results)
