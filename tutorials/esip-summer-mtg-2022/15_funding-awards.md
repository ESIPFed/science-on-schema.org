# 15. Funding & Awards

#### Lesson
> - Re-suing Publisher/Provider `Organization` lessons to describe funding sources
> - Introducing the new `fundedBy` property at schema.org to describe Grants and Awards
> - Re-using `@id` to reference an existing object
> - Re-using the identfier "pattern" with the Funder Registry

**Guidelines:** 
[Funding](/guides/Dataset.md#funding)

**Source:**
[Line 42-53](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt#L42-L53)

```
funding:
  - award:
    name: "R/V Falkor 160115 SOI ProteOMZ Expedition"
    url: "https://www.bco-dmo.org/award/685695"
    source: 
        name: "Schmidt Ocean Institute"
  - award:
    name: "FG-2016-7129"
    url: "https://www.bco-dmo.org/award/875341"
    source:
        name: "Sloan Foundation"
        doi: "10.13039/100000879"
```

### Schema.org - Funding

If you have information about the awards that funded the Dataset,

- <strong>[`funding`](https://schema.org/funding)</strong>
    - [`funder`](https://schema.org/funder) (if you have information about the source of the award(s)

OR, if you only have information about the funding source of the Dataset,

- [`funder`](https://schema.org/funder)

> `funding` wants to be a `Grant`. `Grant` has more specific [sub-types including `MonetaryGrant`](https://schema.org/Grant#subtypes). In this example, we use `MonetaryGrant` but `Grant` may be used in cases where the Dataset was generated under some funding that did not provide financial support.

### Awards

<pre>
{
  "@context": "https://schema.org/",
  "funding": [
    {
      <strong>"@type": "MonetaryGrant",</strong>
      "name": "R/V Falkor 160115 SOI ProteOMZ Expedition",
      "url": "https://www.bco-dmo.org/award/685695",
      "funder": {
        "@type": "Organization",
        "name": "Schmidt Ocean Institute"
      }
    },
    {
      "@type": "MonetaryGrant",
      "name": "FG-2016-7129",
      "url": "https://www.bco-dmo.org/award/875341",
      "funder": {
        "@type": "Organization",
        "name": "Sloan Foundation",
        <strong>"identifier": {
          "@id": "https://doi.org/10.13039/100000879",
          "@type": "PropertyValue",
          "propertyID": "https://registry.identifiers.org/registry/doi",
          "value": "doi:10.13039/100000879",
          "url": "https://doi.org/10.13039/100000879"
        }</strong>
      }
    }
  ]
}
</pre>

#### Funder Registry - Finding the DOI for a funder

https://doi.crossref.org/funderNames

**Schmidt Ocean Institute**
doi:10.13039/100016377

#### Q: What if we have an award number in our metadata?

Let's imagine our Sloane Foundation award metadata was altered to:

<pre>
- award:
    <strong>name: "2016 Award to Alyson Santoro - #7129"
    awardNumber: "FG-2016-7129"</strong>
    url: "https://www.bco-dmo.org/award/875341"
    source:
        name: "Sloan Foundation"
        doi: "10.13039/100000879"
</pre>

Then, we may model the awardNumber using the `identifier` pattern:


<pre>
{
  "@context": "https://schema.org/",
  "funding": [
    {
      "@type": "MonetaryGrant",
      <strong>"name": "2016 Award to Alyson Santoro - #7129",
      "identifier": "FG-2016-7129",</strong>
      "url": "https://www.bco-dmo.org/award/875341",
      "funder": {
        "@type": "Organization",
        "name": "Sloan Foundation",
        <strong>"identifier": {
          "@id": "https://doi.org/10.13039/100000879",
          "@type": "PropertyValue",
          "propertyID": "https://registry.identifiers.org/registry/doi",
          "value": "doi:10.13039/100000879",
          "url": "https://doi.org/10.13039/100000879"
        }</strong>
      }
    }
  ]
}
</pre>

If the awardNumber has more metadata like a URL, etc. we can continue to employ the `identifier` pattern using a `PropertyValue`:
  
<pre>
{
  "@context": "https://schema.org/",
  "funding": [
    {
      "@type": "MonetaryGrant",
      "name": "2016 Award to Alyson Santoro - #7129",
      <strong>"identifier": {
        "@type": "PropertyValue",
        "value": "FG-2016-7129",
        "url": "https://example.award.url/id/FG-2016-7129"
      },</strong>
      "url": "https://www.bco-dmo.org/award/875341",
      "funder": {
        "@type": "Organization",
        "name": "Sloan Foundation",
        <strong>"identifier": {
          "@id": "https://doi.org/10.13039/100000879",
          "@type": "PropertyValue",
          "propertyID": "https://registry.identifiers.org/registry/doi",
          "value": "doi:10.13039/100000879",
          "url": "https://doi.org/10.13039/100000879"
        }</strong>
      }
    }
  ]
}
</pre>

### Updated Markup - Funding & Awards

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
  "provider": { "@id": "https://www.bco-dmo.org" },
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
  <strong>"funding": [
    {
      "@type": "MonetaryGrant",
      "name": "R/V Falkor 160115 SOI ProteOMZ Expedition",
      "url": "https://www.bco-dmo.org/award/685695",
      "funder": {
        "@type": "Organization",
        "name": "Schmidt Ocean Institute"
      }
    },
    {
      "@type": "MonetaryGrant",
      "name": "FG-2016-7129",
      "url": "https://www.bco-dmo.org/award/875341",
      "funder": {
        "@type": "Organization",
        "name": "Sloan Foundation",
        "identifier": {
          "@id": "https://doi.org/10.13039/100000879",
          "@type": "PropertyValue",
          "propertyID": "https://registry.identifiers.org/registry/doi",
          "value": "doi:10.13039/100000879",
          "url": "https://doi.org/10.13039/100000879"
        }
      }
    }
  ],</strong>
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

[Section #16: Variables >>](16_variables.md)

<hr/>

### Resources
- **Source:** [ProteOMZ nitrous oxide data](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt) (example metadata)
- **Testing:** [Google Rich Results Tool](https://search.google.com/test/rich-results)

