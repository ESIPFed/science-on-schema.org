# 7. Authors / Contributors

#### Lesson
> - Create an array of objects
> - How to preserve ordering in arrays


**Guidelines:** 
[Identifier](/guides/Dataset.md#roles-of-people)

**Source:**
[Lines L27-L34](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt#L27-L34)

```
author:
  - name: "Alyson E. Santoro"
    ...
  - name: "Sarah Marie Laperriere"
    ...
contributor:
  - name: "Makoto Saito"
    ...
```

### Schema.org

- https://schema.org/creator
- https://schema.org/contributor
    - Organization
    - <strong>Person</strong>

### Preserving list order

> In support of proper citation, the order in which authors are listed can be preserved by using [`@list`](https://json-ld.org/spec/latest/json-ld/#dfn-list)

### Authors

<pre>
{
  "@context": "https://schema.org/",
  <strong>"creator": {
    "@list":</strong>[
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
</pre>

#### Contributors

<pre>
{
  "@context": "https://schema.org/",
  <strong>"contributor":{
    "@list":</strong>[
      {
        "@type": "Person",
        "name": "Makoto Saito"
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
  <strong>"creator": {
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
  </strong>
}
</pre>

<hr/>

[Section #8: Temporal Coverage >>](08_temporal.md)

<hr/>

### Resources
- **Example `@list` from JSON-LD Spec**: https://json-ld.org/spec/latest/json-ld/#example-51-an-ordered-collection-of-values-in-json-ld
- **Source:** [ProteOMZ nitrous oxide data](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt) (example metadata)
- **Testing:** [Google Rich Results Tool](https://search.google.com/test/rich-results)
