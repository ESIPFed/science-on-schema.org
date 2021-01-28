# Title - Clarify Spatial Extent encoding.

GeoShape box format unclear #

Discussion: https://github.com/ESIPFed/science-on-schema.org/issues/101
https://github.com/ESIPFed/science-on-schema.org/pull/104

## Status ##
 Proposed
 
## Decision ##
per PR #104:
In full.jsonld Example:
 - Fix Duplicate person problem in the JSON. 
 - update the  spatialCoverage content

in guides/Dataset.md
 - edits in the Spatial section, introduction, point location discussion, 
 - edits in geoshape location section, add additional discussion of problems and approaches: bounding box coordinate specification (coordinate order), how to deal with extents that include the poles, 

## Context ##
Questions about coordinate ordering and syntax for describing bounding boxes, and how to describe spatiale extents. Try to clarify behavior of Google Dataset search with spatial extent. 

## Consequences ##
Metadata harvesters should be able to systematically index geolocation specified in schema:spatialCoverage.
