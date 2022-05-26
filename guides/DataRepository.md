<a id="top"></a>
[Home](/README.md) | DataRepository

# Describing a Repository

* [Basic Fields](#basic-fields)
* [Identifier](#identifier)
* [Funding Source](#funding-source)
* [Services](#services)
* [Data Collections](#data-collections)
* [Advanced Publishing Techniques](#advanced-publishing)
  * [How to use external vocabularies](#advanced-publishing-category)

## Describing a Repository

[![Repository  - Overview](/assets/diagrams/repository/repository-overview.svg "Repository - Overview")](#)

In schema.org, we model a repository as both an [schema:ResearchProject](https://schema.org/ResearchProject), a sub-class of an Organization, and a [schema:Service](https://schema.org/Service). This double-typing gives us the most flexibility in describing the characteristics of the organization providing the service and the services offered by the organization.

<pre>
{
  "@context": "https://schema.org/",
  <strong>"@type": ["Service", "ResearchProject"],
  "legalName": "Sample Data Repository Office",
  "name": "SDRO"
  </strong>
}
</pre>

<a id="basic-fields"></a>
The other fields you can use to describe the Organziation and the Service are:

[![Repository  - Basic Fields](/assets/diagrams/repository/repository_basic-fields.svg "Repository - Basic Fields")](#)

* [schema:legalName](https://schema.org/legalName) should be the official name of the  repository,
* [schema:name](https://schema.org/name) can be an acronym or the name typcially used for the repository,
* [schema:url](https://schema.org/url) should be the url of your repository's homepage,
* [schema:description](https://schema.org/description) should be text describing your repository,
* [schema:sameAs](https://schema.org/sameAs) can be used to link the repository to other URLs such as Re3Data, Twitter, LinkedIn, etc.,
* [schema:category](https://schema.org/category) can be used to describe the discipline, domain, area of study that encompasses the repository's holdings.


<pre>
{
  "@context": "https://schema.org/",
  "@type": ["Service", "ResearchProject"],
  "legalName": "Sample Data Repository Office",
  "name": "SDRO",
  <strong>"url": "https://www.sample-data-repository.org",
  "description": "The Sample Data Repository Service provides access to data from an imaginary domain accessible from this website.",
  "sameAs": [
        "http://www.re3data.org/repository/r3d1000000xx",
        "https://twitter.com/SDRO",
        "https://www.linkedin.com/company/123456789/"
    ],
  "category": [
    "Biological Oceanography",
    "Chemical Oceanography"
  ]</strong>
}
</pre>

(See [advanced publishing techniques](#advanced-publishing) for how to [describe categories/disciplines in more detail](#advanced-publishing-category) than just simple text.)

If you are using the "@id" attribute for your Repository, and the provider of the repository's services is the same Organziation, you can specify the [schema:provider](https://schema.org/provider)  of the [schema:Service](https://schema.org/Service) in this way:
<pre>
{
  "@context": "https://schema.org/",
  "@type": ["Service", "ResearchProject"],
  <strong>"@id": "https://www.sample-data-repository.org",</strong>
  "legalName": "Sample Data Repository Office",
  "name": "SDRO",
  "url": "https://www.sample-data-repository.org",
  "description": "The Sample Data Repository Service provides access to data from an imaginary domain accessible from this website.",
  "category": [
    "Biological Oceanography",
    "Chemical Oceanography"
  ],
  <strong>"provider": {
    "@id": "https://www.sample-data-repository.org"
  }</strong>
}
</pre>

However, if your repository has a situation where multiple organizations act as the provider or you want to recognize a different organization as the provider of the repository's service, [schema:provider](https://schema.org/provider) can be used in this way:

<pre>
{
  "@context": "https://schema.org/",
  "@type": ["Service", "ResearchProject"],
  "legalName": "Sample Data Repository Office",
  "name": "SDRO",
  "url": "https://www.sample-data-repository.org",
  "description": "The Sample Data Repository Service provides access to data from an imaginary domain accessible from this website.",
  "category": [
    "Biological Oceanography",
    "Chemical Oceanography"
  ],
  <strong>"provider": [
    {
      "@type": "ResearchProject",
      "name": "SDRO Technical Office",
      "description": "We provide all the infrastructure for the SDRO"
      ...
    },
    {
      "@type": "ResearchProject",
      "name": "SDRO Science Support Office",
      "description": "We provide all the science support functionality for the SDRO"
      ...
    }
  ]</strong>
}
</pre>

Adding additional fields of [schema:ResearchProject](https://schema.org/ResearchProject):

<pre>
{
  "@context": "https://schema.org/",
  "@type": ["Service", "ResearchProject"],
  "legalName": "Sample Data Repository Office",
  "name": "SDRO",
  "url": "https://www.sample-data-repository.org",
  "description": "The Sample Data Repository Service provides access to data from an imaginary domain accessible from this website.",
  "category": [
    "Biological Oceanography",
    "Chemical Oceanography"
  ],
  "provider": {
    "@id": "https://www.sample-data-repository.org"
  }
  <strong>"logo": {
    "@type": "ImageObject",
    "url": "https://www.sample-data-repository.org/images/logo.jpg"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "name": "Support",
    "email": "info@bco-dmo.org",
    "url": "https://www.sample-data-repository.org/about-us",
    "contactType": "customer support"
  },
  "foundingDate": "2006-09-01",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main St.",
    "addressLocality": "Anytown",
    "addressRegion": "ST",
    "postalCode": "12345",
    "addressCountry": "USA"
  }</strong>
}
</pre>

If this ResearchProject, or Organization, has a parent entity such as a college, university or research center, that information can be provided using the [schema:parentOrganization](https://schema.org/parentOrganization) property:

<pre>
{
  "@context": "https://schema.org/",
  "@type": ["Service", "ResearchProject"],
  "legalName": "Sample Data Repository Office",
  "name": "SDRO",
  "url": "https://www.sample-data-repository.org",
  "description": "The Sample Data Repository Service provides access to data from an imaginary domain accessible from this website.",
  "category": [
    "Biological Oceanography",
    "Chemical Oceanography"
  ],
  "provider": {
    "@id": "https://www.sample-data-repository.org"
  },
   <strong>"parentOrganization": {
     "@type": "Organization",
     "@id": "http://www.someinstitute.edu",
     "legalName": "Some Institute",
     "name": "SI",
     "url": "http://www.someinstitute.edu",
     "address": {
       "@type": "PostalAddress",
       "streetAddress": "234 Main St.",
       "addressLocality": "Anytown",
       "addressRegion": "ST",
       "postalCode": "12345",
       "addressCountry": "USA"
     }
   }</strong>
  }
}
</pre>

Back to [top](#top)

<a id="identifier"></a>
### Describing a Repository's Identifier

[![Repository - Identifier](/assets/diagrams/repository/repository_identifier.svg "Repository - Identifier")](#)

Some organizations may have a persistent identifier (DOI) assigned to their organization from authorities like the Registry of Research Data Repositories (re3data.org). The way to describe these organizational identifiers is to use the [schema:identifier](https://schema.org/identifier) property in this way:

<pre>
{
  "@context": "https://schema.org/",
  "@type": ["Service", "ResearchProject"],
  "legalName": "Sample Data Repository Office",
  "name": "SDRO",
  "url": "https://www.sample-data-repository.org",
  "description": "The Sample Data Repository Service provides access to data from an imaginary domain accessible from this website.",
  "category": [
    "Biological Oceanography",
    "Chemical Oceanography"
  ],
  "provider": {
    "@id": "https://www.sample-data-repository.org"
  },
  <strong>"identifier": {
    "@type": "PropertyValue",
    "name": "Re3data DOI: 10.17616/R37P4C",
    "propertyID": "https://registry.identifiers.org/registry/doi",
    "value": "doi:10.17616/R37P4C",
    "url": "https://doi.org/10.17616/R37P4C"
  }</strong>
}
</pre>

For more information on describing identifiers, see the [Dataset - Identifier guide](/guides/Dataset.md#identifier).

<a id="funding-source"></a>
### Describing a Repository's Funding Source

[![Repository - Funding](/assets/diagrams/repository/repository_funding.svg "Repository - Funding")](#)


To describe the funding source of a repository, you use the [schema:funder](https://schema.org/funder) property of [schema:Organization](https://schema.org/Organization):

<pre>
{
  "@context": "https://schema.org/",
  "@type": ["Service", "ResearchProject"],
  "legalName": "Sample Data Repository Office",
  "name": "SDRO",
  "url": "https://www.sample-data-repository.org",
  "description": "The Sample Data Repository Service provides access to data from an imaginary domain accessible from this website.",
  "category": [
    "Biological Oceanography",
    "Chemical Oceanography"
  ],
  "provider": {
    "@id": "https://www.sample-data-repository.org"
  },
   "parentOrganization": {
     "@type": "Organization",
     "@id": "http://www.someinstitute.edu",
     "legalName": "Some Institute",
     "name": "SI",
     "url": "http://www.someinstitute.edu",
     "address": {
       "@type": "PostalAddress",
       "streetAddress": "234 Main St.",
       "addressLocality": "Anytown",
       "addressRegion": "ST",
       "postalCode": "12345",
       "addressCountry": "USA"
     },
     <strong>"funder": {
      "@type": "Organization",
      "@id": "https://doi.org/10.13039/100000141",
      "legalName": "Division of Ocean Sciences",
      "alternateName": "OCE",
      "url": "https://www.nsf.gov/div/index.jsp?div=OCE",
      "identifier": {
        "@type": "PropertyValue",
        "propertyID": "https://registry.identifiers.org/registry/doi",
        "value": "doi:10.13039/100000141",
        "url": "https://doi.org/10.13039/100000141"
      },
      "parentOrganization": {
        "@type": "Organization",
        "@id": "http://doi.org/10.13039/100000085",
        "legalName": "Directorate for Geosciences",
        "alternateName": "NSF-GEO",
        "url": "http://www.nsf.gov",
        "identifier": {
          "@type": "PropertyValue",
          "propertyID": "https://registry.identifiers.org/registry/doi",
          "value": "doi:10.13039/100000085",
          "url": "https://doi.org/10.13039/100000085"
         },
        "parentOrganization": {
          "@type": "Organization",
          "@id": "http://dx.doi.org/10.13039/100000001",
          "legalName": "National Science Foundation",
          "alternateName": "NSF",
          "url": "http://www.nsf.gov",
          "identifier": {
            "@type": "PropertyValue",
            "propertyID": "https://registry.identifiers.org/registry/doi",
            "value": "doi:10.13039/100000001",
            "url": "https://doi.org/10.13039/100000001"
          }
        }
      }</strong>
    }
  }
}
</pre>

Back to [top](#top)

<a id="services"></a>
### Describing a Repository's Services

[![Repository - Services](/assets/diagrams/repository/repository_services.svg "Repository - Services")](#)


For repositories might offer services for accessing data as opposed to directly accessing data files. The [schema:Service](https://schema.org/Service) allows us to describe these services as well as repository searches, data submission services, and syndication services. In this first example, we describe a search service at the repository using [schema:ServiceChannel](https://schema.org/ServiceChannel).

<pre>
{
  "@context": "https://schema.org/",
  "@type": ["Service", "ResearchProject"],
  "legalName": "Sample Data Repository Office",
  "name": "SDRO",
  "url": "https://www.sample-data-repository.org",
  ...
  <strong>"availableChannel": [
    {
      "@type": "ServiceChannel",
      "serviceUrl": "https://www.sample-data-repository.org/search",
      "providesService": {
        "@type": "Service",
        "name": "SDRO Website Search",
        "description": "Search for webpages, datasets, authors, funding awards, instrumentation and measurements",
        "potentialAction": {
          "@type": "SearchAction",
          "target": "https://www.sample-data-repository.org/search?keywords={query_string}",
          "query-input": {
            "@type": "PropertyValueSpecification",
            "valueRequired": true,
            "valueName": "query_string"
          }
        }
      }
    }</strong>
  ]
}
</pre>

By specifying the [schema:potentialAction](https://schema.org/potentialAction), we create a machine-actionable way to execute searches.

Back to [top](#top)

<a id="data-collections"></a>
### Describing a Repository's Data Collections

If your repository has a concept of a data collection, some grouping of a number of datasets, we can use the [schema:DataCatalog](https://schema.org/DataCatalog) to describe these collections using the [schema:OfferCatalog](https://schema.org/OfferCatalog). One exampel of a DataCatalog might be to group datasets by a categorization such as 'biological data' or 'chemical data'. Or a catalog could be grouped by instrument, parameter or whatever logical grouping a repository may have.

[![Repository - Offer Catalog](/assets/diagrams/repository/repository_offer-catalog.svg "Repository - Offer Catalog")](#)

<pre>
{
  "@context": "https://schema.org/",
  "@type": ["Service", "ResearchProject"],
  "legalName": "Sample Data Repository Office",
  "name": "SDRO",
  "url": "https://www.sample-data-repository.org",
  ...
  <strong>"hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Sample Data Repository Resource Catalog",
    "itemListElement": [
      {
       "@type": "DataCatalog",
        "@id": "https://www.sample-data-repository.org/collection/biological-data",
        "name": "Biological Data",
        "audience": {
          "@type": "Audience",
          "audienceType": "public",
          "name": "General Public"
        }
      },
      {
        "@type": "DataCatalog",
        "@id": "https://www.sample-data-repository.org/collection/geological-data",
        "name": "Geological Data",
        "audience": {
          "@type": "Audience",
          "audienceType": "public",
          "name": "General Public"
        }
      }
    ]
  }</strong>
}
</pre>

Back to [top](#top)

<a id="advanced-publishing"></a>
### Advanced Publishing Techniques

<a id="advanced-publishing-category"></a>
#### How to publish resources for the categories/disciplines at repository services.
#### & How to use external vocabularies

The SWEET ontology defines a number of science disciplines and a repository could reference those, or another vocabuary's resources, by adding the vocabular to the `@context` attribute of the JSON-LD markup.

<pre>
{
  "@context": [
    "https://schema.org/",
    {
      <strong>"sweet-rel": "http://sweetontology.net/rela/",
      "sweet-kd": "http://sweetontology.net/humanKnowledgeDomain/"</strong>
    }
  ],
  "@type": ["Service", "ResearchProject"],
  "legalName": "Sample Data Repository Office",
  "name": "SDRO",
  "url": "https://www.sample-data-repository.org",
  "description": "The Sample Data Repository Service provides access to data from an imaginary domain accessible from this website.",
  <strong>"sweet-rel:hasRealm": [
    { "@id": "sweet-kd:Biogeochemistry" },
    { "@id": "sweet-kd:Oceanography" }
  ]
  </strong>
}
</pre>

Back to [top](#top)
