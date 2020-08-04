# Describe variables in Dataset 

Discussion: https://github.com/ESIPFed/science-on-schema.org/issues/27

## Status ##
Proposed

## Decision ##
Updates to the Variable section in the science on Schema.org Dataset.md document, recommending a tiered approach to description of variables in a dataset. 

### specific recommendations for schema.org usage
1. Multiple so:propertyID values could be used to indicate different levels of granularity/detail for the property associated with an attribute. For example there might be a propertyID for 'water temperature', 'sea surface water temperature', 'sea surface water temperature measured with protocol X, daily average, Kelvins, xsd:decimal'.  Each of these description approaches addresses different use cases. Communities can define standard reference resources that provide variable definitions with identifiers that can be used for information interchange. 

1. so:measurementTechnique should provide an identifier for a registered measurement technique description. If one is not available, the measurement technique should be described in text. 

1. For situations where it is not practical to have a registry of variable definitions, take advantage of the open-world nature of rdf data to include an ontologic description of the variable using some other vocabulary, e.g. SVO, SSN, DDI in the PropertyValue instance. This would only be interoperable in the context of a profile that is known to clients parsing the schema.org instance. 

1. The dct:conformsTo property should be asserted in the so:Dataset to identify the profile used for extending the so:PropertyValue description. (see discussion question below on whether dct:conformsTo should be optional at the so:PropertyValue)

1. - Multiple labels that apply to a so:PropertyValue should be represented with an array of so:alternateName. Ideally the names could be scoped in some fashion to associate them with a context in which they are used, but Schema.org does not have an object for representing scoped names.

### Recommended additions in Science on Schema.org vocabulary:
- Add a **valueType** property on so:PropertyValue; controlled vocabulary (or URI) that specifies the kind of value-- numeric, text, categorical, audio, video, boolean, object, binary.... (need to recommend a vocabulary with URIs to use).  The schema.org implementation is strongly oriented towards numeric result values for attributes. This is unnecessarily restrictive. To deal with data objects that are recorded interviews, sound recordings (e.g. whale song), and other 'unstructured' content the valueType could be a MIME type.  Simple literal data types could use the [primitive data types defined by xml schema](https://www.w3.org/TR/xmlschema-2/#built-in-primitive-datatypes).  Object types would need to be defined in a data type registry (e.g. see [RDA Data Type Registries WG](https://www.rd-alliance.org/groups/data-type-registries-wg.html)).  Options: use [rdf:type](https://www.w3.org/TR/rdf-schema/#ch_type). 

- Add a **rangeConstraint** property on so:PropertyValue to allow specification of the range of values expected for a property.  Numeric ranges are already accounted for by so:minValue and so:maxValue. SOSO recommends that these be used to represent the range of actual values in the described dataset. Categorical ranges could be expressed as a URI for the vocabulary used to populate values. Other more complex range constraints might need to be expressed as text or via URI.  The interpretation of the rangeConstraint might vary depending on the valueType. Options: use [rdfs:range](https://www.w3.org/TR/rdf-schema/#ch_range)


## Context ##
Original issue question: which is the best way to represent ontological terms representing observation types of a measuredVariable.  This has evolved into a wider discussion of what needs to be represented in schema.org documents to document dataset variables.  See [discussion document](https://github.com/ESIPFed/science-on-schema.org/blob/issue27-measuredVariable/guides/DiscussionVariableMeasured.md)


## Consequences ##
- inclusion of description of variables included in a dataset will enhance search capabilities, allowing users to find datasets that contain the specific kinds of information they need.
- More in depth information about variable will allow more meaningful assessment of whether a dataset is fit for purpose before accessing the data. This information migh include how variables were determined (measurement technique), the range of values in data, what vocabualsries are used, or what data type is used to quantify a variable.
- 

