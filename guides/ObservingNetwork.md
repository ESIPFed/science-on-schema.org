<a id="top"></a>
[Home](/README.md) | Observing Network

# Describing an Observing Network

An [ObservingNetwork](.) is a collection of observing-related infrastructures and activities – such as monitoring sites,
mobile platforms, research projects, field campaigns, and observing programs – that are deployed in
a diverse and distributed fashion across numerous temporal and spatial scales. Dozens of
agencies, organizations, projects, and initiatives observe or monitor earth, environmental, and human systems – 
each with its own geographic extent, thematic scope,
governance, or funding.

This guide documents a common convention to document an [ObservingNetwork](.) using schema.org vocabulary terms in a consistent way, thereby enabling the creation of information resources about observing netowrks. these information resources wil be useful for many groups, including:

- science planners to assess status, overlap, and gaps of observations
- network managers to co-locate or optimize limited resources
- community members to leverage observational efforts and data collected nearby
- data repositories, to link [Dataset](https://schema.org/Dataset) entries to the observing networks that egnerated them

To describe an ObservingNetwork in schema.org, we will model it with an existing schema.org type [schema:ResearchOrganization](https://schema.org/ResearchOrganization), with properties as shown below in [Identifying Properties](#identifying-properties). We also considered modeling an ObservingNetwork as type [schema:ResearchProject](https://schema.org/ResearchProject), which would be more transient than an organization.

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

![Basic Fields](/assets/diagrams/observingnetwork/obs-net-basic.png "Observing Network - Basic Fields")

<pre>
{
  "@context": "https://schema.org/",
  "@type": "ResearchOrganization",
  <strong>"name": "Polardex Interactive Polar Infrastructure Database",
  "description": "Polardex is a tool for polar scientists and planners. The platform lists key polar infrastructures in both the Arctic and the Antarctic, enabling logistics discovery and enhanced planning opportunities. Polardex has been developed by the EPB through the EPB's Action Group on Infrastructure, in close cooperation in close collaboration with, and data provision by, SOOS, SIOS, INTERACT, IAATO, EU-PolarNet 2, COMNAP, Isaaffik, ARICE, EUROFLEETS, AWI and BAS. The Polardex platform was developed by Blue Lobster IT Ltd.",
  "identifier": "https://polarobservingregistry.org/network/56wdygWLLgW7DOjkCpO790"</strong>
}
</pre>

The following additional basic fields make up a core description of an ObservingNetwork.

* [url](https://schema.org/url) - Location of a web page describing the observing network.
* [sameAs](https://schema.org/sameAs) - Other URLs that can be used to refer to the network.
* [keywords](https://schema.org/keywords) - Keywords summarizing the observing network.

<pre>
{
  "@context": "https://schema.org/",
  "@type": "ResearchOrganization",
  "name": "Polardex Interactive Polar Infrastructure Database",
  "description": "Polardex is a tool for polar scientists and planners. The platform lists key polar infrastructures in both the Arctic and the Antarctic, enabling logistics discovery and enhanced planning opportunities. Polardex has been developed by the EPB through the EPB's Action Group on Infrastructure, in close cooperation in close collaboration with, and data provision by, SOOS, SIOS, INTERACT, IAATO, EU-PolarNet 2, COMNAP, Isaaffik, ARICE, EUROFLEETS, AWI and BAS. The Polardex platform was developed by Blue Lobster IT Ltd.",
  "identifier": "https://polarobservingregistry.org/network/56wdygWLLgW7DOjkCpO790",
  <strong>"url": "https://polardex.org/",
  "sameAs": "https://www.soos.aq/activities/duesouth"</strong>
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
