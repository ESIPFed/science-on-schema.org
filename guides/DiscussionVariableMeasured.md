# Describing variables in datasets using schema.org

## Goal:
Goal is to add information about the variables that are specified for data items in a dataset to enhance discovery and evaluation of the dataset.

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

## Terminology
This discussion can be confusing if there is not some clarity on how terms are being used. Here are some definitions used in this discussion:
- Dataset:  A collection of data items unified by some criteria.
- Data item: a digital representation of some individual of interest, typically a structured set of attributes, but might include unstructured components like images, audio or video recording, or other documents.
- Attribute:  An individual element in a data item. Construed broadly to include those are "measured" in a conventional sense, and those whose values result from "assignment" or "classification". This corresponds to 'variable' or 'field', but we are using a different term to avoid connotation of a quantitative value.
- Type: A specification of the attibutes associated with a data item, along with rules for allowed low-level data types, formatting, value range, and cardinality. The schema for a data item. 
- Entity: a kind of thing in the world.

**so:** prefix to identify schema.org namespace elements

## Background

For our purposes, [so:Dataset](https://schema.org/Dataset) represents a Dataset as defined here, usually with a strong but non-absolute assumption that it is a set of data items, rather than a singular data item. Each data item in the dataset describes an instance of some entity. These data items might be rows in a table, objects in an object store, or graph fragments.

The data items in a dataset have a 'type' that can be described as a set of attributes, each representing some aspect of the subject of the data item. In schema.org terms, these are the variableMeasured. There is a great deal of variability in how data items in a dataset are constructed, i.e. what is the unifying entity the motivates grouping a set of attributes to define a type for a data item. Commonly this unifying entity is a sampled feature, a particular location, an event (e.g. an interview), or some individual.  

In simple cases the attributes might each specify a property that inheres in the entity that the data item is about. A data item commonly includes some attributes that are about the data item itself, e.g. a primary key, creation date/time, who created the record. Complex data items might also include attributes that are about other attributes, e.g. units of measure, instrument used, observer name, or context information specific to a particular attribute value. 

The so:variableMeasured/[so:PropertyValue](https://schema.org/PropertyValue) implementation is focused on a quantitative (numeric) attribute value. In the spectrum of scientific activity, however, the attributes for a data item might represent the result of any kind of information acquisition, for example the output of an electronic sensor, a written description, a category assignment (species, crystal class, color), a measurement made with a ruler or scale, the output of a computer model, a category assignment ("Chinook salmon"; "Kuskokwim River"), a researcher's name, an arbitrarily-assigned ('Specimen 23') or deterministic identifier (e.g. value of a SHA-2 hash), a recording of an interview with a human subject, or the sounds made by a bird or whale...  To understand an attribute value commonly entails not only a property, but also the entity that is carrying that attribute, a measurement procedure, and other context, which might vary from attribute to attribute in a dataset. For example 'nitrate in river water using spectrophotometric method'. 

Description and documentation of attributes at the conceptual level is important for interfaces through which domain practitioners interact with data. Search at this level might involve criteria like 'find data that report calcium ion concentration in river water', 'find data that contain soil porosity measurements', 'find data that have sea-surface water temperature in {some bounding box} in {some time interval}', ' find images of polar bears on Baffin Island between year 2005 and 2010'. 
 
An attribute is anchored by its conceptual definition, but might be more narrowly scoped by concepts such as its value type (e.g. numeric or categorical, vocabulary used),  unit of measurement for reported values, aggregate functions (e.g. average, maximum), and observation context like associated feature-of-interest, sampling feature, or measurement method (Including sensor or device used). Data acquisition location might be defined by geospatial coordinates and/or relationship to the feature of interest (e.g. 10 m above ground surface). Examples of attributes are ‘Methane mass, daily formation rate per unit of sediment mass’, ‘Practical salinity of water body by CTD and computation using UNESCO 1983 algorithm’.  These restrictions and context are likely to be important for evaluating data for fitness for use, but are lower priority for discovery.

An attribute might have a restricted range of valid values, or a cardinality that restricts the the number of values that can be associated with each item instance. The atribute value might have one or more possible implementations in different representations.  Description and documentation of the implementation level, e.g. specific data types, serialization schemes, cardinality, is important for software systems that automate operations on the data, but generally not critical for data discovery or evaluation.


## Current Science on schema.org recommendation.
Some of the characteristics of attributes of an so:Dataset can be described using so:variableMeasured/[so:PropertyValue](https://schema.org/PropertyValue).  

A so:Dataset can have 0 to many so:variableMeasured property elements. Each attribute, e.g. a field in a table, or an element in an object can be described by a variableMeasured.  The range of variableMeasured is text or [so:PropertyValue](https://schema.org/PropertyValue), which inherits properties from [so:Thing](https://schema.org/Thing), and adds these: { minValue, maxValue, measurementTechnique, propertyID, unitCode, unitText, value, valueReference}.  Here are two example attribute descriptions:

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

The PropertyValue entity in schema.org provides a basic framework for  description of variables. For many purposes, the so:propertyID specified in a so:ProperyValue instance can be a URI that references an in-depth property description such as that included with CF names, SWEET, EnvO, or a Scientific Variables Ontology instance. 

1. Multiple so:propertyID values could be used to indicate different levels of granularity/detail for the property associated with an attribute. For example there might be a propertyID for 'water temperature', 'sea surface water temperature', 'sea surface water temperature measured with protocol X, daily average, Kelvins, xsd:decimal'.  Each of these description approaches addresses different use cases. Communities can define standard reference resources that provide variable definitions with identifiers that can be used for information interchange. 

1. so:measurementTechnique should provide an identifier for a registered measurement technique description. If one is not available, the measurement technique should be described in text. 

1. For situations where it is not practical to have a registry of variable definitions, take advantage of the open-world nature of rdf data to include an ontologic description of the variable using some other vocabulary, e.g. SVO, SSN, DDI in the PropertyValue instance. This would only be interoperable in the context of a profile that is known to clients parsing the schema.org instance. 

1. The dct:conformsTo property should be asserted in the so:Dataset to identify the profile used for extending the so:PropertyValue description. (see discussion question below on whether dct:conformsTo should be optional at the so:PropertyValue)

1. - Multiple labels that apply to a so:PropertyValue should be represented with an array of so:alternateName. Ideally the names could be scoped in some fashion to associate them with a context in which they are used, but Schema.org does not have an object for representing scoped names.

## Suggested additions in SOSO usage

Two elements are needed: 
 
- Recommend use of **rdf:dataType** property on soPropertyValue, with range as defined in https://www.w3.org/TR/rdf11-concepts/#section-Datatypes.   The schema.org implementation is strongly oriented towards numeric result values for attributes. This is unnecessarily restrictive. To deal with data objects that are recorded interviews, sound recordings (e.g. whale song), and other 'unstructured' content the valueType could be a MIME type.   Object types would need to be defined in a data type registry (e.g. see [RDA Data Type Registries WG](https://www.rd-alliance.org/groups/data-type-registries-wg.html)).   

- Add a **rangeConstraint** property on so:PropertyValue to allow specification of the range of values expected for a property.  Numeric ranges are already accounted for by so:minValue and so:maxValue. SOSO recommends that these be used to represent the range of actual values in the described dataset. Categorical ranges could be expressed as a URI for the vocabulary used to populate values. Other more complex range constraints might need to be expressed as text or via URI.  The interpretation of the rangeConstraint might vary depending on the valueType. Options: use [rdfs:range](https://www.w3.org/TR/rdf-schema/#ch_range)

- Wishful: so:variableMeasured should be renamed so:attribute to clarify that narrow interpretation as a numeric result is not intended. (NOTE--we are unlikely to convince the schema.org maintainers to make this change...)

# Outstanding issues for discussion:

- Future work:  documentation of data quality is not treated in this recommendation.

- Should an optional dct:conformsTo property be associated with individual so:PropertyValue instances. This would allow different profiles to be used on different attributes (so:variableMeasured) in a dataset. For example at the attribute level there might be a specification for how the attribute value is specified, along with standardized metadata (unit of measure, accuracy estimate), and context (sampling feature, environmental conditions).  

- Representing relationships between attributes in a dataset. For instance in some tabular data designs, a measurement value column will be associated with a unit of measure column, an uncertainty column, and a measurement method column. How can such relationships between fields in data be represented.  One possibility is to leverage so:PropertyValue/[so:valueReference](https://schema.org/valueReference), but need to be able to assert that the target of the reference is another so:PropertyValue in the same so:Dataset instance, as well as what the relationship is.

- Source for property URIs to use in the so:propertyID field. 

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