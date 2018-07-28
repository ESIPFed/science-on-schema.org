<a id="top"></a>
# Getting Started #

If you are new to publishing schema.org, here are some general tips to getting started.

* [Data Types](#data-types)
  * [HTML](#data-types_HTML)
* ...
* ...

<a id="data-types"></a>
## Data Types ##

Knowing the type of data you want to represent in each field can be very helpful. In [schema.org](https://schema.org), the expected data type(s) for each field are defined in the documentation as seen in [Figure 1](#figure-1).

<a id="figure-1"></a>
<p align="center">
  <strong>Figure 1. schema.org field data types</strong><br/>
  <img src="/assets/schemaorg-datatypes.png">
  <em>The expected data type for each field appears in the middle column. The left column is the name of the field, the middle column is the data type, and the right column is the field's description.</em>
</p>

<a id="data-types_HTML"></a>
### HTML Data Type ###
In some cases where `Text` is the expected data type, our actual data type may be HTML. In this case, the [schema.org JSON-LD context](https://schema.org/docs/jsonldcontext.json) defines ```HTML``` to mean [rdf:HTML](http://www.w3.org/1999/02/22-rdf-syntax-ns#HTML), the data type for specifying that a string of text should be interpreted as HTML.

#### Using the HTML data type ####

Let's say you have a [Dataset](https://schema.org/Dataset) where the [description](https://schema.org/description) field contains HTML:

```
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "My Dataset",
  "description": "<h3>Acquisition</h3><p>The data was acquired from a side-scan sonar thrown over the side of an ocean-going research vessel in 15 ft. waves. The calibration information can be found <a href=\"https://example.com/my-dataset/my-cruise/side-scan-sonar-calibration\">here</a>."
}
```

To specify that the ```description``` field should be interpreted as HTML, you specify the type as follows:

<pre>
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "My Dataset",
  "description": { 
    <strong>"@type": "HTML", 
    "@value": "&lt;h3&gt;Acquisition&lt;/h3&gt;&lt;p&gt;The data was acquired from a side-scan sonar thrown over the side of an ocean-going research vessel in 15 ft. waves. The calibration information can be found &lt;a href=\"https://example.com/my-dataset/my-cruise/side-scan-sonar-calibration\"&gt;here&lt;/a&gt;."</strong> 
  }
}
</pre>

*NOTE: As of 7/28/2018, the [Google Structured Data Testing Tool](https://search.google.com/structured-data/testing-tool/u/0/) understands the value of ```description``` to be `rdf:HTML`, but the tool specifies this type is unknown. However, you can see from the schema.org Github repository, that this method was discussed and implemented in [pull #1634: alias HTML to rdf:HTML](https://github.com/schemaorg/schemaorg/pull/1634)*
