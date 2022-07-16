# 5. Identifier

**Guidelines:** 
[Identifier](/guides/Dataset.md#identifier)

**Source:**
[Line 5](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt#L5)

```
doi: "10.26008/1912/bco-dmo.775849.1"
```

### Schema.org Identifier

- https://schema.org/identifier
    - `URL`
    - `PropertyValue`
    - <strong>`Text`</strong>

#### Identifiers as Text - Good

<pre>
{
  "@context": "https://schema.org/",
  <strong>"identifier": "doi:10.26008/1912/bco-dmo.775849.1"</strong>
}
</pre>


#### Identifiers as URL - Better

<pre>
{
  "@context": "https://schema.org/",
  <strong>"identifier": "https://doi.org/10.26008/1912/bco-dmo.775849.1"</strong>
}
</pre>

<hr/>

[Section #6: Publisher >>](06_publisher.md)

<hr/>

### Resources
- **Source:** [ProteOMZ nitrous oxide data](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt) (example metadata)
- **Testing:** [Google Rich Results Tool](https://search.google.com/test/rich-results)
