<a id="top"></a>
![version v0.1.0](https://img.shields.io/badge/documentation-v0.1.0-blue.svg)

* [Basic Fields](#basic-fields)
* [Funding Source](#funding-source)
* [Types of Resources](#resource-types)
* [Identifier](#identifier)
* [Services](#services)
* [Data Collections](#data-collections)

## Describing a Repository

[![Repository  - Overview](/assets/diagrams/repository/repository-overview.svg "Repository - Overview")](#)

In schema.org, we model a repository as both an [schema:Organization](https://schema.org/Organization) and a [schema:Service](https://schema.org/Service). This double-typing gives us the most flexibility in describing the characteristics of the organization providing the service and the services offered by the organization. 

<pre>
{
  "@context": {
    "@vocab": "http://schema.org/"
  },
  <strong>"@type": ["Service", "Organization"],
  "legalName": "Sample Data Repository Office",
  "name": "SDRO"
  </strong>
}
</pre>

<a id="basic-fields"></a>
The other fields you can use to describe the Organziation and the Service are:


* [schema:legalName](https://schema.org/legalName) should be the official name of the  repository,
* [schema:name](https://schema.org/name) can be an acronym or the name typcially used for the repository,
* [schema:url](https://schema.org/url) should be the url of your repository's homepage,
* [schema:description](https://schema.org/description) should be text describing your repository,
* [schema:sameAs](https://schema.org/sameAs) can be used to link the repository to other URLs such as Re3Data, Twitter, LinkedIn, etc.,
* [schema:category](https://schema.org/category) can be used to describe the discipline, domain, area of study that encompasses the repository's holdings.

<pre>
{
  "@context": {
    "@vocab": "http://schema.org/",
    "gdx": "https://geodex.org/voc/"
  },
  "@type": ["Service", "Organization"],
  "additionalType": "https://geodex.org/voc/ResearchRepositoryService",
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

If you are using the "@id" attribute for your Repository, you can specify the [schema:provider](https://schema.org/provider)  of the [schema:Service](https://schema.org/Service) in this way:
<pre>
{
  "@context": {
    "@vocab": "http://schema.org/",
    "gdx": "https://geodex.org/voc/"
  },
  "@type": ["Service", "Organization"],
  <strong>"@id": "https://www.sample-data-repository.org",</strong>
  "additionalType": "https://geodex.org/voc/ResearchRepositoryService",
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
  "@context": {
    "@vocab": "http://schema.org/",
    "gdx": "https://geodex.org/voc/"
  },
  "@type": ["Service", "Organization"],
  "additionalType": "https://geodex.org/voc/ResearchRepositoryService",
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
      "@type": "Organization",
      "name": "SDRO Technical Office",
      "description": "We provide all the infrastructure for the SDRO"
      ...
    },
    {
      "@type": "Organization",
      "name": "SDRO Science Support Office",
      "description": "We provide all the science support functionality for the SDRO"
      ...
    }
  ]</strong>
}
</pre>

Adding additional fields of [schema:Organization](https://schema.org/Organization):

<pre>
{
  "@context": {
    "@vocab": "http://schema.org/",
    "gdx": "https://geodex.org/voc/"
  },
  "@type": ["Service", "Organization"],
  "additionalType": "https://geodex.org/voc/ResearchRepositoryService",
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

If this Organization has a parent entity such as a college, university or research center, that information can be provided using the [schema:parentOrganization](https://schema.org/parentOrganization) property:

<pre>
{
  "@context": {
    "@vocab": "http://schema.org/",
    "gdx": "https://geodex.org/voc/"
  },
  "@type": ["Service", "Organization"],
  "additionalType": "https://geodex.org/voc/ResearchRepositoryService",
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

<a id="funding-source"></a>
### Describing a Repository's Funding Source

To describe the funding source of a repository, you use the [schema:funder](https://schema.org/funder) property of [schema:Organization](https://schema.org/Organization):

<pre>
{
  "@context": {
    "@vocab": "http://schema.org/",
    "gdx": "https://geodex.org/voc/"
  },
  "@type": ["Service", "Organization"],
  "additionalType": "https://geodex.org/voc/ResearchRepositoryService",
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
      "@id": "https://dx.doi.org/10.13039/100000141",
      "legalName": "Division of Ocean Sciences",
      "alternateName": "OCE",
      "url": "https://www.nsf.gov/div/index.jsp?div=OCE",
      "identifier": {
        "@type": "PropertyValue",
        "propertyID": "http://purl.org/spar/datacite/doi",
        "value": "10.13039/100000141",
        "url": "https://doi.org/10.13039/100000141"
      },
      "parentOrganization": {
        "@type": "Organization",
        "@id": "http://dx.doi.org/10.13039/100000085",
        "legalName": "Directorate for Geosciences",
        "alternateName": "NSF-GEO",
        "url": "http://www.nsf.gov",
        "identifier": {
          "@type": "PropertyValue",
          "propertyID": "http://purl.org/spar/datacite/doi",
          "value": "10.13039/100000085",
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
            "propertyID": "http://purl.org/spar/datacite/doi",
            "value": "10.13039/100000001",
            "url": "https://doi.org/10.13039/100000001"
          }
        }
      }</strong>
    }
  }
}
</pre>

<a id="identifier"></a>
### Describing a Repository's Identifier

Some organizations may have a persistent identifier (DOI) assigned to their organization from authorities like the Registry of Research Data Repositories (re3data.org). The way to describe these organizational identifiers is to use the [schema:identifier](https://schema.org/identifier) property in this way:

<pre>
{
  "@context": {
    "@vocab": "http://schema.org/",
    "gdx": "https://geodex.org/voc/",
    <strong>"datacite": "http://purl.org/spar/datacite/"</strong>
  },
  "@type": ["Service", "Organization"],
  "additionalType": "https://geodex.org/voc/ResearchRepositoryService",
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
    "name": "Re3data DOI for this repository",
    "propertyID": "http://purl.org/spar/datacite/doi",
    "value": "10.17616/R37P4C",
    "url": "http://doi.org/10.17616/R37P4C"
  }</strong>
}
</pre>

We add the `datacite` vocabulary to the `@context` because the Datacite Ontology available at [http://purl.org/spar/datacite/](http://purl.org/spar/datacite/) has URIs to describe a DOI, ORCiD, ARK, URI, URN - all identifier scheme that help for disamiguating identifiers. To properly disambiguate a globally unique identifier, 2 pieces of information are needed - 1) the identifier value and 2) the scheme that on which that identifier exists. Some examples of this concept for common identifiers  are:

| Scheme | Value |
| ------ | ----- |
| DOI    | 10.17616/R37P4C |
| ORCiD  | 0000-0002-6059-4651 |

When describing PIDs, it's important to include both of these pieces for downstream activities like searching and linking resources. FOor example, a user may want to query for all repositories with a DOI identifier or all Datasets authored by a researcher with an ORCiD. These types of filters become more difficult when only the URL to these identifiers are provided. The reason here is that there are multiple URLs for an persistent identifier. On example is the DOI:

* http://doi.org/10.17616/R37P4C
* https://doi.org/10.17616/R37P4C
* http://dx.doi.org/10.17616/R37P4C
* https://dx.doi.org/10.17616/R37P4C

So, the best practice is to provide the scheme and value for an identifier, but you can also provide a URL representation using the [schema:url](https://schema.org/url) property.

Back to [top](#top)


<a id="resource-types"></a>
### Describing a Repository's Types of Resources

[![Research Repository Service - Types of Resources](html/voc/static/schema/diagrams/repository-resource-types.png "Research Repository Service - Types of Resources")](#)

To describe the types of research resources a repository curates, we use the [schema:OfferCatalog](https://schema.org/OfferCatalog). With an extension of gdx:ResearchResourceTypes, we define that the OfferCatalog will be a list of types that are dervied from [schema:CreativeWork](https://schema.org/CreativeWork).

<pre>
{
  "@context": {
    "@vocab": "http://schema.org/",
    "gdx": "https://geodex.org/voc/",
    "datacite": "http://purl.org/spar/datacite/",
    <strong>"geolink": "http://schema.geolink.org/1.0/base/main#",
    "schema": "http://schema.org/"</strong>
  },
  "@type": ["Service", "Organization"],
  "additionalType": "https://geodex.org/voc/ResearchRepositoryService",
  "legalName": "Sample Data Repository Office",
  "name": "SDRO",
  "url": "https://www.sample-data-repository.org",
  ...
  <strong>"hasOfferCatalog":{
    "@type": "OfferCatalog",
    "additionalType": "https://geodex.org/voc/ResearchResourceTypes",
    "itemListElement": [
      {"@type": "Thing", "@id": "schema:Dataset", "name": "Dataset"},
      {"@type": "Thing", "@id": "geolink:PhysicalSample", "name": "Physical Sample" }
    ]
  }</strong>
}
</pre>

Notice, that we use `@id` to describe the type of resource. To reference schema.org classes using `@id` properly, we must add schema.org to the `@context` with a prefix name. Here, we chose `schema:` in the `@context`, thus we use `schema:Dataset` to say that our repository curates resource types of [schema.org/Dataset](https://schema.org/Dataset).

Because schema.org does not have a class for a Physical Sample yet, we use teh calss definition from the [EarthCube GeoLink vocabulary](http://schema.geolink.org) to specify that this repository curates physical samples. We add `geolink:` to the `@context` section, and then specify `geolink:PhysicalSample` as another `@id` offered by this repository.

<a id="services"></a>
### Describing a Repository's Services

[![Research Repository Service - Service Channel](html/voc/static/schema/diagrams/repository-servicechannel.png "Research Repository Service - Service Channel")](#)

For repositories might offer services for accessing data as opposed to directly accessing data files. The [schema:Service](https://schema.org/Service) allows us to describe these services as well as repository searches, data submission services, and syndication services. In this first example, we describe a search service at the repository using [schema:ServiceChannel](https://schema.org/ServiceChannel).

<pre>
{
  "@context": {
    "@vocab": "http://schema.org/",
    "gdx": "https://geodex.org/voc/",
    "datacite": "http://purl.org/spar/datacite/"
  },
  "@type": ["Service", "Organization"],
  "additionalType": "https://geodex.org/voc/ResearchRepositoryService",
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
        "additionalType": "https://geodex.org/voc/SearchService",
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
    }</strong>,
    {
       "@type": "ServiceChannel",
       "serviceUrl": "https://www.sample-data-repository.org/sitemap.xml",
       "providesService": {
         "@type": "Service",
         "additionalType": "https://geodex.org/voc/SyndicationService",
         "name": "Sitemap XML",
         "description": "A Sitemap XML providing access to all of the resources for harvesting",
         "potentialAction": {
           "@type": "ConsumeAction",
           "target": {
             "@type": "EntryPoint",
             "additionalType": "https://geodex.org/voc/SitemapXML",
             "urlTemplate": "https://www.sample-data-repository.org/sitemap.xml?page={page}"
           },
           "object": {
             "@type": "DigitalDocument",
             "url": "https://www.sample-data-repository.org/sitemap.xml",
             "fileFormat": "application/xml"
           }
         }
       }
     }
  ]
}
</pre>

By specifying the [schema:potentialAction(https://schema.org/potentialAction), we create a machine-actionable way to execute searches. This means that an EarthCube Registry could take a user submitted query, and pass it along to the repository for the EarthCube Registry user.

If your repository does have datasets or other resources with schema.org JSON-LD markup on their landing pages, Google recommends that all URLs be put inside a sitemap.xml file. To create a sitemap.xml, [go here](https://www.google.com/schemas/sitemap/0.84/). To describe your sitemap.xml, add a [schema:ServiceChannel](https://schema.org/ServiceChannel) similar to the following markup:

<pre>
{
  "@context": {
    "@vocab": "http://schema.org/",
    "gdx": "https://geodex.org/voc/",
    "datacite": "http://purl.org/spar/datacite/"
  },
  "@type": ["Service", "Organization"],
  "additionalType": "https://geodex.org/voc/ResearchRepositoryService",
  "legalName": "Sample Data Repository Office",
  "name": "SDRO",
  "url": "https://www.sample-data-repository.org",
  ...
  "availableChannel": [
    {
      "@type": "ServiceChannel",
      "serviceUrl": "https://www.sample-data-repository.org/search",
      "providesService": {
        "@type": "Service",
        "additionalType": "https://geodex.org/voc/SearchService",
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
    },
    <strong>{
       "@type": "ServiceChannel",
       "serviceUrl": "https://www.sample-data-repository.org/sitemap.xml",
       "providesService": {
         "@type": "Service",
         "additionalType": "https://geodex.org/voc/SyndicationService",
         "name": "Sitemap XML",
         "description": "A Sitemap XML providing access to all of the resources for harvesting",
         "potentialAction": {
           "@type": "ConsumeAction",
           "target": {
             "@type": "EntryPoint",
             "additionalType": "https://geodex.org/voc/SitemapXML",
             "urlTemplate": "https://www.sample-data-repository.org/sitemap.xml?page={page}"
           },
           "object": {
             "@type": "DigitalDocument",
             "url": "https://www.sample-data-repository.org/sitemap.xml",
             "fileFormat": "application/xml"
           }
         }
       }
     }</strong>
  ]
}
</pre>

Back to [top](#top)

<a id="data-collections"></a>
### Describing a Repository's Data Collections

If your repository has a concept of a data collection, some grouping of a number of datasets, we can use the [schema:DataCatalog](https://schema.org/DataCatalog) to describe these collections using the [schema:OfferCatalog](https://schema.org/OfferCatalog). One exampel of a DataCatalog might be to group datasets by a categorization such as 'biological data' or 'chemical data'. Or a catalog could be grouped by instrument, parameter or whatever logical grouping a repository may have.

[![Research Repository Service - Offer Catalog](html/voc/static/schema/diagrams/repository-offerCatalog.png "Research Repository Service - Offer Catalog")](#)

<pre>
{
  "@context": {
    "@vocab": "http://schema.org/",
    "gdx": "https://geodex.org/voc/",
    "datacite": "http://purl.org/spar/datacite/"
  },
  "@type": ["Service", "Organization"],
 "additionalType": "https://geodex.org/voc/ResearchRepositoryService",
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
