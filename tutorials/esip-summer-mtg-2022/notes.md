# Notes

See issue: https://github.com/ESIPFed/science-on-schema.org/issues/226

## On Validation

Issue:  context checking interrupts all other checking

[SHACL Playground](https://shacl.org/playground/)

```bash
curl -F  'datagraph=@./DataGraphs/0-example.json'  -F  'shapegraph=@./ShapeGraphs/sosoShape.ttl' -F 'format=human'  https://tangram.gleaner.io/validate
```