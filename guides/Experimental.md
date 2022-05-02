# Experimental recommendations

This document contains suggestions for recommendations to address use cases and problems that users have identified as possible additions to the science-on-schema.org recommendations. These are presented for discussion and testing, and potentially for inclusion in a future release of the guidelines. Suggestions here should be linked to issues in the Science-On-Schema.org issue tracker. 

# Table of contents
1. [Linking Physical Samples to a Dataset](#LinkingPhysicalSamples)
2. [Advanced variable value type description](#AdvancedVariableValueType)

   2.1 [Variables with non-numeric values](#NonnumericValues)

   2.2 [Value range is controlled vocabulary](#ControlledVocabulary)

   2.3 [Structured values](#StructuredValues)

   2.4 [Variables that contain references](#References)
 
   2.5 [Array, Gridded or Coverage Data](#ArrayValues)
 
 
<div id='LinkingPhysicalSamples'/>

## Linking  Physical Samples to a Dataset

Currently, there isn't a great semantic property for a Dataset to distinguish the related physical samples. However, we can use the [schema:hasPart](https://schema.org/hasPart) property to accomplish this without too much compromise. A [GitHub issue](https://github.com/earthcubearchitecture-project418/p418Vocabulary/issues/16) has been setup to follow this scenario. Here is a suggested approach to link physical samples to a Dataset:

<pre>
{
  "@context": [
    "https://schema.org/",
    {    
    <strong>"igsn": "http://igsn.org/",</strong>
    } 
  ],
  "@type": "Dataset",
  ...,
  <strong>"hasPart": [
    {
      "@type": ["CreativeWork", "http://vocabulary.odm2.org/specimentype/individualSample/"],
      "identifier": {
        "@id": "igsn:WHO000A53",
        "@type": "PropertyValue",
        "propertyID": "https://registry.identifiers.org/registry/igsn",
        "url": "http://igsn.org/WHO000A53",
        "value": "igsn:WHO000A53"
      },
      "spatialCoverage": {
        "@type": "Place",
        "geo": {
          "@type": "GeoCoordinates",
          "latitude": -26.94486389,
          "longitude": 143.43508333,
          "elevation": 219.453
        }
      }
      ...
    },
    {
      "@type": ["CreativeWork", "http://vocabulary.odm2.org/specimentype/individualSample/"],
      "identifier": {
        "@id": "igsn:WHO000A67",
        "@type": "PropertyValue",
        "propertyID": "https://registry.identifiers.org/registry/igsn",
        "url": "http://igsn.org/WHO000A67",
        "value": "IGSN:WHO000A67"
      }
      ...
    }
  ]</strong>
}
</pre>

Here, we use the superclass of a Dataset, the [schema:CreativeWork](https://schema.org/CreativeWork) to also define a Physical Sample. We disambiguate the Creative Work to be a physical sample by using the IGSN type in the `@type` field. See the [schema:CreativeWork](https://schema.org/CreativeWork) for additional fields available for adding to the physical sample.

<div id='AdvancedVariableValueType'/>

## Advanced variable value type description

This section includes suggestions for documenting variable with a wider range of implementations, based on discussions following [Issue 27](https://github.com/ESIPFed/science-on-schema.org/issues/27)

<div id='NonnumericValues'/>

### Variables with non-numeric values
Scientific datasets might have fields containing many other kinds of values than simple numeric values. These include categorical, nominal, ordinal, boolean, identifiers, structured data objects, and unstructured objects like text, audio, video, or images. Some suggestions for describing these kinds of variable are included here, using some elements from other community vocabularies.

For variables that have values that are not numeric, the datatype should be specified using a data type vocabulary. Schema.org does not have a data type property, we recommend extending schema.org using the [Quantity, Units of Measure, Dimensions and Types (QUDT) ontology](http://qudt.org/) (qudt:) dataType property. Schema.org defines a schema:DataType class with the following basic data types:

| type  | subtype  | note  |
|---|---|---|
|[DateTime](https://schema.org/DateTime)| |A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] (see Chapter 5.4 of ISO 8601 or [XSD dateTime](https://www.w3.org/TR/xmlschema-2/#dateTime)).
|[Date](https://schema.org/Date)| |A date value in ISO 8601 date format.
|[Time](https://schema.org/Time)| |A point in time recurring on multiple days in the form    hh:mm:ss[Z|(+|-)hh:mm] (see [XSD time](http://www.w3.org/TR/xmlschema-2/#time))
|[Number](https://schema.org/Number)| |allows integer and decimal number
| |[Float](https://schema.org/Float)|use with scientific notation?
| |[Integer](https://schema.org/Integer)|use to restrict to integer numbers
|[Boolean](http://schema.org/Boolean)| |
|[Text](http://schema.org/Text)| |  
| |[URL](https://schema.org/URL)|  

The QUDT model does not restrict the range of values that can populate qudt:dataType, so the schema.org values can be used. Note that the values used to populate data type should be the full schema.org identifier, e.g. http://schema.org/Text.

If other more specific data types need to be specified, [xml schema datatypes](https://www.w3.org/TR/xmlschema-2/#built-in-primitive-datatypes) ([used in RDF as well](https://www.w3.org/TR/rdf11-concepts/#xsd-datatypes)), or [QUDT quantity kinds](http://qudt.org/doc/2019/12/DOC_VOCAB-QUANTITY-KINDS-ALL-v2.1.html)  may be used. There are QUDT quantity kinds that can be used to specify types of structured data values (see  Variables with components, below).  

Example: a date and time variable data type:

<pre>
 {"@type": "PropertyValue",
   "name": “Date of experiment",
   "description": “date and time when observation was obtained",
   "propertyID": "https://www.ex-data-repo.org/dataset-parameter/20861",
   "qudt:dataType": "https://schema.org/DateTime" },
</pre>

<div id='ControlledVocabulary'/>

### Value range is controlled vocabulary
The `schema:DefinedTermSet` class can be used to specify a controlled vocabulary that populates a text variable value. This requires using the schema:rangeIncludes property outside of its expected domain, which is schema:Property. The schema:DefinedTerm elements in the schema:DefinedTermSet must at least provide a schema:termCode that corresponds to the strings that will appear in the data. Other labels for the vocabulary value can be provided by schema:name and schema:alternateName, as well as a definition in schema:description, and a URI using schema:identifier, all properties on schema:DefinedTerm. The @id on the schema:DefinedTermSet should provide a URI for the controlled vocabulary if one exists.

Example encoding for a variableMeasured that is populated with a controlled vocabulary, using schema:rangeIncludes/DefinedTermSet:

<pre>
 {
    "@type": "PropertyValue",
    "@id": "urn:example:ex_variable0007",
    "propertyID": "http://astromat/parameters/0027",
    "name": "calcAvg",
    "alternateName":"can calculate average",     
    "description": "Value in sample data are 'Can be averaged', 'Cannot be averaged', 'It is average'",
    "qudt:dataType": "https://schema.org/Text"     
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
</pre>

The controlled vocabulary could also be identified by a URI for communities that have identifiers for controlled vocabularies.  In the above example this would be encoded thus:


```
"rangeincludes": <https://www.astromat.org/vocab/calcavg>
```

Ideally, the URI can be dereferenced to obtain a schema:DefinedTermSet object that defines the vocabulary elements. Recognizing that in many cases vocabulary representations use SKOS or a tabular text listing, the critical consideration is that the identifier for the vocabulary is something the user community will recognize.

<div id='StructuredValues'/>

### Structured values
Structured values might appear in two contexts. The structure might include a value, units of measure and measurementMethod--that is a value and associated attributes (i.e. metadata).  In the other case, the structured value might represent a vector, tensor, tuple value, or an object that has some internal data structure. In this case each value is represented by a set of component values.

In the first case, variables in an attribute role provide information about one or more of the measure value variables, e.g. to specify metadata about another variable. Examples: a 'units' variable that specifies the units of measure for the value in a different variable, or a 'measurement method' variable that specifies how the value in a different variable was determined.
<pre>
{
  "@type": "PropertyValue",
  "@id": "http://astromat/dataset/data_astromat_analysis/variable0016",
  "propertyID": "quantitykind:Diameter",
  "name": "mineralSize",
  "description": "length value, UOM is value reference",
  "qudt:dataType": "https://schema.org/Number",
  "valueReference": [
    {"@type": "PropertyValue",
    "name": "Units",
    "description": "unit of measure for diameter length",
    "qudt:dataType": "https://schema.org/Text",
    "rangeIncludes":"http://qudt.org/schema/qudt/LengthUnit"  },
        },
    {"@type": "PropertyValue",
    "name": "Uncertainty",
    "description": "magnitude of uncertainty on diameter measure",
     "qudt:dataType": "https://schema.org/Number"  }  ]  }
</pre>

An example of a variable that has a structured value with measure components is a location variable that has latitude, longitude and spatial reference system as components. The latitude and longitude value each have the same units of measure and measurement method; the spatial reference is asserted, and might itself have component properties. The more complex situations, where the variable value is itself an object (e.g. a JSON object) can be represented using nested schema:valueReference elements.
In this case the PropertyValue should be typed as a qudt Structured Data Type (http://qudt.org/schema/qudt/StructuredDataType). The PropertyValue description aggregates elements of possibly different types, described using nested [schema:valueReference](https://schema.org/valueReference) PropertyValue elements. This type would be used to represent values that are JSON or XML type objects, or ordered sequences like Tuples in which each element in the sequence might represent a different conceptual variable.

 Example describing a structured value:

<pre>{
    "@type": "PropertyValue",
     "name": "PLSSLocation",
     "propertyID":"http://www.opengis.net/def/property/OGC/0/SamplingLocation",
     "alternateName": "US Public Land Survey System location",
     "description": "Location of sampling feature specified using PLSS grid",
     "qudt:dataType": ["http://qudt.org/schema/qudt/StructuredDataType", "https://www.usgs.gov/media/images/public-land-survey-system-plss"],
     "valueReference": [
          {"@type": "PropertyValue",
            "name": "PLSS_Meridians",
            "description": "List north-south baseline and east-west meridian that Townships and Ranges are referenced to.",
            "qudt:dataType": "https://schema.org/Text"  },
           {"@type": "PropertyValue",
            "name": "TWP",
            "alternateName": "Township",
            "description": "Township in PLSS grid, relative to reported baseline. ",
            "qudt:dataType": "https://schema.org/Text"     },
           {"@type": "PropertyValue",
            "name": "RGE",
            "alternateName": "Range",
            "description": "Range in PLSS grid, relative to reported meridian.",
            "qudt:dataType": "https://schema.org/Text"  }
         ]
 },</pre>

<div id='References'/>

### Variables that contain references
For variables with values that are references to data objects stored elsewhere, use the qudt:ReferenceDataType (http://qudt.org/schema/qudt/ReferenceDatatype). Ideally the reference should use a scheme (like http URI) that can be dereferenced to obtain the value.
<pre>
    {"@type": "PropertyValue",
     "name": "Link to rock description",
     "propertyID":"http://geosciml.org/feature/gbEarthMaterialDescription",
     "alternateName": "rock material description",
     "description": "link to structured description of rock material using GeoSciML properties.",
     "qudt:dataType":["xsd:anyURI", "http://qudt.org/schema/qudt/ReferenceDatatype"]
     }
</pre>

<div id='ArrayValues'/>

### Array, Gridded or Coverage Data

For data that represent continuously varying values, data values are typically reported as a function of one or more dimensions. Dimensions might be temporal, spatial, or thematic.  An example is a time series of water levels in a well. In this case, the 'dimension' or independent variable is time, and the dependent variable is water level.  Another common example is a geospatial grid representing magnetic field intensity. The dimensions might be northing and easting in some spatial reference system, and the dependent variable is field intensity. For the basic discovery and evaluation purposes supported by these recommendations, we do not propose how to represent the sampling points along the various dimension, only the dimension and value types and their semantics.  Detailed description of the data structure can be included in the dataset description using one of the standard schemes designed for this purpose (e.g. [OpenDAP v4 DMR](https://docs.opendap.org/index.php/DAP4:_Specification_Volume_1), or [W3C DataCube](https://www.w3.org/TR/vocab-data-cube/#cubes-model)).

The recommended approach is to include a schema:additionalType for the Dataset, with the value 'http://qudt.org/schema/qudt/MultiDimensionalDataFormat'. The variableMeasured for the dataset can be represented with two base schema:PropertyValue instances -- the [dimensions](http://purl.org/linked-data/cube#measureDimension) (independent variable in the data structure) and the [measures](http://purl.org/linked-data/cube#measure) (the dependent variable values that are a function of the dimension coordinates). Each of these schema:PropertyValue instances has a qudt:dataType of 'http://qudt.org/schema/qudt/TupleType' (prefix http://qudt.org/schema/qudt/ <http://qudt.org/schema/qudt/>) and an array of child schema:valueReference objects describing each dimension or measure respectively.  

Each schema:valueReference is a schema:PropertyValue, which has a schema:propertyID specifying the semantics of a dimension or measure, as well as other properties useful to document that variable. The details of the sample spacing along each dimension are not described in this scheme.  

Example for multi-dimensional dataset

```
{"@type": [ "Dataset"],
    "additionalType":[ "http://qudt.org/schema/qudt/MultiDimensionalDataFormat" ],
    "name": "Surface geology and geophysics grid",
...
 "variableMeasured": [
   {"@type": "PropertyValue",
    "name": "Dimensions",
    "propertyID": "http://purl.org/linked-data/cube#measureDimension",
    "description": "The dimensions for logical space in which measured values are positioned...",
    "qudt:dataType": "http://qudt.org/schema/qudt/TupleType",
    "valueReference": [
        {"@type": "PropertyValue",
         "name": "latitude",
         "propertyID": "http://semanticscience.org/resource/latitude",
         "qudt:dataType": "https://schema.org/Number",
         "unitText": "decimal degree"  },
        {"@type": "PropertyValue",
         "name": "longitude",
         "propertyID": "http://semanticscience.org/resource/longitude",
         "qudt:dataType": "https://schema.org/Number",
         "unitText": "decimal degree"}
     ]
  },
  {"@type": "PropertyValue",
   "name": "observation value",
   "propertyID": "http://purl.org/linked-data/cube#measure",
   "description": "tuple with magnetic field intensity, g value, observed outcrop rock type, and elevation",
   "qudt:dataType": "http://qudt.org/schema/qudt/TupleType",
   "valueReference": [
      "@list":{   
       {"@type": "PropertyValue",
         "name": "mag",
         "alternateName": "magnetic field intensity",
         "propertyID": "http://ex.org/resource/magneticFieldIntensity",
          "qudt:dataType": "https://schema.org/Number",
          "unitText": "amperes per metre" },
        { "@type": "PropertyValue",
          "name": "acceleration of gravity",
          "propertyID": "http://ex.org/resource/localAccelGravity",
          "alternateName": "Range",
          "measurementTechnique": "gravimeter model xxx",
          "qudt:dataType": "https://schema.org/Number",
          "unitText": "mgal"},
        { "@type": "PropertyValue",
          "name": "lith",
          "alternateName": "Outcrop lithology",
          "propertyID": "http://ex.org/resource/geosciml/rocktype",
          "qudt:dataType": "https://schema.org/Text"
          "rangeIncludes": [ <https://geosciml.org/vocab/simpleLithology> ] },
         { "@type": "PropertyValue",
           "name": "elevation",
           "propertyID": "http://ex.org/resource/elevation",
           "description": "elevation relative to MSL, in meters",
           "qudt:dataType": "https://schema.org/Number",
           "unitText": "meters" }
            ]   }    }    ]  }
```

In this example each point the measure dimension space is associated with a magnetic field intensity, acceleration of gravity, and outcrop lithology.  Note the use of the @list implementation of the valueReference because the tuple is an ordered list. 
