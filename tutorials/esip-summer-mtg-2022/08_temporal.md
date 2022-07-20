# 8. Temporal Coverage

#### Lesson
> - how to use `temporalCoverage`

**Guidelines:** 
[Temporal Coverage](/guides/Dataset.md#temporal-coverage)

Examples for:
- single date
- single dateTime
- <strong>date range</strong>
- open-ended date range

**Source:**
[Lines L64-L66](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt#L64-L66)

```
collectionDate:
  start: "2016-01-17"
  end: "2016-02-04"
```

### Schema.org Temporal

- https://schema.org/temporalCoverage
    - <strong>`Text`</strong>
    - `DateTime`
    - `URL`

> Uses [ISO 8601 time interval format](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals)

### Temporal Coverage

<pre>
{
  "@context": "https://schema.org/",
  <strong>"temporalCoverage": "2016-01-17/2016-02-04"</strong>
}
</pre>


### Updated Markup - Temporal Coverage

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
  <strong>"temporalCoverage": "2016-01-17/2016-02-04"</strong>
}
</pre>

<hr/>

[Section #9: Spatial >>](09_spatial.md)

<hr/>

### Resources
- **Source:** [ProteOMZ nitrous oxide data](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt) (example metadata)
- **Testing:** [Google Rich Results Tool](https://search.google.com/test/rich-results)
