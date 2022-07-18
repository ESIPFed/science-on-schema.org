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
  ...
  -  
    name: "cast"
    description: "CTD cast number"
  ...
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
  ...
```
