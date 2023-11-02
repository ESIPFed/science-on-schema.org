# ESIP Summer Meeting 2022

THIS TUTORIAL: [bit.ly/soso-tutorial](https://bit.ly/soso-tutorial)

**Tutorial**
- Uses source metadata: ProteOMZ nitrous oxide data from BCO-DMO at [examples/dataset-01.txt](examples/dataset-01.txt)
- Each section has a lesson or exercise about Schema.org or JSON-LD
- At the end of every section will be an updated schema.org record for our source metadata
- _NOTE: some code snippets are shortened for brevity, but each section's updated markup is valid_
- Any suggestions about this tutorial would be greatly appreciated here: [Github Issue 226](https://github.com/ESIPFed/science-on-schema.org/issues/226)

**Tools**: 
- [ESIP Summer Meeting - Session Notes](https://docs.google.com/document/d/1SAuEXBMMQIzdntvlmJ_p4E609sGys21jpCUUfeoxs_M/edit) (Google doc)
    - [Sched Session Page](https://sched.co/12et4)
- [Google Rich Results Tool](https://search.google.com/test/rich-results) - use to test your markup 
- [Schema Builder Chrome browser Extension](https://chrome.google.com/webstore/detail/schema-builder-for-struct/klohjdodjjeocpbpadmkcndjoadijgjg?hl=en-US) - use to build markup for an existing Dataset page
    - go to Dataset page, and click the extension, begin building your schema.org

## Agenda

- **Intro to Schema.org**
    - What is Schema.org?
        - ESIP Soil Cluster Presentation ([slides](https://bit.ly/soso-soil-prezi) | [youtube](https://www.youtube.com/watch?v=s0TzXWGsf34))
    - [Science-on-schema.org ESIP Cluster]([https://science-on-schema.org](https://github.com/ESIPFed/science-on-schema.org//#community))
        - v1.3 Guidelines in May 2022 ([release notes](https://github.com/ESIPFed/science-on-schema.org/releases/tag/1.3.0)) 
            - Thank you to the Cluster members, but special thanks to Matt Jones, Stephen Richard, Nick Jarboe, Dave Vieglais, Douglas Fils, Ruth Duerr, Chantelle Verhey, & Melinda Minch
        - _ESIP Assembly Endorsement_
- **Build a Dataset** (it's not complicated)
    - #1. [JSON-LD Context](01_json-ld-context-type.md)
    - #2. [Basic Fields](02_basic-fields.md)
    - #3. [Keywords](03_keywords.md)
    - #4. [License](04_license.md)
    - #5. [Identifiers](05_identifier.md)
        - [using `sameAs`](05_identifier.md#sameas)
    - #6. [Publisher](06_publisher.md)
    - #7. [Authors / Contributors](07_author-contributor.md)
    - #8. [Temporal Coverage](08_temporal.md)
    - #9. [Spatial Coverage](09_spatial.md)
    - #10. [Data Files](10_data-files.md)
- **Improving the Dataset**
    - #11. [Keywords](11_keywords-vocabulary.md)
    - #12. [Identifiers](12_identifiers-propertyvalue.md)
    - #13. [Authors / Contributors Improved](13_author-contributor.md)
    - #14. [Provider](14_provider.md)
    - #15. [Funding & Awards](15_funding-awards.md)
    - #16. [Variables](16_variables.md)
    - #17. [Metadata Records](17_metadata-records.md)
    - #18. [Checksums](18_checksums.md)
- **Advanced Techniques**
    - [Geologic Time](/guides/Dataset.md#geologic-time)
    - [Provenance](/guides/Dataset.md#provenance-relationships)
    - [Validating with SHACL](validation.md) 
          
