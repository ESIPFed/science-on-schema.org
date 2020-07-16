# Draft revisions to schema:variableMeasured and schema:PropertyValue

## Variables

The schema:variableMeasured/schema:PropertyValue entity provides a basic framework for description of variables that have numeric values. Scientific datasets might have fields containing many other kinds of values, including categorical, nominal, ordinal, boolean, identifiers, structured data objects, and unstructured objects like text, audio, video, or images.
 
We highly recommend using the schema:PropertyValue object to describe variables using one of a tiered set of options, and avoid the simple free text value. The schema:PropertyValue object enables a structured description of  the variable that can provide greater interoperability and machine processing. 
In it's most basic form, a schema:PropertyValue can be published with a name and description of the variable. This is essentially equivalent to the free text option, but makes parsing the metadata simpler.  The name provided should be a meaningful identifier for the variable, along with a text explanation of the property that is quantified, what kind of values are expected, and any measurement method or environmental context information that applies to values for the variable. Example:

{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
  "variableMeasured": [
    {
      "@type": "PropertyValue",
      "name": "Bottle identifier",
      "description": "The bottle number for each associated measurement. The values are prefixed with a three-letter field session identifier, followed by a 6 digit, 0-padded integer value."
    },
    ...
  ]
}

At the next level of description, a resolvable identifier can be provided that links to a variable description. Ideally the variable description would be available in an HTML page for people to use, as well as an RDF representation using a documented vocabulary. HTTP URI is recommended for the identifier scheme, and the URI should be included in the schema:PropertyID field  in the schema:PropertyValue object.  Example: 

{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
  "variableMeasured": [
    {
      "@type": "PropertyValue",
      "name": "latitude",
      "description": "Latitude where water samples were collected; north is positive. Latitude is a geographic coordinate which refers to the angle from a point on the Earth's surface to the equatorial plane",
      "propertyID":"http://semanticscience.org/resource/SIO_000319"},
    ...
  ]
}

These first two levels of property value description will support dataset discovery scenarios. A more complete description of the property value would be useful to support evaluation of a dataset for fitness for an intended use. Such a description should include a name, description and propertyID, with additional information. Here are the other properties of PropertyValue defined by schema.org:
- [unitText](https://schema.org/unitText). A string that identifies a unit of measurement that applies to all values for this variable.
- [unitCode](https://schema.org/unitCode). Value is expected to be TEXT or URL. We recommend providing an HTTP URI that identifies a unit of measure from a vocabulary accessible on the web.  
- [minValue](https://schema.org/minValue). If the value for the variable is numeric, this is the minimum value that occurs in the dataset. Not useful for other value types.
- [maxValue](https://schema.org/maxValue). If the value for the variable is numeric, this is the maximum value that occurs in the dataset. Not useful for other value types.
- [measurementTechnique](https://schema.org/measurementTechnique). A text description of the measurement method used to determine values for this variable. If standard measurement protocols are defined and registered, these can be identified via http URI's.


Properties inherited from schema:Thing 
[url](https://schema.org/url) Any schema:Thing can have a URL property, but because the value is simply a url, this is not very useful because the relationship of the linked resource can not be expressed.  Usage is optional, and urls should be to resources that would be interesting or useful for a person.

Eexample:
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  ...
  "variableMeasured": [
    {
      "@type": "PropertyValue",
      "name": "latitude",
      "propertyID":"http://semanticscience.org/resource/SIO_000319",
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


### For discussion: more in depth variable descriptions.

For situations where it is not practical to have a registry of variable definitions, there are two options. 

1. Use schema:valueReference to add additional content; properties of the measurement could be included as PropertyValue/valueReference instances. 

1. Take advantage of the open-world nature of rdf data to include an ontologic description of the variable using some other vocabulary, e.g. SVO, SSN, DDI in the PropertyValue instance.

Either of these extension mechanisms would only be interoperable in the context of a profile that is known to clients parsing the schema.org instance. The dcat:conformsTo property should be asserted in the schema:Dataset to identify the profile (if any) used for extending the PropertyValue description. 

The schema:valueReference property:
- [valueReference](https://schema.org/valueReference). This is defined as "A pointer to a secondary value that provides additional information on the original value, e.g. a reference temperature.". This is essentially an unconstrained key-value pair, providing great flexibility, but little interoperability. This property could be used to provide additional useful information about a variable in the context of a community-adopted profile. The expected schema.org value type is one of:
  -  [Enumeration](https://schema.org/Enumeration)
  -  [PropertyValue](https://schema.org/PropertyValue)
  -  [QualitativeValue](https://schema.org/QualitativeValue)
  -  [QuantitativeValue](https://schema.org/QuantitativeValue)
  -  [StructuredValue](https://schema.org/StructuredValue).   
