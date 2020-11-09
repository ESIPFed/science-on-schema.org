# Draft revisions to so:variableMeasured and so:PropertyValue

The so:variableMeasured/so:PropertyValue entity provides a framework for description of variables that have numeric values. Scientific datasets might have fields containing many other kinds of values, including categorical, nominal, ordinal, boolean, identifiers, structured data objects, and unstructured objects like text, audio, video, or images.
 
We highly recommend using the so:PropertyValue object to describe variables using one of a tiered set of options, and avoid the simple free text value. The so:PropertyValue object enables a structured description of the variable that can provide greater interoperability and machine processing.

### Basic: Tier 0
In it's most basic form, a so:PropertyValue can be published with a name and description of the variable. This is essentially equivalent to the free text option, but makes parsing the metadata simpler.  The name provided should match the label for the variable in the dataset.  If that label does not clearly convey the meaning of the variable, use so:alternateName to provide a label that better conveys the meaning of the variable. Use so:description to provide a text explanation of the variable, including its data type, what kind of values are expected, and any measurement method or environmental context information that applies to values for the variable in the described dataset. Example:

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
## Variables with Numeric Values
### Recommended: Tier 1
The recommended level of description is to include one or more resolvable identifiers that specify the semanitcs of the variable using [so:propertyID](https://schema.org/propertyID) in the so:PropertyValue object. Identifiers should resolve to a web page that provides a human-friendly description of the variable. Ideally an RDF representation using a documented vocabulary for machine consumption should be accessible via content negotiation. HTTP URI is the recommended identifier scheme. Multiple identifiers could be provided. These could be equivalent identifiers from different registries, or could specify the variable data type and semantics at different granularities. For example there might be a propertyID for 'water temperature', 'sea surface water temperature', 'sea surface water temperature measured with protocol X, daily average, Kelvins, xsd:decimal'. 

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

### More properties: Tier 2

These first two levels of property value description will support dataset discovery scenarios. A more complete description of the property value would be useful to support evaluation of a dataset for an intended use. Such a description should include a name, description and propertyID, with additional information using the other properties of PropertyValue defined by schema.org:
- [unitText](https://schema.org/unitText). A string that identifies a unit of measurement that applies to all values for this variable.
- [unitCode](https://schema.org/unitCode). Value is expected to be TEXT or URL. We recommend providing an HTTP URI that identifies a unit of measure from a vocabulary accessible on the web.  
- [minValue](https://schema.org/minValue). If the value for the variable is numeric, this is the minimum value that occurs in the dataset. Not useful for other value types.
- [maxValue](https://schema.org/maxValue). If the value for the variable is numeric, this is the maximum value that occurs in the dataset. Not useful for other value types.
- [measurementTechnique](https://schema.org/measurementTechnique). A text description of the measurement method used to determine values for this variable. If standard measurement protocols are defined and registered, these can be identified via http URI's.


Properties inherited from so:Thing 
- [url](https://schema.org/url) Any so:Thing can have a URL property, but because the value is simply a url the relationship of the linked resource can not be expressed.  Usage is optional. The recommendation is that URLs should link to resources that would be interesting or useful for a person, but are not intended to be machine-actionable.

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

### More in depth variable descriptions: Tier 3.

For situations in which there is no registry of variable definitions that bind the semantics associated with an identifier that can be used as a so:propertyID, there are two options. In either case the dcat:conformsTo property should be asserted in the so:Dataset to identify a profile used for extending the PropertyValue description. Either of these extension mechanisms would only be interoperable for clients that recognize the meaning of the dcat:conformsTo value. 

#### Option 1 (preferred)
Take advantage of the open-world nature of rdf data to include an ontologic description of the variable using some other more expressive vocabulary, e.g. SVO, SSN, DDI, in the PropertyValue instance. 

Example using the [sosa vocabulary](https://www.w3.org/TR/vocab-ssn/)
 
```
"variableMeasured": 
{
"@type": "PropertyValue",
"@id": "http://example.org/data/property/00246",
"propertyID": "https://www.wikidata.org/wiki/Property:P5596",
"name": "Relative Humidity",
"sosa:isResultOf": {
    "@type":"sosa:Observation", 
    "rdfs:comment": "Relative humidity as averaged over 15min at COPR.",
     "rdfs:label" "Relative humidity, AVG, 15min, COPR, 06.02.2017, 3:00 PM"' ;
     "sosa:madeBySensor": "http://example.org/data/HUMICAP-H",
     "sosa:hasFeatureOfInterest":  "http://example.org/data/COPR_Station",
     "sosa:observedProperty":"http://sweetontology.net/propFraction/RelativeHumidity",
     "sosa:usedProcedure": "https://www.globe.gov/documents/348614/348678/Relative+Humidity+Protocol/89f8c44d-4a99-494b-ba81-1853b80710b4"
}
```
note that this approach assumes that these various properties (e.g. sensor, procedure) are shared by all data items in the dataset.

#### Option 2 (not preferred)
Use [so:valueReference](https://schema.org/valueReference) to add additional content; properties of the measurement could be included as PropertyValue/valueReference instances. so:valueReference is defined as "A pointer to a secondary value that provides additional information on the original value, e.g. a reference temperature.". This is essentially an unconstrained key-value pair, providing great flexibility, but little interoperability. This property could be used to provide additional useful information about a variable in the context of a community-adopted profile. The expected schema.org value type is one of:
  -  [Enumeration](https://schema.org/Enumeration)
  -  [PropertyValue](https://schema.org/PropertyValue)
  -  [QualitativeValue](https://schema.org/QualitativeValue)
  -  [QuantitativeValue](https://schema.org/QuantitativeValue)
  -  [StructuredValue](https://schema.org/StructuredValue).   

## Variables with non-numeric values (Tier 3)

### Data Type
For variables that have values that are not numeric, the datatype should be specified using a data type vocabulary like xml schema, rdf datasets, QUDT datatypes. Schema.org does not have a so:dataType property that can be used for describing so:PropertyValues. We recommend using qudt:dataType as a property on so:PropertyValue to specify the kind of data value for that property in the described dataset. RDF datatypes are recommended to populate the qudt:dataTyep property.  The QUDT unit vocabulary provides and extensive set of register units of measure that can be used with the qudt:hasUnit property to specify the units of measure used to report datavalues when that is appropriate. 

Example with data type and units specified for a dataset measured variable data type:

```
        {
            "@type": "PropertyValue",
            "@id": "http://lod.example-data-repository.org/id/dataset/3300/variable0002",
            "name": "year",
            "description": "year of experiment",
            "propertyID": "https://www.example-data-repository.org/dataset-parameter/20861",
            "unitText": "year",
            "unitCode": "unit:YR",
            "qudt:dataType": "xsd:gYear",
            "qudt:hasUnit": "unit:YR"
        },
```

### Value range is controlled vocabulary

For consideration by ESIP SOSO group: Two options. 1. adopt so:rangeIncludes to point at so:DefinedTermSet. This is outside of the current normal usage of so:rangeIncludes, but seems consistent with the intention of the property.

#### so:DefinedTermSet
schema.org has some additional "pending" elements that use "Defined" in their labels in a fairly loose way semantically speaking:
- [so:DefinedTermSet](https://schema.org/DefinedTermSet) can be used to identify an Ontology or controlled vocabulary using a URL and name, that might pertain to ALL the variableMeasured types in some Dataset, or for each PropertyValue.
- [DefinedTerm](https://schema.org/DefinedTerm) identifies a concept via a URL, and can also have a name, alternate name, identifier, comment, same as, etc. Unfortunately the proposed list of properties that can take DefinedTerm as a value do not include any properties that apply to PropertyValue, so we’d have to extend Schema.org.
- [termCode](https://schema.org/termCode) is a property of DefinedTerm, and only allows a TEXT value. It be an abbreviation or  the hash-suffix that identifies the Term in the DefinedTermSet (note that deconstructing Identifiers in this way, only to have to reconstruct a URL that is dereferenceable, is problematic!)

Example encoding for a variableMeasured that is populated with a controlled vocabulary.  Use so:rangeIncludes property to link to a so:DefinedTermsSet that either provides an identifier for a controlled voabulary, or enumerates the vocabulary values using an array of so:DefinedTerm:

```
 {
    "@type": "PropertyValue",
    "@id": "http://astromat/dataset/data_astromat_analysis/variable0007"
    "propertyID": "http://astromat/parameters/0027",
    "name": "calcAvg",
    "description": "Value in sample data are 'Can be averaged', 'Cannot be averaged', 'It is average' (note spelling errors)",
    "rangeIncludes": {
        "DefinedTermSet": {
            "hasDefinedTerm": [
                 {"DefinedTerm": 
                     {"name":"Can be averaged"},
                     {"description":"description of what this value means"},
                     {"termCode":"expected value is TEXT, recommend making it a URI"}
                 },
                 {"DefinedTerm": {"name":"Cannot be averaged"}},
                 {"DefinedTerm": {"name":"It is average"}}
            ] 
           }
        }
}
```

### qudt:Enumeration

The [Quantity, Units of Measure,Dimensions and Types (QUDT) ontology](http://qudt.org/) provides an extensive set of data type definitions and related properties.  Example encoding for a variableMeasured that is populated with a controlled vocabulary, using qudt:dataType/qudt:Enumeration.

```
 {
    "@type": "PropertyValue",
    "@id": "http://astromat/dataset/data_astromat_analysis/variable0007",
    "propertyID": "http://astromat/parameters/0027",
    "name": "calcAvg",
    "description": "Value in sample data are 'Can be averaged', 'Cannot be averaged', 'It is average'",
    "qudt:cardinality":"0..1",
    "qudt:dataType": {
        "qudt:Enumeration": {
            "qudt:element": [
                {"qudt:EnumeratedValue": {"qudt:symbol":"Can be averaged"}},
                {"qudt:EnumeratedValue": {"qudt:symbol":"Cannot be averaged"}},
                {"qudt:EnumeratedValue": {"qudt:symbol":"It is average"}}
                ]
        }
    }
}
```