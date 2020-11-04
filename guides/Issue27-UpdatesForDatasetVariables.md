# Draft revisions to schema:variableMeasured and schema:PropertyValue

## Variables with Numeric Values

The schema:variableMeasured/schema:PropertyValue entity provides a basic framework for description of variables that have numeric values. Scientific datasets might have fields containing many other kinds of values, including categorical, nominal, ordinal, boolean, identifiers, structured data objects, and unstructured objects like text, audio, video, or images.
 
We highly recommend using the schema:PropertyValue object to describe variables using one of a tiered set of options, and avoid the simple free text value. The schema:PropertyValue object enables a structured description of the variable that can provide greater interoperability and machine processing. 

### Basic
In it's most basic form, a schema:PropertyValue can be published with a name and description of the variable. This is essentially equivalent to the free text option, but makes parsing the metadata simpler.  The name provided should be a meaningful identifier for the variable, along with a text explanation of the property that is quantified, what kind of values are expected, and any measurement method or environmental context information that applies to values for the variable. Example:

```
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
      "description": "The bottle number for each associated measurement. The values are 6 digit, 0-padded integers."
    },
    ...
  ]
}
```

### Recommended
The recommended level of description is to include one or more resolvable identifiers that specify the data type and semanitcs of the variable. The identifiers should resolve to a location on the web that provides a description of the variable for people to use, as well as an RDF representation using a documented vocabulary. An HTTP URI is recommended for the identifier scheme, and the URI should be included in the schema:PropertyID field  in the schema:PropertyValue object. Multiple identifiers could be provided to specify the variable data type and semantics at different granularities. For example there might be a propertyID for 'water temperature', 'sea surface water temperature', 'sea surface water temperature measured with protocol X, daily average, Kelvins, xsd:decimal'. 

Example: 

```
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
```

These first two levels of property value description will support dataset discovery scenarios. A more complete description of the property value would be useful to support evaluation of a dataset for fitness for an intended use. Such a description should include a name, description and propertyID, with additional information. Here are the other properties of PropertyValue defined by schema.org:
- [unitText](https://schema.org/unitText). A string that identifies a unit of measurement that applies to all values for this variable.
- [unitCode](https://schema.org/unitCode). Value is expected to be TEXT or URL. We recommend providing an HTTP URI that identifies a unit of measure from a vocabulary accessible on the web.  
- [minValue](https://schema.org/minValue). If the value for the variable is numeric, this is the minimum value that occurs in the dataset. Not useful for other value types.
- [maxValue](https://schema.org/maxValue). If the value for the variable is numeric, this is the maximum value that occurs in the dataset. Not useful for other value types.
- [measurementTechnique](https://schema.org/measurementTechnique). A text description of the measurement method used to determine values for this variable. If standard measurement protocols are defined and registered, these can be identified via http URI's.


Properties inherited from schema:Thing 
[url](https://schema.org/url) Any schema:Thing can have a URL property, but because the value is simply a url the relationship of the linked resource can not be expressed.  Usage is optional. The recommendation is that URLs should link to resources that would be interesting or useful for a person, but are not intended to be machine-actionable.

Example:
```
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
```

### More in depth variable descriptions.

For situations where it is not practical to have a registry of variable definitions that bind the semantics associated with an identifier, there are two options. In either case the dcat:conformsTo property should be asserted in the schema:Dataset to identify the profile (if any) used for extending the PropertyValue description. Either of these extension mechanisms would only be interoperable for clients that recognize the meaning of the dcat:conformsTo value. 

#### Option 1 (preferred)
Take advantage of the open-world nature of rdf data to include an ontologic description of the variable using some other more expressive vocabulary, e.g. SVO, SSN, DDI, in the PropertyValue instance.


#### Option 2 (not preferred)
Use schema:valueReference to add additional content; properties of the measurement could be included as PropertyValue/valueReference instances. 

- [valueReference](https://schema.org/valueReference). This is defined as "A pointer to a secondary value that provides additional information on the original value, e.g. a reference temperature.". This is essentially an unconstrained key-value pair, providing great flexibility, but little interoperability. This property could be used to provide additional useful information about a variable in the context of a community-adopted profile. The expected schema.org value type is one of:
  -  [Enumeration](https://schema.org/Enumeration)
  -  [PropertyValue](https://schema.org/PropertyValue)
  -  [QualitativeValue](https://schema.org/QualitativeValue)
  -  [QuantitativeValue](https://schema.org/QuantitativeValue)
  -  [StructuredValue](https://schema.org/StructuredValue).   


