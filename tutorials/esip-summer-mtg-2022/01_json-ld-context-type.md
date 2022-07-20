# 1. Schema.org Context & Type

#### Lesson
> - Understanding the Context https://json-ld.org/spec/latest/json-ld/#the-context
> - Specifying Types https://json-ld.org/spec/latest/json-ld/#specifying-the-type


- `@context` - downloads the schema file to define all the terms
- `@type` - specifies the type of object being described (Person, Article, Business, etc.)
    - [`Dataset`](https://schema.org/Dataset)
```
{
  "@context": "https://schema.org/",
  "@type": "Dataset"
}
```


<hr/>

[Section #2: Basic Fields >>](02_basic-fields.md)

<hr/>

### Resources
- **Schema.org Type Dataset:** https://schema.org/Dataset
- **JSON-LD 1.1 Specification:** https://json-ld.org/spec/latest/json-ld/
- **Source:** [ProteOMZ nitrous oxide data](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt) (example metadata)
- **Testing:** [Google Rich Results Tool](https://search.google.com/test/rich-results)
