<a id="top"></a>
[Home](/README.md) | Getting Started

# Getting Started #

If you are new to publishing schema.org, here are some general tips to getting started.

* [Goal](#goals)
* [Approach](#approach)
* [Prerequisites](#prerequisites)
* [Introduction](#introduction)
* [Using schema.org](#using-schemaorg)
  * [Modifying web pages to include schema.org as JSON-LD](#using-schemaorg_adding-jsonld-webpages)
  * [Specifying the context](#context)
  * [Provide a Sitemap](#sitemaps)
  * [Data Types](#data-types)
    * [Text](#data-types_Text)
    * [Number](#data-types_Number)
    * [URL](#data-types_URL)
    * [Boolean](#data-types_Boolean)
    * [Date](#data-types_Date)
    * [DateTime](#data-types_DateTime)
    * [Time](#data-types_Time)
    * [HTML](#data-types_HTML)
  * [Resource Types](#resource-types)
* [Resource Modification Time](#modification_times)
  * [`schema.org/dateModified`](#mod_so)
  * [HTTP `Last-Modified`](#mod_http)
  * [Sitemap `<lastmod>`](#mod_map)
* [JSON-LD Graph Techniques](#json-ld)
  * [Ordered Lists](#json-ld-list)


# Goals #

To provide a place for the scientific data community to work out how best to implement **schema.org** and other external vocabularies on web pages by publishing guidance documents. *[Pull requests](/pulls)* and *[Github Issues](/issues)* are welcome!

<a id="approach"></a>
## Approach ##

1. To be **pragmatic** with our use of schema.org and external vocabulary adoption.
2. To **consider schema.org classes and properties first** before considering external vocabularies.
3. Use **[JSON-LD](https://json-ld.org/)** in our guidance documents for simplicity and terseness as compared to *[Microdata](https://www.w3.org/TR/microdata/)* and *[RDFa](https://rdfa.info/)*. For more, see [Why JSON-LD?](/CONVENTIONS.md#why-jsonld) from the [Conventions](/CONVENTIONS.md) document.
4. Presently, the [Google Rich Results Tool](https://search.google.com/test/rich-results) enforces use of [schema.org](https://schema.org/) classes and properties by displaying an error whenever external vocabularies are used. schema.org proposes linking to external vocabularies using the [schema:additionalType](https://schema.org/additionalType) property. While this property is defined as a sub property of [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type), its data type is a literal. However, using the [Schema.org Validator](https://validator.schema.org/) allows for the use of external vocabularies. We encourage the use of JSON-LD ```'@type'``` for typing classes to external vocabularies. For more, see [Typing to External Vocabularies](/CONVENTIONS.md#external-vocab-typing) from the [Conventions](/CONVENTIONS.md) document.
5. See [Governance](/GOVERNANCE.md) for how we will govern the project.
6. See [Conventions](/CONVENTIONS.md) for guidance on creating/editing guidance documents.

<a id="prerequisites"></a>
## Prerequisites ##

1. We assume a general understanding of [JSON](http://www.json.org/).
2. We assume a basic knowledge about [JSON-LD](https://json-ld.org).

  JSON-LD is valid JSON, so standard developer tools that support JSON can be used. For some specific JSON-LD and schema.org help though, there are some other resources.

  ##### JSON-LD resources https://json-ld.org
  Generating the JSON-LD is best done via libraries like those you can find at https://json-ld.org.
  There are libraries for; Javascript, Python, PHP, Ruby, Java, C# and Go. While JSON-LD is just
  JSON and can be generated many ways, these libraries
  can generate valid JSON-LD spec output.

  ##### JSON-LD playground https://json-ld.org/playground/
  The playground is hosted at the very useful [JSON-LD web site](https://json-ld.org) site. You
  can explore examples of JSON-LD and view how they convert to RDF, flatten, etc. Note that JSON-LD
  is not associated with schema.org. It can be used for much more and so most examples at the JSON-LD
  website don't use schema.org and the site will NOT look to see if you are using schema.org types
  and properties correctly; it will only check that your JSON-LD is well-formed.

3. We assume that you've heard about [schema.org](https://schema.org/) and have already decided that it's useful to you.
4. We assume that you have a general understanding of what may describe a scientific dataset.

Let's go!

<a id="introduction"></a>
## Introduction ##
There is an emerging practice to leverage structured metadata to aid in the discovery of web-based resources. Much of this
work is taking place in the context (no pun intended) of schema.org. This approach has extended to the resource type Dataset.
This page will present approaches, tools and references that will aid in the understanding and development of schema.org in
JSON-LD and its connection to external vocabularies. For a more thorough presentation on this, visit the Google AI Blog entry
of January 24 2017 at https://ai.googleblog.com/2017/01/facilitating-discovery-of-public.html .

<a id="using-schemaorg"></a>
## Using schema.org ##

<a id="using-schemaorg_adding-jsonld-webpages"></a>
### Modifying web pages to include schema.org as JSON-LD ###
JSON-LD should be incorporated into the landing page html inside the `<head></head>` as a `<script>` element with a type of `application/ld+json`.

```
<html>
  <head>
    ...
    <script id="schemaorg" type="application/ld+json">
    {
      "@context": "https://schema.org/",
       "@id": "http://opencoredata.org/id/dataset/bcd15975-680c-47db-a062-ac0bb6e66816",
       "@type": "Dataset",
       "description": "Janus Thermal Conductivity for ocean drilling ..."
    }
    </script>
    ...
  </head>
  ...
</html>
 ```

<a id="context"></a>
### Specifying the `context`

The `context` in a JSON-LD document defines the namespaces used in the document and their mappings to URIs when they
are referenced using prefix notation. The JSON-LD 1.1 specification
[provides many rules](https://www.w3.org/TR/json-ld11-api/#remote-document-and-context-retrieval) that impact how the context is
loaded and how it is retrieved, but ultimately the goal is to define a context map with the namespace mappings for each
vocabulary used in the document. For the schema.org vocabulary specifically, the official namespace is `http://schema.org/`
(note this is not an `https` URI), but the context file for schema.org can be retrieved from the `https` web location at
`https://schema.org` by following the JSON-LD processing rules. For providers, this translates to a few simple recommendations.

1. We recommend retrieving the context file from its `https` location using the following syntax:

```
{
  "@context": "https://schema.org/",
   "@type": "Dataset",
   "name": "Example dataset title",
   ...
}
```

Using this approach, the schema.org namespace will be set to `http` URIs. For example the `Dataset` type will be expanded to
`http://schema.org/Dataset`.

2. Should you need to define additional namespaces in your context, it can be done by expanding the context using a JSON array as follows:

```json
{
  "@context": [
    "https://schema.org/",
    {
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@type": "Dataset",
  "name": "Example dataset title",
  "prov:wasDerivedFrom": {
    "@id": "https://doi.org/10.xxxx/Dataset-1"
  }
}
```

Note the square brackets, in which the first entry is the URL of a context file to be retrieved, and the second value is a JSON object to be
combined with the retrieved context. This approach still retrieves the context from the secure `https` URL at schema.org, but then adds an additional
namespace for the `prov` vocabulary to the context. Now, terms from the PROV namespace can be referenced using prefix notation (e.g., `prov:wasDerivedFrom`).

3. Additional approaches to defining the context are possible, but users should use care to ensure that the terms within schema.org use the
`http://schema.org/` namespace as defined in the official schema.org context file. Because contributors to schema.org are working towards
accepting `https://schema.org/` as an equivalent namespace URI for all terms, processors should treat schema.org terms in the http and https
URI spaces as equivalent, but providers might find it safer to continue to use `http://schema.org/` as the official namespace for now. This
particularly applies when defining a default vocabulary for un-prefixed terms, in which case we recommend using `"@vocab": "http://schema.org/"`
if this is necessary. That said, most users should not have need to define `@vocab` in typical usage.

<a id="sitemaps"></a>
### Provide a Sitemap.xml file

Many harvesters and aggregators depend on the existence of a `sitemap.xml` file on your site that lists all of the dataset landing pages from your site that you want to be harvested and indexed for search. Google Dataset Search, DataONE, and Geocodes all can make use of a sitemap to more efficiently harvest your site. A sitemap is a simple text file that lists each page that you want harvested. This can contain any webpage, but in this context we specifically want to list pages that contain a `schema:Dataset` entry to be harvested. Here's an example `sitemap.xml` file listing two Dataset landing pages, along with their `lastmod` date:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://arcticdata.io/catalog/view/doi%3A10.18739%2FA2GH9BB0Q</loc>
    <lastmod>2021-12-06</lastmod>
  </url>
  <url>
    <loc>https://arcticdata.io/catalog/view/doi%3A10.18739%2FA2ST7DZ2Q</loc>
    <lastmod>2021-12-07T12:15:05Z</lastmod>
  </url>
</urlset>
```

Note the `<lastmod>` field, which indicates the last date on which the page was modified and is formatted as a [W3C DateTime](https://www.w3.org/TR/NOTE-datetime) and may vary in precision. Most harvesters will use that date along with the HTTP `Last-modified` header to determine if a page has changed since the last time that a harvest was attempted. Keeping accurate `lastmod` values can massively improve the efficiency of indexing your catalog, as only the few items that have changed will need to be indexed.

**Location:** The sitemap.xml file can be located anywhere on your site that is above the path in the hierarchy in which your pages are listed. Typically, the sitemap.xml is placed at the root of the site, but other locations can be used as well. A great way to indicate to harvesters where your sitemap is located would be to include it in your `robots.txt` file, which is basically an instruction manual for harvesters, at the root of your web site. For example, you might have a robots.txt file with the following contents:

<pre>
User-agent: *
Sitemap: https://arcticdata.io/sitemap1.xml
</pre>

Sitemaps are limited to 50,000 records and 50MB, so if your site is larger than that you can break up your sitemap into multiple files, linked together using a sitemap index. Details about [`sitemap-index.xml`](https://www.sitemaps.org/protocol.html#index) and other aspects of sitemaps are provided in the https://sitemaps.org site, as well as from the [Google sitemap documentation](https://developers.google.com/search/docs/advanced/sitemaps/build-sitemap).

By providing a sitemap and advertising its location, you make it simple for harvesters to find and index your Dataset listings.

<a id="data-types"></a>
### Data Types ###

For each schema.org type, such as Person or Event, there are fields that let you specify more information about that type. Each of these fields has an expected data type that is defined in the documentation as you can see from [Figure 1.](#figure-1).

<a id="figure-1"></a>
<p align="center">
  <strong>Figure 1. schema.org field data types</strong><br/>
  <img src="/assets/schemaorg-datatypes.png">
  <em>The expected data type for each field appears in the middle column. The left column is the name of the field, the middle column is the data type, and the right column is the description of the field.</em>
</p>

Every data type is either a *resource* or a *literal*. Resources refer to other schema.org types. For example, a Dataset type has a field called 'author' of which the data type can be either a 'Person' or an 'Organization'. Because 'Person' and 'Organization' are other schema.org "types" with their own fields, they are called resources. In JSON-LD, you specify resources by using curly brackets ```{}```:

<pre>
{
  "@context": "https://schema.org/",
  "@type": "Dataset",
  <strong>"author": {
    "@type": "Person",
    "name": "Jane Goodall"
  }</strong>
}
</pre>

In the JSON-LD above, the 'author' is a resource of type 'Person'. Fields that simply have a value are called literal data types. For examples, the 'Person' type above has a 'name' of "Jane Goodall" - a literal text value.

Schema.org defines six literal, or primitive, data types: [Text](https://schema.org/Text), [Number](https://schema.org/Number), [Boolean](https://schema.org/Boolean), [Date](https://schema.org/Date), [DateTime](https://schema.org/DateTime), and [Time](https://schema.org/Time). [Text](https://schema.org/Text) has two special variations: [URL](https://schema.org/URL) and how to specify when text is actually [HTML](#data-type_HTML).

When using schema.org, literal data types are not specified using curly brackets ```{}``` as these are reserved for specifying 'objects' or 'resources' such as other schema.org types like ```Person```, ```Organization```, etc. First, let's see how to use a primitive data type by using fields of [CreativeWork](https://schema.org/CreativeWork), the superclass for [Dataset](https://schema.org/Dataset).

<a id="data-types_Text"></a>
#### Text ####
Imagine we want to say the name of our Creative Work is "Passenger Manifest for H.M.S. Titanic". The [name](https://schema.org/name) field of CreativeWork specifies that it expects Text as the data type. We would use it in this way:

<pre>
{
  "@context": "https://schema.org/",
  "@type": "CreativeWork",
  <strong>"name": "Passenger Manifest for H.M.S. Titanic"</strong>
}
</pre>

<a id="data-types_Number"></a>
#### Number ####
Let's say we want to specify the version number of our manifest using the [version](https://schema.org/version) field of CreativeWork which expects a Number. To specify numbers in JSON-LD, we omit the quotations surrounding the value:

<pre>
{
  "@context": "https://schema.org/",
  "@type": "CreativeWork",
  "name": "Passenger Manifest for H.M.S. Titanic",
  <strong>"version": 1</strong>
}
</pre>

<a id="data-types_URL"></a>
#### URL ####
Now, let's specify the URL of our manifest using the [url](https://schema.org/url) field of CreativeWork, an inherited field from [Thing](https://schema.org/Thing). This fields expects a valid URL represented as Text:

<pre>
{
  "@context": "https://schema.org/",
  "@type": "CreativeWork",
  "name": "Passenger Manifest for H.M.S. Titanic",
  "version": 1,
  <strong>"url": "https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv"</strong>
}
</pre>

<a id="data-types_Boolean"></a>
#### Boolean ####
Using the Boolean value, we can specify that our manifest is accessible for free using the field [isAccessibleForFree](https://schema.org/isAccessibleForFree) by using the text ```true``` or ```false``` and omitting the quotes:

<pre>
{
  "@context": "https://schema.org/",
  "@type": "CreativeWork",
  "name": "Passenger Manifest for H.M.S. Titanic",
  "version": 1,
  "url": "https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv",
  <strong>"isAccessibleForFree": true</strong>
}
</pre>

<a id="data-types_Date"></a>
#### Date ####

To specify the [datePublished](https://schema.org/datePublished), which allows either a Date or DateTime, as a Date, we can use any [ISO 8601 date format](https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations) by wrapping the date in double-quotes:

<pre>
{
  "@context": "https://schema.org/",
  "@type": "CreativeWork",
  "name": "Passenger Manifest for H.M.S. Titanic",
  "version": 1,
  "url": "https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv",
  "isAccessibleForFree": true,
  <strong>"datePublished": "2018-07-29"</strong>
}
</pre>

<a id="data-types_DateTime"></a>
#### DateTime ####

To specify the [dateModified](https://schema.org/dateModified) as a DateTime, as a Date, we must follow the [ISO 8601 format for combining date and time representations](https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations) using the form ```[-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] ```:

<pre>
{
  "@context": "https://schema.org/",
  "@type": "CreativeWork",
  "name": "Passenger Manifest for H.M.S. Titanic",
  "version": 1,
  "url": "https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv",
  "isAccessibleForFree": true,
  "datePublished": "2018-07-29",
  <strong>"dateModified": "2018-07-30T14:30Z"</strong>
}
</pre>

<a id="data-types_Time"></a>
#### Time ####

[Time](https://schema.org/Time) is a rarely-used data type because it must represent a point in time recurring on multiple days following the [XML Schema definition](https://www.w3.org/TR/xmlschema-2/#time) using the form ```hh:mm:ss[Z|(+|-)hh:mm]``` (see XML schema for details).

<pre>
{
  "@context": "https://schema.org/",
  "@type": "CreativeWork",
  "name": "Passenger Manifest for H.M.S. Titanic",
  "version": 1,
  "url": "https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv",
  "isAccessibleForFree": true,
  "datePublished": "2018-07-29",
  <strong>"dateModified": "2018-07-30T14:30Z"</strong>
}
</pre>

<a id="data-types_HTML"></a>
#### HTML ####

The HTML data type is a special variation of the ```Text``` data type. In some cases where `Text` is the expected data type, our actual data type may be HTML (because we are dealing with web pages). In this case, the [schema.org JSON-LD context](https://schema.org/docs/jsonldcontext.json) defines ```HTML``` to mean [rdf:HTML](http://www.w3.org/1999/02/22-rdf-syntax-ns#HTML), the data type for specifying that a string of text should be interpreted as HTML. Let's say that we have a description of our manifest and want to use the [description](https://schema.org/description) field, but we have HTML inside that text. Using the text field as we did above for the ```name``` field, we would specify the ```description``` as:

<pre>
{
  "@context": "https://schema.org/",
  "@type": "CreativeWork",
  "name": "Passenger Manifest for H.M.S. Titanic",
  "version": 1,
  "url": "https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv",
  "isAccessibleForFree": true,
  "datePublished": "2018-07-29",
  "dateModified": "2018-07-30T14:30Z",
  <strong>"description": "&lt;h3&gt;Acquisition&lt;/h3&gt;&lt;p&gt;The data was acquired from an office outside of &lt;a href\"https://en.wikipedia.org/wiki/New_York_City\"&gt;New York City&lt;/a&gt;."</strong>
}
</pre>

However, to specify that the ```description``` field should be *interpreted* as HTML, you specify ```description``` as a resource, setting the ```@type``` of that resource to "HTML" and placing the HTML string in a JSON-LD property ```@value```:

<pre>
{
  "@context": "https://schema.org/",
  "@type": "CreativeWork",
  "name": "Passenger Manifest for H.M.S. Titanic",
  "version": 1,
  "url": "https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv",
  "isAccessibleForFree": true,
  "datePublished": "2018-07-29",
  "dateModified": "2018-07-30T14:30Z",
  "description": {
    <strong>"@type": "HTML",
    "@value": "&lt;h3&gt;Acquisition&lt;/h3&gt;&lt;p&gt;The data was acquired from an office outside of &lt;a href\"https://en.wikipedia.org/wiki/New_York_City\"&gt;New York City&lt;/a&gt;."</strong>
  }
}
</pre>

<a id="resource=types"></a>
### Resource Types ###

All schema.org resources should make use of the ```@type``` property which 'classifies' the resources as a specific type. For example, an un-typed resource would look like:

<pre>
{
  "@context": "https://schema.org/",
  "name": "My Dataset"
}
</pre>

Even though the above resource has a name of 'My Dataset', harvesters are unaware that your *intent* was to classify it as a Dataset. Un-typed resources are not valid schema.org resources, and so they require the ```@type``` property:

<pre>
{
  "@context": "https://schema.org/",
  <strong>"@type": "Dataset",</strong>
  "name": "My Dataset"
}
</pre>

In some cases, it useful to multi-type a resource. One example of this may be a data repository. A data repository is typically functioning as both an 'Organization' that employs people and has an address, but also as a 'Service' to its user community. To assign multiple types to a resource, we use JSON arrays:

<pre>
{
  "@context": "https://schema.org/",
  <strong>"@type": ["Organization", "Service"],</strong>
  "name": "My Data Repository"
}
</pre>

**All [schema.org types may be found here](https://schema.org/docs/full.html).**

<a id="modification_times"></a>
## Time of resource modification

An indication of when a resource was modified is valuable to a consumer for a variety of reasons.

A consumer tracking changes in a collection of `SO:Dataset` or similar resources being advertised
with a `sitemap.xml` or similar mechanism has at least three timestamps that can be examined to
determine if an already retrieved resource may have been modified: the `schema.org/dateModified`
property in the JSON-LD, the `Last-Modified` time reported by the web server, and the `<lastmod>`
time that may be reported in a `sitemap.xml` document.

The `schema.org/dateModified` value should be considered authoritative for indicating when the
resource was modified. The `Last-Modified` header should reflect the corresponding
`schema.org/dateModified` entry. This property provides an important hint for consumers as to
whether a cached copy of a resource should be updated for example. Similarly the `<lastmod>`
entry should reflect the `Last-Modified` header and the `schema.org/dateModified` value.

A typical pattern for a consumer interesting in synchronizing a cache of resource is:

1. Examine the sitemap for new or updated entries using hints from `<lastmod>`
2. Retrieve the resource directly or by previewing with a HTTP HEAD request. A
   `Last-Modified` provides a hint as to whether the resource should be retrieved.
3. Examine the `schema.org/dateModified` property of the resource(s) extracted from the
   resource.

Providing accurate hints early in the process can reduce requirements for effectively
sharing data resources.

<a id="mod_so"></a>
### 1. `schema.org/dateModified`

Each `schema.org` instance derived from [`schema.org/CreativeWork`](https://schema.org/CreativeWork)
may have a [`dateModified`](https://schema.org/dateModified) property to indicate "The date on which
the CreativeWork was most recently modified or when the item's entry was modified within a DataFeed."
This property should be provided with any instance of `schema.org/Dataset` or any other `schema.org`
entity published in a landing page or though other mechanisms. The JSON spec does not include a
built-in type for date time values, but the general consensus and a sensible practice is to
represent a date time value as a time zone aware ISO 8601 formatted string. For example:

```json
{
  "dateModified": "2018-12-10T13:45:00.000Z"
}
```

<a id="mod_http"></a>
### 2. HTTP `Last-Modified` Header

A schema.org instance is typically embedded in a landing page or may be accessed directly as a
JSON-LD document over the HTTP protocol. HTTP resource providers (i.e. web servers) may include
a [`Last-Modified` header](https://tools.ietf.org/html/rfc7232#section-2.2) which contains the
date and time at which the origin server believes the resource was last modified. The format for
the date value follows the [RFC 2616 specification](https://tools.ietf.org/html/rfc2616). For
example:

```
Last-Modified: Mon, 10 Dec 2018 13:45:00 GMT
```

<a id="mod_map"></a>
### 3. `sitemap.xml lastmod` value

A [`sitemap.xml`](https://www.sitemaps.org/protocol.html) document provides a mechanism for a
resource server to advertise available resources. Each `<url>` element may include a `<lastmod>`
tag to indicate when the resource identified by the `<url>/<loc>` was last modified. The
specification is fairly loose, indicating that date in the
[W3C Datetime](https://www.w3.org/TR/NOTE-datetime) format of `YYYY-MM-DD` may be
sufficient. However, for the purposes of content synchronization, a higher precision is
desireable, and should be provided where possible. For example:

```
2018-12-10T13:45:00.000Z
```

<a id="json-ld"></a>
## JSON-LD Graph Techniques

[JSON-LD](https://json-ld.org) documents represent a graph model, even though at times that graph is implicit rather than being named. Here are some techniques that may be useful when constructing such graphs.

<a id="json-ld-list"></a>
### Ordering items with JSON-LD `@list`

Unlike plain JSON, collections in JSON-LD are unordered [[1](https://json-ld/json-ld.org#12), [2](https://www.w3.org/TR/json-ld/#lists)]. In cases where ordering of items needs to be preserved, we can use the `@list` keyword to specify that order should be preserved for a collection. Ordered lists would be important, for example, when a list of authors or creators should be ordered as intended when rendering a view of the metadata, or when a list of bounding box coordinates in an array need to come in a particular order.

In the following example, the list of `creator` items is not ordered, and so client tools could return the creator names in any order, and different tools may return them in different orders. This would be problematic for building a citation, for example.

Example 1. Ordering for this list of creators will not be preserved:
```
{
  "@context": "https://schema.org/",
  "@id": "unordered_01",
  "@type": "Dataset",
  "creator": [
    {
      "@id": "https://www.sample-data-repository.org/person/51317",
      "@type": "Person",
      "name": "Dr Uta Passow"
    },
    {
      "@id": "https://www.sample-data-repository.org/person/50663",
      "@type": "Person",
      "name": "Dr Mark Brzezinski"
    }
  ]
}
```

To order a list, use the JSON-LD [`@list` keyword`](https://www.w3.org/TR/json-ld/#lists), as shown in Example 2:


Example 2. Order will be preserved for this list of creators:
```
{
  "@context": "https://schema.org/",
  "@id": "order_01",
  "@type": "Dataset",
  "creator": {
    "@list": [
      {
        "@id": "https://www.sample-data-repository.org/person/51317",
        "@type": "Person",
        "name": "Dr Uta Passow"
      },
      {
        "@id": "https://www.sample-data-repository.org/person/50663",
        "@type": "Person",
        "name": "Dr Mark Brzezinski"
      }
    ]
  }
}
```

Ordering may be specified globally within the document by specifying the container type in a context. For example,
after retrieving the context file from schema.org, we can define the `schema:creator` to be a list container globally
in the document using the `@container` property:

Example 3. Ordering of a list of creators is preserved anywhere such a list appears within the context.
```
{
  "@context": [
    "https://schema.org/",
    {
      "creator": {
        "@container": "@list"
      }
    }
  ],
  "@id": "order_02",
  "@type": "Dataset",
  "creator": [
    {
      "@id": "https://www.sample-data-repository.org/person/51317",
      "@type": "Person",
      "name": "Dr Uta Passow"
    },
    {
      "@id": "https://www.sample-data-repository.org/person/50663",
      "@type": "Person",
      "name": "Dr Mark Brzezinski"
    }
  ]
}
```

With this technique, ordering can be set once in the context using `@list`, and then order will be preserved any time that concept is used in the document.
