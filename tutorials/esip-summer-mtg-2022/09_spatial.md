# 9. Spatial Coverage

#### Lesson
> - Multi-level object properties
> - Introducing the `PropertyValue` type

**Guidelines:** 
[Spatial Coverage](/guides/Dataset.md#spatial-coverage)

**Source:**
[Lines L54-L63](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt#L54-L63)

```
spatial:
  location: "Central Pacific Ocean (Hawaii to Tahiti)"
  boundingBox:
    west: 139.8
    south: -10.563
    east: 156
    north: 17
  centroid: 
    lat: 3.2185
    lon: 147.9
```

### Schema.org Spatial

- https://schema.org/spatialCoverage
    - `Place` >> `GeoShape`
        - <strong>`box`</strong> - A rectangular (in lat-long space) extent specified by two points, the first in the lower left (southwest) corner and the second in the upper right (northeast) corner.
        - `circle`
        - `elevation`
        - `line`
        - <strong>`polygon`</strong> - A series of four or more points where the first and final points are identical.
    - `Place` >> `GeoCoordinates`
        - `latitude`
        - `longitude`
        - `elevation`
 
### Spatial Coverage - GeoCoordinates

<pre>
{
  "@context": "https://schema.org/",
  <strong>"spatialCoverage": {
    "@type": "Place",
    "geo": {
      "@type": "GeoCoordinates",
      "latitude": 3.2185,
      "longitude": 147.9
    }</strong>
}
</pre>

### Spatial Coverage - GeoShape >> Box

<pre>
{
  "@context": "https://schema.org/",
  <strong>"spatialCoverage": {
    "@type": "Place",
    "geo": {
      "@type": "GeoShape",
      "box": "-10.563 139.8 17 156",
    }</strong>
}
</pre>

### Spatial Coverage - GeoShape >> Polygon

<pre>
{
  "@context": "https://schema.org/",
  <strong>"spatialCoverage": {
    "@type": "Place",
    "geo": {
      "@type": "GeoShape",
      "polygon": "-10.563,139.8 17,139.8 17,156 -10.563,156 -10.563,139.8"
    }</strong>
}
</pre>

### Adding a Spatial Reference System

We aren't on the moon, and harvesters don't know that

<pre>
{
  "@context": "https://schema.org/",
  "spatialCoverage": {
    "@type": "Place",
    "geo": {
      "@type": "GeoShape",
      "polygon": "-10.563,139.8 17,139.8 17,156 -10.563,156 -10.563,139.8"
    },
    <strong>"additionalProperty": {
      "@type": "PropertyValue",
      "propertyID":"http://dbpedia.org/resource/Spatial_reference_system",
      "value": "http://www.w3.org/2003/01/geo/wgs84_pos#lat_long"
    }</strong>
  }
</pre>


### Updated Markup - Spatial Coverage

<pre>
{
  "@context": "https://schema.org/",
  "@type": "Dataset",
  "name": "Nitrous oxide concentrations from the R/V Falkor expedition FK160115 in the Central Pacific from January to February 2016",
  "description": "Dissolved N2O concentrations from were measured in discrete samples on a research expedition to the Equatorial Pacific. Water samples were collected using a 24 bottle Niskin rosette equipped with a CTD. N₂O concentrations were measured using a headspace equilibration method and analyzed on a SRI Greenhouse Gas Monitoring Gas Chromatograph.",
  "url": "https://www.bco-dmo.org/dataset/775849",
  "version": "1",
  "isAccessibleForFree": "true",
  "dateCreated": "2019-08-22",
  "dateModified": "2019-08-22",
  "datePublished": "2022-06-08",
  "keywords": [
    "nitrous oxide", 
    "Central Pacific", 
    "headspace equilibration", 
    "SRI Greenhouse Gas Monitoring Gas Chromatograph",
    "CTD profiler",
    "Gas Chromatograph"
  ],
  "license": ["https://spdx.org/licenses/CC-BY-4.0", "https://creativecommons.org/licenses/by/4.0/"],
  "identifier": "https://doi.org/10.26008/1912/bco-dmo.775849.1",
  "sameAs": "https://doi.org/10.26008/1912/bco-dmo.775849.1",
  "publisher": {
    "@type": "Organization",
    "legalName": "Biological and Chemical Data Management Office",
    "url": "https://www.bco-dmo.org"
  },
  "creator": {
    "@list":[
      {
        "@type": "Person",
        "name": "Alyson E. Santoro"
      },
      {
        "@type": "Person",
        "name": "Sarah Marie Laperriere"
      }
    ]
  },
  "contributor": {
    "@list":[
      {
        "@type": "Person",
        "name": "Makoto Saito"
      }
    ]
  },
  "temporalCoverage": "2016-01-17/2016-02-04",
  <strong>"spatialCoverage": {
    "@type": "Place",
    "geo": {
      "@type": "GeoShape",
      "polygon": "-10.563,139.8 17,139.8 17,156 -10.563,156 -10.563,139.8"
    },
    "additionalProperty": {
      "@type": "PropertyValue",
      "propertyID":"http://dbpedia.org/resource/Spatial_reference_system",
      "value": "http://www.w3.org/2003/01/geo/wgs84_pos#lat_long"
    }
  }</strong>
}
</pre>

<hr/>

[Section #10: Data Files >>](10_data-files.md)

<hr/>

### Resources
- **Source:** [ProteOMZ nitrous oxide data](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt) (example metadata)
- **Testing:** [Google Rich Results Tool](https://search.google.com/test/rich-results)
