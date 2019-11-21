# Conventions #

This document explains the conventions used within this guide.

* [Syntax](#syntax)
    * [General Rules](#syntax)
    * [JSON-LD Snippets](#syntax-snippets)
    * [Creating Diagrams](#syntax-diagrams)
    * [Creating Figures](#syntax-figures)
* [Versioning](#versioning)
* [Why JSON-LD](#why-jsonld)
* [Typing to External Vocabularies](#external-vocab-typing)

<a id="syntax"></a>
## Syntax ##

1. Use **[JSON-LD](https://json-ld.org/)** in our guidance documents for simplicity and terseness as compared to *[Microdata](https://www.w3.org/TR/microdata/)* and *[RDFa](https://rdfa.info/)*.
2. Documents should start with:
  1. An named anchor of 'top': ```<a id="top"></a>```
  2. A breadcrumb trail respective to the level in the guide:  
  
     <pre>[Home](/README.md) | [Some directory](/guides/<dir-name>) | This Location in the guide</pre>

2. Documents should describe *how* and *why* for each class and property being recommended.
<a id="syntax-snippets"></a>
3. **JSON-LD snippets** should be wrapped within a preformatted text block using **&lt;pre&gt;&lt;/pre&gt;** tags. To highlight a section of JSON-LD, use **&lt;strong&gt;&lt;/strong&gt;** tags.

<pre>
{
  "property": "value",
  <strong>"highlighted-property": "highlighted-value",</strong>
}
</pre>

<a id="syntax-diagrams"></a>
4. **Creating Diagrams**

  1. When recommending which properties of a schema.org class to use, creating a diagram of the connections between those resources and literal values can be helpful for visualizing the big picture.
  2. Diagrams should follow the following convention:
  [![Graphical Notation](/assets/diagrams/graphical-notation.svg "Graphical Notation")](#)
  3. Diagrams are currently being made using [Lucidchart](https://www.lucidchart.com), and are being shared to edit here: [schema.org diagrams on Lucidchart](https://www.lucidchart.com/documents#docs?folder_id=170151578&browser=icon&sort=saved-desc)

<a id="syntax-figures"></a>
5. **Creating Figures**

  1. Save the image to the ```/assets``` directory within this guide,
  2. Then, in the document, decide where the figure should be added,
  3. Add a named anchor before the figure, ```<a id="figure-(x)"></a>```, where ```(x)``` is a unique, incremental number.
  4. Center the figure by wrapping it and it's text with: ```<p align="center">...</p>```
  5. The first element in the section should be the figure title: ```Figure (x). The figure title goes here...```
  6. Next, insert the image with: ```<img src="/assets/<path-to-image-file e.g. schemaorg-datatypes.png>">```
  7. Optionally, add an italicized description with: ```<em>optional description goes here...</em>```

Figure example: 
```
  <a id="figure-1"></a>
  <p align="center">
    <strong>Figure 1. schema.org field data types</strong><br/>
    <img src="/assets/schemaorg-datatypes.png">
    <em>The expected data type for each field appears in the middle column. The left column is the name of the field, the middle column is the data type, and the right column is the field's description.</em>
  </p>
```

6. **Namespace for `schema.org`.** Use "`https://schema.org/`". 

  Consistent representation of namespaces simplifies programmatic processing of markup. For example, even though conceptually it is clear the terms "`http://schema.org/Dataset`" and "`https://schema.org/Dataset`" are referring to [https://schema.org/Dataset/](https://schema.org/Dataset), these are programmatically treated as different entities. The [schema.org guidelines](https://schema.org/docs/faq.html#19) are somewhat ambivalent on the topic, with perhaps emphasis on "`https`". 

  The trailing slash (`/`) is also important. Without it, common RDF processing libraries such as [rdflib](https://rdflib.readthedocs.io/en/stable/) will construct a term like "`https://schema.orgDataset`". For example:

  ``` python
  >>> from rdflib import ConjunctiveGraph
  >>> json = """{
  ...    "@context": {"@vocab": "https://schema.org"},
  ...    "@id":"demo",
  ...    "@type":"Dataset"
  ... } """
  >>> g = ConjunctiveGraph().parse(data=json, format="json-ld", publicID="https://my.data/")
  >>> for s,p,o in g:
  ...     print(f"{str(s)}, {str(p)}, {str(o)}")
  ...
  https://my.data/demo, http://www.w3.org/1999/02/22-rdf-syntax-ns#type, https://schema.orgDataset/
  ```
  Including the trailing slash will make the literal representation of terms align with the Internet location of the term definition, and so be clearer for readers and other processors.

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
 
