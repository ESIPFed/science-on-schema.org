# Conventions #

All guidance documents should follow the following conventions:

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
