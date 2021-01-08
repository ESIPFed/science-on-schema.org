# Describing variables in datasets using schema.org

## Goal:
Goal is to add information about the variables that are specified for data items in a dataset to enhance discovery and evaluation of the dataset.

### Approach
- Use relevant schema.org terms in describing variables whenever possible
- Determine what new extensions to schema.org may be necessary to effectively describe variables
--  There are some well-established and maintained systems (e.g. OpenDAP DMR, DDI, ISO19110) available to clarify the contents of a variable description, these need to be accessible online to use. Propose a scheme to link to variable descriptions using one of these systems, or provide them in line in the JSON-LD.


### For discovery 
- Variable name, and description are basic information that should always be included.
- A URI from some known authority that uniquely identifies the variable can greatly improve interoperability and avoid ambiguity in identifying the variable.
### For evaluation
Need to know something about
- Measurement technique
- Data quality (precision, accuracy, validation procedures…)
- Value range in data (this might be useful for discovery as well)
- Units of measure
- Value Types—data types including e.g. simple literals (integer, decimal, float, text) (use [csv on the web types](https://www.w3.org/TR/tabular-data-primer/datatypes.svg)), links, structured objects, binary objects (image, audio, video). This is a more expansive interpretation of 'value type' than some understandings.
- Observation context -- many datasets can benefit from some context information. These might be Properties that apply to the entire Dataset, or to a specific variableMeasured within a Dataset as environmental feature and environmental materials may vary across measurements within a dataset.  The properties specifying context should have values of (at least?) name and URL. Some relevant property examples:
  - biome (e.g. arctic tundra) where the dataset was collected
  - habitat (e.g. thermokarst) where the dataset was collected;
  - the feature that was sampled (e.g.thaw lake) [sampling feature and feature of interest?]
  - material that was sampled (talik).
**Note**  these context properties are likely to be quite domain specific.


**so:** prefix to identify schema.org namespace elements

## Background

See [DDI-Cross Domain Integration: Detailed Model](https://ddi-alliance.atlassian.net/wiki/download/attachments/860815393/Part_2_DDI-CDI_Detailed_Model_PR_1.pdf), section III Data Description, and the [OpenDAP v4 documentation on Characterizing a Data Source](https://docs.opendap.org/index.php?title=DAP4:_Specification_Volume_1#Characterization_of_a_Data_Source) for background on describing data. 

DDI defines a variable as “a mapping between some collection of units (the extension of the general concept for which the variable is a characteristic) to a set of values.”  In the DDI usage, a ‘Unit’ is the entity that a variable is about. 
Roles allow users to assign different functions to variables according to their context of use. Roles are not inherent in variables but can be imposed on them. In DDI-CDI there are currently three roles:
 - Identifier - An identifier role that serves to differentiate one record from another. More than one variable may be used in combination to produce a compound identifier. 
 - Measure – Variables tagged with the measure role represent the values of interest. 
 - Attribute – The attribute role serves to provide information about the measures of interest. Variables might, for example, describe the conditions of a measurement. This way attributes can be used to link metadata or paradata (data about the process by which the data were collected) to the Measure of interest. 

In OpenDAP data description each variable in a dataset has a name, a type, a value, and an (optional) collection of Attributes. The distinction between information in a variable and in an Attribute is somewhat arbitrary. However, the intention is that Attributes hold information that aids in the interpretation of data held in a variable. Variables, on the other hand, hold the primary content of a data source (‘Measures’ in DDI usage).
Data structures are a way to organize data in order to be processed by software programs. The current DDI-CDI model can be used to describe data from different data structures using an approach that involves describing each “cell” in the structure. The following structures are covered: 
 - Wide Data: Traditional rectangular, record-oriented data sets. Each record has an identifier and a set of measures related the same subject (unit, entity, feature of interest). Exemplified by common tabular data formats.
 - Long Data: Each record has an identifier for the subject, and a set of measures, but there might be multiple records for any given subject. The structure is used for  example with event data and spell data (observations for each unit, each covering a span of time (a spell)). Analogous to RDF or [Sixth normal form](https://en.wikipedia.org/wiki/Sixth_normal_form) in relational databases.
 - Multi-Dimensional Data: Data in which observations are identified using a set of dimensions. Examples are multi-dimensional cubes and time series. (Note that support is provided for time-series-specific constructs to support some legacy systems which are not based around the manipulation of multi-dimensional data “cubes”.) Exemplified by geospatial grid data.
 - Key-Value Data: A set of measures, each paired with an identifier, suited to describing No SQL and Big Data systems. JSON is a typical implementation.

Description and documentation of variables at the conceptual level is important for interfaces through which domain practitioners interact with data. Search at this level might involve criteria like 'find data that report calcium ion concentration in river water', 'find data that contain soil porosity measurements', 'find data that have sea-surface water temperature in {some bounding box} in {some time interval}', ' find images of polar bears on Baffin Island between year 2005 and 2010'. 
 
A variable is anchored by its conceptual definition (DDI ConceptualVariable), but might be more narrowly scoped by concepts such as its value type (e.g. numeric or categorical, vocabulary used),  unit of measurement for reported values, aggregate functions (e.g. average, maximum), and observation context like associated feature-of-interest, sampling feature, or measurement method (Including sensor or device used) (DDI RepresentedVariable, DDI InstanceVariable).  

Examples variables: ‘Methane mass, daily formation rate per unit of sediment mass’, ‘Practical salinity of water body by CTD and computation using UNESCO 1983 algorithm’. For example 'nitrate in river water using spectrophotometric method'. Data acquisition location might be defined by geospatial coordinates and/or relationship to the feature of interest (e.g. 10 m above ground surface). These aspects of variables are represented by variables in the role of 'attribute' in a data structure.  The restrictions on measurement method and context are likely to be important for evaluating data for fitness for use, but are lower priority for discovery. 

A variable might have a restricted range of valid values (ValueDomain), or a cardinality that restricts the the number of values that can be associated with each item instance. The variable value might have one or more possible implementations in different representations (DDI InstanceVariable).  Description and documentation of the implementation level, e.g. specific data types, serialization schemes, cardinality, is important for software systems that automate operations on the data, but generally not critical for data discovery or evaluation.

## Current state

The existing so:variableMeasured/[so:PropertyValue](https://schema.org/PropertyValue) implementation is focused on tabular data with quantitative (numeric) variable values that are all about a single subject entity ('unit'). 

This implementation meets a very simple set of requirements, but in the spectrum of scientific activity a variable might represent the result of any kind of information acquisition, for example the output of an electronic sensor, a written description, a measurement made with a ruler or scale, the output of a computer model, a category assignment ("Chinook salmon"; "Kuskokwim River"), a researcher's name, an arbitrarily-assigned ('Specimen 23') or deterministic identifier (e.g. value of a SHA-2 hash), a recording of an interview with a human subject, or the sounds made by a bird or whale.  To understand a variable value entails understanding the property (conceptual variable in DDI terms), but also the entity (unit) that is the subject of the variable, a measurement procedure, and other context represented by variables in the attribute role. 

## Current Science on schema.org recommendation.
Some of the characteristics of variables in an so:Dataset can be described using so:variableMeasured/[so:PropertyValue](https://schema.org/PropertyValue).  A so:Dataset can have 0 to many so:variableMeasured property elements.  The range of so:variableMeasured is text or [so:PropertyValue](https://schema.org/PropertyValue), which inherits properties from [so:Thing](https://schema.org/Thing), and adds additional properties: { minValue, maxValue, measurementTechnique, propertyID, unitCode, unitText, value, valueReference}.  Here are two example attribute descriptions:

**Example 1**
```
 "variableMeasured": [
    {
      "@type": "PropertyValue",
      "name": "latitude",
      "PropertyID": "http://www.w3.org/2003/01/geo/wgs84_pos#lat",
      "url": "https://www.sample-data-repository.org/dataset-parameter/665787",
      "description": "Latitude where water samples were collected; north is positive.",
      "unitText": "decimal degrees",
      "minValue": "45.0",
      "maxValue": "15.0"
    },
```

**Example 2**
```
"variableMeasured": [
	{
	"@type": "PropertyValue",
	"name": "DEPTH,sediment/rock",
	"propertyID":"http://purl.jp/bio/4/id/201006028017141570", 
	"description":"depth to interface between soil and underlying sediment or rock", 
	"unitCode":"MTR"
	}
``` 

# Recommendations

The PropertyValue entity in schema.org provides a basic framework for description of variables. For many purposes, the so:ProperyValue/so:propertyID can be a URI that references an in-depth property (DDI:ConceptualVariable) description such as that included with CF names, SWEET, EnvO, or a Scientific Variables Ontology instance. The value should be a URL (http URI) that points to a dereferenceable term that represents the base conceptual variable, e.g.  http://purl.obolibrary.org/obo/ENVO_04000002.  

The so:ProperyValue/so:propertyID value should be an array, recognizing that there might be identifiers for variables at different levels in the DDI variable cascated (ConceptualVariable, RepresentationVariable, InstanceVariable), or that the property concept might have identifiers in different vocabularies (ontologies) used by different communities.  

Dereferencing the so:ProperyValue/so:propertyID  URI should yield a rich represenation of the meaning of the property that further axiomatizes the phenomenon, e.g. as a  "Feature of Interest: sea surface" and "Observed Property: temperature", etc, with links to ontologies like EnvO or SWEET.  

It would be up to the client to recognize the propertyID identifier, or extract useful information from it representation, to better understand what the PropertyValue actually represents, via its rdfs:label, skos:definition, skos:altLabel, etc. 

### Details on encoding
1. Multiple so:propertyID values could be used to indicate different levels of granularity/detail for the property associated with a variable (the DDI variable cascade...). For example there might be a propertyID for 'water temperature', 'sea surface water temperature', 'sea surface water temperature measured with protocol X, daily average, Kelvins, xsd:decimal'.  Each of these description approaches addresses different use cases. Communities can define standard reference resources that provide variable definitions with identifiers that can be used for information interchange. 

1. so:measurementTechnique should provide an identifier for a registered measurement technique description. If one is not available, the measurement technique should be described in text. 

1. Multiple labels that apply to a so:PropertyValue should be represented with an array of so:alternateName. Ideally the names could be scoped in some fashion to associate them with a context in which they are used, but Schema.org does not have an object for representing scoped names.  [consider shoe-horning so:DefinedTerm for this purpose...]

## Suggested additions in SOSO usage

Two elements are needed: 
 
- Recommend use of **rdf:dataType** or **qudt:dataType** property on soPropertyValue, with range as defined in https://www.w3.org/TR/rdf11-concepts/#section-Datatypes.   The schema.org implementation is strongly oriented towards numeric result values for attributes. This is unnecessarily restrictive. To deal with data objects that are recorded interviews, sound recordings (e.g. whale song), and other 'unstructured' content the valueType could be a MIME type.   Object types would need to be defined in a data type registry (e.g. see [RDA Data Type Registries WG](https://www.rd-alliance.org/groups/data-type-registries-wg.html)).   

- Add a **rangeConstraint** property on so:PropertyValue to allow specification of the range of values expected for a property.  Numeric ranges are already accounted for by so:minValue and so:maxValue. SOSO recommends that these be used to represent the range of actual values in the described dataset. Categorical ranges could be expressed as a URI for the vocabulary used to populate values. Other more complex range constraints might need to be expressed as text or via URI.  The interpretation of the rangeConstraint might vary depending on the valueType. Options: use [rdfs:range](https://www.w3.org/TR/rdf-schema/#ch_range)

# Outstanding issues for discussion:

- Future work:  documentation of data quality is not treated in this recommendation.

- Should an optional dct:conformsTo property be associated with individual so:PropertyValue instances. This would allow different profiles to be used on different variables (so:variableMeasured) in a dataset. For example at the variable level there might be a specification for how the value is specified, along with standardized metadata (unit of measure, accuracy estimate), and context (sampling feature, environmental conditions).  

- Representing relationships between variables and attributes (variables in the attribute role) in a dataset. For instance in some tabular data designs, a measurement value column will be associated with a unit of measure, uncertainty, and measurement method attributes. How can such relationships between fields in data be represented.  One possibility is to leverage so:PropertyValue/[so:valueReference](https://schema.org/valueReference), but need to be able to assert that the target of the reference is another so:PropertyValue in the same so:Dataset instance, as well as what the relationship is.

# Some Property vocabularies
Property URIs that might be used in the so:propertyID field. 

  - **CF names** [CF standard name table]( https://cfconventions.org/Data/cf-standard-names/73/src/cf-standard-name-table.xml); names have an id, but no namespace appears to be defined, so there aren't dereferenceable URIs it seems.
  - **SWEET** has a set of property labels with some hierarchical structure providing weak semantics, but noe explicit definitions in the http://sweetontology.net/prop/Property namespace. Properties are at the conceptual level, e.g. 'total alkalinity', 'pH', 'precision', 'temperature range'. 
  - **LTER Measurements**   Provides [A word net, similar to SWEET, but doesn't provide URI or definition](https://vocab.lternet.edu/vocab/vocab/index.php?tema=667&/measurements).  All term URIs are query fragments on the 'vocab/index.php' resource.
  - **Structured Variable ontology** (SVO) SVO provides a [vocabulary of measured variables based on its model](http://geoscienceontology.org/svo/svl/variable/1.0.0/), it is apparently only accessible on a web page with URIs that are html fragment identifiers.


# Some data type vocabularies

[QUDT](http://www.qudt.org/2.1/catalog/qudt-catalog.html). Focus on units and quantity kinds.

[Linked data model (Used by QUDT) datatypes](http://www.linkedmodel.org/doc/2015/SCHEMA_dtype-v1.2)

[RDF datatypes](https://www.w3.org/TR/rdf11-concepts/#section-Datatypes)

[XML schema datatypes](https://www.w3.org/TR/xmlschema11-2/#built-in-datatypes)

[FHIR specification]( https://www.hl7.org/fhir/datatypes.html) defines a set of data types that are used for the resource elements.  FHIR is a standard for health care data exchange, published by HL7®

# Some property vocabularies

- Wikidata 
- [QUDT quanityKinds]( http://www.qudt.org/doc/DOC_VOCAB-QUANTITY-KINDS.html)
- [Minimum Information about any (x) Sequence (MIxS)](https://gensc.org/mixs/) the GSC family of minimum information standards – 
- [USGS NWIS parameters](https://help.waterdata.usgs.gov/codes-and-parameters/parameters). 
- [Scientific Variables Ontology](http://www.geoscienceontology.org/svo/svl/property/1.0.0/)
- [US EPA substance registry](https://ofmpub.epa.gov/sor_internet/registry/substreg/LandingPage.do)

# Data Description systems
 - [DDI-Cross Domain Integration: Detailed Model](https://ddi-alliance.atlassian.net/wiki/download/attachments/860815393/Part_2_DDI-CDI_Detailed_Model_PR_1.pdf), section III Data Description, 
 - [OpenDAP v4 documentation on Characterizing a Data Source](https://docs.opendap.org/index.php?title=DAP4:_Specification_Volume_1#Characterization_of_a_Data_Source) for background on describing data. 
 - [W3C data cube](https://www.w3.org/TR/vocab-data-cube/). Uses attribute, Dimension, Measure, similar to OpenDAP
 - [EML Data Structure Modules](https://eml.ecoinformatics.org/eml-schema.html#data-structure-modules)

# Reading
[Typology-based Semantic Labeling of Numeric Tabular Data](http://www.semantic-web-journal.net/system/files/swj2393.pdf)


