# Describe variables in Dataset 

Discussion: https://github.com/ESIPFed/science-on-schema.org/issues/27

## Status ##
Proposed

## Decision ##
Updates to the Variable section in the science on Schema.org Dataset.md document, recommending a tiered approach to description of variables in a dataset. 

specific recommended additions in science on Schema.org namespace:
- Add a rangeConstraint property on schema:PropertyValue to allow specification of the range of values expected for a property.  Numeric ranges are already accounted for. Categorical ranges could be expressed as a URI for the vocabualary used to populate values. Other more complex range constraints might need to be expressed as text or via URI.
- Add a valueType property on schema:PropertyValue; controlled vocabulary (or URI) that specifies the kind of value-- numeric, text, categorical, audio, video, boolean, object, binary....


## Context ##
Original issue question: which is the best way to represent ontological terms representing observation types of a measuredVariable.  This has evolved into a wider discussion of what needs to be represented in schema.org documents to document dataset variables.  See [discussion document](https://github.com/ESIPFed/science-on-schema.org/blob/issue27-measuredVariable/guides/DiscussionVariableMeasured.md)


## Consequences ##
- inclusion of description of variables included in a dataset will enhance search capabilities, allowing users to find datasets that contain the specific kinds of information they need.
- More in depth information about variable will allow more meaningful assessment of whether a dataset is fit for purpose before accessing the data. This information migh include how variables were determined (measurement technique), the range of values in data, what vocabualsries are used, or what data type is used to quantify a variable.
- 

