# Shape Graphs

## About

Some details on the shape graphs in this directory

Filename | Description
------------ | -------------
googleRequired.ttl | Checks for the Google required items described in https://developers.google.com/search/docs/data-types/dataset
googleRecommended.ttl | Checks for the Google recommended items described in https://developers.google.com/search/docs/data-types/dataset
googleRecommendedCoverageCheck.ttl | Same as the test for Google recommended but sets all items to min 1 to check for coverage.  Use the one above if you don't care about coverage of recommended items
P418Required.ttl | Same as googleRequired but adds in a check for an @id for Dataset type. Otherwise, checks for the Google recommended items described in https://developers.google.com/search/docs/data-types/dataset
importTest.ttl | TESTING: A testing file for checking if shape imports works to allow people to stack together a set of shape graphs to check with
temporalRange.ttl | TESTING: A file to explore validate temporal items in a data graph 
../testingDataGraphs | A directory with various data graphs (some with errors) to use as part of testing shape graphs and perhaps a CI path in the future
soso_common_v1.1.0.ttl | SHACL for evaluating compliance with Science-on-Schema.org tagged release version 1.1 

## Evaluating Data Compliance with Guidelines

Compliance of a `https://schema.org/Dataset` with the Science-on-Schema.org (SOSO) guidelines and recommendations release 
[version 1.1](https://github.com/ESIPFed/science-on-schema.org/blob/1.1.0/guides/Dataset.md) 
can be evaluated by applying the SHACL shape to the Dataset graph using a SHACL processor.

For example, using [PySHACL](https://github.com/RDFLib/pySHACL):

```shell script
$ DG="../testingDataGraphs/dataset-full.json-ld"
$ SG="soso_common_v1.1.0.ttl"
$ pyshacl -s ${SG} -sf turtle -df json-ld ${DG}
```

Currently generates the following output which indicates that the recommended
`SO:isAccessibleForFree` and `SO:sameAs` are missing from the example:

```
Validation Report
Conforms: False
Results (2):
Constraint Report in MinCountConstraintComponent (http://www.w3.org/ns/shacl#MinCountConstraintComponent):
	Severity: sh:Warning
	Source Shape: soso:isAccessibleForFreeDatasetProperty
	Focus Node: <https://www.bco-dmo.org/dataset/472032>
	Result Path: SO:isAccessibleForFree
	Message: It is recommended that a Dataset indicates accessibility for free or otherwise
Constraint Report in MinCountConstraintComponent (http://www.w3.org/ns/shacl#MinCountConstraintComponent):
	Severity: sh:Warning
	Source Shape: soso:sameAsDatasetProperty
	Focus Node: <https://www.bco-dmo.org/dataset/472032>
	Result Path: SO:sameAs
	Message: It is recommended that a Dataset includes a sameAs URL
```

