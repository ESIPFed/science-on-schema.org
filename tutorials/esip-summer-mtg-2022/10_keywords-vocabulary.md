# 10. Keywords from a Controlled Vocabulary

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
> * `CTP profiler` was a phrase used in this project. It was annotated with the controlled vocabulary term `CTD`.
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
    <strong>"http://vocab.nerc.ac.uk/collection/L05/current/130/",</strong> 
    "Gas Chromatograph"
  ]
}
</pre>

#### Keywords as DefinedTerm

##### Exercise #1

```
{
  "@context": "https://schema.org/",
  "keywords": [
    "CTD profiler",
    {
      "@type": "DefinedTerm",
      "name": "CTD",
      "url": "http://vocab.nerc.ac.uk/collection/L05/current/130/",
      "inDefinedTermSet": "http://vocab.nerc.ac.uk/collection/L05/current/",
    },
    "Gas Chromatograph",
    {
      "@type": "DefinedTerm",
      "name": "gas chromatographs",
      "url": "http://vocab.nerc.ac.uk/collection/L05/current/LAB02/",
      "termCode": "LAB02",
      "inDefinedTermSet": "http://vocab.nerc.ac.uk/collection/L05/current/",
    }
  ]
}
```

##### Exercise #2

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
      "termCode": "LAB02",
      <strong>"inDefinedTermSet": {
        "@id": "http://vocab.nerc.ac.uk/collection/L05/current/"
      }</strong>
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
      "termCode": "LAB02",
      "inDefinedTermSet": {
        "@id": "http://vocab.nerc.ac.uk/collection/L05/current/"
      }
    }</strong>
  ]
}
</pre>
<hr/>

[Section #11: Publisher & Provider >>](11_publisher-provider.md)

<hr/>

### Resources
- **Source:** [ProteOMZ nitrous oxide data](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt) (example metadata)
- **Testing:** [Google Rich Results Tool](https://search.google.com/test/rich-results)
