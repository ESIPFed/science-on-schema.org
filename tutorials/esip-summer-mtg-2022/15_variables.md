# 15. Variables

**Guidelines:** 
[Variables](/guides/Dataset.md#variables)

**Source:**
[Line 92-154](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt#L92-154)

```
parameters:
  - 
    name: "ISO_DateTime_UTC"
    description: "Date time time of cast following ISO 8601 convention in UTC"
    format: "YYYY-MM-DDTHH:MM:SS[.xx]Z"
    identifier:
      uri: "http://vocab.nerc.ac.uk/collection/P01/current/DTUT8601/"
  -  
    name: "station"
    description: "Station number"
  -  
    name: "cast"
    description: "CTD cast number"
  -  
    name: "latitude"
    description: "latitude of station; North is positive; negative denotes South"
    identifier:
      name: "latitude"
      uri: "http://vocab.nerc.ac.uk/collection/P09/current/LATX/"
    units:
      name: "decimal degrees"
  - 
    name: "longitude"
    description: "longitude station East is positive; negative denotes West"
    identifier:
      name: "longitude"
      uri: "http://vocab.nerc.ac.uk/collection/P09/current/LONX/"
    units:
      name: "decimal degrees"
  -  
    name: "depth"
    description: "depth of sampling"
    identifier:
      name: "depth"
      uri: "http://vocab.nerc.ac.uk/collection/P01/current/ADEPZZ01/"
    units:
      name: "meters (m)"
  -  
    name: "salinity"
    description: "Salinity from CTD"
    identifier:
      name: "salinity"
      uri: "https://vocab.nerc.ac.uk/collection/P25/current/SALIN/"
    units:
      name: "practical salinity units (PSU)"
  - 
    name: "temperature"
    description: "Temperature from CTD"
    identifier:
      name: "water temperature"
      uri: "http://vocab.nerc.ac.uk/collection/P01/current/TEMPP901/"
    units:
      name: "Celsius (C)"
  - 
    name: "n2o_1"
    description: "Nitrous oxide concentration replicate 1"
    units:
      name: "nanomoles per liter (nmol/L)"
  - 
    name: "n2o_2"
    description: "Nitrous oxide concentration replicate 2"
    units:
      name: "nanomoles per liter (nmol/L)"
```
