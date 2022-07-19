# On Validation

Reference overview

| References                                                | On-Line Tools                                                   | CLI                                          | Browser Extension                                                                                                                                           | Software                                            |
|-----------------------------------------------------------|-----------------------------------------------------------------|----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| [W3C SHACL](https://www.w3.org/TR/shacl/)                 | [SHACL Playground](https://shacl.org/playground/)               | [pySHACL](https://github.com/RDFLib/pySHACL) | [Schema Builder for Structured Data](https://chrome.google.com/webstore/detail/schema-builder-for-struct/klohjdodjjeocpbpadmkcndjoadijgjg?hl=en-US)         | [Corese SHACL](http://wimmics.inria.fr/corese)      |
| [Editors Draft](https://w3c.github.io/data-shapes/shacl/) | [SHACL Playground zazuko](https://shacl-playground.zazuko.com/) |                                              | [Validate Schema in Schema Markup Validator](https://chrome.google.com/webstore/detail/validate-schema-in-schema/bambpgngabopanfbbpkknnogpomkaipp?hl=en-US) | [dotNetRDF](https://github.com/dotnetrdf/dotnetrdf) |
|                                                           | [Tangram](https://tangram.gleaner.io)                           |                                              | [Science on Schema.org](https://chrome.google.com/webstore/detail/science-on-schemaorg/blpbacopppjgpoedkiglokdheiegajpn?hl=en-US)                           | [Netage](http://www.netage.nl/)                     |
|                                                           |                                                                 |                                              |                                                                                                                                                             | [pySHACL](https://github.com/RDFLib/pySHACL)        |
|                                                           |                                                                 |                                              |                                                                                                                                                             | [RDFUnit](http://aksw.org/projects/RDFUnit)         |
|                                                           |                                                                 |                                              |                                                                                                                                                             | [shaclex](https://github.com/labra/shaclex)         |
|                                                           |                                                                 |                                              |                                                                                                                                                             | [TopBraid](https://github.com/TopQuadrant/shacl)    |


## Online
[SHACL Playground](https://shacl.org/playground/)

[SHACL Playground redux](https://shacl-playground.zazuko.com/)

Issue:  context checking interrupts all other checking at both sites.  

## CLI

```bash
pyshacl -s ../../validation/shapegraphs/soso_common_v1.2.3.ttl -sf turtle  -f human ./09_spatial.md -df json-ld
```

## RESTful
```bash
curl -F  'datagraph=@./DataGraphs/0-example.json'  -F  'shapegraph=@./ShapeGraphs/sosoShape.ttl' -F 'format=human'  https://tangram.gleaner.io/validate
```

## Schema.org validator
Note also the issue around context at [Schema.org Validator](https://validator.schema.org/).  At that location about anything
will work. 

## Notes
Much of this comes down to JSON-LD 1.0 vs 1.1 compliance.  
We can see this at the [JSON-LD Playground V1.0](https://json-ld.org/playground/1.0/)  vs
[JSON-LD Playground V1.1](https://json-ld.org/playground/).   The issue is more problematic when you don't 
know which version a service is using. 

## See Also
More details on validation can be seen at [Gleaner IO Notebooks for Validation](https://github.com/gleanerio/notebooks/tree/master/notebooks/validation)

