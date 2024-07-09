<a id="top"></a>
[Home](/README.md) | Observing Network

# Describing an Observing Network

An [ObservingNetwork](.) is a collection of ... provide definition here...

To describe an ObservingNetwork in schema.org, we will model it with the schema.org type [schema:ResearchOrganization](https://schema.org/ResearchOrganization), as shown below in [Identifying Properties](#identifying-properties).

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Describing an Observing Network](#describing-an-observing-network)
    - [Identifying Properties](#identifying-properties)
    - [Identifer](#roles-of-people)
    - [Roles of People](#roles-of-people)
    - [Publisher and Provider](#publisher-and-provider)
    - [Funding](#funding)

<!-- /TOC -->

## Identifying Properties

Core identifying properties about an observing network include common properties for all schema.org resource types, including the name, description, and identifier for the Observing Network.

- [name](https://schema.org/name) - A descriptive name of the observing network (e.g., “Snow depth in Northern Hemisphere”)
- [description](https://schema.org/description) - A short abstract describing the observing network.
- [identifier](https://schema.org/identifier) - An identifier for the observing network, such as a DOI. (text, URL, or PropertyValue).

<pre>
{
  "@context": "https://schema.org/",
  "@type": "ResearchOrganization",
  <strong>"name": "Example Observing Network",
  "description": "Description of an example observing network."</strong>
}
</pre>

The following additional basic fields make up a core description of an ObservingNetwork.

* [url](https://schema.org/url) - Location of a page describing the dataset.
* [sameAs](https://schema.org/sameAs) - Other URLs that can be used to access the dataset page. A link to a page that provides more information about the same dataset, usually in a different repository.
* [keywords](https://schema.org/keywords) - Keywords summarizing the dataset.

![Basic Fields](/assets/diagrams/dataset/dataset_basic-fields.png "Dataset - Basic Fields")

<pre>
{
  "@context": "https://schema.org/",
  "@type": "ResearchOrganization",
  "name": "Example Observing Network",
  "description": "Description of an example observing network.",
  <strong>"url": "https://example.org/obsnetworks/12345",
  "sameAs": "https://networks.org/network/12345",
  "keywords": ["ocean observing", "carbon dioxide"]
  </strong>
}
</pre>
Back to [top](#top)


## Identifier

Adding the [schema:identifier](https://schema.org/identifier) field can be done in three ways - a text description, a URL, or by using the [schema:PropertyValue](https://schema.org/PropertyValue) field.

Back to [top](#top)


### Roles of People

Back to [top](#top)

### Publisher and Provider

Back to [top](#top)


### Funding

Back to [top](#top)
