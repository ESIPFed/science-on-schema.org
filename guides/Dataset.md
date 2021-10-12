<a id="top"></a>
[Home](/README.md) | Dataset

# Describing a Dataset

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Describing a Dataset](#describing-a-dataset)
	- [Common Properties](#common-properties)
		- [Identifier](#identifier)
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
* [license](https://schema.org/license) - A license under which the dataset is distributed (text or URL).
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
  "keywords": ["ocean acidification", "Dissolved Organic Carbon", "bacterioplankton respiration", "pCO2", "carbon dioxide", "oceans"],
  "license": "http://creativecommons.org/licenses/by/4.0/"</strong>
}
</pre>
Back to [top](#top)

### Identifier

Adding the [schema:identifier](https://schema.org/identifier) field can be done in three ways - a text description, a URL, or by using the [schema:PropertyValue](https://schema.org/PropertyValue) type to describe the identifier in more detail.

![Identifiers](/assets/diagrams/dataset/dataset_identifier.svg "Dataset - Identifier")

In it's most basic form, the identifier as text can be published as:

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
  "license": "http://creativecommons.org/licenses/by/4.0/",
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

For identifiers that do have a well-defined scheme that scopes the identifier value, such as DOI, ARK, ISBN, etc, we can use the [DataCite Ontology Resource Identifier Scheme](https://sparontologies.github.io/datacite/current/datacite.html#d4e638) to specify this identifier scheme:

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/",
    <strong>"datacite": "http://purl.org/spar/datacite/"</strong>
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  "description": "This dataset includes results of laboratory experiments which measured dissolved organic carbon (DOC) usage by natural bacteria in seawater at different pCO2 levels. Included in this dataset are; bacterial abundance, total organic carbon (TOC), what DOC was added to the experiment, target pCO2 level. ",
  "url": "https://www.sample-data-repository.org/dataset/472032",
  "sameAs": "https://search.dataone.org/#view/https://www.sample-data-repository.org/dataset/472032",
  "version": "2013-11-21",
  "keywords": ["ocean acidification", "Dissolved Organic Carbon", "bacterioplankton respiration", "pCO2", "carbon dioxide", "oceans"],
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
    "@vocab": "https://schema.org/",
    <strong>"datacite": "http://purl.org/spar/datacite/"</strong>
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  "description": "This dataset includes results of laboratory experiments which measured dissolved organic carbon (DOC) usage by natural bacteria in seawater at different pCO2 levels. Included in this dataset are; bacterial abundance, total organic carbon (TOC), what DOC was added to the experiment, target pCO2 level. ",
  "url": "https://www.sample-data-repository.org/dataset/472032",
  "sameAs": "https://search.dataone.org/#view/https://www.sample-data-repository.org/dataset/472032",
  "version": "2013-11-21",
  "keywords": ["ocean acidification", "Dissolved Organic Carbon", "bacterioplankton respiration", "pCO2", "carbon dioxide", "oceans"],
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
      "@type": ["PropertyValue"],
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
    "@vocab": "https://schema.org/",
    "datacite": "http://purl.org/spar/datacite/",
    <strong>"gsn-quantity": "http://www.geoscienceontology.org/geo-lower/quantity#"</strong>
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
  "variableMeasured": [
    {
      "@type": "PropertyValue",
      "name": "latitude",
      <strong>"propertyID":"gsn-quantity:latitude"</strong>,
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
    "@vocab": "https://schema.org/",
    "datacite": "http://purl.org/spar/datacite/"
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

Alternative forms of the metadata describing the dataset may be available in other standards compliant formats that may be useful to consumers. The location of the alternative forms of the metadata can be provided with the [`schema:encoding`](https://schema.org/encoding) property which is an instance of [`MediaObject`](https://schema.org/MediaObject).

An example of a MediaObject reference to an instance of ISO TC211 structured metadata:

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/",
    "datacite": "http://purl.org/spar/datacite/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
  <strong>"encoding":{
    "@type":"MediaObject",
    "contentUrl":"https://example.org/link/to/metadata.xml",
    "encodingFormat":"http://www.isotc211.org/2005/gmd",
    "description":"ISO TC211 XML rendering of metadata.",
    "dateModified":"2019-06-12T14:44:15Z"
  }</strong>
}
</pre>

The `encoding` property may contain an array of `MediaObject` instances to describe multiple alternate forms of metadata available.

A SHACL shape graph for verifying the presence and structure of a MediaObject:

```turtle
# Shape to evaluate schema:MediaObject instances that provide the value of
# schema:encoding for an instance of schema:Dataset
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix d1: <http://ns.dataone.org/schema/2019/08/SO/Dataset#> .

d1:rdfPrefix
  sh:declare [
    sh:namespace "http://www.w3.org/1999/02/22-rdf-syntax-ns#"^^xsd:anyURI ;
    sh:prefix "rdf" ;
  ] .

d1:schemaPrefix
  sh:declare [
    sh:namespace "https://schema.org/"^^xsd:anyURI ;
    sh:prefix "schema" ;
  ] .

d1:MediaObjectShape
    a sh:NodeShape ;
    sh:target [
        a sh:SPARQLTarget ;
        sh:prefixes d1:rdfPrefix, d1:schemaPrefix ;
        sh:select """
            SELECT ?this
            WHERE {
                ?DF rdf:type schema:Dataset .
                ?DF schema:encoding ?this .
                ?this rdf:type schema:MediaObject .
            }
        """ ;
    ] ;
    sh:property [
        sh:path schema:contentUrl ;
        sh:minCount 1 ;
        sh:message "schema:contentUrl is required for the encoding property of a Dataset"
    ] ;
    sh:property [
        sh:path schema:encodingFormat ;
        sh:minCount 1 ;
        sh:message "schema:encodingFormat should provide the format of the encoding of the referenced resource" ;
        sh:severity sh:Warning ;
    ] ;
    sh:property [
        sh:path schema:dateModified ;
        sh:minCount 1 ;
        sh:message "schema:dateModified should indicate when the referenced resource was last modified" ;
        sh:severity sh:Warning ;
    ]
.
```
*Note:* The aforementioned SHACL shape uses capabilities from the
[advanced SHACL specification](https://www.w3.org/TR/shacl-af/#SPARQLTarget) which are not implemented by many SHACL validation libraries (including [pySHACL as of this writing](https://github.com/RDFLib/pySHACL/blob/49650b0c483d3fa5e9ab133df5694b739421a8f9/FEATURES.md)). The [TopBraid SHACL commandline validator](https://github.com/TopQuadrant/shacl) implements the required functionality. A simple wrapper in Python is available, see [pyTBSHACL](https://github.com/datadavev/pyTBSHACL). 

Back to [top](#top)

### Distribution: how to access the data

The [schema:url](https://schema.org/url) property of the Dataset should point to an authoritative dataset landing page, which will typically include some links to download data. Use the [schema:distribution](https://schema.org/distribution) property, for which the expected data type is [schema:DataDownload](https://schema.org/DataDownload), for datasets that have direct data download URLs, have a web application that assists users to get subsets of the data for their specific purpose, or are accessible through a web service (WebAPI) that may need input parameters.

![Distributions](/assets/diagrams/dataset/dataset_distribution.svg "Dataset - Distributions")

#### Accessing Data through a direct download URL

The DataDownload/contentURL should be a URL that will get the dataset in a particular format. The data format should be indicated by the schema:DataDownload/schema:encodingFormat string. Recommended usage is to provide a registered MIME type to specify the format; if an identifier string for a particular profile of the format is available, that can be included as a type parameter with the MIME Type. For example 'application/json;type=WaterML'. Specifying a more specific format can enable automation to connect datasets and applications that work with that particular data format profile.  For data available in multiple formats with different URLs for each format, there will be multiple values of the [schema:DataDownload](https://schema.org/DataDownload):

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/",
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

#### Accessing Data through a data selection web application

Some large datasets are accessible via web sites that assist the user to construct a set of filters to subset the dataset and obtain only the data they need. The URL for the web site is not a direct download url, so the address for the web site should be placed in the DataDownload/url element. Adding WebSite as an additional type will make the access approach more explicit. Example:

<pre>
"distribution": {
            "@type": [ "DataDownload", "WebSite" ],
            "name": "ERDDAP Server",
            "description": "Web form to select ARGO data and download one of many offered formats. 
            See https://www.ifremer.fr/erddap/tabledap/ArgoFloats.html#DAS 
            for complete list of variables in data structure",
            "url": "https://www.ifremer.fr/erddap/tabledap/ArgoFloats.html"
        }
</pre>

#### Accessing Data through a Service Endpoint

In some cases the data can be accessed via a WebAPI with a request including parameters that enable, for example, subsetting, filtering, or selection of different format options.  In such cases, we can use the [schema:potentialAction](https://schema.org/potentialAction), which the [schema:DataDownload](https://schema.org/DataDownload) object inherits from [schema:Thing](https://schema.org/Thing). The value expected for a [schema:potentialAction](https://schema.org/potentialAction) is [schema:SearchAction](https://schema.org/SearchAction). In the simplest case, the search action target is a [schema:EntryPoint](https://schema.org/EntryPoint) that specifies a urlTemplate (see [IETF RFC-6570](https://tools.ietf.org/html/rfc6570)), and a set of query-input [schema:PropertyValueSpecification](https://schema.org/PropertyValueSpecification) objects that describe the template parameters. The [schema:valueName](https://schema.org/valueName) in each property value specification matches one of the urlTemplate parameters, which are enclosed in curly braces ('{}'). 

![Service Endpoint](/assets/diagrams/dataset/dataset_service-endpoint.svg "Dataset - Service Endpoint")

The basic pattern looks like this:

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "name": "Argo float data and metadata from Global Data Assembly Centre (Argo GDAC)",
  ...
  "distribution":      {
    "@type": [ "DataDownload","WebAPI" ],
    "name": "Argovis WebAPI",
    "serviceType": "Argovis API",
    "documentation": "https://argovis.colorado.edu/api-docs/#/",
    "description": "Access Argo profiles via API, i.e. temperature, salinity, and biogeochemical data by location. Argo metadata, float trajectory forecasts, gridded fields, weather events are also available through API",
    "potentialAction": {
        "@type": "SearchAction",
        "target": {
            "@type": "EntryPoint",
            "urlTemplate": "https://argovis.colorado.edu/selection/profiles?startDate={start}&endDate={end}&shape={shape}&presRange={presRange}",
            "description": "download profiles within a bounding box for specified start/end dates",
            "httpMethod": ["GET"]
        },
        "query-input": [
            {
                "@type": "PropertyValueSpecification",
                "valueName": "shape",
                "description": "list of lists containing [lon, lat] coordinates that define a polygon; first and last coordinate pair should be the same poitn. example: shape = [[[-144.84375,36.031332],[-136.038755,36.210925],[-127.265625,35.746512],[-128.144531,22.755921],[-136.543795,24.835311],[-145.195313,26.431228],[-144.84375,36.031332]]]",
                "valueRequired": true
            },
            {
                "@type": "PropertyValueSpecification",
                "valueName": "start",
                "description": "string formatted as 'YYYY-MM-DD'",
                "valueRequired": true
            },
            {
                "@type": "PropertyValueSpecification",
                "valueName": "end",
                "description": "string formatted as 'YYYY-MM-DD'",
                "valueRequired": true
            },
            {
                "@type": "PropertyValueSpecification",
                "valueName": "presRange",
                "description": "a string of a list formatted as '[minimum pres,maximum pres]' (no spaces)",
                "valueRequired": false,
                "defaultValue": "None"
            }
        ],
        "result":{
            "@type":"DataDownload",
            "encodingFormat":"application/json"
        }
    }
}
</pre>


Here, we use the [schema:SearchAction](https://schema.org/SearchAction) type becuase it lets you define the template parameters and HTTP methods so that machines can build user interfaces to collect those query parameters and actuate a request to provide the user what they are looking for. Adding 'WebAPI' as an additional type will make the access approach more explicit,and also adds properties to specify serviceType and a link to a service description document like OpenAPI/Swagger or OGC getCapabilities.

Note that the schema:SearchAction object also includes a [schema:result](https://schema.org/result) property that can be used to provide information about the encoding format of the WebAPI response, and a [schema:object](https://schema.org/object) property that can be used to provide a more detailed description of the data type for the WebAPI response. A more detailed description of an API would be like this (elipses ... indicate where some of the template property specifications are omitted for brevity) :

<pre>
  "distribution":      {
    "@type": [ "DataDownload","WebAPI" ],
    "name": "IRIS DMC FDSNWS event Web Service",
    "serviceType": "FDSNWS event API",
    "documentation": "http://service.iris.edu/fdsnws/event/1/",
    "description": "The fdsnws-event web service returns event (earthquake) information from catalogs originating from the NEIC and the ISC data centers. ",
	"potentialAction": [
			"@type": "SearchAction",
			"name": "Query",
			"description": "query service to obtain records of seismic events",
			"result":
				{
					"@type": "DataDownload",
					"encodingFormat": [
						"application/xml;type=QuakeML",
						"text/csv","QuakeML",
						"text/csv+geocsv",
						"GeoCSV-SeismicEvent"
					],
				"description": "XML, csv, or csv fromat for seismic event following EarthCube geoWs conventions."
				},
			"target": {
				"@type": "EntryPoint",
				"urlTemplate": "http://service.iris.edu/fdsnws/event/1/query?{geographic-constraints}&{depth-constraints}&{temporal-constraints}&{magnitude-constraints}&{organization-constraints}&{misc-parameters}&{format-option}&{nodata=404}",
				"description": "URL with multiple query parameters--geographic location, event depth, time period of event, event magnitude, source network, miscellaneous parameters, format for returned data, and what flag to use for no data.  ",
				"httpMethod":"GET",
				"uriTemplate-input": [
					{
						"@id": "urn:iris:fsdn.starttime",
						"@type": "PropertyValueSpecification",
						"valueName": "start",
						"defaultValue": "Any",
						"description": "allowed: Any valid time. Limit to events on or after the specified start time; use UTC for time zone",
						"valueRequired": true,
						"valuePattern": "(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(.[0-9]+)?",
						"xsd:type": "dateTime"
					},
					{
						"@id": "urn:iris:fsdn.endtime",
						"@type": "PropertyValueSpecification",
						"valueName": "end",
						"defaultValue": "Any",
						"description": "allowed: Any valid time. Limit to events on or before the specified start time",
						"valueRequired": true,
						"valuePattern": "(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(.[0-9]+)?"
					},
					{
						"@id": "urn:iris:fsdn.minlatitude",
						"@type": "PropertyValueSpecification",
						"valueName": "minlat",
						"defaultValue": "-90.0",
						"description": "Limit to events with a latitude larger than or equal to the specified minimum. Value must be less that maxlat",
						"valueRequired": true,
						"minValue": -90.0,
						"maxValue": 90.0,
						"xsd:type": "float",
						"unitOfMeasure": "degrees"
					},
....
					{
						"@id": "urn:iris:fsdn.maxlongitude",
						"@type": "PropertyValueSpecification",
						"valueName": "maxlon",
						"defaultValue": "180.0",
						"description": "Limit to events with a longitude smaller than or equal to the specified maximum.",
						"valueRequired": true,
						"minValue":-180.0,
						"maxValue": 180.0,
						"xsd:type": "float",
						"unitOfMeasure": "degrees"
					},
					{
						"@id": "urn:iris:fsdn.latitude",
						"@type": "PropertyValueSpecification",
						"valueName": "lat",
						"defaultValue": "0.0",
						"description": "Specify the latitude to be used for a radius search.",
						"valueRequired": false,
						"minValue":-90.0,
						"maxValue": 90.0,
						"xsd:type": "float",
						"unitOfMeasure": "degrees"
					},
					{
						"@id": "urn:iris:fsdn.longitude",
						"@type": "PropertyValueSpecification",
						"valueName": "lon",
						"defaultValue": "0.0",
						"description": "Specify the longitude to be used for a radius search.",
						"valueRequired": false,
						"minValue":-180.0,
						"maxValue": 180.0,
						"xsd:type": "float",
						"unitOfMeasure": "degrees"
					},
...
					{
						"@id": "urn:iris:fsdn.maxradius",
						"@type": "PropertyValueSpecification",
						"valueName": "maxradius",
						"defaultValue": "180.0",
						"description": "Limit to events within the specified maximum number of degrees from the geographic point defined by the latitude and longitude parameters.",
						"valueRequired": false,
						"minValue": 0.0,
						"maxValue": 180.0,
						"xsd:type": "float",
						"unitOfMeasure": "degrees"
					},
...
			]
			},
			"object": {
				"@type": "DataFeed",
				"description": "list of properties  that are included in seismic event description in response documents. note this example does not include all the variable descriptions for the output object.",
				"variableMeasured": [
					{
						"@type": "PropertyValue",
						"name": "name of the variable",
						"description": "example of documentation for a varible provided in the result object",
						"propertyID": "URI for the property in some ontology",
						"measurementTechnique": "URI for the measurement protocol, or text description of procedure and sensor"
					}
				]
			}
		}
</pre>

Back to [top](#top)

### Temporal Coverage

Temporal coverage is a difficult concept to cover across all the possible scenarios. Schema.org uses [ISO 8601 standard](https://en.wikipedia.org/wiki/ISO_8601) to describe time intervals and time points, but doesn't provide capabilities for geologic time scales or dynamically generated data up to present time. We ask for your [feedback on any temporal coverages you may have that don't currently fit into schema.org](https://github.com/earthcubearchitecture-project418/p418Vocabulary/issues). You can follow [similar issues at the schema.org Github issue queue](https://github.com/schemaorg/schemaorg/issues/242)

![Temporal](/assets/diagrams/dataset/dataset_temporal-coverage.svg "Dataset - Temporal")

To represent a single date and time:
<pre>
{
  "@context": {
    "@vocab": "https://schema.org/",
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
    "@vocab": "https://schema.org/",
    "datacite": "http://purl.org/spar/datacite/"
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
    "@vocab": "https://schema.org/",
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

<a id="spatial_shape"></a>
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

The defined spatial coverages are inadequate for the needs of our community, but we also recognize that schema.org continues to hear the needs of its schema.org publishers on these [issues](https://github.com/schemaorg/schemaorg/issues/1548).

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


<a id="spatial_reference-system"></a>
A Spatial Reference System (SRS) or Coordinate reference systems (CRS) are methodologies for locating geographical features within some frame of reference (e.g. Earth, Moon, etc.). To represent an SRS in schema.org, we should use the `[schema:additionalProperty](https://schema.org/additionalProperty)` property to specify an object of type `[schema:PropertyValue](https://schema.org/PropertyValue)` and `[dbpedia:Spatial_reference_system](http://dbpedia.org/resource/Spatial_reference_system)`, a decent RDF resource on the web for describing what an SRS is.

| Spatial Reference System | IRI                                          |
|--------------------------|----------------------------------------------|
| WGS84                    | http://www.w3.org/2003/01/geo/wgs84_pos#     |
| CRS84                    | http://www.opengis.net/def/crs/OGC/1.3/CRS84 |

A spatial reference system can be added in this way:

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/",
    "datacite": "http://purl.org/spar/datacite/",
    <strong>"dbpedia": "http://dbpedia.org/resource/"</strong>
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
  "spatialCoverage": {
    "@type": "Place",
    "geo": {
      "@type": "GeoShape",
      "line": "39.3280,120.1633 40.445,123.7878"
    },
    <strong>"additionalProperty": {
      "@type": ["PropertyValue", "dbpedia:Spatial_reference_system"],
      "@id": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
    }</strong>
  }
}
</pre>

Back to [top](#top)

### Roles of People

People can be linked to datasets using three fields: author, creator, and contributor. Since  [schema:contributor](https://schema.org/contributor) is defined as a secondary author, and [schema:Creator](https://schema.org/creator) is defined as being synonymous with the [schema:author](https://schema.org/author) field, we recommend using the more expressive fields of creator and contribulds of creator and contributor. But using any of these fields are okay. Becuase there are more things that can be said about how and when a person contributed to a Dataset, we use the [schema:Role](https://schema.org/Role). You'll notice that the schema.org documentation does not state that the Role type is an expected data type of author, creator and contributor, but that is addressed in this [blog post introducing Role into schema.org](http://blog.schema.org/2014/06/introducing-role.html). *Thanks to [Stephen Richard](https://github.com/smrgeoinfo) for this contribution*

![People Roles](/assets/diagrams/dataset/dataset_people-roles.svg "Dataset - People Roles")

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/",
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
    "@vocab": "https://schema.org/",
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
    "@vocab": "https://schema.org/",
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
    "@vocab": "https://schema.org/",
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
    "@vocab": "https://schema.org/",
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


### Funding
![Funding](/assets/diagrams/dataset/dataset_funding.svg "Dataset - Funding")

Linking a Dataset to its funding can be acheived by adding a [schema:MonetaryGrant](https://schema.org/MonetaryGrant) object on your webpage. In order to do this, we have to modify the structure of our JSON-LD to include multiple top-level items, and make sure that our Dataset uses the `@id` to identify its URI. This `@id` will be used by the MonetaryGrant to say it funded the Dataset. First, we add the `@id` to our Dataset:
<pre>
{
  "@context": {
    "@vocab": "https://schema.org/",
    "datacite": "http://purl.org/spar/datacite/"
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
    "@vocab": "https://schema.org/",
    "datacite": "http://purl.org/spar/datacite/"
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
    "@vocab": "https://schema.org/",
    "datacite": "http://purl.org/spar/datacite/"
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
    "@vocab": "https://schema.org/",
    "datacite": "http://purl.org/spar/datacite/"
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
