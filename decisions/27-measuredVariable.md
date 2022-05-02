# Describe variables in Dataset 

Discussion: https://github.com/ESIPFed/science-on-schema.org/issues/27

## Status ##
Accepted

## Decision ##
Update the Variable section in the Science on Schema.org Dataset.md document, replacing text between lines 328 to 379 in Dataset.md with a description of three Tiers of variableMeasured: text only, adding PropertyValue/PropertyID, and adding additional structured properties.

### Specific recommendations for schema.org usage

1. Textual names and descriptions are minimally acceptable but not preferred

1. Multiple `so:propertyID` values could be used to indicate different levels of granularity/detail for the property associated with an attribute. For example there might be a propertyID for 'water temperature', 'sea surface water temperature', 'sea surface water temperature measured with protocol X, daily average, Kelvins, xsd:decimal'.  Each of these description approaches addresses different use cases. Communities can define standard reference resources that provide variable definitions with identifiers that can be used for information interchange.

1. use of other `schema:PropertyValue` properties recommended, including `schema:unitText`, `schema:unitCode`, `qudt:dataType`, and others.

### Recommended additions in Science on Schema.org vocabulary:
- Use [Quantity, Units of Measure,Dimensions and Types (QUDT) ontology](http://qudt.org/) (qudt:) property `qudt:dataType` with values from `schema:DataType` to document basic data types for `schema:PropertyValue`, and other [xml schema](https://www.w3.org/TR/xmlschema-2/#built-in-primitive-datatypes)[  RDF](https://www.w3.org/TR/rdf11-concepts/#xsd-datatypes), or [QUDT quantity kinds](http://qudt.org/doc/2019/12/DOC_VOCAB-QUANTITY-KINDS-ALL-v2.1.html) for more complex data types. Specific types mentioned in the revised text are: `qudt:MultiDimensionalDataFormatType`, `qudtschema:TupleType`, `qudtschema:DimensionalDatatype`, `qudtschema:ReferenceDatatype`, and `qudtschema:CompositeDataStructure`. (prefix qudtschema: <http://qudt.org/schema/qudt/>)


## Context ##
Original issue question: which is the best way to represent ontological terms representing observation types of a measuredVariable.  This has evolved into a wider discussion of what needs to be represented in schema.org documents to document dataset variables.  See [discussion document](https://github.com/ESIPFed/science-on-schema.org/blob/issue27-measuredVariable/guides/DiscussionVariableMeasured.md)

Other more advanced definitions of variables within an Observational data context using `schema:Observation` were explored but only described in a new Experimental.md document as we determined that more work would be needed to reach agreeement on a consistent and logically consistent approach.

## Consequences ##
- inclusion of description of variables included in a dataset will enhance search capabilities, allowing users to find datasets that contain the specific kinds of information they need.
- More in depth information about variable will allow more meaningful assessment of whether a dataset is fit for purpose before accessing the data. This information migh include how variables were determined (measurement technique), the range of values in data, what vocabularies are used, or what data type is used to quantify a variable.

