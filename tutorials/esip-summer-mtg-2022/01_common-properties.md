# Basic Dataset

**Source:** [ProteOMZ nitrous oxide data](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt) (example metadata)

**Testing:** [Google Rich Results Tool](https://search.google.com/test/rich-results)

## 1. Schema.org Context & Type

```
{
  "@context": "https://schema.org/",
  "@type": "Dataset"
}
```

## 2. Common Properties

**Guidelines:** 
[Common Properties](/guides/Dataset.md#common-properties)

**Source:**
[Lines 1-4](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt#L1-L4)

```
{
  "@context": "https://schema.org/",
  "@type": "Dataset",
  "name": "Nitrous oxide concentrations from the R/V Falkor expedition FK160115 in the Central Pacific from January to February 2016",
  "description": "Dissolved N2O concentrations from were measured in discrete samples on a research expedition to the Equatorial Pacific. Water samples were collected using a 24 bottle Niskin rosette equipped with a CTD. N₂O concentrations were measured using a headspace equilibration method and analyzed on a SRI Greenhouse Gas Monitoring Gas Chromatograph.",
  "url": "https://www.bco-dmo.org/dataset/775849",
  "version": "1",
  "isAccessibleForFree": "true"
}
```

[(next ->)](02_keywords.md)
