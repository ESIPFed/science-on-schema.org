# Use SPDX license vocabulary for URIs

Discussion: https://github.com/ESIPFed/science-on-schema.org/issues/47

## Status ##
_Accepted_

## Decision ##

Use SPDX license URIs to unambiguously specify the license for data and metadata use.

## Context ##

Link a Dataset to its license to document legal constraints by adding a [schema:license](https://schema.org/license) property. The [guide](https://developers.google.com/search/docs/data-types/dataset) recommends providing a URL that unambiguously identifies a specific version of the license used, but for many licenses it is hard to determine what that URL should be. Thus, we recommend that the license URL be drawn from the [SPDX license list](https://spdx.org/licenses/), which provides a curated list of licenses and their properties that is well maintained. For each SPDX entry, SPDX provides a canonical URL for the license (e.g., `http://spdx.org/licenses/CC0-1.0`), a unique `licenseId` (e.g., `CC0-1.0`), and other metadata about the license. Here's an example using the SPDX license URI for the Creative Commons CC-0 license:

<pre>
{
  "@context": {
    "@vocab": "https://schema.org/",
  },
  "@id": "http://www.sample-data-repository.org/dataset/123",
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  <strong>"license": "http://spdx.org/licenses/CC0-1.0"</strong>
  ...
}
</pre>

While many licenses are ambiguous about the license URI for the license, the Creative Commons licenses are an exception in that they provide consistent URIs for each license, and these are in widespread use.  While we recommend using the SPDX URI, it is acceptable to use the CC license URIs directly if preferred.  Here's an example using the traditional CC URI for the license.
<pre>
{
  "@context": {
    "@vocab": "https://schema.org/",
  },
  "@id": "http://www.sample-data-repository.org/dataset/123",
  "@type": "Dataset",
  "name": "Removal of organic carbon by natural bacterioplankton communities as a function of pCO2 from laboratory experiments between 2012 and 2016",
  <strong>"license": "https://creativecommons.org/publicdomain/zero/1.0"</strong>
  ...
}
</pre>

One issue is that SPDX URIs currently resolve to a HTML landing page describing a license, rather than a machine-readable version of the license through content negotiation. However, the web page that is returned does contain structured markup in RDFa format indicating the structured license properties.  For example, the HTML page for the [Apache-2.0 license](http://spdx.org/licenses/Apache-2.0) contains property attributes for structured data for `spdx:License`, `spdx:deprecated`, `spdx:name`, `spdx:licenseId`, `rdfs:seeAlso`, `spdx:isOsiApproved`, and `spdx:licenseText`, among others. For example, here is the web snippet for the Apache-2.0 license:

<pre>
&lt;h1 property="dc:title"&gt;Apache License 2.0&lt;/h1&gt;
&lt;div style="display:none;"&gt;&lt;code property="spdx:deprecated"&gt;false&lt;/code&gt;&lt;/div&gt;
&lt;h2&gt;Full name&lt;/h2&gt;
    &lt;p style="margin-left: 20px;"&gt;&lt;code property="spdx:name"&gt;Apache License 2.0&lt;/code&gt;&lt;/p&gt;

&lt;h2&gt;Short identifier&lt;/h2&gt;
    &lt;p style="margin-left: 20px;"&gt;&lt;code property="spdx:licenseId"&gt;Apache-2.0&lt;/code&gt;&lt;/p&gt;

&lt;h2&gt;Other web pages for this license&lt;/h2&gt;
    &lt;div style="margin-left: 20px;"&gt;
      &lt;ul&gt;
       &lt;li&gt;&lt;a href="http://www.apache.org/licenses/LICENSE-2.0" rel="rdfs:seeAlso"&gt;http://www.apache.org/licenses/LICENSE-2.0&lt;/a&gt;&lt;/li&gt;
       &lt;li&gt;&lt;a href="https://opensource.org/licenses/Apache-2.0" rel="rdfs:seeAlso"&gt;https://opensource.org/licenses/Apache-2.0&lt;/a&gt;&lt;/li&gt;
     &lt;/ul&gt;
    &lt;/div&gt;
          
&lt;div property="spdx:isOsiApproved" style="display: none;"&gt;true&lt;/div&gt;

&lt;h2 id="notes"&gt;Notes&lt;/h2&gt;
    &lt;p style="margin-left: 20px;"&gt;This license was released January 2004&lt;/p&gt;

&lt;h2 id="licenseText"&gt;Text&lt;/h2&gt;

&lt;div property="spdx:licenseText" class="license-text"&gt;
      
&lt;div class="optional-license-text"&gt;
   &lt;p&gt;Apache License
  &lt;br /&gt;

Version 2.0, January 2004
  &lt;br /&gt;
...
</pre>

Finally, the SPDX project provides structured data files of the [SPDX license data](https://github.com/spdx/license-list-data) in machine readable formats, including turtle and json-ld.  These could be imported into COR or other vocabulary servers to provide a queryable graph of the license data.

## Consequences ##

- We gain a comprehensive, maintained, unambiguous vocabulary for licenses, increasing consistency across repositories
- We gain compatibility with the software packaging world like Debian and Python
- Licenses that have well-known URIs (e.g., Creative Commons) may be less recognizable by their SPDX URI
- SPDX license URIs only resolve to HTML pages with machine-readable RDFa embedded, but machine-readable representations in other formats do not seem to be available through content negotiation
