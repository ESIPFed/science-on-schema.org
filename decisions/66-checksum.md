# Represent checksum values as instances of `identifier`

Discussion: https://github.com/ESIPFed/science-on-schema.org/issues/66

## Status ##

__Approved__

## Decision ##

Provide checksum values for individual digital objects within a Dataset by using `spdx:checksum`, with a `checksumValue` property that contains the unqualified hash value, and a `checksumAlgorithm` property that refers to the identifier of an SPDX named individual identifying the algorithms class.

## Context ##
Because schema.org does not contain a class for representing checksum values, by convention we recommend using the [`spdx:checksum`](http://spdx.org/rdf/terms#checksum) property, which points at an `spdx:Checksum` instance that provides both the value of the checksum and the algorithm that was used to calculate the checksum.

## Consequences ##

- Because we are using the SPDX vocabulary, it's prefix must be defined in the `@context`
- Because we are using an external vocabulary, some schema.org validators may show errors, but they won't stop processing by Google and related indexers
- This use of `spdx:checksum` is meant to solely provide the checksum for its merits, and not as an identifier. If users also want the checksum to be used as an alternate identifier, they should provide a proper serialization of the value as an identifier string. For example, some providers may want to list the Hash URI serialized format of the identifier in the identifier array as well. For example: `"identifier": "hash://sha256/39ae639d33cea4a287198bbcdca5e6856e6607a7c91dc4c54348031be2ad4c51"`
- Because the example does not include an `@id` for the Checksum object, a blank node will be generated. It can be avoided by providing an `@id` for the checksum, such as `"@id": "hash://sha256/39ae639d33cea4a287198bbcdca5e6856e6607a7c91dc4c54348031be2ad4c51"`, but note that means the hash would represent the linked data identifier of the `Checksum`, rather than of the `DataDownload` object.


