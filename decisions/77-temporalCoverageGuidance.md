# Recommendations for documenting temporal coverage of dataset #

Discussion: [Add OWL-Time and chronometric age extension guidance](https://github.com/ESIPFed/science-on-schema.org/issues/77)

## Status ##
Accepted

## Decision ##
Update the guidance for temporalCoverage description.  Main recommendations:
1. Use http://www.w3.org/2006/time# classes and properties from W3C OWL Time ([Cox and Little, editors draft](https://w3c.github.io/sdw/time/)) to document temporalCoverages that can not be expressed using schema:DateTime.
1. Use https://vocabs.gsq.digital/object?uri=http://linked.data.gov.au/def/trs temporal reference systems (TRS) with the http://www.w3.org/2006/time#hasTRS property. 
1. Provide numeric age positions, if possible. Use the appropriate time unit abbreviations from https://geoschemas.org/extensions/temporal.html for the dating method(s) and geologic date(s)/age(s) (BP, BP-CAL, ka, Ma, Ga). Include [age uncertainties](https://geoschemas.org/extensions/temporal.html#Uncertainty) when known.
1. If age is specified based on a time scale, provide nearest subsuming age from the [International Chronostratigraphic Chart](https://stratigraphy.org/chart). Note that the ICS chart is updated on an ad hoc basis, annually or more frequently. It would be useful to cite the specific version used if you are doing precision chronology.


## Context ##
Temporal coverage is defined as "the time period during which data was collected or observations were made; or a time period that an activity or collection is linked to intellectually or thematically (for example, 1997 to 1998; the 18th century)" ([ARDC RIF-CS](https://documentation.ardc.edu.au/display/DOC/Temporal+coverage)). For documentation of Earth Science, Paleobiology, Paleontology, Archeology, etc. datasets, we are interested in the second case -- the time period that data are linked to thematically. 

[Current guidance for temporal coverage](https://github.com/ESIPFed/science-on-schema.org/blob/master/guides/Dataset.md#temporal-coverage) accounts for [ISO8601 DateTime and DateTime ranges](https://en.wikipedia.org/wiki/ISO_8601), and this guidance is sufficient to account for temporal coverages that are in the range of the [Gregorian calendar](https://en.wikipedia.org/wiki/Gregorian_calendar). 

The schema:temporalCoverage properties includes schema:Text, schema:DateTime, and schema:URL. Specifying temporalCoverage as text would probably be useful for someone reading the metadata record, but as far as interoperability, it wouldn't be useful unless there were detailed conventions about the text that would be used (controlled vocabulary and syntax that could be validated). The same problem holds for specifying temporalCoverage with a URL. Aggregators would have to understand the semantics of the URL to integrate the information in a search interface. Also, there is no way to express a temporalCoverage with the beginning and end of a time interval unless it can be expressed as an ISO8601 DateTime range. 

### Solution
For temporal extents that can not be expressed using schema:DateTime, use W3C OWL time elements from the http://www.w3.org/2006/time# namespace. Science-on-Schema.org (SOSO) is already recommending use of elements from some other namespaces, and OWL time is widely recognized and vetted. A variaty of Temporal Reference Systems are availabe at the Queensland Department of Natural Resources, Mines and Energy: https://vocabs.gsq.digital/object?uri=http://linked.data.gov.au/def/trs and date/age uncertainies can be described using Named Individuals at geoschemas.org: https://geoschemas.org/extensions/temporal.html.  

For user-friendliness, include a text statement of the temporal coverage;

1. The dataset's temporalCoverage is described using ProperInterval, hasBeginning, and hasEnd elements from [OWL Time](http://www.w3.org/2006/time). The human readable description can be found in the description field: "Eruptive activity at Mt. St. Helens, Washington, March 1980 - January 1981".

  *Example*: 

```
{    "@context": {
        "@vocab": "http://schema.org/",
        "time": "http://www.w3.org/2006/time#"
    },
    "@type": "Dataset",
        "description": "Eruptive activity at Mt. St. Helens, Washington, March 1980 - January 1981",
        "temporalCoverage": [
            {
                "@type": "time:ProperInterval",
                "time:hasBeginning": {
                     "@type": "time:Instant",
                     "time:inXSDDateTimeStamp": "1980-03-27T19:36:00Z"
                 },
                 "time:hasEnd": {
                      "@type": "time:Instant",
                    "time:inXSDDateTimeStamp": "1981-01-03T00:00:00Z"
                 }
            }]
}
```

2. The dataset's temporalCoverage is described using Instant, inTimePosition, hasTRS, and numericPosition elements for a single geological date/age without uncertainties from [OWL Time](http://www.w3.org/2006/time).  Use a decimal value with appropriate timescale temporal reference system (TRS) and date/age unit abbreviation. Also provide a text form of the temporalCoverage (here "760 ka"). The human readable description can be found in the description field: "Eruption of Bishop Tuff, about 760,000 years ago".

   *Example*:

```
{    "@context": {
        "@vocab": "http://schema.org/",
        "gsqtime": "https://vocabs.gsq.digital/object?vocab_id=trs&https://vocabs.gsq.digital/object?uri=http://linked.data.gov.au/def/trsuri=http://linked.data.gov.au/def/trs/",
        "time": "http://www.w3.org/2006/time#",
        "xsd": "https://www.w3.org/TR/2004/REC-xmlschema-2-20041028/datatypes.html"
    },
    "@type": "Dataset",
    "description": "Eruption of Bishop Tuff, about 760,000 years ago",
    "temporalCoverage": [
        {
            "@type": "time:Instant",
            "time:inTimePosition": {
				"@type": "time:TimePosition",
                "time:hasTRS": {
                    "@id": "gsqtime:MillionsOfYearsAgo"
                },
                "time:numericPosition": {
                    "@type": "xsd:decimal",
                    "value": 0.76
                },
                "gstime:GeologicTimeUnitAbbreviation": {
                    "@type": "xsd:string",
                    "value": "Ma"
                }
            }
        }]    
}
```

3. The dataset's temporalCoverage is described using the Instant, inTimePosition, TimePosition, numericPosition from [OWL Time](http://www.w3.org/2006/time) with a geological date/age with uncertainties. Use a decimal value with appropriate timescale temporal reference system(TRS), date/age unit abbreviation, the uncertainty value and specify at what sigma. Also provide a text form of the temporalCoverage (here "4.404 +/-+/- 0.008 Ga"). "+/-+/-" indicates the uncertainty is given at 2-sigma. The human readable description can be found in the description field: "Very old zircons from the Jack Hills formation Australia 4.404 +- 0.008 Ga (2-sigma)".
 
   *Example*:

```
{    "@context": {
        "@vocab": "http://schema.org/",
        "gsqtime": "https://vocabs.gsq.digital/object?uri=http://linked.data.gov.au/def/trs",
        "gstime": "http://schema.geoschemas.org/contexts/temporal#",
        "time": "http://www.w3.org/2006/time#",
        "xsd": "https://www.w3.org/TR/200 (from [OWL Time](http://www.w3.org/2006/time))4/REC-xmlschema-2-20041028/datatypes.html"
    },  
    "@type": "Dataset",
    "description": "Very old zircons from the Jack Hills formation Australia 4.404 +- 0.008 Ga (2-sigma)",
    "temporalCoverage": [
        {
            "@type": "time:Instant",
            "time:inTimePosition": {
                "@type": "time:TimePosition",
                "time:hasTRS": {
                    "@id": "gsqtime:BillionsOfYearsAgo"
                },
                "time:numericPosition": {
                    "@type": "xsd:decimal",
                    "value": 4.404 
                },      
                "gstime:GeologicTimeUnitAbbreviation": {
                    "@type": "xsd:string",
                    "value": "Ma"
                },      
                "gstime:Uncertainty": {
                    "@type": "xsd:decimal",
                    "value": 0.008
                },
                "gstime:UncertaintySigma": {
                    "@type": "xsd:decimal",
                    "value": 2.0
                }       
            }       
        }]          
}
```
4. The dataset's temporalCoverage is described using the ProperInterval, hasBeginning, hasEnd, Instant, inTimePosition, TimePosition, and hasTRS elements from [OWL Time](http://www.w3.org/2006/time) with a geological date/age range with uncertainties. Use a decimal value with appropriate timescale temporal reference system(TRS), date/age unit abbreviation, uncertainty value and at what sigma. Also provide a text form of the temporalCoverage (here "17.1 +/- 0.15 to 15.7 +/- 0.14 Ma"). "+/-" indicates the uncertainty is given at 1-sigma. The human readable description can be found in the description field: "Isotopic ages determined at the bottom and top of a stratigraphic section in the Columbia River Basalts".

   *Example*:

```
{    
    "@context": {
        "@vocab": "http://schema.org/",
        "gsqtime": "https://vocabs.gsq.digital/object?uri=http://linked.data.gov.au/def/trs",
        "gstime": "http://schema.geoschemas.org/contexts/temporal#",
        "rdfs": "https://www.w3.org/2001/sw/RDFCore/Schema/200212/",
        "time": "http://www.w3.org/2006/time#",
        "xsd": "https://www.w3.org/TR/2004/REC-xmlschema-2-20041028/datatypes.html"
    },
    "@type": "Dataset",
    "description": "Isotopic ages determined at the bottom and top of a stratigraphic section in the Columbia River Basalts",
    "temporalCoverage": [
        {
            "@type": "time:ProperInterval",
            "time:hasBeginning": {
                "@type": "time:Instant",
                 "time:inTimePosition": {
                    "@type": "time:TimePosition",
                    "rdfs:comment": "beginning is older bound of age envelop",
                    "time:hasTRS": {
                        "@id": "gsqtime:MillionsOfYearsAgo"
                    },
                    "time:numericPosition": {
                        "@type": "xsd:decimal",
                        "value": 17.1
                    },
                    "gstime:GeologicTimeUnitAbbreviation": {
                        "@type": "xsd:string",
                        "value": "Ma"
                    }
                },
                "gstime:Uncertainty": {
                    "@type": "xsd:decimal",
                    "value": 0.15
                },
                "gstime:UncertaintySigma": {
                    "@type": "xsd:decimal",
                    "value": 1.0
                }
            },
            "time:hasEnd": {
                "@type": "time:Instant",
                "time:inTimePosition": {
                    "@type": "time:TimePosition",
                    "rdfs:comment": "ending is younger bound of age envelop",
                    "time:hasTRS": {
                        "@id": "gsqtime:MillionsOfYearsAgo"
                    },
                    "time:numericPosition": {
                        "@type": "xsd:decimal",
                        "value": 15.7
                    },
                    "gstime:GeologicTimeUnitAbbreviation": {
                        "@type": "xsd:string",
                        "value": "Ma"
                    }
                },
                "gstime:Uncertainty": {
                    "@type": "xsd:decimal",
                    "value": 0.14
                },
                "gstime:UncertaintySigma": {
                    "@type": "xsd:decimal",
                     "value": 2.0
                }
            }
        }]
}
```
5. The dataset's temporalCoverage is described using the Instant, inTimePosition, TimePosition, and hasTRS elements from [OWL Time](http://www.w3.org/2006/time) with a archeological date/age range with uncertainties. Use a decimal value with appropriate timescale temporal reference system(TRS), date/age unit abbreviation, the older and younger uncertainty values and at what sigma. Also provide a text form of the temporalCoverage (here "2640 +130 -80 BP-CAL (INTCAL20)"). The human readable description can be found in the description field: "Age of a piece of charcoal found in a burnt hut at an archeological site in Kenya carbon dated at BP Calibrated of 2640 +130 -80 (one-sigma) using the INTCAL20 carbon dating curve."

   *Example:*

```
{
    "@context": {
        "@vocab": "http://schema.org/",
        "gsqtime": "https://vocabs.gsq.digital/object?uri=http://linked.data.gov.au/def/trs",
        "gstime": "http://schema.geoschemas.org/contexts/temporal#",
        "time": "http://www.w3.org/2006/time#",
        "xsd": "https://www.w3.org/TR/2004/REC-xmlschema-2-20041028/datatypes.html"
    },
    "@type": "Dataset",
    "description": "Age of a piece of charcoal found in a burnt hut at an archeological site in Kenya carbon dated at BP Calibrated of 2640 +130 -80 (one-sigma) using the INTCAL20 carbon dating curve.",
    "temporalCoverage": [
        {
            "@type": "time:Instant",
            "time:inTimePosition": {
                 "@type": "time:TimePosition",
                 "time:hasTRS": {
                     "@id": "gsqtime:BeforePresentCalibrated"
                 },
                 "time:numericPosition": {
                     "@type": "xsd:decimal",
                     "value": 2460.0
                 },
                 "gstime:GeologicTimeUnitAbbreviation": {
                     "@type": "xsd:string",
                     "value": "BP-CAL"
                 },
                 "gstime:UncertaintyOlder": {
                     "@type": "xsd:decimal",
                     "value": 130.0
                 },
                 "gstime:UncertaintyYounger": {
                     "@type": "xsd:decimal",
                     "value": 80.0
                 },
                 "gstime:UncertaintySigma": {
                     "@type": "xsd:decimal",
                     "value": 1.0
                }
            }
        }]
}
```

6. The dataset's temporalCoverage is described using the Instant, TimePosition, inTimePosition, NominalPosition, Interval, hasBeginning, hasEnd, and hasTRS elements from [OWL Time](http://www.w3.org/2006/time). With temporal coverage that is a named time interval from a geologic time scale, provide numeric positions of the beginning and end for interoperability. Providing the numeric values is only critical, but still recommended, if the TRS for the nominalPosition is not the [International Chronostratigraphic Chart](https://stratigraphy.org/chart).

   *Example:*

```
{
    "@context": {
        "@vocab": "http://schema.org/",
        "gsqtime": "https://vocabs.gsq.digital/object?uri=http://linked.data.gov.au/def/trs",
        "gstime": "http://schema.geoschemas.org/contexts/temporal#",
        "icsc": "http://resource.geosciml.org/clashttps://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/resource?uri=http://resource.geosciml.org/classifier/ics/ischart/Boundariessifier/ics/ischart/",
        "time": "http://www.w3.org/2006/time#",
        "ts": "http://resource.geosciml.org/vocabulary/timescale/",
        "xsd": "https://www.w3.org/TR/2004/REC-xmlschema-2-20041028/datatypes.html"
    },
    "@type": "Dataset",
    "description": "Temporal position of the Bartonian expressed with a named time ordinal era from [International Chronostratigraphic Chart](https://stratigraphy.org/chart):",
    "temporalCoverage": [
        {
            "@type": "time:Instant",
            "time:inTimePosition": {
                "@type": "time:TimePosition",
                "time:hasTRS": {
                    "@id": "ts:gts2020"
                },
                "time:NominalPosition": {
                    "@type": "xsd:anyURI",
                    "value": "icsc:Bartonian"
                }
            }
        },
        {
            "@type": "time:ProperInterval",
            "time:hasBeginning": {
                "@type": "time:Instant",
                "time:inTimePosition": {
                    "@type": "time:TimePosition",
                    "time:hasTRS": {
                        "@id": "gsqtime:MillionsOfYearAgo"
                    },
                    "time:numericPosition": {
                        "@type": "xsd:decimal",
                        "value": 41.2
                    },
                    "gstime:GeologicTimeUnitAbbreviation": {
                        "@type": "xsd:string",
                        "value": "Ma"
                    }
                }
            },
            "time:hasEnd": {
                "@type": "time:Instant",
                "time:inTimePosition": {
                    "@type": "time:TimePosition",
                    "time:hasTRS": {
                        "@id": "gstime:MillionsOfYearAgo"
                    },
                    "time:numericPosition": {
                        "@type": "xsd:decimal",
                        "value": 37.71
                    },
                    "gstime:GeologicTimeUnitAbbreviation": {
                        "@type": "xsd:string",
                        "value": "Ma"
                    }
                }
            }
        }]
}
```

7. Temporal intervals with nominal temporal position that have identifiers. When possible, use temporal intervals defined by the [International Chronostratigraphic Chart](https://stratigraphy.org/chart), access via [ARDC vocabulary service](https://vocabs.ardc.edu.au/viewById/196), or via [GeoSciML vocabularies landing page](http://geosciml.org/resource/). If temporal intervals with identifies from other schemes are available, they can be included in a separate time:ProperInterval or time:Instant element.  If intervals are not from the ICS chart it is recommended to provide an interval with beginning and end numeric positions for better interoperability.

   *Example:*

```
{
    "@context": {
        "@vocab": "http://schema.org/",
        "icsc": "http://resource.geosciml.org/clashttps://vocabs.ardc.edu.au/repository/api/lda/csiro/international-chronostratigraphic-chart/geologic-time-scale-2020/resource?uri=http://resource.geosciml.org/classifier/ics/ischart/Boundariessifier/ics/ischart/",
        "time": "http://www.w3.org/2006/time#",
        "ts": "http://resource.geosciml.org/vocabulary/timescale/",
        "xsd": "https://www.w3.org/TR/2004/REC-xmlschema-2-20041028/datatypes.html"
	},
    "@type": "Dataset",
    "description": "Temporal position of Triassic to Jurassic expressed with an interval bounded by named time ordinal eras from [International Chronostratigraphic Chart](https://stratigraphy.org/chart). NumericPositions not included, expect clients can lookup bounds for ISC nominal positions:",
    "temporalCoverage": [{
        "@type": "time:ProperInterval",
        "time:hasBeginning": {
            "@type": "time:Instant",
            "time:inTimePosition": {
                "@type": "time:TimePosition",
                "time:hasTRS": {"@id": "ts:gts2020"},
                "time:NominalPosition": { "@value": "icsc:Triassic", "@type": "xsd:anyURI" }
            }
        },
        "time:hasEnd": {
            "@type": "time:Instant",
            "time:inTimePosition": {
                "@type": "time:TimePosition",
                "time:hasTRS": {"@id": "ts:gts2020"},
                "time:NominalPosition": { "@value": "icsc:Jurassic", "@type": "xsd:anyURI" }    
            }
        }
    }]
}
```

8. Temporal aggregates. Option 1. -- Make value of hasTime an array of TemporalEntities (use of hasTine us not recommended by the editors of the OWL Time draft document) or 2. use [TemporalAggregate](https://w3c.github.io/sdw/time-aggregates/) as value of hasTime. (TBD if there is interest - not done) 

### Discussion
Schema.org JSON objects are not intended to encode detailed data -- this is content that would be in the described dataset. In order to keep the basic discovery and evaluation, details about chronometric procedures and the processes for determining uncertainties for assigning temporal coverage can be included in the dataset description. The information will be useful for users evaluating the dataset based on the metadata, but is not necessary to support discovery.

### Deep background
Conceptually, the temporal coverage is a TemporalEntity as defined by OWL time ([Cox and Little, 2022, editors draft](https://w3c.github.io/sdw/time/)).  For the purposes of dataset documentation to support data discovery and evaluation for use, the TemporalEntities of interest are TimeInstants, and ProperIntervals. A TimeInstant has a single TemporalPosition, and a ProperInterval has Beginning and End properties that are each specified by a TemporalPosition. A TemporalPosition can be specified by a nominal value (e.g. a named interval), or a numeric value. 

Temporal coverage might be associated with a single event, or might be specified with named eras, either as a single era (e.g. 'Bartonian', 'Eoarchean'), or with bounding eras (e.g. Cambrian to Mississippian). Named eras might reference the [International Chronostratigraphic Chart](https://stratigraphy.org/chart), or some other time scale, e.g. local chronostratigraphic, biostratigraphic, or magnetostratigraphic reference system, or an astronomic cycle system. Finally temporal coverage might be specified with numeric temporal positions for the beginning and end of an interval. 

Individual events might be associated with calendar dates e.g. '1980 eruption of Mount St. Helens', '1906 San Francisco Earthquake'. Prehistoric events like 'Bonneville Flood', 'Brunhes–Matuyama reversal', or 'Intrusion of Tuolumne Intrusive Suite', will typically have some estimated numeric temporal position or interval. Likewise the temporal position of the beginning and end of a named era from a time scale will generally have some associated estimate of the numeric temporal position.

Numeric temporal positions (a.k.a. 'dates' or 'ages') are based on some chronometric procedure and temporal coordinate reference system. Comparing such dates in detail might require deep understanding of the basis for the value -- the measurement method, constants used (e.g. isotopic decay constants), calibrations applied (e.g. for C-14 data). The temporal coordinate reference system must be known to specify the temporal orgin (commonly taken as 1950 on the Gregorian calendar) and the units of measure, typically years before present (BP, gstime:BP, qudt:YR), thousand years (ka, gstime:ka), million years (Ma, gstime:Ma, qudt:MegaYR) or billion years (Ga, gstime:Ga).

### Related work:
- Earthcube P419 developed a [recommendation for describing Dataset temporal coverage based on OWL-Time]( https://geoschemas.org/extensions/temporal.html).
- Research Data Australia Registry Interchange Format: Collections and Services (RIF-CS) schema: [Temporal Coverage]( https://documentation.ardc.edu.au/display/DOC/Temporal+coverage)
- EML [temporal coverage](https://eml.ecoinformatics.org/schema/eml-coverage_xsd.html#SingleDateTimeType_alternativeTimeScale ) See also [5.3.3 'The eml-coverage module - Geographic, temporal, and taxonomic extents of resources']( https://eml.ecoinformatics.org/eml-schema.html#discovery-and-interpretation-modules)
- ESIP documentation cluster [extent documentation](https://wiki.esipfed.org/Extent_Documentation). Discusses documentaion for spatial and temporal extents in CSDGM, ISO19115, DIF, ECHO. Focus is mostly on DateTime extents, but DIF includes a Paleo_Temporal_Coverage to account for named intervals with identifiers.
- [USGIN ISO19115 profile](http://hdl.handle.net/10150/630040) [temporal extent recommendation](http://usgin.github.io/usginspecs/USGIN_ISO_Metadata.htm#_Toc381426792)
- GeoSciML [GeologicAge](http://docs.opengeospatial.org/is/16-008/16-008.html#183) In GeoSciML, ages are attached to events, but the pattern using 3 parts (NumericAgeRange, olderNamedAge, youngerNamedAge) could equally apply to documenting dataset temporal coverage.

## Consequences ##
Aggregators can parse SOSO profile schema.org JSON to extract temporal coverage information that can be used to construct search interfaces to find data thematically related to time intervals that do not have calendar dates.
