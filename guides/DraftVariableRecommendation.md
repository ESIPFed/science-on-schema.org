# Describing variables in datasets using schema.org

## Background
The description of measured variables for a dataset is an outstanding problem.  Issues include:

- What level of granularity? Variables can be described at a conceptual level, a logical level, or an implementation (physical level).  Each of these description approaches addresses different use cases.
- How much of the conceptual model for a variable instance should be explicitly included in a schema.org dataset description? 
- What ontologies should be recommended to link variables for semantically precise description?

The framework for this discussion is a data object ('type', 'entity', 'object', etc.) that has a collection of attributes, each representing a measured variable. Each variable has a range for valid values, and a cardinality that constrains the number of values associated with the DataObject. The variables have a conceptual level definition that might be a complex object, and can have one or more implementations in particular representations. Description and documentation of the conceptual level is important for interfaces through which domain practitioners interact with data. Description and documentation of the implementation level is important for software systems that automate operations on the data. 

A variable is anchored by a primary observed property, typically a phenomenon concept, and might be more narrowly scoped by concepts such as its value type (e.g. numeric or categorical) and range, feature-of-interest, unit of measurement for reported values, aggregate functions (e.g. average, maximum), or measurement method (Including sensor or device used). Measurements are commonly indirectly linked to a feature of interest through a sampling feature, which has a location that might be defined by geospatial coordinates and/or relationship to the feature of interest (e.g. 10 m above ground surface). Individual measurements are made by some agent at a particular time.  Examples of variables are ‘Methane, daily formation rate per unit of sediment mass’, ‘Practical salinity of the water body by CTD and computation using UNESCO 1983 algorithm’.

In the schema.org description of a dataset, the sdo:Dataset typically represents the data object, and the attributes are described using sdo:variableMeasured/
[sdo:PropertyValue](https://schema.org/PropertyValue). Each record in the dataset describes an instance or individual observation of a feature of interest.

Current Science on schema.org recommendation is to document variables like this:

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


# Issues:


## Source for property URIs to use in the sdo:propertyID field. 

## How are variables defined
CF standard name structure:
[surface][component]base_quantity [at surface][in medium][due to process][assuming condition].
CF names in [CF standard name table]( https://cfconventions.org/Data/cf-standard-names/73/src/cf-standard-name-table.xml) have an id, but no namespace appears to be defined, so there aren't dereferenceable URIs it seems.

Scientific Variables Ontology (SVO) is a blueprint outlining the required and optional components for creating a machine-interpretable scientific variable concept, similar to the structure for a CF standard name. SVO does not provide a vocabulary of measured variables based on this ontology. 

SWEET has a set of property labels with some hierarchical structure providing weak semantics, but noe explicit definitions in the http://sweetontology.net/prop/Property namespace. Properties are at the conceptual level, e.g. 'total alkalinity', 'pH', 'precision', 'temperature range'. 

LTER Measurements https://vocab.lternet.edu/vocab/vocab/index.php?tema=667&/measurements. A word net, similar to SWEET, but doesn't provide URI or definition.  All term URIs are query fragments on the 'vocab/index.php' resource.

From ENVO (Via Kai )
- Entity: e.g., sediment or rock [Feature of interest]
- Characteristic/Quality: e.g., depth of sediment (we can create entity quality pairings like this in ENVO using sediment and PATO:depth in the axiom). [Property]
- Standard/Unit: e.g., meter
- Measurement technique or protocol
- Additional environmental context concept to describe the environment where the measurement was made e.g., tundra biome, mine


## Recommendations

schema.org is not designed as an ontology to describe scientific data. It is intended to support basic data discovery and initial evaluation. The PropertyValue entity in schema.org provides a basic framework for  description of variables. For many purposes, the PropertyID specified in a schema:ProperyValue instance can be a URI that references an in-depth property description such as that included with CF names, or a Scientific Variables Ontology instance. Communities can define standard reference resources that provide variable definitions to be used for information interchange. 

For situations where it is not practical to have a registry of variable definitions, there are two options. 
1. Other schema.org properties like measurementTechnique and valueReference. If standard measurement protocols are defined an registered, these can be identified via http URI's in the measurementTechnique.  Other properties of the measurement could be included as valueReference/PropertyValue instances in the variableMeasured instance. 
1. Take advantage of the open-world nature of rdf data to include an ontologic description of the variable using e.g. SVO or SSN in the PropertyValue instance.

Either of these extension mechanisms would only be interoperable in the context of a profile that is known to clients parsing the schema.org instance. The dcat:conformsTo property should be asserted in the schema:Dataset to identify the profile used for extending the PropertyValue description. 

Do we need to allow for different profiles used on different variables....??? I don't think so, but if so the dcat:conforms to would need to be asserted on each PropertyValue that is extended.  This might be a recommended extension pattern for any element.
