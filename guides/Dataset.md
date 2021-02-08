<a id="top"></a>
[Home](/README.md) | Dataset

# Describing a Dataset

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Describing a Dataset](#describing-a-dataset)
	- [Common Properties](#common-properties)
		- [Identifier](#identifier)
			- [How to reference Short DOIs](#how-to-reference-short-dois)
		- [Variables](#variables)
		- [Catalog](#catalog)
		- [Metadata](#metadata)
		- [Distributions](#distributions)
			- [Accessing Data through a Service Endpoint](#accessing-data-through-a-service-endpoint)
		- [Temporal Coverage](#temporal-coverage)
		- [Spatial Coverage](#spatial-coverage)
		- [Roles of People](#roles-of-people)
		- [Publisher / Provider](#publisher-provider)
		- [Funding](#funding)
		- [License](#license)
		- [Provenance Relationships](#provenance-relationships)
	- [Advanced Publishing Techniques](#advanced-publishing-techniques)
		- [Attaching Physical Samples to a Dataset](#attaching-physical-samples-to-a-dataset)

<!-- /TOC -->

## Common Properties

Google has drafted a [guide to help publishers](https://developers.google.com/search/docs/data-types/dataset). The guide describes the only required fields as - name and description.
* [name](https://schema.org/name) - A descriptive name of a dataset (e.g., “Snow depth in Northern Hemisphere”)
* [description](https://schema.org/description) - A short summary describing a dataset.

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  <strong>"name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  "description": "This dataset includes results of laboratory experiments which measured dissolved organic carbon (DOC) usage by natural bacteria in seawater at different pCO2 levels. Included in this dataset are; bacterial abundance, total organic carbon (TOC), what DOC was added to the experiment, target pCO2 level. "</strong>
}
</pre>

The [guide](https://developers.google.com/search/docs/data-types/dataset) suggests the following recommended fields:

* [url](https://schema.org/url) - Location of a page describing the dataset.
* [sameAs](https://schema.org/sameAs) - Other URLs that can be used to access the dataset page. A link to a page that provides more information about the same dataset, usually in a different repository.
* [version](https://schema.org/version) - The version number or identifier for this dataset (text or numeric).
* [isAccessibleForFree](https://schema.org/isAccessibleForFree) - Boolean (true|false) speficying if the dataset is accessible for free.
* [keywords](https://schema.org/keywords) - Keywords summarizing the dataset.
* [identifier](https://schema.org/identifier) - An identifier for the dataset, such as a DOI. (text,URL, or PropertyValue).
* [variableMeasured](https://schema.org/variableMeasured) - What does the dataset measure? (e.g., temperature, pressure)

![Basic Fields](/assets/diagrams/dataset/dataset_basic-fields.svg "Dataset - Basic Fields")

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  "description": "This dataset includes results of laboratory experiments which measured dissolved organic carbon (DOC) usage by natural bacteria in seawater at different pCO2 levels. Included in this dataset are; bacterial abundance, total organic carbon (TOC), what DOC was added to the experiment, target pCO2 level. ",
  <strong>"url": "https://www.sample-data-repository.org/dataset/472032",
  "sameAs": "https://search.dataone.org/#view/https://www.sample-data-repository.org/dataset/472032",
  "version": "2013-11-21",
  "isAccessibleForFree": true,
  "keywords": ["ocean acidification", "Dissolved Organic Carbon", "bacterioplankton respiration", "pCO2", "carbon dioxide", "oceans"]
  "license": [ "http://spdx.org/licenses/CC0-1.0", "https://creativecommons.org/publicdomain/zero/1.0"]
  </strong>
}
</pre>
Back to [top](#top)

### Identifier

Adding the [schema:identifier](https://schema.org/identifier) field can be done in three ways - a text description, a URL, or by using the [schema:PropertyValue](https://schema.org/PropertyValue) field.

![Identifiers](/assets/diagrams/dataset/dataset_identifier.svg "Dataset - Identifier")

**We _highly recommend_ using [schema:PropertyValue](https://schema.org/PropertyValue).**

**Q: Why are simple text or URLs not good enough?**  
**A:** Identifiers have multiple properties that are useful when trying to find them across the web.

Most identifiers have these properties:

- a **value**,
- a **domain** or **scheme** (in which the value is guaranteed to be unique),
- (optionally) a **resolvable URL** (where the thing being identified can be found),
- (optionally) a **domain prefix** (a token string of characters succeeded by a colon ':' that represents the domain or scheme).

For example, the Digital Object Identifier (DOI) for a dataset may be: doi:10.5066/F7VX0DMQ. To break it down into its properties, we arrive at:

- **value**: `10.5066/F7VX0DMQ`
- **scheme**: `Digital Object Identifier (DOI)`
- **url**: `https://doi.org/10.5066/F7VX0DMQ`
- **prefix**: `doi`

**Q: Can't we just say the scheme is a 'DOI'?**  
**A:** Yes, but there's a better way - a URI or URL. Because the we are publishing schema.org to express the explicit values of our content, we want to explicitly identify and classify our content such that harvesters can determine when our content appears elsewhere on the web. By detectinng these shared pieces content, we form the [Web of Data](https://www.w3.org/standards/semanticweb/data).

Because the **scheme** `Digital Object Identifier (DOI)` is described using unstructured text, we need a better way to explicitly state this value. Fortunately, [identifiers.org](https://registry.identifiers.org/registry) has registered URIs for almost 700 different identifier schemes which can be browsed at: [https://registry.identifiers.org/registry](https://registry.identifiers.org/registry).

We can specify the **scheme** as being a DOI with this identifiers.org Registry URI:

[https://registry.identifiers.org/registry/doi](https://registry.identifiers.org/registry/doi)

Looking at the available fields from [schema:PropertyValue](https://schema.org/PropertyValue), we can map our identifier fields as such:

- `schema:value` as the identifier value `10.5066/F7VX0DMQ`
- `schema:propertyID` is the registry.identifiers.org URI for the identifier scheme `https://registry.identifiers.org/registry/doi`,
- `schema:url` is the resolvable url for that identifier `https://doi.org/10.5066/F7VX0DMQ`.

**Q: Where should the prefix go?**  
**A:** There is no ideal property for the prefix. But, we may include it as part of the `schema:value`.

**Q: Why include `doi:` as part of the value? Doesn't the URL `https://doi.org/10.5066/F7VX0DMQ` acheive the same result?**  
**A:** While the actual value of the DOI is `10.5066/F7VX0DMQ`, we felt that this representation helps schema.org publishers specify an identifier value that is familiar to the research community. For example, in most citation styles such as APA, the DOI 10.5066/F7VX0DMQ is cited as `doi:10.5066/F7VX0DMQ`. Also, there can be many proper URLs for a specific identifier:

- http://doi.org/10.5066/F7VX0DMQ
- https://doi.org/10.5066/F7VX0DMQ
- http://dx.doi.org/10.5066/F7VX0DMQ
- https://dx.doi.org/10.5066/F7VX0DMQ
- https://www.sciencebase.gov/catalog/item/56b3e649e4b0cc79997fb5ec

For these reasons, we recommend that any identifier having a known prefix value should be included in the value succeeded by a colon to form '<prefix>:<value>', or for this DOI: `doi:10.5066/F7VX0DMQ`.

**Q: How do I know if an Identifier has a known prefix?**  
**A:** Each Identifier in the identifiers.org Registry that has a known prefix will be specified on the identifers.org registry page under the section called '**Identifier Schemes**' at the field labeled '**Prefix**'.

An example of using [schema:PropertyValue](https://schema.org/PropertyValue) to describe an Identifier:

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  "description": "This dataset includes results of laboratory experiments which measured dissolved organic carbon (DOC) usage by natural bacteria in seawater at different pCO2 levels. Included in this dataset are; bacterial abundance, total organic carbon (TOC), what DOC was added to the experiment, target pCO2 level. ",
  "url": "https://www.sample-data-repository.org/dataset/472032",
  "sameAs": "https://search.dataone.org/#view/https://www.sample-data-repository.org/dataset/472032",
  "version": "2013-11-21",
  "keywords": ["ocean acidification", "Dissolved Organic Carbon", "bacterioplankton respiration", "pCO2", "carbon dioxide", "oceans"],
  <strong>"identifier":
      {
        "@id": "https://doi.org/10.5066/F7VX0DMQ",
        "@type": "PropertyValue",
        "propertyID": "https://registry.identifiers.org/registry/doi",
        "value": "doi:10.5066/F7VX0DMQ",
        "url": "https://doi.org/10.5066/F7VX0DMQ"
      }</strong>
}
</pre>

Optionally, the `schema:name` field can be used to give this specific identifier a label such as "DOI: 10.5066/F7VX0DMQ" or "DOI 10.5066/F7VX0DMQ", but `schema:name` should never be used to simply say "DOI".

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
  <strong>"identifier":
      {
        "@id": "https://doi.org/10.5066/F7VX0DMQ",
        "@type": "PropertyValue",
	    "name": "DOI: 10.5066/F7VX0DMQ",
        "propertyID": "https://registry.identifiers.org/registry/doi",
        "value": "doi:10.5066/F7VX0DMQ",
        "url": "https://doi.org/10.5066/F7VX0DMQ"
      }</strong>
}
</pre>

For more examples of using `schema:PropertyValue` for identifiers other than DOIs:

- ARK: https://registry.identifiers.org/registry/ark
- PubMed: https://registry.identifiers.org/registry/pubmed
- PaleoDB: https://registry.identifiers.org/registry/paleodb
- Protein Data Bank: https://registry.identifiers.org/registry/pdb

<pre>
"identifier": [
    {
        "@id": "https://n2t.net/ark:13030/c7833mx7t",
        "@type": "PropertyValue",
        "propertyID": "https://registry.identifiers.org/registry/ark",
        "name": "ARK: 13030/c7833mx7t",
        "value": "ark:13030/c7833mx7t",
        "url": "https://n2t.net/ark:13030/c7833mx7t"
    },
    {
        "@id": "http://www.ncbi.nlm.nih.gov/pubmed/16333295",
        "@type": "PropertyValue",
        "propertyID": "https://registry.identifiers.org/registry/pubmed",
        "name": "Pubmed ID #16333295",
        "value": "pubmed:16333295",
        "url": "http://www.ncbi.nlm.nih.gov/pubmed/16333295"
    },
    {
        "@id": "https://identifiers.org/paleodb:83088",
        "@type": "PropertyValue",
        "propertyID": "https://registry.identifiers.org/registry/paleodb",
        "name": "Paleo Database ID #83088",
        "value": "paleodb:83088",
        "url": "https://identifiers.org/paleodb:83088"
    },
    {
        "@id": "https://identifiers.org/pdb:2gc4",
	    "@type": "PropertyValue",
        "propertyID": "https://registry.identifiers.org/registry/pdb",
        "name": "Protein Data Bank 2gc4",
        "value": "pdb:2gc4",
        "url": "https://identifiers.org/pdb:2gc4"
    }
]
</pre>

While we strongly recommend using a [schema:PropertyValue](https://schema.org/PropertyValue), in it's most basic form, the `schema:identifier` as text can be published as:

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  "description": "This dataset includes results of laboratory experiments which measured dissolved organic carbon (DOC) usage by natural bacteria in seawater at different pCO2 levels. Included in this dataset are; bacterial abundance, total organic carbon (TOC), what DOC was added to the experiment, target pCO2 level. ",
  "url": "https://www.sample-data-repository.org/dataset/472032",
  "sameAs": "https://search.dataone.org/#view/https://www.sample-data-repository.org/dataset/472032",
  "version": "2013-11-21",
  "keywords": ["ocean acidification", "Dissolved Organic Carbon", "bacterioplankton respiration", "pCO2", "carbon dioxide", "oceans"],
  <strong>"identifier": "urn:sdro:dataset:472032"</strong>
}
</pre>

Or as a URL:

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
  <strong>"identifier": "http://id.sampledatarepository.org/dataset/472032/version/1"</strong>
}
</pre>

However, if the identifier is a persistent identifier such as a DOI, ARK, or accession nmumber, then the best way to represent these identifiers is by using a [schema:PropertyValue](https://schema.org/PropertyValue). The PropertyValue allows for more information about the identifier to be represented such as the identifier type or scheme, the identifier's value, it's URL and more. Because of this flexibility, we recommend using PropertyValue for all identifier types.

[schema:Dataset](https://schema.org/Dataset) also defines a field for the [schema:citation](https://schema.org/citation) as either text or a [schema:CreativeWork](https://schema.org/CreativeWork). To provide citation text:

NOTE: If you have a DOI, the citation text can be [automatically generated](https://citation.crosscite.org/docs.html#sec-4-1) for you by querying a DOI URL with the Accept Header of 'text/x-bibliography'.

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  "description": "This dataset includes results of laboratory experiments which measured dissolved organic carbon (DOC) usage by natural bacteria in seawater at different pCO2 levels. Included in this dataset are; bacterial abundance, total organic carbon (TOC), what DOC was added to the experiment, target pCO2 level. ",
  "url": "https://www.sample-data-repository.org/dataset/472032",
  "sameAs": "https://search.dataone.org/#view/https://www.sample-data-repository.org/dataset/472032",
  "version": "2013-11-21",
  "keywords": ["ocean acidification", "Dissolved Organic Carbon", "bacterioplankton respiration", "pCO2", "carbon dioxide", "oceans"],
  "identifier": {
    "@id": "https://doi.org/10.5066/F7VX0DMQ",
    "@type": "PropertyValue",
    "name": "DOI: 10.5066/F7VX0DMQ",
    "propertyID": "https://registry.identifiers.org/registry/doi",
    "value": "doi:10.5066/F7VX0DMQ",
    "url": "https://doi.org/10.5066/F7VX0DMQ"
  },
  <strong>"citation": "J.Smith 'How I created an awesome dataset’, Journal of Data Science, 1966"</strong>
}
</pre>

#### How to reference Short DOIs

[Short DOIs](http://shortdoi.org/) is a redirect service offered by the International DOI Foundation that provides a shorter version of an orginial DOI. For example, the original DOI `doi:10.5066/F7VX0DMQ` has a short DOI of `doi.org/csgf`. Short DOIs are resolvable using standard DOI URLS such as `http://doi.org/fg5v`. These short DOIs are treated identically to the original DOI. If you are using the short DOI service, we recommend publishing a short DOI URL using the `schema:sameAs` property of the `schema:Dataset`:

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  "description": "This dataset includes results of laboratory experiments which measured dissolved organic carbon (DOC) usage by natural bacteria in seawater at different pCO2 levels. Included in this dataset are; bacterial abundance, total organic carbon (TOC), what DOC was added to the experiment, target pCO2 level. ",
  "url": "https://www.sample-data-repository.org/dataset/472032",
  "sameAs": [
    "https://search.dataone.org/#view/https://www.sample-data-repository.org/dataset/472032",
    <strong>"http://doi.org/fg5v"</strong>
  ],
  "version": "2013-11-21",
  "keywords": ["ocean acidification", "Dissolved Organic Carbon", "bacterioplankton respiration", "pCO2", "carbon dioxide", "oceans"],
  "identifier":
      {
        "@id": "https://doi.org/10.5066/F7VX0DMQ",
        "@type": "PropertyValue",
        "propertyID": "https://registry.identifiers.org/registry/doi",
        "value": "doi:10.5066/F7VX0DMQ",
        "url": "https://doi.org/10.5066/F7VX0DMQ"
      }
}
</pre>

`schema:sameAs` is used here for the following reasons:

1. It doesn't add too many more statements that might increase the page weight (which may impact major search engine crawlers stopping the crawl of schema.org markup).
2. Crawlers that follow the URL for the short DOI can retrieve structured metadata for the DOI itself: 

`curl --location --request GET "http://doi.org/fg5v" --header "Accept: application/ld+json"`

Back to [top](#top)

### Variables

Adding the [schema:variableMeasured](https://schema.org/variableMeasured) field can be done in two ways - a text description of each variable or by using the [schema:PropertyValue](https://schema.org/PropertyValue) type to describe the variable in more detail. We highly recommend using the [schema:PropertyValue](https://schema.org/PropertyValue).

![Variables](/assets/diagrams/dataset/dataset_variables.svg "Dataset - Variables")

In it's most basic form, the variable as a [schema:PropertyValue](https://schema.org/PropertyValue) can be published as:

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
  <strong>"variableMeasured": [
    {
      "@type": "PropertyValue",
      "name": "Bottle identifier",
      "description": "The bottle number for each associated measurement."
    },
    ...
  ]</strong>
}
</pre>
<a id="variables_external-vocab-example"></a>
If a URI is available that identifies the variable, it should be included as the
[PropertyID](https://schema.org/propertyID):

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
    <strong>"gsn-quantity": "http://www.geoscienceontology.org/geo-lower/quantity#"</strong>
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
  "variableMeasured": [
    {
      "@type": "PropertyValue",
      "name": "latitude",
      <strong>"propertyID":"http://www.geoscienceontology.org/geo-lower/quantity#latitude"</strong>,
      "url": "https://www.sample-data-repository.org/dataset-parameter/665787",
      "description": "Latitude where water samples were collected; north is positive.",
      "unitText": "decimal degrees",
      "minValue": "45.0",
      "maxValue": "15.0"
    },
    ...
  ]
}
</pre>

Back to [top](#top)

### Catalog

For some repositories, defining a one or many data collections helps contextualize the datasets. In schema.org, you define these collections using [schema:DataCatalog](https://schema.org/DataCatalog).

![DataCatalog](/assets/diagrams/dataset/dataset_datacatalog.svg "Dataset - Data Catalog")

The most optimal way to use these DataCatalogs for a repository is to define these catalogs as an ["offering" of your repository](#repository-offercatalog) and including the `@id` property to be reused in the dataset JSON-LD. For example, the repository JSON-LD defines a [schema:DataCatalog](https://schema.org/DataCatalog) with the

`"@id": "https://www.sample-data-repository.org/collection/biological-data"`.

In the dataset JSON-LD, we reuse that `@id` to say a dataset belongs in that catalog:

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
  <strong>"includedInDataCatalog": {
    "@id": "https://www.sample-data-repository.org/collection/biological-data",
    "@type": "DataCatalog"
  }</strong>
}
</pre>


Back to [top](#top)

### Metadata

While this schema.org record represents metadata about a Dataset, many providers will also have other metadata records that may be more complete or that conform to other metadata formats and vocabularies that might be useful. For example, repositories often contain detailed records in ISO TC 211 formats, [EML](https://eml.ecoinformatics.org), and other formats. Aggregators and other consumers can make use of this additional metadata if they are linked in a standardized way to the schema.org record.  We recommend that the location of the alternative forms of the metadata be provided using the [schema:subjectOf](https://schema.org/subjectOf) and [schema:about](https://schema.org/about) properties:

Link metadata documents to a [schema:Dataset](https://schema.org/Dataset) by using [schema:subjectOf](https://schema.org/subjectOf).
    - Or if a schema.org snippet describes the metadata as the main resource, then link to the Dataset it describes using [schema:about](https://schema.org/about).

These two approaches are equivalent, and which is used depends on the subject of the schema.org record.

![Metadata](/assets/diagrams/dataset/dataset_metadata.svg "Dataset - Metadata")

Once the linkage has been made, further details about the metadata can be provided. We recommend using [schema:encodingFormat](https://schema.org/encodingFormat) to indicate the metadata format/vocabulary to which the metadata record conforms.  If it conforms to multiple formats, or to a specific and general format types, multiple types can be listed.  
We use the [schema:DataDownload](https://schema.org/DataDownload) class for Metadata files so that we can use the [schema:MediaObject](https://schema.org/MediaObject) properties for describing bytesize, encoding, etc.

It can be useful to aggregators and other consumers to indicate when the metadata record was last modified using `schema:dateModified`, which can be used to optimize harvesting schedules for search indices and other applications.

An example of a metadata reference to an instance of EML-formatted structured metadata, embedded within a `schema:Dataset` record:

<pre>
  {
    "@context": "https://schema.org/",
    "@type": "Dataset",
    "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
    "distribution": {
      "@type": "DataDownload",
      ...
    },
    <strong>"subjectOf": {
      "@type": "DataDownload",
      "name": "eml-metadata.xml",
      "description": "EML metadata describing the dataset",
      "encodingFormat": ["application/xml", "https://eml.ecoinformatics.org/eml-2.2.0"],
      "dateModified":"2019-06-12T14:44:15Z"
    }</strong>
  }
</pre>

Alternatively, if the schema.org record is meant to describe the metadata record, one could use the inverse property `schema:about` to indicate the linkage back to the Dataset that it describes.  This would be a more rare situation, as typically the schema.org record would be focused on the Dataset itself.

Note that the The `encodingFormat` property contains an array of formats to describe multiple formats to which the document conforms (in this example, the document is both conformant with XML and the EML metadata dialect).

Back to [top](#top)

### Distributions

Where the [schema:url](https://schema.org/url) property of the Dataset should point to a landing page, the way to describe how to download the data in a specific format is through the [schema:distribution](https://schema.org/distribution) property. The "distribution" property describes where to get the data and in what format by using the [schema:DataDownload](https://schema.org/DataDownload) type. If your dataset is not accessible through a direct download URL, but rather through a service URL that may need input parameters jump to the next section [Accessing Data through a Service Endpoint](#dataset-service-endpoint).

![Distributions](/assets/diagrams/dataset/dataset_distribution.svg "Dataset - Distributions")

For data available in multipe formats, there will be multiple values of the [schema:DataDownload](https://schema.org/DataDownload):

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
  <strong>"distribution": {
    "@type": "DataDownload",
    "contentUrl": "https://www.sample-data-repository.org/dataset/472032.tsv",
    "encodingFormat": "text/tab-separated-values"
  }</strong>
}
</pre>


#### Accessing Data through a Service Endpoint

If access to the data requires some input parameters before a download can occur, we can use the [schema:potentialAction](https://schema.org/potentialAction) in this way:

![Service Endpoint](/assets/diagrams/dataset/dataset_service-endpoint.svg "Dataset - Service Endpoint")

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
  <strong>"potentialAction": {
    "@type": "SearchAction",
    "target": {
        "@type": "EntryPoint",
        "contentType": ["application/x-netcdf", "text/tab-separated-values"],
        "urlTemplate": "https://www.sample-data-repository.org/dataset/1234/download?format={format}&startDateTime={start}&endDateTime={end}&bounds={bbox}",
        "description": "Download dataset 1234 based on the requested format, start/end dates and bounding box",
        "httpMethod": ["GET", "POST"]
    },
    "query-input": [
      {
        "@type": "PropertyValueSpecification",
        "valueName": "format",
        "description": "The desired format requested either 'application/x-netcdf' or 'text/tab-separated-values'",
        "valueRequired": true,
        "defaultValue": "application/x-netcdf",
        "valuePattern": "(application\/x-netcdf|text\/tab-separated-values)"
      },
      {
        "@type": "PropertyValueSpecification",
        "valueName": "start",
        "description": "A UTC ISO DateTime",
        "valueRequired": false,
        "valuePattern": "(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(.[0-9]+)?(Z)?"
      },
      {
        "@type": "PropertyValueSpecification",
        "valueName": "end",
        "description": "A UTC ISO DateTime",
        "valueRequired": false,
        "valuePattern": "(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(.[0-9]+)?(Z)?"
      },
      {
        "@type": "PropertyValueSpecification",
        "valueName": "bbox",
        "description": "Two points in decimal degrees that create a bounding box fomatted at 'lon,lat' of the lower-left corner and 'lon,lat' of the upper-right",
        "valueRequired": false,
        "valuePattern": "(-?[0-9]+(.[0-9]+)?),[ ]*(-?[0-9]+(.[0-9]+)?)[ ]*(-?[0-9]+(.[0-9]+)?),[ ]*(-?[0-9]+(.[0-9]+)?)"
      }
    ]
  }</strong>
}
</pre>

Here, we use the [schema:SearchAction](https://schema.org/SearchAction) type becuase it lets you define the query parameters and HTTP methods so that machines can build user interfaces to collect those query parmaeters and actuate a request to provide the user what they are looking for.

Back to [top](#top)

### Temporal Coverage

Temporal coverage is a difficult concept to cover across all the possible scenarios. Schema.org uses [ISO 8601 standard](https://en.wikipedia.org/wiki/ISO_8601) to describe time intervals and time points, but doesn't provide capabilities for geologic time scales or dynamically generated data up to present time. We ask for your [feedback on any temporal coverages you may have that don't currently fit into schema.org](https://github.com/earthcubearchitecture-project418/p418Vocabulary/issues). You can follow [similar issues at the schema.org Github issue queue](https://github.com/schemaorg/schemaorg/issues/242)

![Temporal](/assets/diagrams/dataset/dataset_temporal-coverage.svg "Dataset - Temporal")

To represent a single date and time:
<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
  <strong>"temporalCoverage": "2018-01-22T14:51:12+00:00"</strong>
}
</pre>

Or a single date:
<pre>
{
  ...
  <strong>"temporalCoverage": "2018-01-22"</strong>
}
</pre>

Or a date range:
<pre>
{
  ...
  <strong>"temporalCoverage": "2012-09-20/2016-01-22"</strong>
}
</pre>

Or an open-ended date range _(thanks to [@lewismc](https://github.com/lewismc) for this example from [NASA PO.DAAC](https://github.com/lewismc/podaac.geosci.schema.org/blob/master/Dataset.jsonld))_ :
<pre>
{
  ...
  <strong>"temporalCoverage": "2012-09-20/.."</strong>
}
</pre>

Schema.org also lets you provide date ranges and other temporal coverages through the [DateTime](https://schema.org/DateTime) data type and [URL](https://schema.org/URL). For more granular temporal coverages go here: [https://schema.org/DateTime](https://schema.org/DateTime).

One example of a URL temporal coverage might be for named periods in time:

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
  <strong>"temporalCoverage": "http://sweetontology.net/stateTimeGeologic/Paleocene"</strong>
}
</pre>

Even though `http://sweetontology.net/stateTimeGeologic/Paleocene` is a valid RDF resource, and the natural tendency would be to use it as such:
```
"temporalCoverage": { "@id": "http://sweetontology.net/stateTimeGeologic/Paleocene" }
```
Because [schema:URL (rdf)](https://schema.org/URL.rdf) is defined as an rdfs:Class, these URLs can be interepreted by harvesters as an RDF resource, but that is a decision left to the harvester, not the publisher. So here, the publisher simply uses the resources URL.

Back to [top](#top)

### Spatial Coverage

![Spatial](/assets/diagrams/dataset/dataset_spatial-coverage.svg "Dataset - Spatial")

Used to document the location on Earth that is the focus of the  dataset content, using  [schema:Place](https://schema.org/Place). Recommended practice is to use the [schema:geo](https://schema.org/geo) property with either a [schema:GeoCoordinates](https://schema.org/GeoCoordinates) object to specify a point location, or a [schema:GeoShape](https://schema.org/GeoShape) object to specify a line or area coverage extent. Coordinates describing these extents are expressed as latitude longitude tuples (in that order) using decimal degrees. 

Schema.org documentation does not specify a convention for the coordinate reference system, our recommended practice is to use [WGS84](EPSG:3857) for at least one spatial coverage description if applicable. Spatial coverage location using other coordinate systems can be included, see recommendation for specifying coordinate reference systems, [below](#spatial_reference-system).  

#### Point location
A point location specified by a  [schema:GeoCoordinates](https://schema.org/GeoCoordinates) object with   [schema:latitude](https://schema.org/latitude) and [schema:longitude](https://schema.org/longitude) properties. 
*Not Recommended* the [schema:Place](https://schema.org/Place) definition allows the latitude and longitude of a point location to be specified as properties directly of place; although this is more succinct, it makes parsing the metadata more complex and should be avoided.

Point locations are recommended for data that is associated with specific sample locations, particularly if these are widely spaced such that an enclosing bounding box would be a misleading representation of the spatial location. Be aware that some client applications might only index or display bounding box extents or a single point location. 

<a id="spatial_point"></a> A schema:Dataset that is about a point location would documented in this way:
<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton ....",
  ...
  <strong>"spatialCoverage": {
    "@type": "Place",
    "geo": {
      "@type": "GeoCoordinates",
      "latitude": 39.3280
      "longitude": 120.1633
    }
  }</strong>
}
</pre>

#### GeoShape location extent

<a id="spatial_shape"></a>A [schema:GeoShape](https://schema.org/GeoShape) can describe spatial coverage as a line (e.g. a ship track), a bounding box, a polygon, or a circle. The geometry is described with a set of latitude/longitude pairs. The spatial definitions were added to schema.org early in its [development](https://github.com/schemaorg/schemaorg/issues/8#issuecomment-97667478) based on the [GeoRSS specification](http://docs.opengeospatial.org/cs/17-002r1/17-002r1.html#21). The documentation for [schema:GeoShape](https://schema.org/GeoShape) states "Either whitespace or commas can be used to separate latitude and longitude; whitespace should be used when writing a list of several such points." At least for bounding boxes (see the discussion below), it appears that the Google Dataset Search parsing of the coordinate strings depends on whether a comma or space is used to delimit the coordinates in an individual tuple.  

Be aware that some client applications might only index or display bounding box extents. 

* [line](https://schema.org/line) - a series of two or more points.
* [polygon](https://schema.org/polygon) - a series of four or more points where the first and final points are identical.
* [box](https://schema.org/box) - A rectangular (in lat-long space) extent specified by two points, the first in the lower left (southwest) corner and the second in the upper right (northeast) corner.
* [circle](https://schema.org/circle) - A circular region of a specified radius centered at a specified latitude and longitude, represented as a coordinate pair followed by a radius in meters. *Not recommended for use*.


Examples
<a id="geoshape-line">Linear spatial location</a>
A line spatial location. Useful for data that were collected along a traverse, ship track, flight line or other linear sampling feature. 

<pre>
  <strong>"spatialCoverage": {
    "@type": "Place",
    "geo": {
      "@type": "GeoShape",
      "line": "39.3280 120.1633 40.445 123.7878"
    }
  }</strong>
}
</pre>

<a id="geoshape-polygon">Polygon spatial location</a>
A polygon provides the most precise approach to delineating the spatial extent of the focus area for a dataset, but polygon spatial locations might not be recognized (indexed, displayed) by some client applications. 

<pre>
  <strong>"polygon": "39.3280 120.1633 40.445 123.7878 41 121 39.77 122.42 39.3280 120.1633"</strong>
</pre>

<a id="geoshape-box">Bounding Boxes</a>
A GeoShape box defines an area on the surface of the earth defined by point locations of the southwest corner and northeast corner of the rectangle in latitude-longitude coordinates. Point locations are tuples of {latitude  east-longitude} (y x). The schema.org [GeoShape](https://schema.org/GeoShape) documentation states "*Either whitespace or commas can be used to separate latitude and longitude; whitespace should be used when writing a list of several such points*." Since the box is a list of points, a space should be used to separate the latitude and longitude values. The two corner coordinate points are separated by a space. 'East longitude' means positive longitude values are east of the prime (Greenwich) meridian.  A box where 'lower-left' (southwest) corner is 39.3280/120.1633 and 'upper-right' (northeast) corner is 40.445/123.7878 would be encoded thus: 
<pre>
  <strong>"box": "39.3280 120.1633 40.445 123.7878"</strong>
</pre>

NOTE-- see [discussion in GitHub issue 101](https://github.com/ESIPFed/science-on-schema.org/issues/101#issuecomment-720808142) on what works with Google Dataset search to display spatial locatation in their search results.

East longitude values can be reported 0 <= X <= 360 or -180 <= X <= 180. Some applications will fail under one or the other of these conventions. Recommendation is to use -180 <= X <= 180, consistent with the [WKT specification](https://docs.opengeospatial.org/is/18-010r7/18-010r7.html#33).  Following this recommendation, bounding boxes that cross the antimeridian at ±180° longitude, the West longitude value will be numerically greater than the East longitude value. For example, to describe Fiji the box might be
<pre>
  <strong>"box": "-19 176 -15 -178"</strong>
</pre>

NOTES: Some spatial data processors will not correctly interpret the bounding coordinates across the antimeridian even if they follow the recommended southwest, northeast corner convention, resulting in boxes that span the circumference of the Earth, excluding the actual area of interest. For applications operating with data in the vicinity of longitude 180, testing is strongly recommended to determine if it works for bounding boxes crossing the antimeridian (+/- 180); an alternative is to define two bounding boxes, one on each side of 180.

For bounding boxes that include the north or south pole, schema:box will not work. Recommended practice is to use a schema:polygon to describe spatial location extents that include the poles.  

<a id="spatial_multiple-geometries">Multiple geometries</a>
If you have multiple geometries, you can publish those by making the [schema:geo](https://schema.org/geo) field an array of [GeoShape](https://schema.org/GeoShape) or [GeoCoordinates](https://schema.org/GeoCoordinates) like so:

<pre>
{
  ...
  "spatialCoverage": {
    "@type": "Place",
    <strong>"geo": [</strong>
      {
        "@type": "GeoCoordinates",
        "latitude": -17.65,
        "longitude": 50
      },
      {
        "@type": "GeoCoordinates",
        "latitude": -19,
        "longitude": 51
      },
      ...
    <strong>]</strong>
  }
  ...
}
</pre>

Be aware that some client application might not index or display multiple geometries.

<a id="spatial_reference-system"></a>
A Spatial Reference System (SRS) or Coordinate Reference System (CRS) is the method for defining the [frame of reference for geospatial location representation](https://developers.arcgis.com/documentation/core-concepts/spatial-references/). Schema.org currently has no defined property for specifying a Spatial Reference System; the assumption is that coordinates are WGS84 decimal degrees. 

In the mean time, to represent an SRS in schema.org, we recommend using the [schema:additionalProperty](https://schema.org/additionalProperty) property to specify an object of type [schema:PropertyValue](https://schema.org/PropertyValue), with a [schema:propertyID](https://schema.org/propertyID) of 
[http://dbpedia.org/resource/Spatial_reference_system](http://dbpedia.org/resource/Spatial_reference_system) to identify the property as a spatial reference system, and the schema:PropertyValue/schema:value is a URI (IRI) that identifies a specific SRS. Some commonly used values are: 

| Spatial Reference System | IRI                                          |
|--------------------------|----------------------------------------------|
| WGS84                    | http://www.w3.org/2003/01/geo/wgs84_pos#lat_long     |
| CRS84                    | http://www.opengis.net/def/crs/OGC/1.3/CRS84 |
| EPSG:26911               | https://spatialreference.org/ref/epsg/nad83-utm-zone-11n/  |
| EPSG:3413                | https://spatialreference.org/ref/epsg/wgs-84-nsidc-sea-ice-polar-stereographic-north/ |

NOTE: Beware of coordinate order differences. WGS84 in the table above specifies latitude, longitude coordinate order, whereas CRS84 specifies longitude, latitude order (like GeoJSON). WGS84 is the assumed typical value for coordinates, so in general the SRS does not need to be specified. 

A spatial reference system can be added in this way:

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/",
    <strong>"dbpedia": "http://dbpedia.org/resource/"</strong>
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
  "spatialCoverage": {
    "@type": "Place",
    "geo": {
      "@type": "GeoShape",
      "line": "39.3280 120.1633 40.445 123.7878"
    },
    <strong>"additionalProperty": {
      "@type": "PropertyValue",
      "propertyID":"http://dbpedia.org/resource/Spatial_reference_system",
      "value": "http://www.w3.org/2003/01/geo/wgs84_pos#lat_long"
    }</strong>
  }
}
</pre>

Back to [top](#top)

### Roles of People

People can be linked to datasets using three fields: author, creator, and contributor. Since  [schema:contributor](https://schema.org/contributor) is defined as a secondary author, and [schema:Creator](https://schema.org/creator) is defined as being synonymous with the [schema:author](https://schema.org/author) field, we recommend using the more expressive fields creator and contributor, but using any of these fields is acceptable. Becuase there are more things that can be said about how and when a person contributed to a Dataset, we use the [schema:Role](https://schema.org/Role). You'll notice that the schema.org documentation does not state that the Role type is an expected data type of author, creator and contributor, but that is addressed in this [blog post introducing Role into schema.org](http://blog.schema.org/2014/06/introducing-role.html). *Thanks to [Stephen Richard](https://github.com/smrgeoinfo) for this contribution*

![People Roles](/assets/diagrams/dataset/dataset_people-roles.svg "Dataset - People Roles")

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
  <strong>"creator": [
    {
      "@id": "https://www.sample-data-repository.org/person-role/472036",
      "@type": "Role",
      "roleName": "Principal Investigator",
      "creator": {
        "@id": "https://www.sample-data-repository.org/person/51317",
        "@type": "Person",
        "name": "Dr Uta Passow",
        "givenName": "Uta",
        "familyName": "Passow",
        "url": "https://www.sample-data-repository.org/person/51317"
      }
    },
    {
      "@id": "https://www.sample-data-repository.org/person-role/472038",
      "@type": "Role",
      "roleName": "Co-Principal Investigator",
      "url": "https://www.sample-data-repository.org/person-role/472038",
      "creator": {
        "@id": "https://www.sample-data-repository.org/person/50663",
        "@type": "Person",
        "identifier": {
	  "@id": "https://orcid.org/0000-0003-3432-2297",
          "@type": "PropertyValue",
          "propertyID": "https://registry.identifiers.org/registry/orcid",
          "url": "https://orcid.org/0000-0003-3432-2297",
          "value": "orcid:0000-0003-3432-2297"
        },
        "name": "Dr Mark Brzezinski",
        "url": "https://www.sample-data-repository.org/person/50663"
      }
    }</strong>
}
</pre>
NOTE that the Role inherits the property `creator` and `contributor` from the Dataset when pointing to the [schema:Person](https://schema.org/Person).

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/",
    ...
  },
  <strong>"@type": "Dataset"</strong>,
  ...
  <strong>"creator"</strong>: [
    {
      "@id": "https://www.sample-data-repository.org/person-role/472036",
      <strong>"@type": "Role"</strong>,
      "roleName": "Principal Investigator",
      "url": "https://www.sample-data-repository.org/person-role/472036",
      <strong>"creator":</strong> {
        "@id": "https://www.sample-data-repository.org/person/51317",
        "@type": "Person",
        "name": "Dr Uta Passow",
        "givenName": "Uta",
        "familyName": "Passow",
        "url": "https://www.sample-data-repository.org/person/51317"
      }
    }
}
</pre>

If a single Person plays multiple roles on a Dataset, each role should be explicitly defined in this way:

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
  "creator": [
    {
      "@id": "https://www.sample-data-repository.org/person-role/472036",
      "@type": "Role",
      "roleName": "Principal Investigator",
      "url": "https://www.sample-data-repository.org/person-role/472036",
      "creator": {
        <strong>"@id": "https://www.sample-data-repository.org/person/51317"</strong>,
        "@type": "Person",
        "name": "Dr Uta Passow",
        "givenName": "Uta",
        "familyName": "Passow",
        "url": "https://www.sample-data-repository.org/person/51317"
      }
    },
    <strong>{
      "@id": "https://www.sample-data-repository.org/person-role/472037",
      "@type": "Role",
      "roleName": "Contact",
      "url": "https://www.sample-data-repository.org/person-role/472037",
      "creator": { "@id": "https://www.sample-data-repository.org/person/51317" }
    }</strong>,
    {
      "@id": "https://www.sample-data-repository.org/person-role/472038",
      "@type": "Role",
      "roleName": "Co-Principal Investigator",
      "url": "https://www.sample-data-repository.org/person-role/472038",
      "creator": {
        "@id": "https://www.sample-data-repository.org/person/50663",
        "@type": "Person",
        "identifier": {
	  "@id": "https://orcid.org/0000-0003-3432-2297",
          "@type": "PropertyValue",
          "propertyID": "https://registry.identifiers.org/registry/orcid",
          "url": "https://orcid.org/0000-0003-3432-2297",
          "value": "orcid:0000-0003-3432-2297"
        },
        "name": "Dr Mark Brzezinski",
        "url": "https://www.sample-data-repository.org/person/50663"
      }
    }
}
</pre>

Notice that since Uta Passow has already been defined in the document with `"@id": "https://www.sample-data-repository.org/person/51317"` for her role as Principal Investigator, the `@id` can be used for her role as Contact by defining the Role's creator as `"creator": { "@id": "https://www.sample-data-repository.org/person/51317" }`.

Back to [top](#top)

### Publisher / Provider

![Publisher/Provider](/assets/diagrams/dataset/dataset_publisher-provider.svg "Dataset - Publisher/Provider")

If your repository is the publisher and/or provider of the dataset then you don't have to describe your repository as a [schema:Organziation](https://schema.org/Organization) **if** your repository markup includes the **`@id`**. For example, if you published repository markup such as:
<pre>
{
  "@context": {...},
  "@type": ["Service", "Organization"],
  ...
  <strong>"@id": "https://www.sample-data-repository.org"</strong>
  ...
}
</pre>

then you can reuse that `@id` here. Harvesters such as Google and Project418 will make the appropriate linkages and your dataset publisher/provider can be published in this way:

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
<strong>"provider": {
    "@id": "https://www.sample-data-repository.org"
  },
  "publisher": {
    "@id": "https://www.sample-data-repository.org"
  }</strong>
}
</pre>

Otherwise, you can define the organization inline in this way:

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
<strong>"provider": {
    "@id": "https://www.sample-data-repository.org",
    "@type": "Organization",
    "legalName": "Sample Data Repository Office",
    "name": "SDRO",
    "sameAs": "http://www.re3data.org/repository/r3dxxxxxxxxx",
    "url": "https://www.sample-data-repository.org"
  },
  "publisher": {
    "@id": "https://www.sample-data-repository.org"
  }</strong>
}
</pre>

Back to [top](#top)


### Funding
![Funding](/assets/diagrams/dataset/dataset_funding.svg "Dataset - Funding")

Linking a Dataset to its funding can be acheived by adding a [schema:MonetaryGrant](https://schema.org/MonetaryGrant) object on your webpage. In order to do this, we have to modify the structure of our JSON-LD to include multiple top-level items, and make sure that our Dataset uses the `@id` to identify its URI. This `@id` will be used by the MonetaryGrant to say it funded the Dataset. First, we add the `@id` to our Dataset:
<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  <strong>"@id": "http://www.sample-data-repository.org/dataset/123",</strong>
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
}
</pre>

Next, we must make our JSON-LD allow multiple top-level items by using the `@graph` property.
<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  <strong>"@graph":[{</strong>
      "@id": "http://www.sample-data-repository.org/dataset/123",
      "@type": "Dataset",
      "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
      ...
    <strong>}
  ]</strong>
}
</pre>

You can now see that the Dataset object `{}` is now the first element in the `@graph` array. Next, we add our [schema:MonetaryGrant](https://schema.org/MonetaryGrant) object.

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@graph":[{
      "@id": "http://www.sample-data-repository.org/dataset/123",
      "@type": "Dataset",
      "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
      ...
    }<strong>,
    {
      "@type": "MonetaryGrant",
      "fundedItem": { "@id": "http://www.sample-data-repository.org/dataset/123" },
      "name": "NSF Award# 143211",
      "funder": {
        "@type": "Organization",
        "name": "National Science Foundation",
        "url": "http://www.nsf.gov"
      },
      "sameAs": "https://www.nsf.gov/awardsearch/showAward?AWD_ID=1435578",
      "identifier": "143211"
    }
  ]</strong>
}
</pre>

Now, because there are two top-level items on this webpage, harvesters will be unsure which element is the main resource. But, we can specify this by using the [schema:mainEntityOfPage](https://schema.org/mainEntityOfPage) property.

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@graph":[{
      "@id": "http://www.sample-data-repository.org/dataset/123",
      "@type": "Dataset",
      "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
      <strong>"mainEntityOfPage": {
         "@type": "WebPage",
         "@id": "http://www.sample-data-repository.org/dataset/123"
      },</strong>
      ...
    },
    {
      "@type": "MonetaryGrant",
      "fundedItem": { "@id": "http://www.sample-data-repository.org/dataset/123" },
      "name": "NSF Award# 143211",
      "funder": {
        "@type": "Organization",
        "name": "National Science Foundation",
        "url": "http://www.nsf.gov"
      },
      "sameAs": "https://www.nsf.gov/awardsearch/showAward?AWD_ID=1435578",
      "identifier": "143211"
    }
  ]
}
</pre>

Back to [top](#top)

### License

Link a Dataset to its license to document legal constraints by adding a [schema:license](https://schema.org/license) property. The [guide](https://developers.google.com/search/docs/data-types/dataset) recommends providing a URL that unambiguously identifies a specific version of the license used, but for many licenses it is hard to determine what that URL should be. Thus, we recommend that the license URL be drawn from the [SPDX license list](https://spdx.org/licenses/), which provides a curated list of licenses and their properties that is well maintained. For each SPDX entry, SPDX provides a canonical URL for the license (e.g., `http://spdx.org/licenses/CC0-1.0`), a unique `licenseId` (e.g., `CC0-1.0`), and other metadata about the license. Here's an example using the SPDX license URI for the Creative Commons CC-0 license:

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/",
  },
  "@id": "http://www.sample-data-repository.org/dataset/123",
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  <strong>"license": "http://spdx.org/licenses/CC0-1.0"</strong>
  ...
}
</pre>

SPDX URIs for each license can be found by finding the appropriate license in the [SPDX license list](https://spdx.org/licenses/), and then remove the final `.html` extension from the filename.  For example, in the table one can find the license page for Apache at the URI `https://spdx.org/licenses/Apache-2.0.html`, which can be converted into the associated linked data URI by removing the `.html`, leaving us with `https://spdx.org/licenses/Apache-2.0`. Alternatively, one can find the license file in the [structured data listings](https://github.com/spdx/license-list-data/tree/master/rdfturtle) and copy the URL from the associated file. For example, the URL for the Apache-2.0 license is listed in the file at https://github.com/spdx/license-list-data/blob/master/rdfturtle/Apache-2.0.turtle.

While many licenses are ambiguous about the license URI for the license, the Creative Commons licenses and a few others are exceptions in that they provide extremely consistent URIs for each license, and these are in widespread use.  So, while we recommend using the SPDX URI, we recognize that some sites may want to use the CC license URIs directly, which is helpful in recognizing the license.  In this case, we recommend that the SPDX URI still be used as described above, and the other URI also be provided as well in a list. Here's an example using the traditional Creative Commons URI along with the SPDX URI.
<pre>
{
  "@context": {
    "@vocab": "https://schema.org/",
  },
  "@id": "http://www.sample-data-repository.org/dataset/123",
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  <strong>"license": [ "http://spdx.org/licenses/CC0-1.0", "https://creativecommons.org/publicdomain/zero/1.0"]</strong>
  ...
}
</pre>

The following table contains the SPDX URIs for some of the most common licenses.  Others can be looked up at the SPDX site as described above.

|License          |  SPDX URI                                  |
|-----------------|--------------------------------------------|
|Apache-2.0       | https://spdx.org/licenses/Apache-2.0       |
|BSD-3-Clause     | https://spdx.org/licenses/BSD-3-Clause     |
|CC-BY-3.0        | https://spdx.org/licenses/CC-BY-3.0        |
|CC-BY-4.0        | https://spdx.org/licenses/CC-BY-4.0        |
|CC-BY-SA-4.0     | https://spdx.org/licenses/CC-BY-SA-4.0     |
|CC0-1.0          | https://spdx.org/licenses/CC0-1.0          |
|GPL-3.0-only     | https://spdx.org/licenses/GPL-3.0-only     |
|GPL-3.0-or-later | https://spdx.org/licenses/GPL-3.0-or-later |
|MIT              | https://spdx.org/licenses/MIT              |
|MIT-0            | https://spdx.org/licenses/MIT-0            |

Back to [top](#top)

### Provenance Relationships

High level relationships that link datasets based on their processing workflows and versioning relationships are critical for data consumers and search engines to link different versions of a [schema:Dataset](https://schema.org/Dataset), to clarify when a dataset is derived from one or more source Datasets, and to specify linkages to the software and activities that created these derived datasets for reproducibility. Collectively, this is provenance information.

The [PROV-O](https://www.w3.org/TR/prov-o/) recommendation provides the widely-adopted vocabulary for representing this type of provenance information, and should be used within Dataset descriptions, as most of the necessary provenance properties are currently missing from schema.org. The main exception is [`schema:isBasedOn`](https://schema.org/isBasedOn), which provides a predicate for indicating that a Dataset was derived from one or more source Datasets. Producers and consumers should interpret `schema:isBasedOn` to be an equivalent property to `prov:wasDerivedFrom` (in the `owl:equivalentProperty` sense). Either is acceptable for representing derivation relationships, but there is utility in expressing the relationship with both predicates for consumers that might only be looking for one or the other. When other `PROV` predicates are used, it is preferred to use `prov:wasDerivedFrom` for consistency.

We recommend providing provenance information about data processing workflows, data derivation relationships, and versioning information using PROV-O and schema.org predicates, and describe the structures to do this in the following subsections. Aggregators and search systems should use these properties to cluster and cross-link versions of Datasets, and to provide bi-directional linkages to source and derived data products.

#### Indicating an earlier version: `prov:wasRevisionOf`

![Prov_versions](/assets/diagrams/dataset/dataset_prov_revision.svg "Dataset - Revisions")

Link a Dataset to a prior version that it replaces by adding a [`prov:wasRevisionOf`](https://www.w3.org/TR/prov-o/#wasRevisionOf) property. This indicates that the current `schema:Dataset` replaces or obsoletes the source Dataset indicated.  The value of the `prov:wasRevisionOf` should be the canonical IRI for the identifier for the original dataset, preferably to a persistently resolvable IRI such as as a DOI, but other persistent identifiers for the dataset can be used.

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "https://doi.org/10.xxxx/Dataset-2.v2",
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  <strong>"prov:wasRevisionOf": { "@id": "https://doi.org/10.xxxx/Dataset-2.v1" }</strong>
}
</pre>

#### Indicating a source dataset: `schema:isBasedOn` and `prov:wasDerivedFrom`

A derived Dataset is one in which the values in the data are somehow related or created from the values in one or more source datasets. For example, raw voltage values from a sensor might be recorded in a raw data file, which is then processed through calibration functions to produce a derived dataset with values in scientific units. Other examples of derived data include data that has been error corrected, gap-filled, or integrated with other sources.

To indicate that a Dataset has been derived from a source Dataset, use the [`prov:wasDerivedFrom`](https://www.w3.org/TR/prov-o/#wasDerivedFrom) property. This indicates that the current `schema:Dataset` was created in whole or in part from content in the source Dataset, and therefore does not represent an independent set of measurements.  The value of the `prov:wasDerivedFrom` should be the canonical IRI for the identifer for the source dataset, preferably to a persistently resolvable IRI such as as a DOI, but other persistent identifiers for the dataset can be used. In addition, if a persistent identifier for a digital object within a Dataset is available, the `prov:wasDerivedFrom` may also be used to indicate that that digital object was derived from that particular source object, rather than the overall Dataset. This allows one to be more specific about the exact relationship between the source and derived data objects.

In addition to `prov:wasDerivedFrom`, schema.org provides the [`schema:isBasedOn`](https://schema.org/isBasedOn) property, which should be considered to be an equivalent property to `prov:wasDerivedFrom`. For compatibility with schema.org, we recommend that producers use `schema:isBasedOn` in addition to or instead of `prov:wasDerivedFrom` to indicate derivation relationships.

![Prov_derived](/assets/diagrams/dataset/dataset_prov_derived.svg "Dataset - Derivations")

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "https://doi.org/10.xxxx/Dataset-2",
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  <strong>"prov:wasDerivedFrom": { "@id": "https://doi.org/10.xxxx/Dataset-1" }</strong>,
  <strong>"schema:isBasedOn": { "@id": "https://doi.org/10.xxxx/Dataset-1" }</strong>
}
</pre>

#### Indicating a software workflow or processing activity: `prov:used` and `prov:wasGeneratedBy`

Frequently data are processed to create derived Datasets or other products using software programs that use some source data, transform it in various ways, and create the derived products. Understanding these software workflows promotes understanding of the products, and facilitates reproducibility. Describing a software workflow is really just a mechanism to provide more detail about how derived products were created when software was executed. The [ProvONE](https://purl.dataone.org/provone-v1-dev) vocabulary extends PROV to define a specific concept for an execution event (`provone:Execution`) during which a software program (`provone:Program`) is executed. During this execution, the software can use source data (`prov:used`) and generate outputs (`prov:wasGeneratedBy`), which then can be inferred to have been derived from the source data.

![Prov_program](/assets/diagrams/dataset/dataset_prov_program.svg "Dataset - Workflow")

Any portion of the software workflow can be described to increase information about derived datasets. For example, use `prov:used` to link an execution to one or more source datasets, and use `prov:wasGeneratedBy` to link an execution to one or more derived products. When information about the execution event itself is known, use `provone:Execution` to describe that event, and link it to the source and derived products, as well as the program. The program is often a software script that is itself dereferenceable, and may be part of the archived Dataset itself if it has an accessible IRI.

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "provone": "http://purl.dataone.org/provone/2015/01/15/ontology#"
  },
  "@id": "https://doi.org/10.xxxx/Dataset-2",
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  "prov:wasDerivedFrom": { "@id": "https://doi.org/10.xxxx/Dataset-1" },
  "schema:isBasedOn": { "@id": "https://doi.org/10.xxxx/Dataset-1" },
  <strong>"prov:wasGeneratedBy": 
      {
        "@id": "https://example.org/executions/execution-42",
        "@type": "provone:Execution",
        "prov:hadPlan": "https://somerepository.org/datasets/10.xxxx/Dataset-2.v2/process-script.R",
        "prov:used": { "@id": "https://doi.org/10.xxxx/Dataset-1" }
      }</strong>
}
</pre>


Back to [top](#top)

## Advanced Publishing Techniques


### Attaching Physical Samples to a Dataset

Currently, there isn't a great semantic property for a Dataset to distinguish the related physical samples. However, we can use the [schema:hasPart](https://schema.org/hasPart) property to accomplish this without too much compromise. A [GitHub issue](https://github.com/earthcubearchitecture-project418/p418Vocabulary/issues/16) has been setup to follow this scenario. Here is the best way, so far, to link physical samples to a Dataset:

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/",
    "gdx": "https://geodex.org/voc/",
    <strong>"geolink": "http://schema.geolink.org/1.0/base/main#",
    "igsn": "http://pid.geoscience.gov.au/def/voc/igsn-codelists/",</strong>
  },
  "@type": "Dataset",
  ...,
  <strong>"hasPart": [
    {
      "@type": ["CreativeWork", "geolink:PhysicalSample"],
      "identifier": {
        "@id": "https://doi.org/10273/WHO000A53",
        "@type": "PropertyValue",
        "propertyID": "https://registry.identifiers.org/registry/doi",
        "url": "https://doi.org/10273/WHO000A53",
        "value": "IGSN:WHO000A53"
      },
      "spatialCoverage": {
        "@type": "Place",
        "geo": {
          "@type": "GeoCoordinates",
          "latitude": -26.94486389,
          "longitude": 143.43508333,
          "elevation": 219.453
        }
      }
      ...
    },
    {
      "@type": ["CreativeWork", "geolink:PhysicalSample"],
      "identifier": {
        "@id": "https://doi.org/10273/WHO000A67",
        "@type": "PropertyValue",
        "https://registry.identifiers.org/registry/doi",
        "url": "https://doi.org/10273/WHO000A67",
        "value": "IGSN:WHO000A67"
      }
      ...
    }
  ]</strong>
}
</pre>

Here, we use the superclass of a Dataset, the [schema:CreativeWork](https://schema.org/CreativeWork) to also define a Physical Sample. We disambiguate the Creative Work to be a physical sample by using the GeoLink definition in the `@type` field. See the [schema:CreativeWork](https://schema.org/CreativeWork) to for the additional fields available for adding to the physical sample.
