# 3. Keywords

#### Lesson
> - Building an [array](https://json-ld.org/spec/latest/json-ld/#sets-and-lists) in JSON-LD
> - Focus on multiple values with no inherent order ([example from JSON-LD spec](https://json-ld.org/spec/latest/json-ld/#example-48-multiple-values-with-no-inherent-order))


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
      ...
  - name: "Gas Chromatograph"
      ...
```

### Schema.org Keywords

- <strong>`Text`</strong>
- `URL`
- `DefinedTerm`

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
- _@see_ https://json-ld.org/spec/latest/json-ld/#sets-and-lists
- **Advanced Tutorial:** [Section #11: Keywords from a Controlled Vocabulary](11_keywords-vocabulary.md)
- **Source:** [ProteOMZ nitrous oxide data](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt) (example metadata)
- **Testing:** [Google Rich Results Tool](https://search.google.com/test/rich-results)
