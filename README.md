<a id="top"></a>
![version 0.1.0](https://img.shields.io/badge/version-0.1.0-blue.svg)

*This guide is a continuation of the [P418 NSF EarthCube](https://github.com/earthcubearchitecture-project418/p418Vocabulary) vocabulary guidance which ended in April 2018.*

* [Goal](#goals)
* [Approach](#approach)
* [Guidance Documents](#guides)

# Goals #

To provide a place for the scientific data community to work out how best to implement **schema.org** and other external vocabularies on web pages by publishing guidance documents. *[Pull requests](/pulls)* and *[Github Issues](/issues)* are welcome!

<a id="approach"></a>
## Approach ##

1. To be **pragmatic** instead of dogmatic.
2. To **consider schema.org classes and properties first** before considering external vocabularies.
3. Use **[JSON-LD](https://json-ld.org/)** in our guidance documents for simplicity and terseness as compared to *[Microdata](https://www.w3.org/TR/microdata/)* and *[RDFa](https://rdfa.info/)*. For more, see [Why JSON-LD?](/CONVENTIONS.md#why-jsonld) from the [Conventions](/CONVENTIONS.md) document.
4. Presently, the [Google Structured Data Testing Tool](https://search.google.com/structured-data/testing-tool/u/0/) enforces use of [schema.org](http://schema.org) classes and properties by displaying an error whenever external vocabularies are used. schema.org proposes linking to external vocabularies usuing the [schema:additionalType](http://schema.org/additionalType) property. While this property is defined as a sub property of [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type), it's data type is a literal. We encourage the use of JSON-LD ```'@type'``` for typing classes to external vocabularies. For more, see [Typing to External Vocabularies]((/CONVENTIONS.md#external-vocab-typing) from the [Conventions](/CONVENTIONS.md) document.
5. See [Governance](/GOVERNANCE.md) for how we will govern the project.
6. See [Conventions](/CONVENTIONS.md) for guidance on creating/editing guidance documents.

<a id="guides"></a>
## Guidance Documents - Table of Contents ##
* [Dataset](/guides/Dataset.md)
