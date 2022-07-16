##### Adding ORCiDs to People

- Re-use the [Identifier pattern](03_identifiers.md) from Section #3
- Identifiers.org defines ORCiD: `https://registry.identifiers.org/registry/orcid`
- 
<pre>
{
  "@context": "https://schema.org/",
  "creator": {
    "@list":[
      {
        "@type": "Person",
        "name": "Alyson E. Santoro",
        <strong>"identifier": {
          "@id": "https://orcid.org/0000-0003-2503-8219",
          "@type": "PropertyValue",
          "propertyID": "https://registry.identifiers.org/registry/orcid",
          "url": "https://orcid.org/0000-0003-2503-8219",
          "value": "orcid:0000-0003-2503-8219"
        }</strong>
      },
      {
        "@type": "Person",
        "name": "Sarah Marie Laperriere",
        <strong>"identifier": {
          "@id": "https://orcid.org/0000-0003-4691-8741",
          "@type": "PropertyValue",
          "propertyID": "https://registry.identifiers.org/registry/orcid",
          "url": "https://orcid.org/0000-0003-4691-8741",
          "value": "orcid:0000-0003-4691-8741"
        }</strong>
      }
    ]
  },
  "contributor": {
    "@list":[
      {
        "@type": "Person",
        "name": "Makoto Saito",
        <strong>"identifier": {
          "@id": "https://orcid.org/0000-0001-6040-9295",
          "@type": "PropertyValue",
          "propertyID": "https://registry.identifiers.org/registry/orcid",
          "url": "https://orcid.org/0000-0001-6040-9295",
          "value": "orcid:0000-0001-6040-9295"
        }</strong>
      }
    ]
  }
}
</pre>

##### Breaking down people names

<pre>
{
  "@context": "https://schema.org/",
  "creator": {
    "@list":[
      {
        "@type": "Person",
        "name": "Alyson E. Santoro",
        <strong>"givenName": "Alyson",
        "familyName": "Santoro",</strong>
      }
    ]
  }
}
</pre>
