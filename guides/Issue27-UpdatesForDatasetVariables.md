# Draft revisions to so:variableMeasured and so:PropertyValue

The so:variableMeasured/so:PropertyValue entity provides a framework for description of variables that have numeric values. Scientific datasets might have fields containing many other kinds of values, including categorical, nominal, ordinal, boolean, identifiers, structured data objects, and unstructured objects like text, audio, video, or images.
 
We highly recommend using the so:PropertyValue object to describe variables using one of a tiered set of options, and avoid the simple free text value. The so:PropertyValue object enables a structured description of a variable that can provide greater interoperability and machine processing. The Starter tier is the simplest approach to describing a variable, followed by the Basic Recommended Tier.  Other sections below provide recommendations for various kinds of property values.

### Starter
A so:PropertyValue can be documented minimally with a name and description of the variable. This is essentially equivalent to the free text option, but makes parsing the metadata simpler.  The name provided should match the label for the variable in the dataset.  If that label does not clearly convey the meaning of the variable, use so:alternateName to provide a label that better conveys the meaning of the variable. Use so:description to provide a text explanation of the variable, including its data type, what kind of values are expected, and any measurement method or environmental context information that applies to values for the variable in the described dataset. Example:

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

## Basic Recommended: 
The recommended level of description is to include one or more resolvable identifiers that specify the semanitcs of a variable using [so:propertyID](https://schema.org/propertyID) in the so:PropertyValue object. Identifiers should resolve to a web page that provides a human-friendly description of the variable. Ideally an RDF representation using a documented vocabulary for machine consumption should be accessible via content negotiation. HTTP URI is the recommended identifier scheme. Multiple identifiers could be provided. These could be equivalent identifiers from different registries, or could specify the variable data type and semantics at different granularities, analogous to the variable cascade from conceptual, to representation, to instance, described in the [DDI data description model](https://ddi-alliance.atlassian.net/wiki/spaces/DDI4/pages/860815393/DDI+Cross+Domain+Integration+DDI-CDI+Review?preview=/860815393/932249666/Part_2_DDI-CDI_Detailed_Model_PR_1.pdf). For example there might be a propertyID for 'water temperature', 'sea surface water temperature', 'sea surface water temperature measured with protocol X, daily average, Kelvins, xsd:decimal'. 

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

## Simple Numeric Data
Standard schema.org properties allow a more complete description of simple numeric variables with additional information using the other properties of so:PropertyValue:
- [unitText](https://schema.org/unitText). A string that identifies a unit of measurement that applies to all values for this variable.
- [unitCode](https://schema.org/unitCode). Value is expected to be TEXT or URL. We recommend providing an HTTP URI that identifies a unit of measure from a vocabulary accessible on the web.  The QUDT unit vocabulary provides and extensive set of registered units of measure that can be used to populate the schema:unitCode property to specify the units of measure used to report datavalues when that is appropriate. 
- [minValue](https://schema.org/minValue). If the value for the variable is numeric, this is the minimum value that occurs in the dataset. Not useful for other value types.
- [maxValue](https://schema.org/maxValue). If the value for the variable is numeric, this is the maximum value that occurs in the dataset. Not useful for other value types.
- [measurementTechnique](https://schema.org/measurementTechnique). A text description of the measurement method used to determine values for this variable. If standard measurement protocols are defined and registered, these can be identified via http URI's.
- [url](https://schema.org/url) Any so:Thing can have a URL property, but because the value is simply a url the relationship of the linked resource can not be expressed.  Usage is optional. The recommendation is that so:url should link to a web page that would be useful for a person, but are not intended to be machine-actionable.

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

### Variable description using an external vocabulary.

For situations in which there is no registry of variable definitions that define identifiers that can be used as a so:propertyID, take advantage of the open-world nature of rdf data to include an ontologic description of the variable using some other more expressive vocabulary, e.g. SVO, SSN, DDI, or W3C DataCube in the PropertyValue instance. If this approach is used, the so:PropertyValue/so:description text should contain text describing the variable scope etc, for clients that do not recognize the extenal vocabulary that is used. The dcat:conformsTo property should be asserted in the so:PropertyValue to identify a profile used for extending the PropertyValue description. This extension mechanisms would only be interoperable for clients that recognize the meaning of the dcat:conformsTo value. 

Example using the [sosa vocabulary](https://www.w3.org/TR/vocab-ssn/)
 
```
"variableMeasured": 
{
"@type": "PropertyValue",
"@id": "http://example.org/data/property/00246",
"propertyID": "https://www.wikidata.org/wiki/Property:P5596",
"name": "Relative Humidity",
"dcat:conformsTo":"https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/",
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

## Variables with non-numeric values

### Data Type
For variables that have values that are not numeric, the datatype should be specified using a data type vocabulary like xml schema, rdf datasets, QUDT datatypes. Schema.org does not have a so:dataType property that can be used for describing so:PropertyValues. We recommend using qudt:dataType as a property on so:PropertyValue to specify the kind of data value for that property in the described dataset. The qudt schema does not constrain the domain or range of the qudt:dataType property.  RDF datatypes are recommended to populate the qudt:dataType property, and several QUDT data types are recommended to identify kinds of structured data values (see  Variables with components, below).  

Example with data type and units specified for a dataset measured variable data type:

```
        {
            "@type": "PropertyValue",
            "@id": "ex:variable0002",
            "name": "year",0
            "description": "year of experiment",
            "propertyID": "https://www.example-data-repository.org/dataset-parameter/20861",
            "unitText": "year",
            "unitCode": "http://qudt.org/vocab/unit/YR",
            "qudt:dataType": "xsd:gYear",
            "qudt:hasUnit": "http://qudt.org/vocab/unit/YR"
        },
```

### Value range is controlled vocabulary
The [Quantity, Units of Measure,Dimensions and Types (QUDT) ontology](http://qudt.org/) provides an extensive set of data type definitions and related properties. The qudt:Enumeration type can be used to specify a controlled vocabulary range for a variable.  Example encoding for a variableMeasured that is populated with a controlled vocabulary, using qudt:dataType/qudt:Enumeration. 

```
 {
    "@type": "PropertyValue",
    "@id": "ex_variable0007",
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

The controlled vocabulary could also be identified by a URI for communities that have identifiers for controlled vocabularies.  In the above example this would be encoded thus:
```
"qudt:dataType": [<qudt:Enumeration>, <https://www.astromat.org/vocab/isaverage>]  
```
 The intention here is that the URI can be dereference to obtain the qudt:Enumeration object that defines the vocabulary elements.
 
## Variables with components
### Variable is represented by a dimensioned set of values (grid, coverage, time series, data cube)
A variable might be represented as a function of one or more dimensions. An example is a time series of water levels in a well; the 'dimension' or independent variable is time, and the dependent variable is water level.  Another common example is a geospatial grid representing magnetic field intensity; the dimensions might be northing, easting, and elevation in some spatial reference system, and the dependent variable is field intensity.  A data cube structure can be implemented in various ways. Measured values might be regularly spaced along each dimension (as in many satellite imagery or time series types) in which case the dimension would be characterized by a start and end value and sample spacing; alternatively the dimension coordinate values might be associated with each measured value to account for irregular measured value spacing. Another variant in the data structure is how multiple measure values at each sampled location are represented.  For the basic discovery and evaluation purposes supported by these recommendations, we do not propose how to represent the sampling points along the various dimension, only the basic value types and their semantics.  Detailed description of the cube structure can be included in the dataset description. 
 - Multi Dimensional Data Format Type: http://qudt.org/schema/qudt/MultiDimensionalDataFormatType.  Value is scoped by one or more associated Dimension variables. This would be the data type for the container PropertyValue with valueReference child elements documenting the dimensions and measured values

 
### Structured values 
A variable in a attribute role provides information about one or more of the measure value variables, e.g. to specify metadata about another variable. Examples: a 'units' variable that specifies the units of measure for a value in a different variable, or a 'measurement method' variable that specifies how the value in a different variable was determined. Other structured values might represent vector, tensor, tuples. In these cases a measure value is represented by a set of component measure values. The structure can be recursive. This kind of structure is typical of JSON or XML value representations, a tree graph. A example of a variable that has a structured value with measure components is a location variable that has latitude, longitude and spatial reference system as component variables. The reference system value might be another structure with components. Recommended data types for container PropertyValue with valueReference child elements documenting the attributes or component and measured values
 - Dimensional Data type: http://qudt.org/schema/qudt/DimensionalDatatype. Value specifies a physical quantity and unit of measuure is embedded in the value.
 - Composite Data Structure: http://qudt.org/schema/qudt/CompositeDataStructure. The Variable value aggregates elements of possibly different types, described using nested [so:valueReference](https://schema.org/valueReference) PropertyValue elements. This type would be used to represent values that are JSON or XML type objects, or ordered sequences like Tuples in which each element in the sequence might represent a different conceptual variable. 
 
 Example describing a structured value:

```
{
    "@type": "PropertyValue",
     "name": "PLSSLocation",
     "propertyID":"http://www.opengis.net/def/property/OGC/0/SamplingLocation",
     "alternateName": "US Public Land Survey System location",
     "description": "Location of sampling feature specified using PLSS grid",
     "qudt:dataType": ["http://qudt.org/schema/qudt/CompositeDataStructure", "https://www.usgs.gov/media/images/public-land-survey-system-plss"],
     "valueReference": [
          {"@type": "PropertyValue",
            "name": "PLSS_Meridians",
            "description": "List north-south baseline and east-west meridian that Townships and Ranges are referenced to.",
            "qudt:dataType": "xsd:token"  },
           {"@type": "PropertyValue",
            "name": "TWP",
            "alternateName": "Township",
            "description": "Township in PLSS grid, relative to reported baseline. ",
            "qudt:dataType": "xsd:token"     },
           {"@type": "PropertyValue",
            "name": "RGE",
            "alternateName": "Range",
            "description": "Range in PLSS grid, relative to reported meridian.",
            "qudt:dataType": "xsd:token"  }
         ]
 },
```

## Variables that contain references
For variables that are references to data objects stored elsewhere, use the  qudt:ReferenceDataType (http://qudt.org/schema/qudt/ReferenceDatatype).  Ideally the referece should use a scheme (like http URI) that can be dereferenced to obtain the value.

    {"@type": "PropertyValue",
     "name": "Link to rock description",
     "propertyID":"geosciml:gbEarthMaterialDescription",
     "alternateName": "rock material description",
     "description": "link to structured description of rock material using GeoSciML properties.",
     "qudt:dataType":["xsd:anyURI", "qudt:ReferenceDatatype"]
     }
