# 11. Keywords from a Controlled Vocabulary

#### Lesson
> - Multiple array values with different types
> - Introducing the `DefinedTerm` type
> - Introducing reuse of objects with `@id`

**Guidelines:** 
[Keywords](/guides/Dataset.md#keywords)

**Source:**
[Lines 9-26](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt#L9-L26)

```
keywords:
  - name: "nitrous oxide"
  - name: "Central Pacific"
  - name: "headspace equilibration"
  - name: "SRI Greenhouse Gas Monitoring Gas Chromatograph"
  - name: "CTD profiler"
    identifier:
      name: "CTD"
      uri: "http://vocab.nerc.ac.uk/collection/L05/current/130/"
      source:
        name: "SeaDataNet device categories"
        url: "http://vocab.nerc.ac.uk/collection/L05/current/"
    
  - name: "Gas Chromatograph"
    identifier:
      name: "gas chromatographs"
      id: "LAB02"
      uri: "http://vocab.nerc.ac.uk/collection/L05/current/LAB02/"
```
> NOTE: 
> * `CTD profiler` was a phrase used in this project. It was annotated with the controlled vocabulary term `CTD`.
> * `Gas Chromatograph` was annotated with the controlled vocaublary term `gas chromatographs`.

### Schema.org Keywords

- Text
- <strong>`URL`
- `DefinedTerm`</strong>

### Keywords as URL

<pre>
{
  "@context": "https://schema.org/",
  "keywords": "keywords": [
    "nitrous oxide", 
    "Central Pacific", 
    "headspace equilibration", 
    "SRI Greenhouse Gas Monitoring Gas Chromatograph", 
    "CTD profiler",
    <strong>"http://vocab.nerc.ac.uk/collection/L05/current/130/",</strong> 
    "Gas Chromatograph",
    <strong>"http://vocab.nerc.ac.uk/collection/L05/current/LAB02/"</strong>
  ]
}
</pre>

#### Keywords as DefinedTerm

##### Exercise #1

<pre>
{
  "@context": "https://schema.org/",
  "keywords": [
    "CTD profiler",
    <strong>{
      "@type": "DefinedTerm",
      "name": "CTD",
      "url": "http://vocab.nerc.ac.uk/collection/L05/current/130/",
      "inDefinedTermSet": "http://vocab.nerc.ac.uk/collection/L05/current/"
    },</strong>
    "Gas Chromatograph",
    <strong>{
      "@type": "DefinedTerm",
      "name": "gas chromatographs",
      "url": "http://vocab.nerc.ac.uk/collection/L05/current/LAB02/",
      "inDefinedTermSet": "http://vocab.nerc.ac.uk/collection/L05/current/",
      "termCode": "LAB02"
    }</strong>
  ]
}
</pre>

##### Exercise #2

> Using `@id`

<pre>
{
  "@context": "https://schema.org/",
  "keywords": [
    "CTD profiler",
    {
      "@type": "DefinedTerm",
      "name": "CTD",
      "url": "http://vocab.nerc.ac.uk/collection/L05/current/130/",
      <strong>"inDefinedTermSet": {
        "@id": "http://vocab.nerc.ac.uk/collection/L05/current/",
        "@type" : "DefinedTermSet",
        "name": "SeaDataNet device categories"
      }</strong>
    },
    "Gas Chromatograph",
    {
      "@type": "DefinedTerm",
      "name": "gas chromatographs",
      "url": "http://vocab.nerc.ac.uk/collection/L05/current/LAB02/",
      <strong>"inDefinedTermSet": {
        "@id": "http://vocab.nerc.ac.uk/collection/L05/current/"
      },</strong>
      "termCode": "LAB02"
    }
  ]
}
</pre>

[>> JSON-LD Playground](https://json-ld.org/playground/#startTab=tab-normalized&json-ld=%7B%22%40context%22%3A%22https%3A%2F%2Fschema.org%2F%22%2C%22keywords%22%3A%5B%22CTD%20profiler%22%2C%7B%22%40type%22%3A%22DefinedTerm%22%2C%22name%22%3A%22CTD%22%2C%22url%22%3A%22http%3A%2F%2Fvocab.nerc.ac.uk%2Fcollection%2FL05%2Fcurrent%2F130%2F%22%2C%22inDefinedTermSet%22%3A%7B%22%40id%22%3A%22http%3A%2F%2Fvocab.nerc.ac.uk%2Fcollection%2FL05%2Fcurrent%2F%22%2C%22%40type%22%3A%22DefinedTermSet%22%2C%22name%22%3A%22SeaDataNet%20device%20categories%22%7D%7D%2C%22Gas%20Chromatograph%22%2C%7B%22%40type%22%3A%22DefinedTerm%22%2C%22name%22%3A%22gas%20chromatographs%22%2C%22url%22%3A%22http%3A%2F%2Fvocab.nerc.ac.uk%2Fcollection%2FL05%2Fcurrent%2FLAB02%2F%22%2C%22termCode%22%3A%22LAB02%22%2C%22inDefinedTermSet%22%3A%7B%22%40id%22%3A%22http%3A%2F%2Fvocab.nerc.ac.uk%2Fcollection%2FL05%2Fcurrent%2F%22%7D%7D%5D%7D&frame=%7B%7D&context=%7B%7D)

### Updated Markup - Keywords w. Controlled Vocabulary

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
    <strong>{
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
    }</strong>
  ],
  "license": ["https://spdx.org/licenses/CC-BY-4.0", "https://creativecommons.org/licenses/by/4.0/"],
  "identifier": "https://doi.org/10.26008/1912/bco-dmo.775849.1",
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

[Section #12: Identifiers as `PropertyValue` >>](12_identifiers-propertyvalue.md)

<hr/>

### Resources
- **Multiple array values w. differing types:** https://json-ld.org/spec/latest/json-ld/#example-50-multiple-array-values-of-different-types
- **Node Identifiers with `@id`:** https://json-ld.org/spec/latest/json-ld/#node-identifiers
- **Source:** [ProteOMZ nitrous oxide data](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt) (example metadata)
- **Testing:** [Google Rich Results Tool](https://search.google.com/test/rich-results)
