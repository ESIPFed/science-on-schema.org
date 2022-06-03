# Conventions #

This document explains the conventions used within this guide.

* [Syntax](#syntax)
    * [General Rules](#syntax)
    * [JSON-LD Snippets](#syntax-snippets)
    * [Creating Diagrams](#syntax-diagrams)
    * [Creating Figures](#syntax-figures)
    * [Schema.org Namespace](#syntax-namespace)
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

<a id="syntax-namespace"></a>
6. **Namespace for `schema.org`.** 

We recommend that the namespace URI for the schema.org vocabulary be consistently set to the value `http://schema.org/`.

 Consistent representation of namespaces simplifies programmatic processing of schema.org markup. For example, even though conceptually it is clear that the terms `http://schema.org/Dataset` and `https://schema.org/Dataset` (note the protocol difference) are referring to [http://schema.org/Dataset](https://schema.org/Dataset), these are programmatically treated as different entities. The [schema.org guidelines](https://schema.org/docs/faq.html#19) are somewhat ambivalent on the topic. Their context files maintain an `http` namespace for all terms, but can also be resolved from `https`-based addresses.

While the schema.org context is resolvable at both the original `http` address and the newer `https` address, changing the namespace to `https` references would also effectively change the namespace of the terms to a new namespace. While schema.org maintainers have clarified that both namespaces have been actively recommended for 5 years, and are considered synonomous, the official context file that is retrieved from both `https://schema.org/` and `http://schema.org` define the namespace URI for the vocabulary as `http://schema.org/`. For consistency, we thus recommend using the `http`-based namespace so that term URIs stay comparable over time, but also that harvesters consumers treat the http and https namespaced terms as logical synonyms.

One consistent mechanism to use the `http`-based namespace is to load the context from the context file maintained by schema.org. This can be accomplished using:

```json
{
    "@context": "https://schema.org/",
    "@type": "Dataset",
    "name": "Example dataset title"
}
```

While that context is loaded from the `https` address above, the resulting JSON-LD fragment uses the `http` namespace when it is expanded:

```json
[
  {
    "@type": [
      "http://schema.org/Dataset"
    ],
    "http://schema.org/name": [
      {
        "@value": "Example dataset title"
      }
    ]
  }
]
```

Finally, if referencing the namespace inside context definitions using `@vocab` or when defining a prefix, then the `http`-baased namespace should be used. For example:

```json
{
    "@context": {
        "@vocab": "http://schema.org/",
        "schema": "http://schema.org/"
    },
    "@type": "Dataset",
    "name": "Example dataset title",
    "schema:isAccessibleForFree": true
}
```

In addition to the `http`, we also need the trailing slash to be consistently applied, so that term URIs that are constructed become properly expanded. For example, `schema:Dataset` should expand to `http://schema.org/Dataset`. Without the trailing slash, it would expand to the incorrect `http://schema.orgDataset`.

  See also discussion at [issue #52](https://github.com/ESIPFed/science-on-schema.org/issues/52)

<a id="versioning"></a>
## Versioning ##

1.  will follow the [semantic versioning](https://semver.org/) pattern:

Given a version number MAJOR.MINOR.PATCH, increment the:

  * MAJOR version when you make incompatible changes to a recommendation,
  * MINOR version when you add functionality in a backwards-compatible manner, and
  * PATCH version when you make backwards-compatible bug fixes.

<a id="why-jsonld"></a>
## Why JSON-LD? ##

Schema.org allows descriptions using Microdata, RDFa, and JSON-LD. In this guide, we will use JSON-LD because:

1. **Simplicity** - JSON-LD is the *most succinct* of the formats for communicating our *intent* with the recommendations.
2. **Terseness** - the JSON-LD ```[@context](https://json-ld.org/spec/latest/json-ld/#the-context)``` property allows publishers to express the data type of a specific properties of the data graph.

*NOTE: Our intent is not to override [https://schema.org/](https://schema.org/) classes and properties, but to provide flexibility to our examples and recommendations when using external vocabularies.*


<a id="external-vocab-typing"></a>
## Typing to External Vocabularies ##

While schema.org provides a property called [schema:additionalType](https://schema.org/additionalType) for specifying additional classes from vocabularies outside schema.org, this technique does not follow best practices of typing using JSON-LD. Instead, we __highly recommend__ using the `@type` field. For example:

```
{
 "@context": "http://schema.org",
 "@type": "PropertyValue",
 "additionalType": "http://vocabulary.example.org/ScientificInstrument",
 "name": "My Property"
}
```

would become:

```
{
 "@context": "http://schema.org",
 "@type": ["PropertyValue", "http://vocabulary.example.org/ScientificInstrument"],
 "name": "My Property"
}
```

or:

```
{
 "@context": {
   "@vocab": "http://schema.org",
   "ex": "http://vocabulary.example.org/"
 },
 "@type": ["PropertyValue", "ex:ScientificInstrument"],
 "name": "My Property"
}
```

**WHY?**

When data is harvested using `schema:additionalType` the URLs in these fields are not automatically converted into types as content in the `@type` field would be. Searching the results of that harvester for all data typed as `http://vocabulary.example.org/ScientificInstrument` would not automatically work. We recommend following the JSON-LD best practice of using the `@type` field as shown above.

**Google Rich Results Tool**

One impact of this change is that the Google Rich Results Tool presently considers all external vocabulary references as an error. This tool is ONLY checking for conformance to Google's interpretation of schema.org (see the [Google Dataset recommendations](https://developers.google.com/search/docs/data-types/dataset)). This might influence a publisher to think that their schema.org markup is wrong when in fact it is not. The errors simply mean that your schema.org markup doesn't conform to Google's preference. Nevertheless, Google still accepts, harvests, and makes available JSON-LD compliant schema.org markup that does not conform to their preference; the additional types and content are simply ignored by Google, but can be used by other applications. Results have shown this to be evident at the [Google Dataset Search](https://datasetsearch.research.google.com/).

**Using external vocabulary prefixes**
In addition, if one uses [schema:additionalType](https://schema.org/additionalType), then one cannot use prefixes defined in the `@context` section when referencing these external concepts.  Instead, the concept must be specified with its full URL. This is illustrated in the example above, where we have to use `"additionalType": "http://vocabulary.example.org/ScientificInstrument"`  rather than the more compact prefixed version `"@type": ["ex:ScientificInstrument"]`.

If one does decide to use `additionalType`, then opening the example in the JSON-LD Playground will show how the element type is not expanded and there is no triple generated for the additionalType.  Thus, we recommend using the `@type` field directly for associating fields with types so that they become part of the knowledge graph for the Dataset.

