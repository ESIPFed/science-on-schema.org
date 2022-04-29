# Recommendations for documenting temporal coverage of dataset #

Discussion: [Add OWL-Time and chronometric age extension guidance](https://github.com/ESIPFed/science-on-schema.org/issues/77)

## Status ##
Proposed, for discussion

## Decision ##
Update the guidance for temporalCoverage description.  Main recommendations:
1. use [http://www.w3.org/2006/time#hasTime](https://w3c.github.io/sdw/time/#time:hasTime) property from W3C OWL Time ([Cox and Little, 2021-06-29 editors draft](https://w3c.github.io/sdw/time/)) to document temporalCoverages that can not be expressed using schema:DateTime
1. Provide numeric age positions, if possible. Use the appropriate time units for the dating method and geologic age (BP,ka,Ma,Ga). Include age uncertainty when known.
1. If age is specified based on a time scale, provide nearest subsuming age from the [International Chronostratigraphic Chart](https://stratigraphy.org/chart). Note that the ICS chart is updated on an ad hoc basis, annually or more frequently. It would be useful to cite the specific version used if you are doing precision chronology.

## Context ##
Temporal coverage is defined as "the time period during which data was collected or observations were made; or a time period that an activity or collection is linked to intellectually or thematically (for example, 1997 to 1998; the 18th century)" ([ARDC RIF-CS](https://documentation.ardc.edu.au/display/DOC/Temporal+coverage)). For documentation of Earth Science, Paleobiology or Paleontology datasets, we are interested in the second case-- the time period that data are linked to thematically. 

[Current guidance for temporal coverage](https://github.com/ESIPFed/science-on-schema.org/blob/master/guides/Dataset.md#temporal-coverage) accounts for [ISO8601 DateTime and DateTime ranges](https://en.wikipedia.org/wiki/ISO_8601), and this guidance is sufficient to account for temporal coverates that are in the range of the [Gregorian calendar](https://en.wikipedia.org/wiki/Gregorian_calendar). 

The schema:temporalCoverage property has rangeIncludes schema:Text, schema:DateTime, and schema:URL. Specifying temporalCoverage as text would probably be useful for someone reading the metadata record, but as far as interoperability, it wouldn't be useful unless there were detailed conventions about the text that would be used (controlled vocabulary and syntax that could be validated).  The same problem holds for specifying temporalCoverage with a URL. Aggregators whould have to understand the semantics of the URL to integrate the information in a search interface. Also, there is no way to express a temporalCoverage with the beginning and end of a time interval unless it can be expressed as an ISO8601 DateTime range. 

### Solution
For temporal extents that can not be expressed using schema:DateTime, use W3C OWL time elements from the http://www.w3.org/2006/time# namespace. SOSO is already recommending use of elements from some other namespaces, and OWL time is widely recognized and vetted.

For user-friendliness, include a text statement of the temporal coverage; aggregators might not be able to handle the more precise information in the time:hasTime elements.

1. Temporal interval with hasTime beginning and end. 

  *Example*: 

```
{    "@context": {
        "@vocab": "http://schema.org/",
        "isc": "http://resource.geosciml.org/classifier/ics/ischart/",
        "gstime": "http://schema.geoschemas.org/contexts/temporal#",
        "time": "http://www.w3.org/2006/time#",
        "ts": "http://resource.geosciml.org/vocabulary/timescale/",
        "xsd": "https://www.w3.org/TR/2004/REC-xmlschema-2-20041028/datatypes.html"
    },
    {
        "@type": "Dataset",
        "description": "Eruptive activity at Mt. St. Helens, Washington, March 1980- January 1981; temporalCoverage string is ISO8601 time interval; show representation as OWL Time interval for example.",
        "temporalCoverage": "1980-03-27T19:36:00Z/1981-01-03T00:00:00Z",
        "time:hasTime": {
            "@type": "time:Interval",
            "time:hasBeginning": {
                "@type": "time:Instant",
                "time:inXSDDateTimeStamp": "1980-03-27T19:36:00Z"
            },
            "time:hasEnd": {
                "@type": "time:Instant",
                "time:inXSDDateTimeStamp": "1981-01-03T00:00:00Z"
            }  
         } 
     } 
}
```
2. Numeric TimePosition for a single geological date/age. Use decimal value and appropriate time unit. Include uncertainties in the dates/ages when known.  

*Example: Dataset with single time instant temporal coverage. Context same as example 1.*

```
{   "@type": "Dataset",
    "description": "Temporal position expressed numerically scaled in millions of years increasing backwards relative to 1950. To specify a Geologic Time Scale, we use an OWL Time Instant. The example below specifies 760,000 years (0.760 Ma) before present with an error of 0.04 Ma at one sigma.",
    "temporalCoverage": "Eruption of Bishop Tuff, about 760,000 years ago",
    "time:hasTime": {
        "@type": "time:Instant",
        "time:inTimePosition": {
            "@type": "time:TimePosition",
            "time:hasTRS": {"@id": "gstime:MillionsOfYears"},
            "time:numericPosition": { "@value": 0.76, "@type": "xsd:decimal" },
            "gstime:GeologicTimeUnitAbbreviation": { "@value": "Ma, "@type": "xsd:string" } 
            "gstime:Uncertainty": { "@value": 0.35, "@type": "xsd:decimal" },
        }  
        "gstime:UncertaintySigma": { "@value": 2.0, "@type": "xsd:decimal" }
    }   
}
```

*Example: Dataset with temporal coverage that is named time interval from geologic time scale, provide numeric positions of beginning and end for interoperability. Providing the numeric values is only critical if the TRS for the nominalPosition is not the [International Chronostratigraphic Chart](https://stratigraphy.org/chart).
Context same as example 1.

```
{   
    "@type": "Dataset",
    "description": "Temporal position expressed with a named time ordinal era from [International Chronostratigraphic Chart](https://stratigraphy.org/chart):",
    "temporalCoverage": "Bartonian",
    "time:hasTime": {
        "@type": "time:Instant",
        "time:inTimePosition": [
            {
                "@type": "time:TimePosition",
                "time:hasTRS": {"@id": "ts:gts2020"},
                "time:NominalPosition": { "@value": "isc:Bartonian", "@type": "xsd:anyURI" }
            },
            {
                "@type": "time:Interval",
                "time:hasBeginning": {
                    "@type": "time:Instant",
                    "rdfs:comment": "temporal positions from ICS 2020-03 (https://stratigraphy.org/ICSchart/ChronostratChart2020-03.pdf)",
                    "time:inTimePosition": {
                        "@type": "time:TimePosition",
                        "time:hasTRS": {"@id": "gstime:MillionsOfYear"},
                        "time:numericPosition": { "@value": "41.2", "@type": "xsd:decimal" }  
                    }
                },
                "time:hasEnd": {
                    "@type": "time:Instant",
                    "rdfs:comment": "temporal positions from ICS 2020-03 (https://stratigraphy.org/ICSchart/ChronostratChart2020-03.pdf)",
                    "time:inTimePosition": {
                        "@type": "time:TimePosition",
                        "time:hasTRS": {"@id": "gstime:MillionsOfYear"},
                        "time:numericPosition": { "@value": "37.71", "@type": "xsd:decimal" }  
                    }   
                }    
            }
        ]
    }   
}
```

3. Temporal intervals with nominal temporal position that have identifiers. When possible, used temporal intervals defined by the [International Chronostratigraphic Chart](https://stratigraphy.org/chart), access via [ARDC vocabulary service](https://vocabs.ardc.edu.au/viewById/196), or via [GeoSciML vocabularies landing page](http://geosciml.org/resource/).  If temporal intervals with identifies from other schemes are available, they can be included in a separate time:hasTime element.  If intervals are not from the ICS chart it is recommended to provide an interval with beginning and end numeric positions for better interoperability.

*Example: Context same as example 1.*:

```
   {"@type": "Dataset",
    "description": "Temporal position expressed with an interval bounded by named time ordinal eras from [International Chronostratigraphic Chart](https://stratigraphy.org/chart). NumericPositions not included, expect clients can lookup bounds for ISC nominal positions:",
    "temporalCoverage": "Triassic to Jurassic",
    "time:hasTime": {
        "@type": "time:Interval",
        "time:hasBeginning": {
            "@type": "time:Instant",
            "time:inTimePosition": {
                "@type": "time:TimePosition",
                "time:hasTRS": {"@id": "ts:gts2020"},
                "time:NominalPosition": { "@value": "isc:Triassic", "@type": "xsd:anyURI" }
            }
        },
        "time:hasEnd": {
            "@type": "time:Instant",
            "time:inTimePosition": {
                "@type": "time:TimePosition",
                "time:hasTRS": {"@id": "ts:gts2020"},
                "time:NominalPosition": { "@value": "isc:Jurassic", "@type": "xsd:anyURI" }    
                }
            }
        }
    }
```

Temporal intervals with beginning and end specified by numeric positions; source data specifies uncertainties on the numeric positions.

*Example* Context same as example 1.:

```
       { "@type": "Dataset",
            "description": "Isotopic ages determined at the bottom and top of a stratigraphic section in the Columbia River Basalts",
            "temporalCoverage": "Between 18.0 +/- 0.35 and 12.7 +/- 0.4 Ma",
            "time:hasTime": {
                "@type": "time:Interval",
                "time:hasBeginning": {
                    "@type": "time:Instant",
                    "time:inTimePosition": {
                        "@type": "time:TimePosition",
                        "rdfs:comment": "beginning is older bound of age envelop",
                        "time:hasTRS": {"@id": "gstime:MillionsOfYears"},
                        "time:numericPosition": { "@value": 18.0, "@type": "xsd:decimal" },
                        "gstime:GeologicTimeUnitAbbreviation": { "@value": "Ma, "@type": "xsd:string" },
                        "gstime:Uncertainty": { "@value": 0.35, "@type": "xsd:decimal" }
                    },
                    "gstime:UncertaintySigma": { "@value": 2.0, "@type": "xsd:decimal" }
                },
                "time:hasEnd": {
                    "@type": "time:Instant",
                    "time:inTimePosition": {
                        "@type": "time:TimePosition",
                        "rdfs:comment": "ending is younger bound of age envelop",
                        "time:hasTRS": {"@id": "gstime:MillionsOfYears"},
                        "time:numericPosition": { "@value": 12.7, "@type": "xsd:decimal" },
                        "gstime:GeologicTimeUnitAbbreviation": { "@value": "Ma, "@type": "xsd:string" },
                        "gstime:Uncertainty": { "@value": 0.4, "@type": "xsd:decimal" }

                    "gstime:UncertaintySigma": { "@value": 2.0, "@type": "xsd:decimal" }
                }
            }
        }
```
5. Temporal aggregates. Option 1. -- make value of hasTime an array of TemporalEntities. or 2. use [TemporalAggregate](https://w3c.github.io/sdw/time-aggregates/) as value of hasTime. (TBD if there is interest - not done) 


### Discussion
Schema.org JSON objects are not intended to encode detailed data -- this is content that would be in the described dataset. In order to keep the basic discovery and evaluation, details about chronometric procedures and the processes for determining uncertainties for assigning temporal coverage can be included in the dataset description. The information will be useful for users evaluating the dataset based on the metadata, but is not necessary to support discovery.

### Deep background
Conceptually, the temporal coverage is a TemporalEntity as defined by OWL time ([Cox and Little, 2021-06-29 editors draft](https://w3c.github.io/sdw/time/)).  For the purposes of dataset documentation to support data discovery and evaluation for use, the TemporalEntities of interest are TimeInstants, and ProperIntervals. A TimeInstant has a single TemporalPosition, and a ProperInterval has Beginning and End properties that are each specified by a TemporalPosition. A TemporalPosition can be specified by a nominal value (e.g. a named interval), or a numeric value. 

Temporal coverage might be associated with a single event, or might be specified with named eras, either as a single era (e.g. 'Bartonian', 'Eoarchean'), or with bounding eras (e.g. Cambrian to Mississippian). Named eras might reference the [International Chronostratigraphic Chart](https://stratigraphy.org/chart), or some other time scale, e.g. local chronostratigraphic, biostratigraphic, or magnetostratigraphic reference system, or an astronomic cycle system. Finally temporal coverage might be specified with numeric temporal positions for the beginning and end of an interval. 

Individual events might be associated with calendar dates e.g. '1980 eruption of Mount St. Helens', '1906 San Francisco Earthquake'. Prehistoric events like 'Bonneville Flood', 'Brunhes–Matuyama reversal', or 'Intrusion of Tuolumne Intrusive Suite', will typically have some estimated numeric temporal position or interval. Like wise the temporal position of the beginning and end of a named era from a time scale will generally have some associated estimate of the numeric temporal position. 

Numeric temporal positions (a.k.a. 'dates' or 'ages') are based on some chronometric procedure and temporal coordinate reference system. Comparing such dates in detail might require deep understanding of the basis for the value -- the measurement method, constants used (e.g. isotopic decay constants), calibrations applied (e.g. for C-14 data). The temporal coordinate reference system must be known to specify the temporal orgin (commonly taken as 1950 on the Gregorian calendar) and the units of measure, typically years before present (BP, geoschemas:BP, qudt:YR), thousand years (ka, geoschemas:ka), million years (Ma, geoschemas:Maqudt:MegaYR) or billion years (Ga, geoschemas:Ga).



### Related work:
- Earthcube P419 developed a [recommendation for describing Dataset temporal coverage based on OWL-Time]( https://geoschemas.org/extensions/temporal.html).
- Research Data Australia Registry Interchange Format: Collections and Services (RIF-CS) schema: [Temporal Coverage]( https://documentation.ardc.edu.au/display/DOC/Temporal+coverage)
- EML [temporal coverage](https://eml.ecoinformatics.org/schema/eml-coverage_xsd.html#SingleDateTimeType_alternativeTimeScale ) See also [5.3.3 'The eml-coverage module - Geographic, temporal, and taxonomic extents of resources']( https://eml.ecoinformatics.org/eml-schema.html#discovery-and-interpretation-modules)
- ESIP documentation cluster [extent documentation](https://wiki.esipfed.org/Extent_Documentation). Discusses documentaion for spatial and temporal extents in CSDGM, ISO19115, DIF, ECHO. Focus is mostly on DateTime extents, but DIF includes a Paleo_Temporal_Coverage to account for named intervals with identifiers.
- [USGIN ISO19115 profile](http://hdl.handle.net/10150/630040) [temporal extent recommendation](http://usgin.github.io/usginspecs/USGIN_ISO_Metadata.htm#_Toc381426792)
- GeoSciML [GeologicAge](http://docs.opengeospatial.org/is/16-008/16-008.html#183) In GeoSciML, ages are attached to events, but the pattern using 3 parts (NumericAgeRange, olderNamedAge, youngerNamedAge) could equally apply to documenting dataset temporal coverage.

## Consequences ##
Aggregators can parse SOSO profile schema.org JSON to extract temporal coverage information that can be used to construct search interfaces to find data thematically related to time intervals that do not have calendar dates.
