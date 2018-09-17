<a id="top"></a>
![version 0.1.0](https://img.shields.io/badge/version-0.1.0-blue.svg)

# Describing a Dataset

* [Identifier](#identifiers)
* [Variables](#variables)
  * [Using External Vocabularies for Describing Variables](#variables_external-vocab-example)
* [DataCatalog](#catalog)
* [Distributions](#distributions)
   * [Accessing Data through a Service Endpoint](#service-endpoint)
* [Temporal](#temporal)
* [Spatial](#spatial)
  * [Point/Coordinates](#spatial_point)
  * [Multiple geometries](#spatial_multiple-geometries)
* [Authors, Creators, and Contributors](#author-creator-contributor)
* [Publisher/Provider](#publisher-provider)
* [Protocols](#protocols)
* [Funding](#funding)
* [Advanced Publishing Tehcniques(#advanced-publishing)
  * [Linking Physical Samples to Datasets(#physical-sample-igsn)
    

Google has drafted a [guide to help publishers](https://developers.google.com/search/docs/data-types/dataset). The guide describes the only required fields as - name and description.
* [name](https://schema.org/name) - A descriptive name of a dataset (e.g., “Snow depth in Northern Hemisphere”)
* [description](https://schema.org/description) - A short summary describing a dataset.


<pre>
{
  "@context": {
    "@vocab": "http://schema.org/"
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
* [license](https://schema.org/license) - A license under which the dataset is distributed (text or URL).
* [identifier](https://schema.org/identifier) - An identifier for the dataset, such as a DOI. (text,URL, or PropertyValue).
* [variableMeasured](https://schema.org/variableMeasured) - What does the dataset measure? (e.g., temperature, pressure)

![Basic Fields](/assets/diagrams/dataset/dataset_basic-fields.svg "Dataset - Basic Fields")

<pre>
{
  "@context": {
    "@vocab": "http://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  "description": "This dataset includes results of laboratory experiments which measured dissolved organic carbon (DOC) usage by natural bacteria in seawater at different pCO2 levels. Included in this dataset are; bacterial abundance, total organic carbon (TOC), what DOC was added to the experiment, target pCO2 level. ",
  <strong>"url": "https://www.sample-data-repository.org/dataset/472032",
  "sameAs": "https://search.dataone.org/#view/https://www.sample-data-repository.org/dataset/472032",
  "version": "2013-11-21",
  "isAccessibleForFree": true,
  "keywords": "ocean acidification, Dissolved Organic Carbon, bacterioplankton respiration, pCO2, carbon dioxide, oceans",
  "license": "http://creativecommons.org/licenses/by/4.0/"</strong>
}
</pre>

Back to [top](#top)

<a id="identifiers"></a>
Adding the [schema:identifier](https://schema.org/identifier) field can be done in three ways - a text description, a URL, or by using the [schema:PropertyValue](https://schema.org/PropertyValue) type to describe the identifier in more detail.

#### Describing a Dataset Identifier
![Identifiers](/assets/diagrams/dataset/dataset_identifier.svg "Dataset - Identifier")

In it's most basic form, the identifier as text can be published as:

<pre>
{
  "@context": {
    "@vocab": "http://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  "description": "This dataset includes results of laboratory experiments which measured dissolved organic carbon (DOC) usage by natural bacteria in seawater at different pCO2 levels. Included in this dataset are; bacterial abundance, total organic carbon (TOC), what DOC was added to the experiment, target pCO2 level. ",
  "url": "https://www.sample-data-repository.org/dataset/472032",
  "sameAs": "https://search.dataone.org/#view/https://www.sample-data-repository.org/dataset/472032",
  "version": "2013-11-21",
  "keywords": "ocean acidification, Dissolved Organic Carbon, bacterioplankton respiration, pCO2, carbon dioxide, oceans",
  "license": "http://creativecommons.org/licenses/by/4.0/",
  <strong>"identifier": "urn:sdro:dataset:472032"</strong>
}
</pre>

Or as a URL:
<pre>
{
  "@context": {
    "@vocab": "http://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
  <strong>"identifier": "http://id.sampledatarepository.org/dataset/472032/version/1"</strong>
}
</pre>

However, if the identifier is a persistent identifier such as a DOI, ARK, or accession nmumber, then the best way to represent these identifiers is by using a [schema:PropertyValue](https://schema.org/PropertyValue). The PropertyValue allows for more information about the identifier to be represented such as the identifier type or scheme, the identifier's value, it's URL and more. Because of this flexibility, we recommend using PropertyValue for all identifier types. 

For identifiers that do have a well-defined scheme that scopes the identifier value, such as DOI, ARK, ISBN, etc, we can use the [DataCite Ontology Resource Identifier Scheme](https://sparontologies.github.io/datacite/current/datacite.html#d4e638) to specify this identifier scheme:

<pre>
{
  "@context": {
    "@vocab": "http://schema.org/",
    <strong>"datacite": "http://purl.org/spar/datacite/"</strong>
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  "description": "This dataset includes results of laboratory experiments which measured dissolved organic carbon (DOC) usage by natural bacteria in seawater at different pCO2 levels. Included in this dataset are; bacterial abundance, total organic carbon (TOC), what DOC was added to the experiment, target pCO2 level. ",
  "url": "https://www.sample-data-repository.org/dataset/472032",
  "sameAs": "https://search.dataone.org/#view/https://www.sample-data-repository.org/dataset/472032",
  "version": "2013-11-21",
  "keywords": "ocean acidification, Dissolved Organic Carbon, bacterioplankton respiration, pCO2, carbon dioxide, oceans",
  "license": "http://creativecommons.org/licenses/by/4.0/",
  <strong>"identifier": {
    "@type": ["PropertyValue", "datacite:ResourceIdentifier"],
    "datacite:usesIdentifierScheme": { "@id": "datacite:doi" },
    "propertyID": "DOI",
    "url": "https://doi.org/10.1575/1912/bco-dmo.665253",
    "value": "10.1575/1912/bco-dmo.665253"
  }</strong>
}
</pre>

[schema:Dataset](https://schema.org/Dataset) also defines a field for the [schema:citation](https://schema.org/citation) as either text or a [schema:CreativeWork](https://schema.org/CreativeWork). To provide citation text:

NOTE: If you have a DOI, the citation text can be [automatically generated](https://citation.crosscite.org/docs.html#sec-4-1) for you by querying a DOI URL with the Accept Header of 'text/x-bibliography'.

<pre>
{
  "@context": {
    "@vocab": "http://schema.org/",
    <strong>"datacite": "http://purl.org/spar/datacite/"</strong>
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  "description": "This dataset includes results of laboratory experiments which measured dissolved organic carbon (DOC) usage by natural bacteria in seawater at different pCO2 levels. Included in this dataset are; bacterial abundance, total organic carbon (TOC), what DOC was added to the experiment, target pCO2 level. ",
  "url": "https://www.sample-data-repository.org/dataset/472032",
  "sameAs": "https://search.dataone.org/#view/https://www.sample-data-repository.org/dataset/472032",
  "version": "2013-11-21",
  "keywords": "ocean acidification, Dissolved Organic Carbon, bacterioplankton respiration, pCO2, carbon dioxide, oceans",
  "license": "http://creativecommons.org/licenses/by/4.0/",
  "identifier": {
    "@id": "https://doi.org/10.1575/1912/bco-dmo.665253",
    "@type": ["PropertyValue", "datacite:Identifier"],
    "propertyID": "http://purl.org/spar/datacite/doi",
    "url": "https://doi.org/10.1575/1912/bco-dmo.665253",
    "value": "10.1575/1912/bco-dmo.665253"
   },
   <strong>"citation": "J.Smith 'How I created an awesome dataset’, Journal of Data Science, 1966"</strong>
}
</pre>

Back to [top](#top)

<a id="variables"></a>
Adding the [schema:variableMeasured](https://schema.org/variableMeasured) field can be done in two ways - a text description of each variable or by using the [schema:PropertyValue](https://schema.org/PropertyValue) type to describe the variable in more detail. We highly recommend using the [schema:PropertyValue](https://schema.org/PropertyValue).

#### Describing a Dataset's Variables
![Variables](/assets/diagrams/dataset/dataset_identifier.svg "Dataset - Variables")

In it's most basic form, the variable as a [schema:PropertyValue](https://schema.org/PropertyValue) can be published as:

<pre>
{
  "@context": {
    "@vocab": "http://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
  <strong>"variableMeasured": [
    {
      "@type": ["PropertyValue"],
      "name": "Bottle identifier",
      "description": "The bottle number for each associated measurement."
    },
    ...
  ]</strong>
}
</pre>
<a id="variables_external-vocab-example"></a>
A fully-fleshed out example that uses a vocabulary to describe the variable can be published as:

<pre>
{
  "@context": {
    "@vocab": "http://schema.org/",
    "datacite": "http://purl.org/spar/datacite/",
    <strong>"gsn-quantity": "http://www.geoscienceontology.org/geo-lower/quantity#"</strong>
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
  "variableMeasured": [
    {
      <strong>"@type": ["PropertyValue", "gsn-quantity:latitude"],</strong>
      "name": "latitude",
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

<a id="catalog"></a>
#### Describing a Dataset's Catalog

For some repositories, defining a one or many data collections helps contextualize the datasets. In schema.org, you define these collections using [schema:DataCatalog](https://schema.org/DataCatalog).

![DataCatalog](html/voc/static/schema/diagrams/dataset-catalog.png "Dataset - Catalog")

The most optimal way to use these DataCatalogs for a repository is to define these catalogs as an ["offering" of your repository](#repository-offercatalog) and including the `@id` property to be reused in the dataset JSON-LD. For example, the repository JSON-LD defines a [schema:DataCatalog](https://schema.org/DataCatalog) with the

`"@id": "https://www.sample-data-repository.org/collection/biological-data"`.

In the dataset JSON-LD, we reuse that `@id` to say a dataset belongs in that catalog:

<pre>
{
  "@context": {
    "@vocab": "http://schema.org/",
    "datacite": "http://purl.org/spar/datacite/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
  <strong>"includedInDataCatalog": {
    "@id": "https://www.sample-data-repository.org/collection/biological-data"
  }</strong>
}
</pre>

Back to [top](#top)

<a id="distributions"></a>
#### Describing a Dataset's Distributions

Where the [schema:url](https://schema.org/url) property of the Dataset should point to a landing page, the way to describe how to download the data in a specific format is through the [schema:distribution](https://schema.org/distribution) property. The "distribution" property describes where to get the data and in what format by using the [schema:DataDownload](https://schema.org/DataDownload) type. If your dataset is not accessible through a direct download URL, but rather through a service URL that may need input parameters jump to the next section [Accessing Data through a Service Endpoint](#dataset-service-endpoint).

![Distributions](html/voc/static/schema/diagrams/dataset-distribution.png "Dataset - Distributions")

For data available in multipe formats, there will be multiple values of the [schema:DataDownload](https://schema.org/DataDownload):

<pre>
{
  "@context": {
    "@vocab": "http://schema.org/",
    "datacite": "http://purl.org/spar/datacite/"
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

<a id="service-endpoint"></a>
##### Accessing Data through a Service Endpoint

If access to the data requires some input parameters before a download can occur, we can use the [schema:potentialAction](https://schema.org/potentialAction) in this way:

<pre>
{
  "@context": {
    "@vocab": "http://schema.org/",
    "datacite": "http://purl.org/spar/datacite/"
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

<a id="temporal"></a>
#### Describing a Dataset's Temporal Coverage

Temporal coverage is a difficult concept to cover across all the possible scenarios. Schema.org uses [ISO 8601 standard](https://en.wikipedia.org/wiki/ISO_8601) to describe time intervals and time points, but doesn't provide capabilities for geologic time scales or dynamically generated data up to present time. We ask for your [feedback on any temporal coverages you may have that don't currently fit into schema.org](https://github.com/earthcubearchitecture-project418/p418Vocabulary/issues). You can follow [similar issues at the schema.org Github issue] queue(https://github.com/schemaorg/schemaorg/issues/242)

![Temporal](html/voc/static/schema/diagrams/dataset-temporal.png "Dataset - Temporal")

To represent a single date and time:
<pre>
{
  "@context": {
    "@vocab": "http://schema.org/",
    "datacite": "http://purl.org/spar/datacite/"
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

Schema.org also lets you provide date ranges and other temporal coverages through the [DateTime](http://schema.org/DateTime) data type. For more granular temporal coverages go here: [http://schema.org/DateTime](http://schema.org/DateTime).


Back to [top](#top)

<a id="spatial"></a>
#### Describing a Dataset's Spatial Coverage

![Spatial](html/voc/static/schema/diagrams/dataset-spatial.png "Dataset - Spatial")

The types of spatial coverages in schema.org are

* [point](https://schema.org/GeoCoordinates) - specify the [schema:latitude](https://schema.org/latitude) and [schema:longitude](https://schema.org/longitude) properties of the schema:GeoCoordinates]() type.

The following shapes use the [schema:GeoShape](https://schema.org/GeoShape) type where a 'point' is defined as a latitude/longitude pair separated by a comma.

* [line](https://schema.org/line) - a series of two or more point objects separated by space.
* [polygon](https://schema.org/polygon) - a series of four or more space delimited points where the first and final points are identical.
* [box](https://schema.org/polboxygon) - two points separated by a space character where the first point is the lower corner and the second point is the upper corner.

These spatial definitiosn were added to schema.org very early on in its [development](https://github.com/schemaorg/schemaorg/issues/8#issuecomment-97667478) where they decided to follow the [GeoRSS specification](http://www.georss.org/simple). While this is not ideal, there are ongoing conversations about improving this in schema.org.

<a id="spatial_point"></a>
A point, or coordinate, would defined in this way:

<pre>
{
  "@context": {
    "@vocab": "http://schema.org/",
    "datacite": "http://purl.org/spar/datacite/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
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

<a id="dataset-spatial-shape"></a>
All other shapes, are defined using the [schema:GeoShape](https://schema.org/GeoShape):

<pre>
  <strong>"spatialCoverage": {
    "@type": "Place",
    "geo": {
      "@type": "GeoShape",
      "line": "39.3280,120.1633 40.445,123.7878"
    }
  }</strong>
}
</pre>

A polygon
<pre>
  <strong>"polygon": "39.3280 120.1633 40.445 123.7878 41 121 39.77 122.42 39.3280 120.1633"</strong>
</pre>

A box where 'lower-left' corner is 39.3280/120.1633 and 'upper-right' corner is 40.445/123.7878
<pre>
  <strong>"box": "39.3280 120.1633 40.445 123.7878"</strong>
</pre>

For Project418, we feel the defined spatial coverages are inadequate for the needs of our community, but we also recognize that schema.org continues to hear the needs of its schema.org publishers on these [issues](https://github.com/schemaorg/schemaorg/issues/1548).

To alleviate some of the pain of converting spatial information into these defined shapes, Project418 offers support for GeoJSON by using the [schema:subjectOf](https://schema.org/subjectOf) property of the [schema:Place](https://schema.org/Place) type. The [schema:fileFormat](https://schema.org/fileFormat) property should have the value of the GeoJSON mime type `application\/vnd.geo+json` and the [schema:text](https://schema.org/text) property should be the encoded value of the GeoJSON itself:

<pre>
"spatialCoverage": {
    "@type": "Place",
    <strong>"subjectOf": {
      "@type": "CreativeWork",
      "fileFormat": "application\/vnd.geo+json",
      "text":"{\u0022type\u0022:\u0022Feature\u0022,\u0022geometry\u0022: {\u0022type\u0022:\u0022Polygon\u0022,\u0022coordinates\u0022:[[[-64.6353,34.407],[-149.8727,34.407],[-149.8727,-17.45],[-64.6353,-17.45],[-64.6353,34.407]]],\u0022properties\u0022:[]}}"
    }</strong>
  }
</pre>

We also recognize that there is no defined property for specifying a Coordinate Reference System, but we see from the [schema.org issue queue](https://github.com/schemaorg/schemaorg/issues) that this has been mentioned.

<a id="spatial_multiple-geometries"></a>
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

Back to [top](#top)

<a id="author-creator-contributor"></a>
#### Describing a Dataset's Creators/Contributors

People can be linked to datasets iusing three fields: author, creator, and contributor. Since  [schema:contributor](https://schema.org/contributor) is defined as a secondary author, and [schema:Creator](https://schema.org/creator) is defined as being synonymous with the [schema:author](https://schema.org/author) field, we recommend using the more expressive fields of creator and contribulds of creator and contributor. But using any of these fields are okay. Becuase there are more things that can be said about how and when a person contributed to a Dataset, we use the [schema:Role](https://schema.org/Role). You'll notice that the schema.org documentation does not state that the Role type is an expected data type of author, creator and contributor, but that is addressed in this [blog post introducing Role into schema.org](http://blog.schema.org/2014/06/introducing-role.html). *Thanks to [Stephen Richard](https://github.com/smrgeoinfo) for this contribution*

![Variables](html/voc/static/schema/diagrams/dataset-creator_contributor.png "Dataset - Creator/Contributor")

<pre>
{
  "@context": {
    "@vocab": "http://schema.org/",
    "datacite": "http://purl.org/spar/datacite/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
  <strong>"creator": [
    {
      "@id": "http://lod.bco-dmo.org/id/person-role/472036",
      "@type": "Role",
      "roleName": "Principal Investigator",
      "url": "http://lod.bco-dmo.org/id/person-role/472036",
      "creator": {
        "@id": "https://www.bco-dmo.org/person/51317",
        "@type": "Person",
        "name": "Dr Uta Passow",
        "givenName": "Uta",
        "familyName": "Passow",
        "url": "https://www.bco-dmo.org/person/51317"
      }
    },
    {
      "@id": "http://lod.bco-dmo.org/id/person-role/472038",
      "@type": "Role",
      "roleName": "Co-Principal Investigator",
      "url": "https://www.bco-dmo.org/person-role/472038",
      "creator": {
        "@id": "https://www.bco-dmo.org/person/50663",
        "@type": "Person",
        "identifier": {
          "@type": ["PropertyValue", "datacite:Identifier"],
          "propertyID": "http://purl.org/spar/datacite/orcid",
          "url": "https://orcid.org/0000-0003-3432-2297",
          "value": "0000-0003-3432-2297"
        },
        "name": "Dr Mark Brzezinski",
        "url": "https://www.bco-dmo.org/person/50663"
      }
    }</strong>
}
</pre>
NOTE that the Role inherits the property `creator` and `contributor` from the Dataset when pointing to the [schema:Person](https://schema.org/Person).

<pre>
{
  "@context": {
    "@vocab": "http://schema.org/",
    ...
  },
  <strong>"@type": "Dataset"</strong>,
  ...
  <strong>"creator"</strong>: [
    {
      "@id": "http://lod.bco-dmo.org/id/person-role/472036",
      <strong>"@type": "Role"</strong>,
      "roleName": "Principal Investigator",
      "url": "http://lod.bco-dmo.org/id/person-role/472036",
      <strong>"creator":</strong> {
        "@id": "https://www.bco-dmo.org/person/51317",
        "@type": "Person",
        "name": "Dr Uta Passow",
        "givenName": "Uta",
        "familyName": "Passow",
        "url": "https://www.bco-dmo.org/person/51317"
      }
    }
}
</pre>

If a single Person plays multiple roles on a Dataset, each role should be explicitly defined in this way:

<pre>
{
  "@context": {
    "@vocab": "http://schema.org/",
    "datacite": "http://purl.org/spar/datacite/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
  "creator": [
    {
      "@id": "http://lod.bco-dmo.org/id/person-role/472036",
      "@type": "Role",
      "roleName": "Principal Investigator",
      "url": "http://lod.bco-dmo.org/id/person-role/472036",
      "creator": {
        <strong>"@id": "https://www.bco-dmo.org/person/51317"</strong>,
        "@type": "Person",
        "name": "Dr Uta Passow",
        "givenName": "Uta",
        "familyName": "Passow",
        "url": "https://www.bco-dmo.org/person/51317"
      }
    },
    <strong>{
      "@id": "https://www.bco-dmo.org/person-role/472037",
      "@type": "Role",
      "roleName": "Contact",
      "url": "https://www.bco-dmo.org/person-role/472037",
      "creator": { "@id": "https://www.bco-dmo.org/person/51317" }
    }</strong>,
    {
      "@id": "http://lod.bco-dmo.org/id/person-role/472038",
      "@type": "Role",
      "roleName": "Co-Principal Investigator",
      "url": "https://www.bco-dmo.org/person-role/472038",
      "creator": {
        "@id": "https://www.bco-dmo.org/person/50663",
        "@type": "Person",
        "identifier": {
          "@type": ["PropertyValue", "datacite:Identifier"],
          "propertyID": "http://purl.org/spar/datacite/orcid",
          "url": "https://orcid.org/0000-0003-3432-2297",
          "value": "0000-0003-3432-2297"
        },
        "name": "Dr Mark Brzezinski",
        "url": "https://www.bco-dmo.org/person/50663"
      }
    }
}
</pre>

Notice that since Uta Passow has already been defined in the document with `"@id": "https://www.bco-dmo.org/person/51317"` for her role as Principal Investigator, the `@id` can be used for her role as Contact by defining the Role's creator as `"creator": { "@id": "https://www.bco-dmo.org/person/51317" }`.

Back to [top](#top)

<a id="publisher-provider"></a>
#### Describing a Dataset's Publisher/Provider

![Publisher/Provider](html/voc/static/schema/diagrams/dataset-publisher_provider.png "Dataset - Publisher/Provider")

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
    "@vocab": "http://schema.org/",
    "datacite": "http://purl.org/spar/datacite/"
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
    "@vocab": "http://schema.org/",
    "datacite": "http://purl.org/spar/datacite/"
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

<a id="protocols"></a>
#### Describing a Dataset's Protocols

Datasets can have a number of policies and protocols attached to them - Terms of Use, access restrictions, certain licenses, etc. If you want to represent one or more of these protocols and there is a URL at which a user can read that protocol, we can use the [schema:DigitalDocument](https://schema.org/DigitalDocument) to describe the protocol using the [schema:publishingPrinciples](https://schema.org/publishingPrinciples) field.

![Protocols](html/voc/static/schema/diagrams/dataset-protocols.png "Dataset - Protocols")

<pre>
{
  "@context": {
    "@vocab": "http://schema.org/",
    "datacite": "http://purl.org/spar/datacite/",
    <strong>"gdx": "https://geodex.org/voc/"</strong>
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
<strong>"publishingPrinciples": {
    "@id": "http://creativecommons.org/licenses/by/4.0/",
    "@type": ["DigitalDocument", "gdx:Protocol-License"],
    "name": "Dataset Usage License",
    "url": "http://creativecommons.org/licenses/by/4.0/"
  }</strong>
}
</pre>

P418 has created some class names for some common protocol document types. These will help make it clear to users what types of policies you have. If you would like us to add more, please let us know by creating an [Issue](https://github.com/earthcubearchitecture-project418/p418Vocabulary/issues/new).

Back to [top](#top)

<a id="funding"></a>

Trying to describe a Dataset's funding award is one area of schema.org that doesn't fit all that well. There is a lot of [discussion](https://github.com/schemaorg/schemaorg/issues/383) on this topic already happening with schema.org governance.
Schema.org's most recent communication with P418 recommended that the award be something generated from the [schema:funder](https://schema.org/funder). We feel the best class to classify as an Award **until this is addressed by schema.org** is the [schema:Offer](https://schema.org/Offer). If you specify an Award, you **should** also use the `gdx:fundedBy` property to directly link the Dataset to the Award in this way.

#### Describing a Dataset's Funding
![Funding](html/voc/static/schema/diagrams/dataset-funding.png "Dataset - Funding")

* [schema:name](https://schema.org/name) - The award title
* [schema:description](https://schema.org/description) - The award description/abstract
* [schema:identifier](https://schema.org/identifier) - The award identifier,number,etc.
* [schema:validFrom](https://schema.org/validFrom) - The award start date
* [schema:validThrough](https://schema.org/validThrough) - The award end date

<pre>
{
  "@context": {
    "@vocab": "http://schema.org/",
    "datacite": "http://purl.org/spar/datacite/",
    <strong>"geolink": "http://schema.geolink.org/1.0/base/main#",
    "geolinkvoc": "http://schema.geolink.org/1.0/voc/local#"</strong>
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
<strong>"funder": {
    "@type": "Organization",
    "legalName": "National Science Foundation",
    "name": "NSF",
    "url": "https://www.nsf.gov",
    "identifier": {
      "@type": ["PropertyValue", "datacite:Identifier"],
      "propertyID": "http://purl.org/spar/datacite/doi",
      "value": "10.13039/100000141",
      "url": "https://doi.org/10.13039/100000001"
    },
    "makesOffer": {
      "@type": ["Offer", "geolink:Award"],
      "@id": "https://www.nsf.gov/awardsearch/showAward?AWD_ID=1623751",
      "name": "EarthCube Science Support Office (ESSO)",
      "description": "EarthCube is a community-driven effort with the goal of transforming the conduct of geoscience research and education by creating a well-integrated and facile environment to share scientific data, information tools and services, and knowledge in an open, transparent, and inclusive manner....[truncated]",
      "identifier": {
        "@type": "PropertyValue",
        "name": "NSF Award Number",
        "value": "1623751",
        "url": "https://www.nsf.gov/awardsearch/showAward?AWD_ID=1623751"
      },
      "validFrom": "2016-05-01",
      "validThrough": "2019-04-30",
      "offeredBy": {
        "@type": ["Role", "geolinkvoc:roletype_program_manager"],
        "roleName": "Program Manager",
        "offeredBy": {
          "@id": "https://www.bco-dmo.org/person/51317",
          "@type": "Person",
          "name": "Eva E. Zanzerkia"
        },        
      }
    },
    "parentOrganization": {
      "@type": "Organization",
      "legalName": "Directorate for Geosciences",
      "identifier": {
        "@type": ["PropertyValue", "datacite:Identifier"],
        "propertyID": "http://purl.org/spar/datacite/doi",
        "value": "10.13039/100000085",
        "url": "https://doi.org/10.13039/100000085"
       },
      "parentOrganization": {
        "@type": "Organization",
        "legalName": "National Science Foundation",
        "url": "http://www.nsf.gov",
        "identifier": {
          "@type": ["PropertyValue", "datacite:Identifier"],
          "propertyID": "http://purl.org/spar/datacite/doi",
          "value": "10.13039/100000001",
          "url": "https://doi.org/10.13039/100000001"
        }
      }
    }
  },
  "gdx:fundedBy": { "@id": "https://www.nsf.gov/awardsearch/showAward?AWD_ID=1623751" }</strong>
 }
</pre>


Back to [top](#top)

<a id="advanced-publishing"></a>
### Advanced Publishing Techniques

<a id="physical-sample-igsn"></a>
#### Attaching Physical Samples to a Dataset

Currently, there isn't a breat semantic property for a Dataset to distinguish the related physical samples. However, we can use the [schema:hasPart](https://schema.org/hasPart) property to accomplish this without too much compromise. A [GitHub issue](https://github.com/earthcubearchitecture-project418/p418Vocabulary/issues/16) has been setup to follow this scenario. Here is the best way, so far, to link physical samples to a Dataset:

<pre>
{
  "@context": {
    "@vocab": "http://schema.org/",
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
        "@type": ["PropertyValue", "datacite:ResourceIdentifier"],
        "propertyID": "IGSN",
        "url": "https://app.geosamples.org/sample/igsn/WHO000A53",
        "value": "WHO000A53"
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
        "@type": ["PropertyValue", "datacite:ResourceIdentifier"],
        "propertyID": "IGSN",
        "url": "https://app.geosamples.org/sample/igsn/WHO000A67",
        "value": "WHO000A67"
      }
      ...
    }
  ]</strong>
}
</pre>

Here, we use the superclass of a Dataset, the [schema:CreativeWork](https://schema.org/CreativeWork) to also define a Physical Sample. We disambiguate the Creative Work to be a physical sample by using the GeoLink definition in the `@type` field. See the [schema:CreativeWork](https://schema.org/CreativeWork) to for the additional fields available for adding to the physical sample.

**NOTE:** We use "IGSN" as the [schema:propertyID](https://schema.org/propertyID) until a canonical URI is defined by IGSN governance to where we can use [datacite:usesIdentifierScheme](https://sparontologies.github.io/datacite/current/datacite.html#d4e239) to link to a well-defined identifier type definition such as other [persistent identifiers](https://sparontologies.github.io/datacite/current/datacite.html#d4e638).
