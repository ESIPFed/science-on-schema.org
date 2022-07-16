# 3. Keywords

**Guidelines:** 
[Keywords](/guides/Dataset.md#keywords)

**Source:**
[Lines 9-26](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt#L9-L26)

#### Keywords as Text

```
{
  "@context": "https://schema.org/",
  "keywords": [
    "nitrous oxide", 
    "Central Pacific", 
    "headspace equilibration", 
    "SRI Greenhouse Gas Monitoring Gas Chromatograph", 
    "CTD profiler", 
    "Gas Chromatograph"
  ]
}
```



### Updated Markup - Keywords

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
  <strong>"keywords": [
    "nitrous oxide", 
    "Central Pacific", 
    "headspace equilibration", 
    "SRI Greenhouse Gas Monitoring Gas Chromatograph",
    "CTD profiler",
    "Gas Chromatograph"
  ]</strong>
}
</pre>
<hr/>

[Section #4: License >>](04_license.md)

<hr/>

### Resources
- **Source:** [ProteOMZ nitrous oxide data](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt) (example metadata)
- **Testing:** [Google Rich Results Tool](https://search.google.com/test/rich-results)
