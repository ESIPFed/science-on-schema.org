# Conventions #

* [Syntax](#syntax)
* [Versioning](#versioning)
* [Why JSON-LD](#why-jsonld)
* [Typing to External Vocabularies](#external-vocab-typing)

<a id="syntax"></a>
## Syntax ##

1. Use **[JSON-LD](https://json-ld.org/)** in our guidance documents for simplicity and terseness as compared to *[Microdata](https://www.w3.org/TR/microdata/)* and *[RDFa](https://rdfa.info/)*.
2. Documents should describe *how* and *why* for each class and property being recommended.
3. JSON-LD snippets should be wrapped within a preformatted text block using **&lt;pre&gt;&lt;/pre&gt;** tags. To highlight a section of JSON-LD, use **&lt;strong&gt;&lt;/strong&gt;** tags.

<pre>
{
  "property": "value",
  <strong>"highlighted-property": "highlighted-value",</strong>
}
</pre>

<a id="versioning"></a>
## Versioning ##

1.  will follow the [semantic versioning](https://semver.org/) pattern:

Given a version number MAJOR.MINOR.PATCH, increment the:

  * MAJOR version when you make incompatible changes to a recommendation,
  * MINOR version when you add functionality in a backwards-compatible manner, and
  * PATCH version when you make backwards-compatible bug fixes.

<a id="why-jsonld"></a>
## Why JSON-LD? ##

Schema.org allows can be described using Microdata, RDFa, and JSON-LD. In this guide, we will use JSON-LD because:

1. **Simplicity** - JSON-LD is the *most succinct* of the formats for communicating our *intent* with the recommendations.
2. **Tersenees** - the JSON-LD ```[@context](https://json-ld.org/spec/latest/json-ld/#the-context)``` property allows publishers to express the data type of a specific properties of the data graph. 

*NOTE: Our intent is not to override [http://schema.org/](http://schema.org/) classes and properties, but to provide flexibility to our examples and recommendations when using external vocabularies.*


<a id="external-vocab-typing"></a>
## Typing to External Vocabularies ##

Schema.org provides a property called [schema:additionalType](http://schema.org/additionalType) for typing resources in a data graph to external vocabularies. Here is the RDF that defines this property:

```
<rdf:RDF
  xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
  xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
  xmlns:schema="http://schema.org/"
>
    <rdf:Property rdf:about="http://schema.org/additionalType">
        <schema:rangeIncludes rdf:resource="http://schema.org/URL"/>
        <rdfs:comment>An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. In RDFa syntax, it is better to use the native RDFa syntax - the 'typeof' attribute - for multiple types. Schema.org tools may have only weaker understanding of extra types, in particular those defined externally.</rdfs:comment>
        <schema:sameAs rdf:resource="https://schema.org/additionalType"/>
        <rdfs:subPropertyOf rdf:resource="http://www.w3.org/1999/02/22-rdf-syntax-ns#type"/>
        <rdfs:label>additionalType</rdfs:label>
        <schema:domainIncludes rdf:resource="http://schema.org/Thing"/>
    </rdf:Property>
</rdf:RDF>
```

### rdfs:subPropertyOf rdf:type with range of schema:URL ###

```
...
<schema:rangeIncludes rdf:resource="http://schema.org/URL"/>
<rdfs:subPropertyOf rdf:resource="http://www.w3.org/1999/02/22-rdf-syntax-ns#type"/>
...
```

Publishers who have a ```@context``` with prefixes for external vocabularies cannot use the prefixed URL in schema:additionalType

...add JSON-LD Playground example showing that additionalType does not expand the prefix nor generate an rdf:type triple...
 
