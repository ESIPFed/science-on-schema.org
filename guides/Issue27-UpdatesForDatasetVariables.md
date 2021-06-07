# Variables

Variables in a dataset present various kinds of information, for example:
- Data management information related to the data item (record) in the dataset, e.g. identifier (primary key), create or update data, data source information.
- A data value that is a result of an observation, e.g. a temperature value, color, species categorization
- Metadata useful to understand and use an observation result reported in the data, e.g. method used, units of measure, context for the observation.

It is useful to add information about the variables in a dataset to enhance discovery and support evaluation of the data. This can be done using the [schema:variableMeasured](https://schema.org/variableMeasured) field. Schema.org allows the value of variableMeasured to be a simple text string, but it is strongly recommended to use the [schema:PropertyValue](https://schema.org/PropertyValue) type to describe the variable in more detail. 

![Variables](/assets/diagrams/dataset/dataset_variables.svg "Dataset - Variables")


The [schema:propertyID](https://schema.org/propertyID) in the schema:PropertyValue object should resolve to a web page that provides a human-friendly description of the variable.  Ideally, the identifier should also be resolved to obtain an RDF representation using a documented vocabulary for machine consumption, for example a [sosa:Observation](https://www.w3.org/TR/vocab-ssn/#SOSAObservation)or [DDI represented variable](https://ddi-lifecycle-technical-guide.readthedocs.io/en/latest/Specific%20Structures/Data%20Description.html#represented-variable). Describing the variables with machine understandable vocabularies is necessary if you want your data to be interoperable with other data - i.e., to be more FAIR.  The property can be identified at any level of granularity, depending on what the data provider can determine. For example there might be a propertyID for 'water temperature', 'sea surface water temperature', 'sea surface water temperature measured with protocol X, daily average, Kelvins, xsd:decimal'.   If there are choices, the most specific property identifier should be used.

The schema:name should match the label associated with the variable in the dataset serialization (e.g. the column name in a CSV file). If the variable name in the dataset does not clearly convey the variable concept, a more human-intelligible name can be provide using schema:alternateName.


Example:
<pre>
{
  "@context": {
    "@vocab": "https://schema.org/"
  },
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities ...",
  ...
  "variableMeasured": [
    {
      "@type": "PropertyValue",
      "name": "latdd",
      "alternateName":"latitude, decimal degrees",
      <strong>"propertyID":"http://www.geoscienceontology.org/geo-lower/quantity#latitude"</strong>,
      "description": "Latitude where water samples were collected ...",
    },
    ...
  ]
}
</pre>

Other properties of schema:PropertyValue can add additional useful information about variables with measured numeric values:

- [unitText](https://schema.org/unitText). A string that identifies a unit of measurement that applies to all values for this variable.
- [unitCode](https://schema.org/unitCode). Value is expected to be TEXT or URL. We recommend providing an HTTP URI that identifies a unit of measure from a vocabulary accessible on the web.  The QUDT unit vocabulary provides and extensive set of registered units of measure that can be used to populate the schema:unitCode property to specify the units of measure used to report datavalues when that is appropriate. 
- [minValue](https://schema.org/minValue). If the value for the variable is numeric, this is the minimum value that occurs in the dataset. Not useful for other value types.
- [maxValue](https://schema.org/maxValue). If the value for the variable is numeric, this is the maximum value that occurs in the dataset. Not useful for other value types.
- [measurementTechnique](https://schema.org/measurementTechnique). A text description of the measurement method used to determine values for this variable. If standard measurement protocols are defined and registered, these can be identified via http URI's.
- [url](https://schema.org/url) Any schema:Thing can have a URL property, but because the value is simply a url the relationship of the linked resource can not be expressed.  Usage is optional. The recommendation is that schema:url should link to a web page that would be useful for a person, but are not intended to be machine-actionable.

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

## Variables with non-numeric values
Scientific datasets might have fields containing many other kinds of values, including categorical, nominal, ordinal, boolean, identifiers, structured data objects, and unstructured objects like text, audio, video, or images. Some recommendations for describing these kinds of variable are included here.

### Data Type
For variables that have values that are not numeric, the datatype should be specified using a data type vocabulary. Schema.org does not have a data type property, we recommend extending schema.org using the [Quantity, Units of Measure,Dimensions and Types (QUDT) ontology](http://qudt.org/) (qudt:) dataType property. Schema.org defines a schema:DataType class with the following basic data types: 

| type  | subtype  | note  |
|---|---|---|
|[DateTime](https://schema.org/DateTime)| |A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] (see Chapter 5.4 of ISO 8601 or [XSD dateTime](https://www.w3.org/TR/xmlschema-2/#dateTime)).
|[Date](https://schema.org/Date)| |A date value in ISO 8601 date format.
|[Time](https://schema.org/Time)| |A point in time recurring on multiple days in the form    hh:mm:ss[Z|(+|-)hh:mm] (see [XSD time](http://www.w3.org/TR/xmlschema-2/#time))
|[Number](https://schema.org/Number)| |allows integer and decimal number
| |[Float](https://schema.org/Float)|use with scientific notation?
| |[Integer](https://schema.org/Integer)|use to restrict to integer numbers
|[Boolean](https://schema.org/Boolean)| |   
|[Text](https://schema.org/Text)| |  
| |[URL](https://schema.org/URL)|  

The QUDT model does not restrict the range of values that can populate qudt:dataType, so the schema.org values can be used.

If other more specific data types need to be specified, [xml schema datatypes](https://www.w3.org/TR/xmlschema-2/#built-in-primitive-datatypes) ([used in RDF as well](https://www.w3.org/TR/rdf11-concepts/#xsd-datatypes)), or [QUDT quantity kinds](http://qudt.org/doc/2019/12/DOC_VOCAB-QUANTITY-KINDS-ALL-v2.1.html)  may be used. There are QUDT quantity kinds that can be used to specify types of structured data values (see  Variables with components, below).  

Example: a date and time variable data type:

```
 {"@type": "PropertyValue",
   "name": “Date of experiment",
   "description": “date and time when observation was obtained",
   "propertyID": "https://www.ex-data-repo.org/dataset-parameter/20861",
   "qudt:dataType": "DateTime" },
,
```

### Value range is controlled vocabulary
The schema:DefinedTermSet  class can be used to specify a controlled vocabulary that populates a text variable value. This requires using the schema:rangeIncludes property outside of its expected domain, which is schema:Property. The schema:DefinedTerm elements in the schema:DefinedTermSet must at least provide a schema:termCode that corresponds to the strings that will appear in the data. Other labels for the vocabulary value can be provided by schema:name and schema:alternateName, as well as a definition in schema:description, and a URI using schema:identifier, all properties on schema:DefinedTerm. The @id on the schema:DefinedTermSet should provide a URI for the controlled vocabulary if one exists. 

Example encoding for a variableMeasured that is populated with a controlled vocabulary, using schema:rangeIncludes/DefinedTermSet:

```
 {
    "@type": "PropertyValue",
    "@id": "ex_variable0007",
    "propertyID": "http://astromat/parameters/0027",
    "name": "calcAvg",
    "alternateName":"can calculate average",     
    "description": "Value in sample data are 'Can be averaged', 'Cannot be averaged', 'It is average'",
    "qudt:dataType": "Text"     
    "rangeIncludes": {
        "@type":"DefinedTermSet",
        "@id":"https://www.astromat.org/vocab/calcavg",        
        "name":"calcAvg controlled vocabulary",        
        "hasDefinedTerm": [
            {"@type": "DefinedTerm", "termCode":"Can be averaged"},
            {"@type": "DefinedTerm", "termCode":"Cannot be averaged"},
            {"@type": "DefinedTerm", "termCode":"It is average"}
                ]
        }
}
```

The controlled vocabulary could also be identified by a URI for communities that have identifiers for controlled vocabularies.  In the above example this would be encoded thus:

```
"rangeincludes": [ <https://www.astromat.org/vocab/calcavg>]  
```
Ideally, the URI can be dereferenced to obtain a schema:DefinedTermSet object that defines the vocabulary elements. Recognizing that in many cases vocabulary representations use SKOS or a tabular text listing, the critical consideration is that the identifier for the vocabulary is something the user community will recognize.
 
## Variables with components

### Structured values 
Structured values might appear in two contexts. The structure might include a value, units of measure and measurementMethod--that is a value and associated attributes (i.e. metadata).  In the other case, the structured value might represent a vector, tensor, tuple value, or an object that has some internal data structure. In this case each value is represented by a set of component values. 

In the first case, variables in an attribute role provide information about one or more of the measure value variables, e.g. to specify metadata about another variable. Examples: a 'units' variable that specifies the units of measure for the value in a different variable, or a 'measurement method' variable that specifies how the value in a different variable was determined. 
```
{
  "@type": "PropertyValue",
  "@id": "http://astromat/dataset/data_astromat_analysis/variable0016",
  "propertyID": "quantitykind:Diameter",
  "name": "mineralSize",
  "description": "length value, UOM is value reference",
  "qudt:dataType": "Number",
  "valueReference": [
    {"@type": "PropertyValue",
    "name": "Unit of Measure",
    "description": "unit of measure for diameter length",
    "qudt:dataType": "Text",
    "rangeIncludes":"http://qudt.org/schema/qudt/LengthUnit"  },
        },
    {"@type": "PropertyValue",
    "name": "Uncertainty",
    "description": "magnitude of uncertainty on diameter measure",
     "qudt:dataType": "Number"  }  ]  }
```

An example a variable that has a structured value with measure components is a location variable that has latitude, longitude and spatial reference system as components. The latitude and longitude value each have the same units of measure and measurement method; the spatial reference is asserted, and might itself have component properties. The more complex situations, where the variable value is itself an object (e.g. a JSON object) can be represented using nested schema:valueReference elements. 
In this case the PropertyValue should be typed as a [Composite Data Structure](http://qudt.org/schema/qudt/CompositeDataStructure). The Variable value aggregates elements of possibly different types, described using nested [schema:valueReference](https://schema.org/valueReference) PropertyValue elements. This type would be used to represent values that are JSON or XML type objects, or ordered sequences like Tuples in which each element in the sequence might represent a different conceptual variable. 
 
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
            "qudt:dataType": "Text"  },
           {"@type": "PropertyValue",
            "name": "TWP",
            "alternateName": "Township",
            "description": "Township in PLSS grid, relative to reported baseline. ",
            "qudt:dataType": "Text"     },
           {"@type": "PropertyValue",
            "name": "RGE",
            "alternateName": "Range",
            "description": "Range in PLSS grid, relative to reported meridian.",
            "qudt:dataType": "Text"  }
         ]
 },
```

## Variables that contain references
For variables that are references to data objects stored elsewhere, use the  qudt:ReferenceDataType (http://qudt.org/schema/qudt/ReferenceDatatype).  Ideally the referece should use a scheme (like http URI) that can be dereferenced to obtain the value.
```
    {"@type": "PropertyValue",
     "name": "Link to rock description",
     "propertyID":"geosciml:gbEarthMaterialDescription",
     "alternateName": "rock material description",
     "description": "link to structured description of rock material using GeoSciML properties.",
     "qudt:dataType":["xsd:anyURI", "qudtschema:ReferenceDatatype"]
     }
```   
 
## Array, Gridded or Coverage Data

For data that represent continuously varying values, data values are typically reported as a function of one or more dimensions. Dimensions might be temporal, spatial, or thematic.  An example is a time series of water levels in a well. In this case, the 'dimension' or independent variable is time, and the dependent variable is water level.  Another common example is a geospatial grid representing magnetic field intensity. The dimensions might be northing and easting in some spatial reference system, and the dependent variable is field intensity. For the basic discovery and evaluation purposes supported by these recommendations, we do not propose how to represent the sampling points along the various dimension, only the dimension and value types and their semantics.  Detailed description of the data structure can be included in the dataset description using one of the standard schemes designed for this purpose (e.g. [OpenDAP v4 DMR](https://docs.opendap.org/index.php/DAP4:_Specification_Volume_1), or [W3C DataCube](https://www.w3.org/TR/vocab-data-cube/#cubes-model)). 

The recommended approach is to include a schema:additionalType for the Dataset, with the value 'qudt:MultiDimensionalDataFormatType'. The variableMeasured for the dataset can be represented with two base schema:PropertyValue instances -- the [dimensions](http://purl.org/linked-data/cube#measureDimension) (independent variable in the data structure) and the [measures](http://purl.org/linked-data/cube#measure) (the dependent variable values that are a function of the dimension coordinates). Each of these schema:PropertyValue instances has a qudt:dataType of 'qudtschema:TupleType' (prefix qudtschema: <http://qudt.org/schema/qudt/>) and an array of child schema:valueReference objects describing each dimension or measure respectively.  

Each schema:valueReference is a schema:PropertyValue, which has a schema:propertyID specifying the semantics of a dimension or measure, as well as other properties useful to document that variable. The details of the sample spacing along each dimension are not described in this scheme.  
 
Example for multi-dimensional dataset 
```
{"@type": [ "Dataset"]
    "additionalType":[ "qudt:MultiDimensionalDataFormat" ],
    "name": "Surface geology and geophysics grid",
...
 "variableMeasured": [
   {"@type": "PropertyValue",
    "name": "Dimensions",
    "propertyID": "http://purl.org/linked-data/cube#measureDimension",
    "description": "The dimensions for logical space in which measured values are positioned...",
    "qudt:dataType": "qudtschema:TupleType",
    "valueReference": [
        {"@type": "PropertyValue",
         "name": "latitude",
         "propertyID": "http://semanticscience.org/resource/latitude",
         "qudt:dataType": "Number",
         "unitText": "decimal degree"  },
        {"@type": "PropertyValue",
         "name": "longitude",
         "propertyID": "http://semanticscience.org/resource/longitude",
         "qudt:dataType": "Number",
         "unitText": "decimal degree"}
     ]
  },
  {"@type": "PropertyValue",
   "name": "observation value",
   "propertyID": "http://purl.org/linked-data/cube#measure",
   "description": "tuple with magnetic field intensity, g value, observed outcrop rock type, and elevation",
   "qudt:dataType": "qudtschema:TupleType",
   "valueReference": [
       {"@type": "PropertyValue",
         "name": "mag",
         "alternateName": "magnetic field intensity",
         "propertyID": "http://ex.org/resource/magneticFieldIntensity",
          "qudt:dataType": "Number",
          "unitText": "amperes per metre" },
        { "@type": "PropertyValue",
          "name": "acceleration of gravity",
          "propertyID": "http://ex.org/resource/localAccelGravity",
          "alternateName": "Range",
          "measurementTechnique": "gravimiter model xxx",
          "qudt:dataType": "Number",
          "unitText": "mgal"},
        { "@type": "PropertyValue",
          "name": "lith",
          "alternateName": "Outcrop lithology",
          "propertyID": "http://ex.org/resource/geosciml/rocktype",
          "qudt:dataType": "Text"
          "rangeIncludes": [ <https://geosciml.org/vocab/simpleLithology> ] },
         { "@type": "PropertyValue",
           "name": "elevation",
           "propertyID": "http://ex.org/resource/elevation",
           "description": "elevation relative to MSL, in meters",
           "qudt:dataType": "Number",
           "unitText": "meters" }
            ]        }    ]  }
```
In this example each point the measure dimension space is associated with a magnetic field intensity, acceleration of gravity, and outcrop lithology.
           
## Use of schema:Observation to describe properties:

More in depth description can be provided for dataset variables that are the result of an observation process, and not registered such that a single schema:propertyID will suffice to enable users to evaluate the value for fitness to their purpose. In this case, the variable can be represented with schema:propertyID typed as schema:Observation.

example: 

```
 "@type": "PropertyValue",
      "name": "sea_surface_temp",
      "description": "sea surface temperature measured in degrees Fahrenheit",
      "propertyID": {
        "@type": "Observation",
        "observedNode": { 
          "@id": "http://purl.obolibrary.org/obo/ENVO_01001581",
          "name": "sea surface layer"
	},
        "measuredProperty": { 
          "@id": "http://purl.obolibrary.org/obo/PATO_0000146",
          "name": "temperature"
        }
      }
```

This approach uses unexpected value ranges for schema:propertyID, which expects Text or URL, and for schema:observedNode, which expects schema:StatisticalPopulation (see [schema.org Issue 2291](https://github.com/schemaorg/schemaorg/issues/2291)).  Other useful Observation properties could be included based on the rdf open world, like observation procedure (schema:measurementTechnique), or the sensor used (sosa:madeBySensor)

example:
```
{
"@type": "PropertyValue",
"@id": "http://example.org/data/property/00246",
 "name": "Relative Humidity",
"propertyID": {
    "@type":"Observation", 
    "description": "Relative humidity as averaged over 15min at COPR.",
     "name" "Relative humidity, AVG, 15min, COPR, 06.02.2017, 3:00 PM"' ;
     "sosa:madeBySensor": "http://example.org/data/HUMICAP-H",
     "observedNode":  "http://example.org/data/COPR_Station",
     "measuredProperty":"http://sweetontology.net/propFraction/RelativeHumidity",
     "measurementTechnique": "https://www.globe.gov/documents/348614/348678/Relative+Humidity+Protocol/89f8c44d-4a99-494b-ba81-1853b80710b4"
}
```
This approach allows a semantically rich description of a property, but is quite different and would not be interoperable with variable described using the other recommendations here. 
