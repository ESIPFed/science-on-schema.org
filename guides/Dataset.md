<a id="top"></a>
[Home](/README.md) | Dataset

# Describing a Dataset

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Describing a Dataset](#describing-a-dataset)
    - [Common Properties](#common-properties)
    - [Keywords](#keywords)
    - [Identifier](#identifier)
        - [How to reference Short DOIs](#how-to-reference-short-dois)
    - [Variables](#variables)
    - [Collections of datasets using schema.org DataCatalog](#collections-of-datasets-using-schemaorg-datacatalog)
    - [Metadata](#metadata)
    - [Distributions](#distributions)
        - [Accessing Data through a Service Endpoint](#accessing-data-through-a-service-endpoint)
    - [Dates](#dates)
    - [Temporal Coverage](#temporal-coverage)
        - [Geologic Time](#geologic-time)
    - [Spatial Coverage](#spatial-coverage)
        - [Use GeoCoordinates for Point locations](#use-geocoordinates-for-point-locations)
        - [Use GeoShape for all other location types](#use-geoshape-for-all-other-location-types)
        - [Handling multiple locations](#handling-multiple-locations)
        - [Spatial Reference Systems](#spatial-reference-systems)
    - [Roles of People](#roles-of-people)
    - [Publisher and Provider](#publisher-and-provider)
    - [Funding](#funding)
    - [License](#license)
    - [Checksum](#checksum)
    - [Provenance Relationships](#provenance-relationships)

<!-- /TOC -->

## Common Properties

Google has drafted a [guide to help publishers](https://developers.google.com/search/docs/data-types/dataset). The guide describes the only required fields as - name and description.
* [name](https://schema.org/name) - A descriptive name of a dataset (e.g., “Snow depth in Northern Hemisphere”)
* [description](https://schema.org/description) - A short summary describing a dataset.

<pre>
{
  "@context": "https://schema.org/",
  "@type": "Dataset",
  <strong>"name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  "description": "This dataset includes results of laboratory experiments which measured dissolved organic carbon (DOC) usage by natural bacteria in seawater at different pCO2 levels. Included in this dataset are; bacterial abundance, total organic carbon (TOC), what DOC was added to the experiment, target pCO2 level. "</strong>
}
</pre>

The [Google guide](https://developers.google.com/search/docs/data-types/dataset) also recommends following fields:

* [url](https://schema.org/url) - Location of a page describing the dataset.
* [sameAs](https://schema.org/sameAs) - Other URLs that can be used to access the dataset page. A link to a page that provides more information about the same dataset, usually in a different repository.
* [version](https://schema.org/version) - The version number or identifier for this dataset (text or numeric).
* [isAccessibleForFree](https://schema.org/isAccessibleForFree) - Boolean (true|false) specifying if the dataset is accessible for free.
* [keywords](https://schema.org/keywords) - Keywords summarizing the dataset.
* [identifier](https://schema.org/identifier) - An identifier for the dataset, such as a DOI. (text,URL, or PropertyValue).
* [variableMeasured](https://schema.org/variableMeasured) - What does the dataset measure? (e.g., temperature, pressure)

![Basic Fields](/assets/diagrams/dataset/dataset_basic-fields.png "Dataset - Basic Fields")

<pre>
{
  "@context": "https://schema.org/",
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  "description": "This dataset includes results of laboratory experiments which measured dissolved organic carbon (DOC) usage by natural bacteria in seawater at different pCO2 levels. Included in this dataset are; bacterial abundance, total organic carbon (TOC), what DOC was added to the experiment, target pCO2 level. ",
  <strong>"url": "https://www.sample-data-repository.org/dataset/472032",
  "sameAs": "https://search.dataone.org/#view/https://www.sample-data-repository.org/dataset/472032",
  "version": "2013-11-21",
  "isAccessibleForFree": true,
  "keywords": ["ocean acidification", "Dissolved Organic Carbon", "bacterioplankton respiration", "pCO2", "carbon dioxide", "oceans"],
  "license": [ "http://spdx.org/licenses/CC0-1.0", "https://creativecommons.org/publicdomain/zero/1.0"]
  </strong>
}
</pre>
Back to [top](#top)


### Keywords

Adding the [schema:keywords](https://schema.org/keywords) field can be done in three ways - a text description, a URL, or by using [schema:DefinedTerm](https://schema.org/DefinedTerm). We recommend using `schema:DefinedTerm` if a keyword comes from a controlled vocabulary.

![Keywords](/assets/diagrams/dataset/dataset_keywords.png "Dataset - Keywords")

#### Keywords as Text ####

For a dataset with the keywords of: `ocean acidification`, `Dissolved Organic Carbon`, `bacterioplankton respiration`, `pCO2`, `carbon dioxide`, `oceans`, you can express these:

<pre>
{
  "@context": "https://schema.org/",
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  "description": "This dataset includes results of laboratory experiments which measured dissolved organic carbon (DOC) usage by natural bacteria in seawater at different pCO2 levels. Included in this dataset are; bacterial abundance, total organic carbon (TOC), what DOC was added to the experiment, target pCO2 level. ",
  "url": "https://www.sample-data-repository.org/dataset/472032",
  <strong>"keywords": ["ocean acidification", "Dissolved Organic Carbon", "bacterioplankton respiration", "pCO2", "carbon dioxide", "oceans"]</strong>
}
</pre>

#### Keywords as DefinedTerm ####

If you have information about a controlled vocabulary from which keywords come, use `schema:DefinedTerm` to describe that keyword. The relevant properties of a `schema:DefinedTerm` are:

* [name](https://schema.org/name) - The name of the keyword. (Required)
* [inDefinedTermSet](https://schema.org/inDefinedTermSet) - The controlled vocabulary responsible for this keyword. (Required)
* [url](https://schema.org/url) - The canonical URL for the keyword. (Optional)
* [termCode](https://schema.org/termCode) - A representative code for this keyword in the controlled vocabulary (Optional)

As an example, we demonstrate these fields using the `oceans` keyword from the NASA GCMD Keyword vocabulary, `ice core studies` from  [SnowTerm](https://vocabularyserver.com/cnr/ml/snowterm/en/index.php), and `Baked Clay` from [EarthRef controlled vocabulary](https://www2.earthref.org/vocabularies/controlled).

<pre>
{
  "@context": "https://schema.org/",
  "@type": "Dataset",
  "name": "Dataset shell for example DefinedTerm keywords",
  "keywords": [
    {
      <strong>"@type": "DefinedTerm",
      "name": "OCEANS",
      "inDefinedTermSet": "https://gcmd.earthdata.nasa.gov/kms/concepts/concept_scheme/sciencekeywords",
      "url": "https://gcmd.earthdata.nasa.gov/kms/concept/91697b7d-8f2b-4954-850e-61d5f61c867d",
      "termCode": "91697b7d-8f2b-4954-850e-61d5f61c867d"</strong>
    },
    {
      <strong>"@type": "DefinedTerm",
      "name": "ice core studies",
      "inDefinedTermSet": "https://vocabularyserver.com/cnr/ml/snowterm/en/",
      "url": "https://vocabularyserver.com/cnr/ml/snowterm/en/index.php?tema=29330",
      "identifier": {
        "@type": "PropertyValue",
        "propertyID": "https://registry.identifiers.org/registry/ark",
        "value": "ark:/99152/t3v4yo3eeqepj0",
        "url": "https://vocabularyserver.com/cnr/ml/snowterm/en/?ark=ark:/99152/t3v4yo3eeqepj0"
      }</strong>
    },
    {
      <strong>"@type": "DefinedTerm",
      "name": "Baked Clay",
      "inDefinedTermSet": "https://www2.earthref.org/vocabularies/controlled"</strong>
    }
  ]
}
</pre>


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
**A:** Yes, but there's a better way - a URI or URL. Because we are using schema.org to express the explicit values of our content, we want to explicitly identify and classify our content such that harvesters can determine when our content appears elsewhere on the web. By detecting these shared pieces of content, we form the [Web of Data](https://www.w3.org/standards/semanticweb/data).

Because the **scheme** `Digital Object Identifier (DOI)` is described using unstructured text, we need a better way to explicitly state this value. Fortunately, [identifiers.org](https://registry.identifiers.org/registry) has registered URIs for almost 700 different identifier schemes which can be browsed at: [https://registry.identifiers.org/registry](https://registry.identifiers.org/registry).

We can specify the **scheme** as being a DOI with this identifiers.org Registry URI:

[https://registry.identifiers.org/registry/doi](https://registry.identifiers.org/registry/doi)

Looking at the available fields from [schema:PropertyValue](https://schema.org/PropertyValue), we can map our identifier fields as follows:

- `schema:value` as the identifier value `10.5066/F7VX0DMQ`
- `schema:propertyID` is the registry.identifiers.org URI for the identifier scheme `https://registry.identifiers.org/registry/doi`,
- `schema:url` is the resolvable url for that identifier `https://doi.org/10.5066/F7VX0DMQ`.

**Q: Where should the prefix go?**
**A:** There is no ideal property for the prefix, but we may include it as part of the `schema:value`.

**Q: Why include `doi:` as part of the value? Doesn't the URL `https://doi.org/10.5066/F7VX0DMQ` achieve the same result?**
**A:** While the actual value of the DOI is `10.5066/F7VX0DMQ`, we felt that this representation helps schema.org publishers specify an identifier value that is familiar to the research community. For example, in most citation styles such as APA, the DOI 10.5066/F7VX0DMQ is cited as `doi:10.5066/F7VX0DMQ`. Also, there can be many proper URLs for a specific identifier:

- http://doi.org/10.5066/F7VX0DMQ
- https://doi.org/10.5066/F7VX0DMQ
- http://dx.doi.org/10.5066/F7VX0DMQ
- https://dx.doi.org/10.5066/F7VX0DMQ
- https://www.sciencebase.gov/catalog/item/56b3e649e4b0cc79997fb5ec

For these reasons, we recommend that any identifier having a known prefix value should be included in the value succeeded by a colon to form '<prefix>:<value>', or for this DOI: `doi:10.5066/F7VX0DMQ`.

**Q: How do I know if an Identifier has a known prefix?**
**A:** Each Identifier in the identifiers.org Registry that has a known prefix will be specified on the identifiers.org registry page under the section called '**Identifier Schemes**' at the field labeled '**Prefix**'.

An example of using [schema:PropertyValue](https://schema.org/PropertyValue) to describe an Identifier:

<pre>
{
  "@context": "https://schema.org/",
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
  "@context": "https://schema.org/",
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

While we strongly recommend using a [schema:PropertyValue](https://schema.org/PropertyValue), in its most basic form, the `schema:identifier` as text can be published as:

<pre>
{
  "@context": "https://schema.org/",
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
  "@context": "https://schema.org/",
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
  <strong>"identifier": "http://id.sampledatarepository.org/dataset/472032/version/1"</strong>
}
</pre>

However, if the identifier is a persistent identifier such as a DOI, ARK, or accession number, then the best way to represent these identifiers is by using a [schema:PropertyValue](https://schema.org/PropertyValue). The PropertyValue allows for more information about the identifier to be represented such as the identifier type or scheme, the identifier's value, its URL and more. Because of this flexibility, we recommend using PropertyValue for all identifier types.

[schema:Dataset](https://schema.org/Dataset) also defines a field for the [schema:citation](https://schema.org/citation) as either text or a [schema:CreativeWork](https://schema.org/CreativeWork). To provide citation text:


<pre>
{
  "@context": "https://schema.org/",
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

NOTE: If you have a DOI, the citation text can be [automatically generated](https://citation.crosscite.org/docs.html#sec-4-1) for you by querying a DOI URL with the Accept Header of 'text/x-bibliography'.

#### How to reference Short DOIs

[Short DOI](http://shortdoi.org/) is a redirect service offered by the International DOI Foundation that provides a shorter version of an original DOI. For example, the original DOI `doi:10.5066/F7VX0DMQ` has a short DOI of `doi.org/csgf`. Short DOIs are resolvable using standard DOI URLS such as `http://doi.org/fg5v`. These short DOIs are treated identically to the original DOI. If you are using the short DOI service, we recommend publishing a short DOI URL using the `schema:sameAs` property of the `schema:Dataset`:

<pre>
{
  "@context": "https://schema.org/",
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
<a id="variables"></a>
### Variables

A Dataset is a collection of data entities, each of which contains structured and unstructured values for a set of properties about that entity. For example, an hypothetical Dataset might contain three data files: 1) a data table in CSV format containing columns of data that both classify and measure the properties of a set of lakes in a region; 2) an image file containing rasterized geospatial data values for each location for properties like water temperature at multiple depths; and 3) a text file containing responses to a survey assessing perspectives on water rights, with values for questions containing both natural language responses and responses on a Likert scale. In each of these examples, we are recording the value of attributes (aka properties) about an entity of interest (lake). In schema.org, details about these attributes can be recorded using `schema:variableMeasured`. So, while schema.org uses the term "variable" and the term "measured", it is usually conceptualized as a listing of any of the properties or attributes of an entity that are recorded, and not strictly a measured variable. Thus, we recommend using `schema:variableMeasured` to represent any recordable property of an entity that is found in the dataset. While this includes quantitatively "measured" observations (e.g., rainfall in mm), it also includes classification values that are asserted or qualitatively assigned (e.g., "moderate velocity"), contextual attributes such as spatial locations, times, or sampling information associated with a value, and textual values such as narrative text.

Information about the variables/attributes in a dataset can enhance discovery and support evaluation of the data. This can be done using the [schema:variableMeasured](https://schema.org/variableMeasured) field. Schema.org allows the value of variableMeasured to be a simple text string, but it is strongly recommended to use the [schema:PropertyValue](https://schema.org/PropertyValue) type to describe the variable in more detail.

![Variables](/assets/diagrams/dataset/dataset_variables.svg "Dataset - Variables")

This recommendation outlines several tiers of variable description. Tier 1 is the simplest, with other tiers adding recommendations for additional content (Tier 2 and 3). See [Experimental Recommendations](/guides/Experimental.md) for proposed recommendations to document variables with with non-numeric or enumerated (controlled vocabulary) values, variables whose values are structured objects (e.g., json objects, arrays, gridded data), or are references to external value representations.

#### Tier 1. Simple list of variable names

The simplest approach is to provide a `schema:name` and a textual description of the variable. The `schema:name` should match the label associated with the variable in the dataset serialization (e.g., the column name in a CSV file). If the variable name in the dataset does not clearly convey the variable concept, a more human-intelligible name can be provide using `schema:alternateName`. The field `schema:description` is used to provide a definition of the variable/property/attribute that allows others to correctly understand and interpret the values.

Example:
<pre>
{
  "@context": "https://schema.org/",
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities ...",
  ...
  "variableMeasured": [
    {
      "@type": "PropertyValue",
      "name": "latdd",
      "alternateName":"latitude, decimal degrees",
      "description": "Latitude where water samples were collected ...",
    },
    ...
  ]
}
</pre>

#### Tier 2: Names of variables with formal property types

In Tier 2, we recommend using a `schema:PropertyValue` object to provide a [schema:propertyID](https://schema.org/propertyID) that better defines the semantics of the variable than plain text can. This `schema:propertyID` should be a URI that resolves to a web page providing a human-friendly description of the variable and, ideally, this identifier should also be resolvable to obtain an RDF representation using a documented vocabulary for machine consumption, for example a [sosa:Observation](https://www.w3.org/TR/vocab-ssn/#SOSAObservation) or [DDI represented variable](https://ddi-lifecycle-technical-guide.readthedocs.io/en/latest/Specific%20Structures/Data%20Description.html#represented-variable). Describing the variables with machine understandable vocabularies is necessary if you want your data to be interoperable with other data, i.e. to be more FAIR. The property can be identified at any level of specificity, depending on what the data provider can determine about the interpretation of the variable. For example, one might use a propertyID for the property 'temperature', or use a more specific property like 'water temperature', 'sea surface water temperature', or 'sea surface water temperature measured with protocol X, daily average, Kelvins, xsd:decimal'. If there are choices, the most specific property identifier should be used.

Example:
<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities ...",
  ...
  "variableMeasured": [
    {
      "@type": "PropertyValue",
      "name": "latdd",
      "alternateName":"latitude, decimal degrees",
      <strong>"propertyID":"http://purl.obolibrary.org/obo/NCIT_C68642"</strong>,
      "description": "Latitude where water samples were collected ...",
    },
    ...
  ]
}
</pre>

#### Tier 3: Numeric values

For variables with numeric measured values, other properties of schema:PropertyValue can add additional useful information:

- [schema:unitText](https://schema.org/unitText). A string that identifies a unit of measurement that applies to all values for this variable.
- [schema:unitCode](https://schema.org/unitCode). Value is expected to be TEXT or URL. We recommend providing an HTTP URI that identifies a unit of measure from a vocabulary accessible on the web. The QUDT unit vocabulary provides an extensive set of registered units of measure that can be used to populate the schema:unitCode property to specify the units of measure used to report data values when that is appropriate.
- [schema:minValue](https://schema.org/minValue). If the value for the variable is numeric, this is the minimum value that occurs in the dataset. Not useful for other value types.
- [schema:maxValue](https://schema.org/maxValue). If the value for the variable is numeric, this is the maximum value that occurs in the dataset. Not useful for other value types.
- [schema:measurementTechnique](https://schema.org/measurementTechnique). A text description of the measurement method used to determine values for this variable. If standard measurement protocols are defined and registered, these can be identified via http URIs.
- [schema:url](https://schema.org/url) Any schema:Thing can have a URL property, but because the value is simply a url the relationship of the linked resource can not be expressed. Usage is optional. The recommendation is that `schema:url` should link to a web page that would be useful for a person to interpret the variable, but is not intended to be machine-actionable.

Example:
<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",

  "variableMeasured": [
    {
      "@type": "PropertyValue",
      "name": "latitude",
      "propertyID":"http://purl.obolibrary.org/obo/NCIT_C68642",
      "url": "https://www.sample-data-repository.org/dataset-parameter/665787",
      "description": "Latitude where water samples were collected; north is positive. Latitude is a geographic coordinate which refers to the angle from a point on the Earth's surface to the equatorial plane",
      "unitText": "decimal degrees",
      "unitCode":"http://qudt.org/vocab/unit/DEG",
      "minValue": "45.0",
      "maxValue": "15.0"
    },
    ...
  ]
}
</pre>

Back to [top](#top)

### Collections of datasets using schema.org DataCatalog

For some repositories, data collections containing multiple data sets are used to help contextualize or organize the data. In schema.org, you define these collections using [schema:DataCatalog](https://schema.org/DataCatalog).

![DataCatalog](/assets/diagrams/dataset/dataset_datacatalog.svg "Dataset - Data Catalog")

The best way to use these DataCatalogs is to define these catalogs as an ["offering" of your repository](#repository-offercatalog) and including the offering `@id` in the dataset JSON-LD. For example, the repository JSON-LD defines a [schema:DataCatalog](https://schema.org/DataCatalog) with the

`"@id": "https://www.sample-data-repository.org/collection/biological-data"`.

In the dataset JSON-LD, we reuse that `@id` to say a dataset belongs in that DataCatalog:

<pre>
{
  "@context": "https://schema.org/",
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

While this schema.org record represents metadata about a Dataset, many providers will also have other metadata records that may be more complete or that conform to other metadata formats and vocabularies that might be useful. For example, repositories often contain detailed records in ISO TC 211 formats, [EML](https://eml.ecoinformatics.org), and other formats. Aggregators and other consumers can make use of this additional metadata if they are linked in a standardized way to the schema.org record. We recommend that the location of the alternative forms of the metadata be provided using the [schema:subjectOf](https://schema.org/subjectOf) and [schema:about](https://schema.org/about) properties:

- Link metadata documents to a [schema:Dataset](https://schema.org/Dataset) by using [schema:subjectOf](https://schema.org/subjectOf).
- Or if a schema.org snippet describes the metadata as the main resource, then link to the Dataset it describes using [schema:about](https://schema.org/about).

These two approaches are equivalent, and which is used depends on the subject of the schema.org record.

![Metadata](/assets/diagrams/dataset/dataset_metadata.svg "Dataset - Metadata")

Once the linkage has been made, further details about the metadata can be provided. We recommend using [schema:encodingFormat](https://schema.org/encodingFormat) to indicate the metadata format/vocabulary to which the metadata record conforms. If it conforms to multiple formats, or to a specific and general format types, multiple types can be listed.
We use the [schema:DataDownload](https://schema.org/DataDownload) class for Metadata files so that we can use the [schema:MediaObject](https://schema.org/MediaObject) properties for describing bytesize, encoding, etc.

It can be useful to aggregators and other consumers to indicate when the metadata record was last modified using `schema:dateModified`, which can be used to optimize harvesting schedules for search indices and other applications.

An example of a metadata reference to an instance of EML-formatted structured metadata, embedded within a `schema:Dataset` record follows:

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
      "name": "EML metadata for dataset",
      "description": "EML metadata describing the dataset",
      "encodingFormat": ["application/xml", "https://eml.ecoinformatics.org/eml-2.2.0"],
      "contentURL":"https://example.com/metadata/eml-metadata.xml",
      "dateModified":"2019-06-12T14:44:15Z"
    }</strong>
  }
</pre>

Alternatively, if the schema.org record is meant to describe the metadata record, one could use the inverse property `schema:about` to indicate the linkage back to the Dataset that it describes. This should be a rare situation, as typically the schema.org record will describe the Dataset itself.

Note that the `encodingFormat` property contains an array of formats to describe multiple formats to which the document conforms (in this example, the document is both conformant with XML and the EML metadata dialect).

Back to [top](#top)

### Distributions

While the [schema:url](https://schema.org/url) property of the Dataset should point to a landing page, the way to describe how to download the data is through the [schema:distribution](https://schema.org/distribution) property. The "distribution" property describes where to get the data and in what format by using the [schema:DataDownload](https://schema.org/DataDownload) type. If your dataset is not accessible through a direct download URL, but rather through a service URL that may need input parameters jump to the next section [Accessing Data through a Service Endpoint](#dataset-service-endpoint).

![Distributions](/assets/diagrams/dataset/dataset_distribution.svg "Dataset - Distributions")

For data available in multiple formats, there will be multiple values of the [schema:DataDownload](https://schema.org/DataDownload):

<pre>
{
  "@context": "https://schema.org/",
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
  "@context": "https://schema.org/",
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

Here, we use the [schema:SearchAction](https://schema.org/SearchAction) type because it lets you define the query parameters and HTTP methods so that machines can build user interfaces to collect those query parameters and actuate a request to provide the user what they are looking for.

Back to [top](#top)

### Dates

Scientific datasets typically have multiple associated date or time periods. Time periods can be specified for 1) the time at which an entity or phenomenon occurred or was measured, and 2) the time periods when a dataset containing that information was created, changed, published, etc. `temporalCoverage` describes the age of the sample and the other dates describe the data created from observations or process. For example, if one took a sample 200 ft down in an ice core, `temporalCoverage` would describe the period when that layer of ice was deposited in geologic time, while other date properties (dateCreated, dateModified, datePublished, and expired) would describe the dataset that was created by measuring and analyzing that ice core sample. The temporalCoverage might also be a range of ages. For example if the dataset was from a study of the whole ice core it could have a range of ages from 300 to 6000 years before present (BP).

Schema.org offers various date properties that can be used to encode this information. We recommend use of the following fields for Dates:

- `schema:temporalCoverage` :: use to specify the **time period(s) that the content applies to**, i.e. the time the entity or phenomenon described in the dataset occurred. See details at [temporalCoverage](#temporal-coverage). `temporalCoverage` is usually prior to the date of data publication for observational data, and can be afterwards for models, simulations, and forecasts.

- `schema:dateCreated` :: use to specify the date the dataset was initially generated (e.g., when a sensor recorded a value, when a model was run, or when data processing was completed). This is typically fixed when the first dataset version is created.
- `schema:dateModified` :: use to specify the date the dataset was most recently updated or changed.
- `schema:datePublished` :: use to specify the date when a dataset was made available to the public through a publication process.
- `schema:expires` :: use to specify the date when the dataset expires and is no longer useful or available. If `datePublished` is when the dataset is made available, then 'expires' brackets the time the dataset is valid or recommended for use.

Back to [top](#top)

### Temporal Coverage
Temporal coverage is defined as "the time period during which data was collected or observations were made; or a time period that an activity or collection is linked to intellectually or thematically (for example, 1997 to 1998; the 18th century)" ([ARDC RIF-CS](https://documentation.ardc.edu.au/display/DOC/Temporal+coverage)). For documentation of Earth Science, Paleobiology or Paleontology datasets, we are interested in the second case: the time period that data are linked to thematically.

Temporal coverage is a difficult concept to cover across all the possible scenarios. Schema.org uses [ISO 8601 time interval format](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals) to describe time intervals and time points, but doesn't provide capabilities for geologic time scales or dynamically generated data up to present time. We ask for your [feedback](https://github.com/earthcubearchitecture-project418/p418Vocabulary/issues) on any temporal coverages you may have that don't currently fit into schema.org. You can follow [similar issues](https://github.com/schemaorg/schemaorg/issues/242) on the schema.org GitHub issue queue. We hope that our examples of the use of [OWL Time](https://www.w3.org/TR/owl-time/) and temporal reference system ([TRS](https://vocabs.gsq.digital/object?uri=http://linked.data.gov.au/def/trs)) elements will help you describe the dates or ages of the entities in a dataset. We have also included examples that describe dataset's [time uncertainties](http://geoschemas.org/extensions/temporal.html).

![Temporal](/assets/diagrams/dataset/dataset_temporal-coverage.svg "Dataset - Temporal")

To represent a single date and time:
<pre>
{
  "@context": "https://schema.org/",
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

#### Geologic Time

Dates or ages used for describing geological, archeological, and paleontological samples range from the very simple to highly complex. A lava rock age could be simply described as 1.23 million years. Other ages are more descriptive. Some other examples are: a zircon crystal with an age of 456.4 +/- 1.4 billion years (Ga) at a standard error of 2-sigma, a core with rocks from the Triassic to the Jurassic, a carbon date of a bone with non-symmetrical uncertainties of 3242 (+160 -40) B.C. We make use of the OWL time ([Cox and Little](https://w3c.github.io/sdw/time/)) descriptive tags (elements), the Queensland Department of Natural Resources, Mines and Energy Temporal Reference Systems ([TRS](https://vocabs.gsq.digital/object?uri=http://linked.data.gov.au/def/trs)), and geoschemas' [properties](https://geoschemas.org/extensions/temporal.html#properties) to describe ages and age ranges in detail. These methods could also be used to describe the temporal coverage for other disciplines as well.

There are two main types of geologic time: Proper Intervals and Instants. They are diagrammed below and used in the examples that follow.

  *Proper Interval*

![Geologic Time 1](/assets/diagrams/dataset/dataset_temporal-coverage_geo-time_properInterval.svg "Dataset - Geologic Time - Proper Interval")

  *Instant*

![Geologic Time 2](/assets/diagrams/dataset/dataset_temporal-coverage_geo-time_instant.svg "Dataset - Geologic Time - Instant")

These examples can be found in one JSON-LD file at [temporalCoverage.jsonld](/examples/dataset/temporalCoverage.jsonld)

1. The dataset's temporalCoverage is described using ProperInterval, hasBeginning, and hasEnd elements from [OWL Time](http://www.w3.org/2006/time). The human readable description can be found in the description field: "Eruptive activity at Mt. St. Helens, Washington, March 1980 - January 1981".

  *Example*:

<pre>
{    "@context": {
        "@vocab": "http://schema.org/",
        "time": "http://www.w3.org/2006/time#",
    },

    "@type": "Dataset",
        "description": "Eruptive activity at Mt. St. Helens, Washington, March 1980 - January 1981",
<strong>        "temporalCoverage": [
            {
                "@type": "time:ProperInterval",
                "time:hasBeginning": {
                     "@type": "time:Instant",
                     "time:inXSDDateTimeStamp": "1980-03-27T19:36:00Z"
                 },
                 "time:hasEnd": {
                    "@type": "time:Instant",
                    "time:inXSDDateTimeStamp": "1981-01-03T00:00:00Z"
                 }
            }]
}</strong>
</pre>

2. The dataset's temporalCoverage is described using Instant, inTimePosition, hasTRS, and numericPosition elements for a single geological date/age without uncertainties from [OWL Time](http://www.w3.org/2006/time). Use a decimal value with appropriate timescale temporal reference system (TRS) and date/age unit abbreviation. The human readable description can be found in the description field: "Eruption of Bishop Tuff, about 760,000 years ago".

   *Example*:

<pre>
{    "@context": {
        "@vocab": "http://schema.org/",
        "gsqtime": "https://vocabs.gsq.digital/object?uri=http://linked.data.gov.au/def/trs",
        "time": "http://www.w3.org/2006/time#",
        "xsd": "https://www.w3.org/TR/2004/REC-xmlschema-2-20041028/datatypes.html"
    },
    "@type": "Dataset",
    "description": "Eruption of Bishop Tuff, about 760,000 years ago",
<strong>    "temporalCoverage": [
        {
            "@type": "time:Instant",
            "time:inTimePosition": {
                "@type": "time:TimePosition",
                "time:hasTRS": {
                    "@id": "gsqtime:MillionsOfYearsAgo"
                },
                "time:numericPosition": {
                    "@type": "xsd:decimal",
                    "value": 0.76
                },
                "gstime:geologicTimeUnitAbbreviation": {
                    "@type": "xsd:string",
                    "value": "Ma"
                }
            }
        }
    ]</strong>
}
</pre>

3. The dataset's temporalCoverage is described using the Instant, inTimePosition, TimePosition, numericPosition from [OWL Time](http://www.w3.org/2006/time) with a geological date/age with uncertainties. Use a decimal value with appropriate timescale temporal reference system(TRS), date/age unit abbreviation, the uncertainty value and specify at what sigma. The human readable description can be found in the description field: "Very old zircons from the Jack Hills formation Australia 4.404 +- 0.008 Ga (2-sigma)".

   *Example*:

<pre>
{    "@context": {
        "@vocab": "http://schema.org/",
        "gsqtime": "https://vocabs.gsq.digital/object?uri=http://linked.data.gov.au/def/trs",
        "gstime": "http://schema.geoschemas.org/contexts/temporal#",
        "time": "http://www.w3.org/2006/time#",
        "xsd": "https://www.w3.org/TR/200 (from [OWL Time](http://www.w3.org/2006/time))4/REC-xmlschema-2-20041028/datatypes.html"
    },
    "@type": "Dataset",
    "description": "Very old zircons from the Jack Hills formation Australia 4.404 +- 0.008 Ga (2-sigma)",
<strong>    "temporalCoverage": [
        {
            "@type": "time:Instant",
            "time:inTimePosition": {
                "@type": "time:TimePosition",
                "time:hasTRS": {
                    "@id": "gsqtime:BillionsOfYearsAgo"
                },
                "time:numericPosition": {
                    "@type": "xsd:decimal",
                    "value": 4.404
                },
                "gstime:geologicTimeUnitAbbreviation": {
                    "@type": "xsd:string",
                    "value": "Ma"
                },
                "gstime:uncertainty": {
                    "@type": "xsd:decimal",
                    "value": 0.008
                },
                "gstime:uncertaintySigma": {
                    "@type": "xsd:decimal",
                    "value": 2.0
                }
            }
        }
    ]</strong>
}
</pre>

4. The dataset's temporalCoverage is described using the ProperInterval, hasBeginning, hasEnd, Instant, inTimePosition, TimePosition, and hasTRS elements from [OWL Time](http://www.w3.org/2006/time) with a geological date/age range with uncertainties. Use a decimal value with appropriate timescale temporal reference system(TRS), date/age unit abbreviation, uncertainty value and at what sigma. The human readable description can be found in the description field: "Isotopic ages determined at the bottom and top of a stratigraphic section in the Columbia River Basalts".

   *Example*:

<pre>
{
    "@context": {
        "@vocab": "http://schema.org/",
        "gsqtime": "https://vocabs.gsq.digital/object?uri=http://linked.data.gov.au/def/trs",
        "gstime": "http://schema.geoschemas.org/contexts/temporal#",
        "rdfs": "https://www.w3.org/2001/sw/RDFCore/Schema/200212/",
        "time": "http://www.w3.org/2006/time#",
        "xsd": "https://www.w3.org/TR/2004/REC-xmlschema-2-20041028/datatypes.html"
    },
    "@type": "Dataset",
    "description": "Isotopic ages determined at the bottom and top of a stratigraphic section in the Columbia River Basalts",
<strong>    "temporalCoverage": [
        {
            "@type": "time:ProperInterval",
            "time:hasBeginning": {
                "@type": "time:Instant",
                 "time:inTimePosition": {
                    "@type": "time:TimePosition",
                    "rdfs:comment": "beginning is older bound of age envelop",
                    "time:hasTRS": {
                        "@id": "gsqtime:MillionsOfYearsAgo"
                    },
                    "time:numericPosition": {
                        "@type": "xsd:decimal",
                        "value": 17.1
                    },
                    "gstime:geologicTimeUnitAbbreviation": {
                        "@type": "xsd:string",
                        "value": "Ma"
                    }
                },
                "gstime:uncertainty": {
                    "@type": "xsd:decimal",
                    "value": 0.15
                },
                "gstime:uncertaintySigma": {
                    "@type": "xsd:decimal",
                    "value": 1.0
                }
            },
            "time:hasEnd": {
                "@type": "time:Instant",
                "time:inTimePosition": {
                    "@type": "time:TimePosition",
                    "rdfs:comment": "ending is younger bound of age envelop",
                    "time:hasTRS": {
                        "@id": "gsqtime:MillionsOfYearsAgo"
                    },
                    "time:numericPosition": {
                        "@type": "xsd:decimal",
                        "value": 15.7
                    },
                    "gstime:geologicTimeUnitAbbreviation": {
                        "@type": "xsd:string",
                        "value": "Ma"
                    }
                },
                "gstime:uncertainty": {
                    "@type": "xsd:decimal",
                    "value": 0.14
                },
                "gstime:uncertaintySigma": {
                    "@type": "xsd:decimal",
                     "value": 2.0
                }
            }
        }
    ]</strong>
}
</pre>

5. The dataset's temporalCoverage is described using the Instant, inTimePosition, TimePosition, and hasTRS elements from [OWL Time](http://www.w3.org/2006/time) with an archeological date/age range with uncertainties. Use a decimal value with appropriate timescale temporal reference system (TRS), date/age unit abbreviation, the older and younger uncertainty values and at what sigma. The human readable description can be found in the description field: "Age of a piece of charcoal found in a burnt hut at an archeological site in Kenya carbon dated at BP Calibrated of 2640 +130 -80 (one-sigma) using the INTCAL20 carbon dating curve."

   *Example:*

<pre>
{
    "@context": {
        "@vocab": "http://schema.org/",
        "gsqtime": "https://vocabs.gsq.digital/object?uri=http://linked.data.gov.au/def/trs",
        "gstime": "http://schema.geoschemas.org/contexts/temporal#",
        "time": "http://www.w3.org/2006/time#",
        "xsd": "https://www.w3.org/TR/2004/REC-xmlschema-2-20041028/datatypes.html"
    },
    "@type": "Dataset",
    "description": "Age of a piece of charcoal found in a burnt hut at an archeological site in Kenya carbon dated at BP Calibrated of 2640 +130 -80 (one-sigma) using the INTCAL20 carbon dating curve.",
<strong>    "temporalCoverage": [
        {
            "@type": "time:Instant",
            "time:inTimePosition": {
                 "@type": "time:TimePosition",
                 "time:hasTRS": {
                     "@id": "gsqtime:BeforePresentCalibrated"
                 },
                 "time:numericPosition": {
                     "@type": "xsd:decimal",
                     "value": 2460.0
                 },
                 "gstime:geologicTimeUnitAbbreviation": {
                     "@type": "xsd:string",
                     "value": "BP-CAL"
                 },
                 "gstime:uncertaintyOlder": {
                     "@type": "xsd:decimal",
                     "value": 130.0
                 },
                 "gstime:uncertaintyYounger": {
                     "@type": "xsd:decimal",
                     "value": 80.0
                 },
                 "gstime:uncertaintySigma": {
                     "@type": "xsd:decimal",
                     "value": 1.0
                }
            }
        }
    ]</strong>
}
</pre>

6. The dataset's temporalCoverage is described using the Instant, TimePosition, inTimePosition, NominalPosition, Interval, hasBeginning, hasEnd, and hasTRS elements from [OWL Time](http://www.w3.org/2006/time). With temporal coverage that is a named time interval from a geologic time scale, provide numeric positions of the beginning and end for interoperability. Providing the numeric values is only critical, but still recommended, if the TRS for the nominalPosition is not the [International Chronostratigraphic Chart](https://stratigraphy.org/chart). In this example the temporalCoverage is described in two ways: by the named interval Bartonian and by defining a time interval using numerical beginning and end values.

   *Example:*

<pre>
{
    "@context": {
        "@vocab": "http://schema.org/",
        "gsqtime": "https://vocabs.gsq.digital/object?uri=http://linked.data.gov.au/def/trs",
        "gstime": "http://schema.geoschemas.org/contexts/temporal#",
        "icsc": "http://resource.geosciml.org/clashttps://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/resource?uri=http://resource.geosciml.org/classifier/ics/ischart/Boundariessifier/ics/ischart/",
        "time": "http://www.w3.org/2006/time#",
        "ts": "http://resource.geosciml.org/vocabulary/timescale/",
        "xsd": "https://www.w3.org/TR/2004/REC-xmlschema-2-20041028/datatypes.html"
    },
    "@type": "Dataset",
    "description": "Temporal position expressed with a named time ordinal era from [International Chronostratigraphic Chart](https://stratigraphy.org/chart):",
<strong>    "temporalCoverage": [
        {
            "@type": "time:Instant",
            "time:inTimePosition": {
                "@type": "time:TimePosition",
                "time:hasTRS": {
                    "@id": "ts:gts2020"
                },
                "time:nominalPosition": {
                    "@type": "xsd:anyURI",
                    "value": "icsc:Bartonian"
                }
            }
        },
        {
            "@type": "time:ProperInterval",
            "time:hasBeginning": {
                "@type": "time:Instant",
                "time:inTimePosition": {
                    "@type": "time:TimePosition",
                    "time:hasTRS": {
                        "@id": "gsqtime:MillionsOfYearAgo"
                    },
                    "time:numericPosition": {
                        "@type": "xsd:decimal",
                        "value": 41.2
                    },
                    "gstime:geologicTimeUnitAbbreviation": {
                        "@type": "xsd:string",
                        "value": "Ma"
                    }
                }
            },
            "time:hasEnd": {
                "@type": "time:Instant",
                "time:inTimePosition": {
                    "@type": "time:TimePosition",
                    "time:hasTRS": {
                        "@id": "gsqtime:MillionsOfYearAgo"
                    },
                    "time:numericPosition": {
                        "@type": "xsd:decimal",
                        "value": 37.71
                    },
                    "gstime:geologicTimeUnitAbbreviation": {
                        "@type": "xsd:string",
                        "value": "Ma"
                    }
                }
            }
        }
    ]</strong>
}
</pre>

7. Temporal intervals with nominal temporal position that have identifiers. When possible, use temporal intervals defined by the [International Chronostratigraphic Chart](https://stratigraphy.org/chart), access via [ARDC vocabulary service](https://vocabs.ardc.edu.au/viewById/196), or via [GeoSciML vocabularies landing page](http://geosciml.org/resource/). If temporal intervals with identifiers from other schemes are available, they can be included in a separate time:ProperInterval or time:Instant element. If intervals are not from the ICS chart it is recommended to provide an interval with beginning and end numeric positions for better interoperability.

   *Example:*

<pre>
{
    "@context": {
        "@vocab": "http://schema.org/",
        "icsc": "http://resource.geosciml.org/clashttps://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/resource?uri=http://resource.geosciml.org/classifier/ics/ischart/Boundariessifier/ics/ischart/",
        "time": "http://www.w3.org/2006/time#",
        "ts": "http://resource.geosciml.org/vocabulary/timescale/",
        "xsd": "https://www.w3.org/TR/2004/REC-xmlschema-2-20041028/datatypes.html"
    },
    "@type": "Dataset",
    "description": "Temporal position expressed with an interval bounded by named time ordinal eras from [International Chronostratigraphic Chart](https://stratigraphy.org/chart). NumericPositions not included, expect clients can lookup bounds for ISC nominal positions:",
<strong>    "temporalCoverage": [{
        "@type": "time:ProperInterval",
        "time:hasBeginning": {
            "@type": "time:Instant",
            "time:inTimePosition": {
                "@type": "time:TimePosition",
                "time:hasTRS": {"@id": "ts:gts2020"},
                "time:nominalPosition": { "@value": "icsc:Triassic", "@type": "xsd:anyURI" }
            }
        },
        "time:hasEnd": {
            "@type": "time:Instant",
            "time:inTimePosition": {
                "@type": "time:TimePosition",
                "time:hasTRS": {"@id": "ts:gts2020"},
                "time:nominalPosition": { "@value": "icsc:Jurassic", "@type": "xsd:anyURI" }
            }
        }
    }]</strong>
}
</pre>

Back to [top](#top)

### Spatial Coverage

![Spatial](/assets/diagrams/dataset/dataset_spatial-coverage.svg "Dataset - Spatial")

Used to document the location on Earth that is the focus of the dataset content, using [schema:Place](https://schema.org/Place). Recommended practice is to use the [schema:geo](https://schema.org/geo) property with either a [schema:GeoCoordinates](https://schema.org/GeoCoordinates) object to specify a point location, or a [schema:GeoShape](https://schema.org/GeoShape) object to specify a line or area coverage extent. Coordinates describing these extents are expressed as latitude longitude tuples (in that order) using decimal degrees.

Schema.org documentation does not specify a convention for the coordinate reference system, our recommended practice is to use [WGS84](EPSG:3857) for at least one spatial coverage description if applicable. Spatial coverage location using other coordinate systems can be included, see recommendation for specifying coordinate reference systems, [below](#spatial_reference-system).

#### Use GeoCoordinates for Point locations

Please indicate a point location by using a [schema:GeoCoordinates](https://schema.org/GeoCoordinates) object with [schema:latitude](https://schema.org/latitude) and [schema:longitude](https://schema.org/longitude) properties.

*Not Recommended* The [schema:Place](https://schema.org/Place) definition allows the latitude and longitude of a point location to be specified directly; although this is more succinct, it makes parsing the metadata more complex and should be avoided.

Point locations are recommended for data that is associated with specific sample locations, particularly if these are widely spaced such that an enclosing bounding box would be a misleading representation of the spatial location. Be aware that some client applications might only index or display bounding box extents or a single point location.

<a id="spatial_point"></a> A schema:Dataset that is about a point location would documented in this way:
<pre>
{
  "@context": "https://schema.org/",
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

#### Use GeoShape for all other location types

<a id="spatial_shape"></a>A [schema:GeoShape](https://schema.org/GeoShape) can describe spatial coverage as a line (e.g., a ship track), a bounding box, a polygon, or a circle. The geometry is described with a set of latitude/longitude pairs. The spatial definitions were added to schema.org early in its [development](https://github.com/schemaorg/schemaorg/issues/8#issuecomment-97667478) based on the [GeoRSS specification](http://docs.opengeospatial.org/cs/17-002r1/17-002r1.html#21). The documentation for [schema:GeoShape](https://schema.org/GeoShape) states "Either whitespace or commas can be used to separate latitude and longitude; whitespace should be used when writing a list of several such points." At least for bounding boxes (see the discussion below), it appears that the Google Dataset Search parsing of the coordinate strings depends on whether a comma or space is used to delimit the coordinates in an individual tuple.

Be aware that some client applications might only index or display bounding box extents.

* [line](https://schema.org/line) - a series of two or more points.
* [polygon](https://schema.org/polygon) - a series of four or more points where the first and final points are identical.
* [box](https://schema.org/box) - A rectangular (in lat-long space) extent specified by two points, the first in the lower left (southwest) corner and the second in the upper right (northeast) corner.
* [circle](https://schema.org/circle) - A circular region of a specified radius centered at a specified latitude and longitude, represented as a coordinate pair followed by a radius in meters. *Not recommended for use*.


**Examples:**

##### <a id="geoshape-line">Linear spatial location</a>

Useful for data that were collected along a traverse, ship track, flight line or other linear sampling feature.

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

##### <a id="geoshape-polygon">Polygon spatial location</a>

A polygon provides the most precise approach to delineating the spatial extent of the focus area for a dataset, but polygon spatial locations might not be recognized (indexed, displayed) by some client applications.

<pre>
  <strong>"polygon": "39.3280 120.1633 40.445 123.7878 41 121 39.77 122.42 39.3280 120.1633"</strong>
</pre>

##### <a id="geoshape-box">Bounding Boxes</a>

A GeoShape box defines an area on the surface of the earth defined by point locations of the southwest corner and northeast corner of the rectangle in latitude-longitude coordinates. Point locations are tuples of {latitude east-longitude} (y x). The schema.org [GeoShape](https://schema.org/GeoShape) documentation states "*Either whitespace or commas can be used to separate latitude and longitude; whitespace should be used when writing a list of several such points*." Since the box is a list of points, a space should be used to separate the latitude and longitude values. The two corner coordinate points are separated by a space. 'East longitude' means positive longitude values are east of the prime (Greenwich) meridian. A box where 'lower-left' (southwest) corner is 39.3280/120.1633 and 'upper-right' (northeast) corner is 40.445/123.7878 would be encoded thus:
<pre>
  <strong>"box": "39.3280 120.1633 40.445 123.7878"</strong>
</pre>

NOTE-- see [discussion in GitHub issue 101](https://github.com/ESIPFed/science-on-schema.org/issues/101#issuecomment-720808142) on what works with Google Dataset search to display spatial location in their search results.

East longitude values can be reported 0 <= X <= 360 or -180 <= X <= 180. Some applications will fail under one or the other of these conventions. Recommendation is to use -180 <= X <= 180, consistent with the [WKT specification](https://docs.opengeospatial.org/is/18-010r7/18-010r7.html#33). Following this recommendation, bounding boxes that cross the antimeridian at ±180° longitude, the West longitude value will be numerically greater than the East longitude value. For example, to describe Fiji the box might be
<pre>
  <strong>"box": "-19 176 -15 -178"</strong>
</pre>

NOTES: Some spatial data processors will not correctly interpret the bounding coordinates across the antimeridian even if they follow the recommended southwest, northeast corner convention, resulting in boxes that span the circumference of the Earth, excluding the actual area of interest. For applications operating with data in the vicinity of longitude 180, testing is strongly recommended to determine if it works for bounding boxes crossing the antimeridian (+/- 180); an alternative is to define two bounding boxes, one on each side of 180.

For bounding boxes that include the north or south pole, schema:box will not work. Recommended practice is to use a schema:polygon to describe spatial location extents that include the poles.

#### Handling multiple locations

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

Be aware that some client applications might not index or display multiple geometries.

#### Spatial Reference Systems

A Spatial Reference System (SRS) or Coordinate Reference System (CRS) is the method for defining the [frame of reference for geospatial location representation](https://developers.arcgis.com/documentation/core-concepts/spatial-references/). Schema.org currently has no defined property for specifying a Spatial Reference System; the assumption is that coordinates are WGS84 decimal degrees.

In the meantime, to represent an SRS in schema.org, we recommend using the [schema:additionalProperty](https://schema.org/additionalProperty) property to specify an object of type [schema:PropertyValue](https://schema.org/PropertyValue), with a [schema:propertyID](https://schema.org/propertyID) of
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
  "@context": [
    "https://schema.org/",
    {
        <strong>"dbpedia": "http://dbpedia.org/resource/"</strong>
    }
  ],
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

People can be linked to datasets using three fields: author, creator, and contributor. Since  [schema:contributor](https://schema.org/contributor) is defined as a secondary author, and [schema:Creator](https://schema.org/creator) is defined as being synonymous with the [schema:author](https://schema.org/author) field, we recommend using the more expressive fields creator and contributor, but using any of these fields is acceptable.

NOTE: JSON-LD doesn't preserve the order of its collection values, so if you need to preserve the order of people's names (e.g., for a citation) you can do so by applying the `@list` JSON-LD keyword (for more information about this see [Getting Started - JSON-LD Lists](GETTING-STARTED.md#json-ld-list)).

Given the following `creator` JSON-LD block:

```
{
  ...
  "creator:[
    {
        "@type": "Person",
        "name": "Creator #1"
    },
    {
        "@type": "Person",
        "name": "Creator #2"
    }
  ]
}
```

The order of these creators can be preserved by the using the `@list` JSON-LD keyword:

```
{
  ...
  "creator:{
    "@list": [
      {
          "@type": "Person",
          "name": "Creator #1"
      },
      {
          "@type": "Person",
          "name": "Creator #2"
      }
    ]
  }
}
```

Because there are more things that can be said about how and when a person contributed to a Dataset, we use the [schema:Role](https://schema.org/Role). You'll notice that the schema.org documentation does not state that the Role type is an expected data type of author, creator and contributor, but that is addressed in this [blog post introducing Role into schema.org](http://blog.schema.org/2014/06/introducing-role.html). *Thanks to [Stephen Richard](https://github.com/smrgeoinfo) for this contribution*

![People Roles](/assets/diagrams/dataset/dataset_people-roles.svg "Dataset - People Roles")

<pre>
{
  "@context": "https://schema.org/",
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
NOTE that the Role inherits the property `creator` and `contributor` from the Dataset when pointing to the [schema:Person](http://schema.org/Person).

<pre>
{
  "@context": "https://schema.org/",
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
  "@context": "https://schema.org/",
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

### Publisher and Provider

![Publisher/Provider](/assets/diagrams/dataset/dataset_publisher-provider.svg "Dataset - Publisher/Provider")

If your repository is the publisher and/or provider of the dataset then you don't have to describe your repository as a [schema:Organization](https://schema.org/Organization) **if** your repository markup includes the **`@id`**. For example, if you published repository markup such as:
<pre>
{
  "@context": "https://schema.org/",
  "@type": ["Service", "Organization"],
  ...
  <strong>"@id": "https://www.sample-data-repository.org"</strong>
  ...
}
</pre>

then you can reuse that `@id` here. Harvesters such as Google and Project418 will make the appropriate linkages and your dataset publisher/provider can be published in this way:

<pre>
{
  "@context": "https://schema.org/",
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
  "@context": "https://schema.org/",
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

![Funding](/assets/diagrams/dataset/dataset_funding.png "Dataset - Funding")

Data providers should include funding information in their Dataset descriptions to enable discovery and cross-linking. The information that would be useful includes the title, identifier, and url of the grant or award, along with structured information about the funding organization, including its name and identifier. Organizational identifiers are best represented using either a general purpose institutional identifier such as a [ROR](https://ror.org), [GRID](https://grid.ac/), or ISNI identifier, or a more specific [Funder ID](https://api.crossref.org/funders/) from the [Crossref Funder Registry](https://www.crossref.org/services/funder-registry/). The ROR for the National Science Foundation (https://ror.org/021nxhr62), for example, provides linkages to related identifiers as well. The Funder ID has the advantage that it includes both agency funders like the National Science Foundation (http://dx.doi.org/10.13039/100000001), but also provides identifiers for individual funding programs within those agencies, such as the NSF GEO Directorate (https://api.crossref.org/funders/100000085). When possible, providing both a ROR and Funder ID is helpful. Here's an example of identifiers for the National Science Foundation:

![NSF ROR Entry](/assets/images/ror.png "Dataset - Funder Identifiers")

Linking a Dataset to the grants and awards that fund it can be achieved by adding a [schema:MonetaryGrant](https://schema.org/MonetaryGrant) through the `schema:funding` property.

<pre>
{
  "@context": "https://schema.org/",
  "@type": "Dataset",
  "@id": "https://doi.org/10.18739/A22V2CB44",
  "name": "Stable water isotope data from Arctic Alaska snow pits in 2019",
<strong>
  "funding": [
    {
      "@id": "https://www.nsf.gov/awardsearch/showAward?AWD_ID=1604105",
      "@type": "MonetaryGrant",
      "identifier": "1604105",
      "name": "Collaborative Research: Nutritional Landscapes of Arctic Caribou: Observations, Experiments, and Models Provide Process-Level Understanding of Forage Traits and Trajectories",
      "url": "https://www.nsf.gov/awardsearch/showAward?AWD_ID=1604105",
      "funder": {
        "@id": "http://dx.doi.org/10.13039/100000001",
        "@type": "Organization",
        "name": "National Science Foundation",
        "identifier": [
          "http://dx.doi.org/10.13039/100000001",
          "https://ror.org/021nxhr62"
        ]
      }
    },
    {
      "@type": "MonetaryGrant",
      "@id": "https://akareport.aka.fi/ibi_apps/WFServlet?IBIF_ex=x_hakkuvaus2&HAKNRO1=316349&UILANG=en&TULOSTE=HTML",
      "identifier": "316349",
      "name": "Where does water go when snow melts? New spatio-temporal resolution in stable water isotopes measurements to inform cold climate hydrological modelling",
      "url": "https://akareport.aka.fi/ibi_apps/WFServlet?IBIF_ex=x_hakkuvaus2&HAKNRO1=316349&UILANG=en&TULOSTE=HTML",
      "funder": {
        "@id": "http://dx.doi.org/10.13039/501100002341",
        "@type": "Organization",
        "name": "Academy of Finland",
        "identifier": [
          "http://dx.doi.org/10.13039/501100002341",
          "https://ror.org/05k73zm37"
        ]
      }
    }
  ]
</strong>
}
</pre>

We recommend providing as much structured information about the grants that fund a Dataset as possible so that aggregators and harvesters can crosslink to the Funding agencies and grants that provided resources for the Dataset.

Back to [top](#top)

### License

Link a Dataset to its license to document legal constraints by adding a [schema:license](https://schema.org/license) property. The [guide](https://developers.google.com/search/docs/data-types/dataset) recommends providing a URL that unambiguously identifies a specific version of the license used, but for many licenses it is hard to determine what that URL should be. Thus, we recommend that the license URL be drawn from the [SPDX license list](https://spdx.org/licenses/), which provides a curated list of licenses and their properties that is well maintained. For each SPDX entry, SPDX provides a canonical URL for the license (e.g., `http://spdx.org/licenses/CC0-1.0`), a unique `licenseId` (e.g., `CC0-1.0`), and other metadata about the license. Here's an example using the SPDX license URI for the Creative Commons CC-0 license:

<pre>
{
  "@context": "https://schema.org/",
  "@id": "http://www.sample-data-repository.org/dataset/123",
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  <strong>"license": "http://spdx.org/licenses/CC0-1.0"</strong>
  ...
}
</pre>

SPDX URIs for each license can be found by finding the appropriate license in the [SPDX license list](https://spdx.org/licenses/), and then remove the final `.html` extension from the filename. For example, in the table one can find the license page for Apache at the URI `https://spdx.org/licenses/Apache-2.0.html`, which can be converted into the associated linked data URI by removing the `.html`, leaving us with `https://spdx.org/licenses/Apache-2.0`. Alternatively, one can find the license file in the [structured data listings](https://github.com/spdx/license-list-data/tree/master/rdfturtle) and copy the URL from the associated file. For example, the URL for the Apache-2.0 license is listed in the file at https://github.com/spdx/license-list-data/blob/master/rdfturtle/Apache-2.0.turtle.

While many licenses are ambiguous about the license URI for the license, the Creative Commons licenses and a few others are exceptions in that they provide extremely consistent URIs for each license, and these are in widespread use. So, while we recommend using the SPDX URI, we recognize that some sites may want to use the CC license URIs directly, which is helpful in recognizing the license. In this case, we recommend that the SPDX URI still be used as described above, and the other URI also be provided as well in a list. Here's an example using the traditional Creative Commons URI along with the SPDX URI.
<pre>
{
  "@context": "https://schema.org/",
  "@id": "http://www.sample-data-repository.org/dataset/123",
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  <strong>"license": [ "http://spdx.org/licenses/CC0-1.0", "https://creativecommons.org/publicdomain/zero/1.0"]</strong>
  ...
}
</pre>

The following table contains the SPDX URIs for some of the most common licenses. Others can be looked up at the SPDX site as described above.

|License          | SPDX URI                                  |
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

### Checksum

A `schema:Dataset` can be composed of multiple digital objects which are listed in the `schema:distribution` list. For each `schema:DataDownload`, it can be useful to provide an cryptographic checksum value (like SHA 256 or MD5) that can be used to characterize the contents of the object. Aggregators and distributors can use these values to verify that they have retrieved exactly the same content as the original provider made available, and that replica copies of an object are identical to the original, among other uses. Because schema.org does not contain a class for representing checksum values, by convention we recommend using the [`spdx:checksum`](http://spdx.org/rdf/terms#checksum) property, which points at an `spdx:Checksum` instance that provides both the value of the checksum and the algorithm that was used to calculate the checksum.

Here's an example that provides two different checksum values for a single digital object within a `schema:DataDownload` description. Note that providers will need to define the `spdx` prefix in their `@context` block in order to use the prefix as shown in the example.

<pre>
{
    "@context": [
      "https://schema.org/",
      {
        <strong>"spdx": "http://spdx.org/rdf/terms#"</strong>
      }
    ],
    "@type": "Dataset",
    "@id": "https://dataone.org/datasets/doi%3A10.18739%2FA2NK36607",
    "sameAs": "https://doi.org/10.18739/A2NK36607",
    "name": "Conductivity-Temperature-Depth (CTD) data along DBO5 (Distributed Biological Observatory - Barrow Canyon), from the 2009 Circulation, Cross-shelf Exchange, Sea Ice, and Marine Mammal Habitat on the Alaskan Beaufort Sea Shelf cruise on USCGC Healy (HLY0904)",
    "distribution": {
        "@type": "DataDownload",
        "@id": "https://dataone.org/datasets/urn%3Euuid%3E2646d817-9897-4875-9429-9c196be5c2ae",
        "identifier": "urn:uuid:2646d817-9897-4875-9429-9c196be5c2ae",
        <strong>"spdx:checksum": [
            {
                "@type": "spdx:Checksum",
                "spdx:checksumValue": "39ae639d33cea4a287198bbcdca5e6856e6607a7c91dc4c54348031be2ad4c51",
                "spdx:algorithm": {
                    "@id": "spdx:checksumAlgorithm_sha256"
                }
            },
            {
                "@type": "spdx:Checksum",
                "spdx:checksumValue": "65d3616852dbf7b1a6d4b53b00626032",
                "spdx:algorithm": {
                    "@id": "spdx:checksumAlgorithm_md5"
                }
            }
        ]</strong>
    }
}
</pre>

The algorithm property is chosen from the controlled [SPDX vocabulary of checksum types](http://spdx.org/rdf/terms#ChecksumAlgorithm), making it easy for processors to recalculate checksum values to verify them. Common algorithms that many providers would use include `spdx:checksumAlgorithm_sha256` and `spdx:checksumAlgorithm_md5`. Note specifically that the `spdx:checksumAlgorithm_sha256` value is inside of an `@id` property so that the SPDX namespace from the context definition is used to define the algorithm URI.


Back to [top](#top)

### Provenance Relationships

High level relationships that link datasets based on their processing workflows and versioning relationships are critical for data consumers and search engines to link different versions of a [schema:Dataset](https://schema.org/Dataset), to clarify when a dataset is derived from one or more source Datasets, and to specify linkages to the software and activities that created these derived datasets for reproducibility. Collectively, this is provenance information.

The [PROV-O](https://www.w3.org/TR/prov-o/) recommendation provides the widely-adopted vocabulary for representing this type of provenance information, and should be used within Dataset descriptions, as most of the necessary provenance properties are currently missing from schema.org. The main exception is [`schema:isBasedOn`](https://schema.org/isBasedOn), which provides a predicate for indicating that a Dataset was derived from one or more source Datasets. Producers and consumers should interpret `schema:isBasedOn` to be an equivalent property to `prov:wasDerivedFrom` (in the `owl:equivalentProperty` sense). Either is acceptable for representing derivation relationships, but there is utility in expressing the relationship with both predicates for consumers that might only be looking for one or the other. When other `PROV` predicates are used, it is preferred to use `prov:wasDerivedFrom` for consistency.

We recommend providing provenance information about data processing workflows, data derivation relationships, and versioning information using PROV-O and schema.org predicates, and describe the structures to do this in the following subsections. Aggregators and search systems should use these properties to cluster and cross-link versions of Datasets, and to provide bi-directional linkages to source and derived data products.

#### Indicating an earlier version: `prov:wasRevisionOf`

![Prov_versions](/assets/diagrams/dataset/dataset_prov_revision.svg "Dataset - Revisions")

Link a Dataset to a prior version that it replaces by adding a [`prov:wasRevisionOf`](https://www.w3.org/TR/prov-o/#wasRevisionOf) property. This indicates that the current `schema:Dataset` replaces or obsoletes the source Dataset indicated. The value of the `prov:wasRevisionOf` should be the canonical IRI for the identifier for the original dataset, preferably to a persistently resolvable IRI such as as a DOI, but other persistent identifiers for the dataset can be used.

<pre>
{
  "@context": [
    "https://schema.org/",
    {
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "https://doi.org/10.xxxx/Dataset-2.v2",
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  <strong>"prov:wasRevisionOf": { "@id": "https://doi.org/10.xxxx/Dataset-2.v1" }</strong>
}
</pre>

#### Indicating a source dataset: `schema:isBasedOn` and `prov:wasDerivedFrom`

A derived Dataset is one in which the values in the data are somehow related or created from the values in one or more source datasets. For example, raw voltage values from a sensor might be recorded in a raw data file, which is then processed through calibration functions to produce a derived dataset with values in scientific units. Other examples of derived data include data that has been error corrected, gap-filled, or integrated with other sources.

To indicate that a Dataset has been derived from a source Dataset, use the [`prov:wasDerivedFrom`](https://www.w3.org/TR/prov-o/#wasDerivedFrom) property. This indicates that the current `schema:Dataset` was created in whole or in part from content in the source Dataset, and therefore does not represent an independent set of measurements. The value of the `prov:wasDerivedFrom` should be the canonical IRI for the identifier for the source dataset, preferably to a persistently resolvable IRI such as a DOI, but other persistent identifiers for the dataset can be used. In addition, if a persistent identifier for a digital object within a Dataset is available, the `prov:wasDerivedFrom` may also be used to indicate that that digital object was derived from that particular source object, rather than the overall Dataset. This allows one to be more specific about the exact relationship between the source and derived data objects.

In addition to `prov:wasDerivedFrom`, schema.org provides the [`schema:isBasedOn`](https://schema.org/isBasedOn) property, which should be considered to be an equivalent property to `prov:wasDerivedFrom`. For compatibility with schema.org, we recommend that producers use `schema:isBasedOn` in addition to or instead of `prov:wasDerivedFrom` to indicate derivation relationships.

![Prov_derived](/assets/diagrams/dataset/dataset_prov_derived.svg "Dataset - Derivations")

<pre>
{
  "@context": [
    "https://schema.org/",
    {
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "https://doi.org/10.xxxx/Dataset-2",
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  <strong>"prov:wasDerivedFrom": { "@id": "https://doi.org/10.xxxx/Dataset-1" }</strong>,
  <strong>"isBasedOn": { "@id": "https://doi.org/10.xxxx/Dataset-1" }</strong>
}
</pre>

#### Indicating a software workflow or processing activity: `prov:used` and `prov:wasGeneratedBy`

Frequently data are processed to create derived Datasets or other products using software programs that use some source data, transform it in various ways, and create the derived products. Understanding these software workflows promotes understanding of the products, and facilitates reproducibility. Describing a software workflow is really just a mechanism to provide more detail about how derived products were created when software was executed. The [ProvONE](https://purl.dataone.org/provone-v1-dev) vocabulary extends PROV to define a specific concept for an execution event (`provone:Execution`) during which a software program (`provone:Program`) is executed. During this execution, the software can use source data (`prov:used`) and generate outputs (`prov:wasGeneratedBy`), which then can be inferred to have been derived from the source data.

![Prov_program](/assets/diagrams/dataset/dataset_prov_program.svg "Dataset - Workflow")

Any portion of the software workflow can be described to increase information about derived datasets. For example, use `prov:used` to link an execution to one or more source datasets, and use `prov:wasGeneratedBy` to link an execution to one or more derived products. When information about the execution event itself is known, use `provone:Execution` to describe that event, and link it to the source and derived products, as well as the program. The program is often a software script that is itself dereferenceable, and may be part of the archived Dataset itself if it has an accessible IRI.

<pre>
{
  "@context": [
    "https://schema.org/",
    {
      "prov": "http://www.w3.org/ns/prov#",
      "provone": "http://purl.dataone.org/provone/2015/01/15/ontology#"
    }
  ],
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
