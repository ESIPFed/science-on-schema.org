# Describing variables in datasets using schema.org

## Background
The description of measured variables for a dataset is an outstanding problem. A first order issue is the name of the property in schema.org. The label  'schema:variableMeasured' has the connotation of a quantitative (numeric) value. In the spectrum of scientific activity, the fields (for lack of a better term...) in a dataset might represent the result of any kind of observation, ranging from the output of an electronic sensor, a written description, a category assignment (species, crystal class, color), a measurement made with a ruler or scale, the output of a computer model, a recording of an interview with a human subject or the sounds made by a bird or whale...   In this broader interpretation of what the records in a dataset might contain, a different label for this property would be appropriate.  'attribute' is the the label that will be used in this discussion. 

In the schema.org description of a dataset, the sdo:Dataset typically represents the data object, and the attributes are described using sdo:variableMeasured/
[sdo:PropertyValue](https://schema.org/PropertyValue). Each record in the dataset describes an instance or individual observation of a feature of interest.

Issues include:

- What level of granularity? Variables can be described at a conceptual level, a logical level, or an implementation (physical level).  Each of these description approaches addresses different use cases.
- How much of the conceptual model for a variable instance should be explicitly included in a schema.org dataset description? 
- What ontologies should be recommended to link variables for semantically precise description?
- How to deal with datasets that contain recorded interviews, sound recordings (e.g. whale song), other 'unstructured' content. 

The framework for this discussion is a data object ('type', 'entity', 'object', etc.) that has a collection of attributes, each representing an observation result for some property. Each attribute has a range for valid values, and a cardinality that constrains the number of values associated with each data object instance. The atributes have a conceptual level definition that might be a complex object, and can have one or more implementations in particular representations. Description and documentation of the conceptual level is important for interfaces through which domain practitioners interact with data. Search at this level might involve criteria 'find data that report calcium ion concentration in river water', or 'data that contain soil porosity measurements'. Description and documentation of the implementation level is important for software systems that automate operations on the data.  

A attribute is anchored by a primary observed property, typically a phenomenon concept, and might be more narrowly scoped by concepts such as its value type (e.g. numeric or categorical) and range, feature-of-interest, unit of measurement for reported values, aggregate functions (e.g. average, maximum), or measurement method (Including sensor or device used). Reported values are commonly indirectly linked to a feature of interest through a sampling feature, which has a location that might be defined by geospatial coordinates and/or relationship to the feature of interest (e.g. 10 m above ground surface). Individual result values are obtained by some agent at a particular time.  Examples of attributes are ‘Methane mass, daily formation rate per unit of sediment mass’, ‘Practical salinity of water body by CTD and computation using UNESCO 1983 algorithm’.

Current Science on schema.org recommendation.
A schema:Dataset can have 0 to many schema:variableMeasured property elements. Each field in a table, or element in an object can be considered a variableMeasure.  The range of variableMeasured is text or [schema:PropertyValue](https://schema.org/PropertyValue), which inherits properties from [schema:Thing](https://schema.org/Thing), and adds these: { minValue, maxValue, measurementTechnique, propertyID, unitCode, unitText, value, valueReference}.  Here are two example variable descriptions:

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

## How are attributes (variables) defined


### CF standard name structure:

Based on [Guidelines for Construction of CF Standard Names](http://cfconventions.org/Data/cf-standard-names/docs/guidelines.html).  A standard name is constructed by joining a base standard name to  qualifiers using underscores.
[surface] [component] standard_name [at surface] [in medium] [due to process] [assuming condition]

[surface](http://cfconventions.org/Data/cf-standard-names/docs/guidelines.html#surface). A surface is defined as a function of horizontal position.
[component](http://cfconventions.org/Data/cf-standard-names/docs/guidelines.html#component). The direction of the spatial component of a vector is indicated by one of the words upward, downward, northward, southward, eastward, westward, x, y.
base_quantity. a standard name from the [CF standard names table](https://cfconventions.org/standard-names.html).
at [surface](http://cfconventions.org/Data/cf-standard-names/docs/guidelines.html#surface).
in [medium](http://cfconventions.org/Data/cf-standard-names/docs/guidelines.html#medium). A medium indicates the local medium or layer within which an intensive quantity applies
due to [process](http://cfconventions.org/Data/cf-standard-names/docs/guidelines.html#process). The specification of a physical process. 
assuming [condition](http://cfconventions.org/Data/cf-standard-names/docs/guidelines.html#condition). The named quantity is the value which would obtain if all aspects of the system were unaltered except for the assumption of the circumstances specified by the condition

### [Scientific Variables Ontology (SVO)](http://www.geoscienceontology.org/svo/1.0.0/)
A blueprint outlining the required and optional components for creating a machine-interpretable scientific variable concept, similar to the structure for a CF standard name. SVO does not provide a vocabulary of measured variables based on this ontology. 

### ENVO 
from Kai Blumberg
- Entity: e.g., sediment or rock [Feature of interest]
- Characteristic/Quality: e.g., depth of sediment (we can create entity quality pairings like this in ENVO using sediment and PATO:depth in the axiom). [Property]
- Standard/Unit: e.g., meter
- Measurement technique or protocol
- Additional environmental context concept to describe the environment where the measurement was made e.g., tundra biome, mine


# Issues:

## Data type for PropertyValue
The schema.org implementation is strongly oriented towards numeric result values for attributes. This is unnecessarily restrictive. Categorical, ordinal, boolean, and unstructured (text, audio, video, image) values need to be described.  

## Range for categorical property value
For non-numeric values, there is no mechanism to express the domain of allowed values, e.g. an identifier for a controlled vocabulary used to populate a variable's values.

## Source for property URIs to use in the sdo:propertyID field. 
### CF names 
[CF standard name table]( https://cfconventions.org/Data/cf-standard-names/73/src/cf-standard-name-table.xml); names have an id, but no namespace appears to be defined, so there aren't dereferenceable URIs it seems.

### SWEET
SWEET has a set of property labels with some hierarchical structure providing weak semantics, but noe explicit definitions in the http://sweetontology.net/prop/Property namespace. Properties are at the conceptual level, e.g. 'total alkalinity', 'pH', 'precision', 'temperature range'. 

### LTER Measurements
https://vocab.lternet.edu/vocab/vocab/index.php?tema=667&/measurements. A word net, similar to SWEET, but doesn't provide URI or definition.  All term URIs are query fragments on the 'vocab/index.php' resource.


# Recommendations

schema.org is not designed as an ontology to describe scientific data. It is intended to support basic data discovery and initial evaluation. The PropertyValue entity in schema.org provides a basic framework for  description of variables. For many purposes, the PropertyID specified in a schema:ProperyValue instance can be a URI that references an in-depth property description such as that included with CF names, or a Scientific Variables Ontology instance. Communities can define standard reference resources that provide variable definitions to be used for information interchange. 

For situations where it is not practical to have a registry of variable definitions, there are two options. 
1. Other schema.org properties like measurementTechnique and valueReference. If standard measurement protocols are defined an registered, these can be identified via http URI's in the measurementTechnique.  Other properties of the measurement could be included as valueReference/PropertyValue instances in the variableMeasured property. 
1. Take advantage of the open-world nature of rdf data to include an ontologic description of the variable using some other vocabulary, e.g. SVO, SSN, DDI in the PropertyValue instance.

Either of these extension mechanisms would only be interoperable in the context of a profile that is known to clients parsing the schema.org instance. The dcat:conformsTo property should be asserted in the schema:Dataset to identify the profile used for extending the PropertyValue description. 

Do we need to allow for different profiles used on different variables....??? I don't think so, but if so the dcat:conforms to would need to be asserted on each PropertyValue that is extended.  This might be a recommended extension pattern for any element.

## Suggested updates to schema.org
- schema:variableMeasured should be renamed schema:attribute to clarify that narrow interpretation as a numeric result is not intended. 
- Add a rangeConstraint property on schema:PropertyValue to allow specification of the range of values expected for a property.  Numeric ranges are already accounted for. Categorical ranges could be expressed as a URI for the vocabualary used to populate values. Other more complex range constraints might need to be expressed as text or via URI.
- Add a valueType property on schema:PropertyValue; controlled vocabulary (or URI) that specifies the kind of value-- numeric, text, categorical, audio, video, boolean, object, binary....