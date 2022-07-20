# 6. Publisher

#### Lesson
> - Re-using how to create object properties

**Guidelines:** 
[Publisher / Provider](/guides/Dataset.md#publisher--provider)

**Source:**
[Line 39-41](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt#L39-L41)

```
publisher:
  name: "Biological and Chemical Data Management Office (BCO-DMO)"
  url: "https://www.bco-dmo.org"
```

### Schema.org Publisher

- https://schema.org/publisher
    - <strong>`Organization`</strong>
    - `Person`

### Publisher as Organization

<pre>
{
  "@context": "https://schema.org/",
  <strong>"publisher": {
    "@type": "Organization",
    "legalName": "Biological and Chemical Data Management Office",
    "url": "https://www.bco-dmo.org"
  }</strong>
}
</pre>

### Updated Markup - Publisher

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
  <strong>"publisher": {
    "@type": "Organization",
    "legalName": "Biological and Chemical Data Management Office",
    "url": "https://www.bco-dmo.org"
  }</strong>
}
</pre>
<hr/>

[Section #7: Author / Contributor >>](07_author-contributor.md)

<hr/>

### Resources
- **Source:** [ProteOMZ nitrous oxide data](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt) (example metadata)
- **Testing:** [Google Rich Results Tool](https://search.google.com/test/rich-results)
