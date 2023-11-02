# 14. Provider

- For this section, we are no longer the publisher, 'Biological and Chemical Data Management Office'
- Rather, imagine we are a downstream **provider** called 'Woods Hole Open Access Server' for this very same dataset. 
- We have a webpage describing our copy of the dataset at url https://darchive.mblwhoilibrary.org/handle/1912/28977

_NOTE: A provider may be a metadata aggregator or another repository with a duplicate copy._


#### Lesson
> - Difference between publisher and provider (for proper credit)
> - Revisiting `sameAs` for Dataset web pages
> - Re-using `@id` to reference an existing object

**Guidelines:** 
[Publisher / Provider](/guides/Dataset.md#publisher--provider)

**Source:**
[Line 39-41](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt#L39-L41)

```
publisher:
  name: "Biological and Chemical Data Management Office (BCO-DMO)"
  url: "https://www.bco-dmo.org"
```

> New Data about a provider

```
provider:
  name: "Woods Hole Open Access Server"
  url: "https://darchive.mblwhoilibrary.org/"
  dataset: "https://darchive.mblwhoilibrary.org/handle/1912/28977"
```

#### Provider

##### Exercise #1

> As the provider, create schema.org markup for the `publisher` and the `provider`

<pre>
{
  "@context": "https://schema.org/",
  "@type": "Dataset",
  <strong>"url": "https://darchive.mblwhoilibrary.org/handle/1912/28977",</strong>
  "publisher": {
    "@type": "Organization",
    "legalName": "Biological and Chemical Data Management Office",
    "url": "https://www.bco-dmo.org"
  },
  <strong>"provider": {
    "@type": "Organization",
    "legalName": "Woods Hole Open Access Server",
    "url": "https://darchive.mblwhoilibrary.org/"
  }</strong>
}
</pre>


#### Using `sameAs`

##### Exercise #2

> As the provider, link your copy of the dataset (provider) to the publisher's copy

<pre>
{
  "@context": "https://schema.org/",
  "@type": "Dataset",
  "url": "https://darchive.mblwhoilibrary.org/handle/1912/28977",
  <strong>"sameAs": "https://www.bco-dmo.org/dataset/775849",</strong>
  "publisher": {
    "@type": "Organization",
    "legalName": "Biological and Chemical Data Management Office",
    "url": "https://www.bco-dmo.org"
  },
  "provider": {
    "@type": "Organization",
    "legalName": "Woods Hole Open Access Server",
    "url": "https://darchive.mblwhoilibrary.org/"
  }
}
</pre>

##### Exercise #3

> Specify the DOI landing page using `sameAs`

<pre>
{
  "@context": "https://schema.org/",
  "@type": "Dataset",
  "url": "https://darchive.mblwhoilibrary.org/handle/1912/28977",
  <strong>"sameAs": ["https://www.bco-dmo.org/dataset/775849", "https://doi.org/10.26008/1912/bco-dmo.775849.1"],</strong>
  "publisher": {
    "@type": "Organization",
    "legalName": "Biological and Chemical Data Management Office",
    "url": "https://www.bco-dmo.org"
  },
  "provider": {
    "@type": "Organization",
    "legalName": "Woods Hole Open Access Server",
    "url": "https://darchive.mblwhoilibrary.org/"
  }
}
</pre>

##### Exercise #4

- Now that we've seen what schema.org looks like from a downstream dataset provider,
- Let's go back to being the publisher 'Biological and Chemical Data Management Office'

<pre>
{
  "@context": "https://schema.org/",
  "@type": "Dataset",
  "url": "https://www.bco-dmo.org/dataset/775849",
  "sameAs": "https://doi.org/10.26008/1912/bco-dmo.775849.1",
  <strong>"publisher": {
    "@type": "Organization",
    "legalName": "Biological and Chemical Data Management Office",
    "url": "https://www.bco-dmo.org"
  }</strong>
}
</pre>

> Add schema.org markup specifying that you are both the `publisher` and `provider`

<pre>
{
  "@context": "https://schema.org/",
  "@type": "Dataset",
  "url": "https://www.bco-dmo.org/dataset/775849",
  "sameAs": "https://doi.org/10.26008/1912/bco-dmo.775849.1",
  "publisher": {
    <strong>"@id": "https://www.bco-dmo.org",</strong>
    "@type": "Organization",
    "legalName": "Biological and Chemical Data Management Office",
    "url": "https://www.bco-dmo.org"
  },
  <strong>"provider": { "@id": "https://www.bco-dmo.org" }</strong>
}
</pre>

### Updated Markup - Adding a Provider

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
    {
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
    }
  ],
  "license": ["https://spdx.org/licenses/CC-BY-4.0", "https://creativecommons.org/licenses/by/4.0/"],
  "identifier": {
    "@id": "https://doi.org/10.26008/1912/bco-dmo.775849.1",
    "@type": "PropertyValue",
    "propertyID": "https://registry.identifiers.org/registry/doi",
    "value": "doi:10.26008/1912/bco-dmo.775849.1",
    "url": "https://doi.org/10.26008/1912/bco-dmo.775849.1"
  },
  "sameAs": "https://doi.org/10.26008/1912/bco-dmo.775849.1",
  "publisher": {
    "@type": "Organization",
    "legalName": "Biological and Chemical Data Management Office",
    "url": "https://www.bco-dmo.org"
  },
  <strong>"provider": { "@id": "https://www.bco-dmo.org" },</strong>
  "creator": {
    "@list":[
      {
        "@type": "Person",
        "name": "Alyson E. Santoro",
        "identifier": {
          "@id": "https://orcid.org/0000-0003-2503-8219",
          "@type": "PropertyValue",
          "propertyID": "https://registry.identifiers.org/registry/orcid",
          "url": "https://orcid.org/0000-0003-2503-8219",
          "value": "orcid:0000-0003-2503-8219"
        }
      },
      {
        "@type": "Person",
        "name": "Sarah Marie Laperriere",
        "identifier": {
          "@id": "https://orcid.org/0000-0003-4691-8741",
          "@type": "PropertyValue",
          "propertyID": "https://registry.identifiers.org/registry/orcid",
          "url": "https://orcid.org/0000-0003-4691-8741",
          "value": "orcid:0000-0003-4691-8741"
        }
      }
    ]
  },
  "contributor": {
    "@list":[
      {
        "@type": "Person",
        "name": "Makoto Saito",
        "identifier": {
          "@id": "https://orcid.org/0000-0001-6040-9295",
          "@type": "PropertyValue",
          "propertyID": "https://registry.identifiers.org/registry/orcid",
          "url": "https://orcid.org/0000-0001-6040-9295",
          "value": "orcid:0000-0001-6040-9295"
        }
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

[Section #15: Funding & Awards >>](15_funding-awards.md)

<hr/>

### Resources
- **Source:** [ProteOMZ nitrous oxide data](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt) (example metadata)
- **Testing:** [Google Rich Results Tool](https://search.google.com/test/rich-results)


