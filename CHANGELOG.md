# CHANGELOG

## 1.3.0

----------
**FIXES**

- Namespace Consistency ([decision](https://github.com/ESIPFed/science-on-schema.org/blob/1.3.0/decisions/52-namespace-consistency.md), [Issue #52](https://github.com/ESIPFed/science-on-schema.org/issues/52))
- Moved experimental recommendations to a [separate document](https://github.com/ESIPFed/science-on-schema.org/blob/1.3.0/guides/Experimental.md)

**IMPROVEMENTS**

- Describing dataset funding ([decision](https://github.com/ESIPFed/science-on-schema.org/blob/1.3.0/decisions/109-funding.md), [Issue #109](https://github.com/ESIPFed/science-on-schema.org/issues/109))
- Describing dataset variables ([decision](https://github.com/ESIPFed/science-on-schema.org/blob/1.3.0/decisions/27-measuredVariable.md), [Issue #27](https://github.com/ESIPFed/science-on-schema.org/issues/27))
- Improving temporal coverage of a dataset ([decision](https://github.com/ESIPFed/science-on-schema.org/blob/1.3.0/decisions/77-temporalCoverageGuidance.md), [Issue #77](https://github.com/ESIPFed/science-on-schema.org/issues/77))
- Preserving item order ([Issue #135](https://github.com/ESIPFed/science-on-schema.org/issues/135))
- Describe need for a sitemap ([Issue #192](https://github.com/ESIPFed/science-on-schema.org/issues/192))
- New JSON-LD [examples](https://github.com/ESIPFed/science-on-schema.org/blob/1.3.0/examples/)
- Updated SHACL validation [shape](https://github.com/ESIPFed/science-on-schema.org/blob/1.3.0/validation/shapegraphs/soso_common_v1.2.3.ttl)

**NEW FEATURES**

- Representing checksums as identifiers([decision](http://github.com/ESIPFed/science-on-schema.org/blob/1.3.0/decisions/66-checksum.md), [Issue #66](https://github.com/ESIPFed/science-on-schema.org/issues/66))

## 1.2.0

**FIXES**

* Fix various errors in <a href="http://github.com/ESIPFed/science-on-schema.org/blob/1.2.0/examples/dataset/full.jsonld" target="_blank">Dataset full example</a> JSON-LD (<a href="https://github.com/ESIPFed/science-on-schema.org/issues/115" target="_blank">Issue #115</a>)
    * the `identifier` should be of type `PropertyValue`
    * the `sameAs` property is missing
    * the `isAccessibleForFree` property is missing

**IMPROVEMENTS**

* Improvements for describing geospatial coverage (<a href="http://github.com/ESIPFed/science-on-schema.org/blob/1.2.0/decisions/101-spatialExtent.md" target="_blank">decision</a>, <a href="https://github.com/ESIPFed/science-on-schema.org/issues/101" target="_blank">Issue #101</a>)
* Dataset Provenance for processing workflows, data derivation, and dataset versioning (<a href="http://github.com/ESIPFed/science-on-schema.org/blob/1.2.0/decisions/72-provenance.md" target="_blank">decision</a>, <a href="https://github.com/ESIPFed/science-on-schema.org/issues/72" target="_blank">Issue #72</a>)
    * <a href="https://github.com/ESIPFed/science-on-schema.org/blob/1.2.0/guides/Dataset.md##provenance-relationships" target="_blank">Guide: Dataset - Provenance Relationships</a>
* Use `schema:dateModified`for announcing when a Dataset resource has changed (<a href="https://github.com/ESIPFed/science-on-schema.org/issues/67" target="_blank">Issue #67</a>)
    * <a href="https://github.com/ESIPFed/science-on-schema.org/blob/1.2.0/guides/Dataset.md#howmodification_times">Guide: Dataset - Time of resource modification</a>
* How to reference a short DOI (<a href="https://github.com/ESIPFed/science-on-schema.org/issues/120" target="_blank">Issue #120</a>)
    * <a href="https://github.com/ESIPFed/science-on-schema.org/blob/1.2.0/guides/Dataset.md#how-to-reference-short-dois" target="_blank">Guide: Dataset - How to reference Short DOI</a>
* Update GOVERNANCE &amp; README to list ESIP Schema.org Cluster meeting times (<a href="https://github.com/ESIPFed/science-on-schema.org/issues/111" target="_blank">Issue #111</a>)

**NEW FEATURES**

* Add SHACL shape to validate schema.org namespace (<a href="http://github.com/ESIPFed/science-on-schema.org/blob/1.2.0/decisions/52-namespace-consistency.md" target="_blank">decision</a>, <a href="https://github.com/ESIPFed/science-on-schema.org/issues/59" target="_blank">Issue #59</a>)

## 0.2.0

- changed the DataRepository class `[schema:Organization](https://schema.org/Organization)` to the more specific `[schema:ResearchProject](https://schema.org/ResearchProject)`
- added how to use [schema:MonetaryGrant](https://schema.org/MonetaryGrant) for describing Dataset funding grants.

## 0.1.0

- initial import from github.com/earthcubearchitecture-project418/p418Vocabulary
- removed the 'gdx' vocabulary since it was specific to EarthCube and Re3data schema
- added /decisions directory for storing Architecture Decision Records.
