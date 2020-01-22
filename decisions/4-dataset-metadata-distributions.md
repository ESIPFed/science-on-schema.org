# Specific Recommendations for Metadata Distribution Information

Discussion: https://github.com/ESIPFed/science-on-schema.org/issues/4

## Status ##
_Proposed_

## Decision ##

1. Link metadata documents to a dataset by using `schema:subjectOf`. Or if a schema.org snippet describes the metadata, link to the Dataset it describes using `schema:about`.
2. Describe the encoding format(s) of the metadata file by using the `schema:encodingFormat` with multiple values to specify more detail about any profiles the media type conforms to.

### 1. Linking Metadata docs to Datasets: Use `schema:subjectOf` or `schema:about` ###
	
  ```<Dataset> schema:subjectOf <Metadata>```
  
  or inversely
  
  ```<Metadata> schema:about <Dataset>```
  
  <pre>
  {
    "@context": "https://schema.org/",
    "@type": "Dataset",
    "name": "Example Dataset",
    "distribution": {
      "@type": "DataDownload",
      ...
    },
    <strong>"subjectOf": {
      "@type": "DataDownload",
      "name": "EML file that describes the Example Dataset",
      "description": "We use the DataDownload class for Metadata files so that we can use the schema:MediaObject properties for describing bytesize, encoding, etc.",
      ...
    }</strong>
  }
  </pre>
  
  inversely
  
  <pre>
  {
    "@context": "https://schema.org/",
    "@type": "DataDownload",
    "name": "EML file that describes the Example Dataset",
    "description": "We use the DataDownload class for Metadata files so that we can use the schema:MediaObject properties for describing bytesize, encoding, etc.",
    ...
    <strong>"about": {
      "@type": "Dataset",
      "name": "Example Dataset",
      "distribution": {
        "@type": "DataDownload",
        ...
      },
    }</strong>
  }
  </pre>
  
### 2. Describing the encoding format of the metadata file ###

Some metadata files have an encodingFormat of 'application/xml' but follow a certain profile such as 'ISO 19115-2' or 'EML 2.2.' 

Since `schema:encodingFormat` allows for Text and URL values, we can specify both the MIME type and the profile inside an array:

 <pre>
  {
    "@context": "https://schema.org/".
    "@type": "Dataset",
    "name": "Example Dataset",
    "distribution": {
      "@type": "DataDownload",
      ...
    },
    "subjectOf": {
      "@type": "DataDownload",
      "name": "EML file that describes the Example Dataset",
      <strong>"encodingFormat": ["application/xml", "https://eml.ecoinformatics.org/eml-2.2.0"],</strong>
      "description": "We use the DataDownload class for Metadata files so that we can use the schema:MediaObject properties for describing bytesize, encoding, etc.",
      ...
    }
  </pre>
  
However, experience has shown that in order to use the values within strings like encodingFormat, a controlled vocabulary is required.  

## Context ##

It isn't obvious how to build a package of related files for a Dataset. To include metadata files in the schema.org description of a Dataset, reusing the `schema:distribution` property doesn't seem correct as it should serialize the actual data. As a result this issue only addresses how to use core schema.org properties to create a link between Metadata files and Datasets.

- https://github.com/ESIPFed/science-on-schema.org/issues/4
- Decision discussed at ESIP Winter Meeting. Notes here: https://docs.google.com/document/d/1ycG9Dlt6xRr9wxjqkQrPkJQJvm83E34eue_cxkrSGUI/edit?ts=5e1503e3#
- https://schema.org/subjectOf and https://schema.org/about
- https://schema.org/encodingFormat

## Consequences ##

1. `schema:subjectOf` and `schema:about` are very broad and may be alongside other resources that aren't necessarily metadata-dataset relationships. We need a SHACL shape to help define what conformance to the pattern looks like.  Best practices in implementing this guidance is also needed.
