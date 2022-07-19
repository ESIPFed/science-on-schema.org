# On Validation


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

