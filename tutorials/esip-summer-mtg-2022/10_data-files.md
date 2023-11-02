# 10. Data Files

#### Lesson
> - Introducing the `DataDownload` type

**Guidelines:** 
[Variables](/guides/Dataset.md#distributions)

**Source:**
[Line 70-91](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt#L70-L91)

> Files shortened for brevity

```
files:
  - 
    url: "https://darchive.mblwhoilibrary.org/bitstream/1912/28977/1/dataset-775849_proteomz-nitrous-oxide-data__v1.tsv"
    bytesize: 15077
    mimetype: "text/tab-separated-values"
    ...
```

### Schema.org Data Downloads

- [`distribution`](https://schema.org/distribution)
    - DataDownload
        - `contentSize`	Text	File size in (mega/kilo) bytes.
        - `contentUrl`	URL	Actual bytes of the media object, for example the image file or video file.
        - `encodingFormat` Media type typically expressed using a MIME format (see IANA site and MDN reference) e.g. application/zip for a SoftwareApplication binary, audio/mpeg for .mp3 etc.). _Unregistered or niche encoding and file formats can be indicated instead via the most appropriate URL_


#### Data Downloads

<pre>
{
  "@context": "https://schema.org/",
  <strong>"distribution": [
    {
      "@type": "DataDownload",
      "contentUrl": "https://darchive.mblwhoilibrary.org/bitstream/1912/28977/1/dataset-775849_proteomz-nitrous-oxide-data__v1.tsv",
      "encodingFormat": "text/tab-separated-values",
      "contentSize": "15077 bytes"
    }
  ]</strong>
}
</pre>

### Unpdated Markup - Variables

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
    "Gas Chromatograph"
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
  <strong>"distribution": [
    {
      "@type": "DataDownload",
      "contentUrl": "https://darchive.mblwhoilibrary.org/bitstream/1912/28977/1/dataset-775849_proteomz-nitrous-oxide-data__v1.tsv",
      "encodingFormat": "text/tab-separated-values",
      "contentSize": "15077 bytes"
    }
  ]</strong>
}
</pre>

<hr/>

[Section #11: Keywords (Controlled Vocabulary) >>](11_keywords-vocabulary.md)

<hr/>

### Resources
- **Source:** [ProteOMZ nitrous oxide data](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt) (example metadata)
- **Testing:** [Google Rich Results Tool](https://search.google.com/test/rich-results)
