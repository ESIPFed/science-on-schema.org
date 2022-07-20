# 4. License

#### Lesson
> - Creating Object properties with their own `@type`
> - Weighing expressivity vs. simplicity
> - Re-using what we learned about arrays

**Guidelines:** 
[License](/guides/Dataset.md#license)

**Source:**
[Lines 35-37](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt#L35-L37)

```
license: 
  name: "Creative Commons Attribution 4.0"
  url: "https://creativecommons.org/licenses/by/4.0/"
```

### Schema.org License

- https://schema.org/license
    - `URL`
    - `CreativeWork`

#### License as URL - Good

<pre>
{
  "@context": "https://schema.org/",
  <strong>"license": "https://creativecommons.org/licenses/by/4.0/"</strong>
}
</pre>

#### License as CreativeWork - Better?

<pre>
{
  "@context": "https://schema.org/",
  <strong>"license": {
    "@type": "CreativeWork",
    "name": "Creative Commons Attribution 4.0",
    "url": "https://creativecommons.org/licenses/by/4.0/"
  }</strong>
}
</pre>

#### License as SPDX URL - Best

- Use a simple URL
- [SPDX](https://spdx.org/licenses/) creates URLs for many licenses including those that don't have URLs
- From a source that <em>harvesters</em> can rely on (e.g. use URL to lookup more information about the license)

<pre>
{
  "@context": "https://schema.org/",
  <strong>"license": "https://spdx.org/licenses/CC-BY-4.0"</strong>
}
</pre>

OR, include both the SPDX and the Creative Commons URLs in an array:

<pre>
{
  "@context": "https://schema.org/",
  <strong>"license": ["https://spdx.org/licenses/CC-BY-4.0", "https://creativecommons.org/licenses/by/4.0/"]</strong>
}
</pre>

### Updated Markup - License

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
  <strong>"license": ["https://spdx.org/licenses/CC-BY-4.0", "https://creativecommons.org/licenses/by/4.0/"]</strong>
}
</pre>
<hr/>

[Section #5: Identifier >>](05_identifier.md)

<hr/>

### Resources
- **Source:** [ProteOMZ nitrous oxide data](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt) (example metadata)
- **Testing:** [Google Rich Results Tool](https://search.google.com/test/rich-results)
