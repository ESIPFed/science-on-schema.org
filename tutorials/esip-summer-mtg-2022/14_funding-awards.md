# 14. Funding & Awards

**Guidelines:** 
[Funding](/guides/Dataset.md#funding)

**Source:**
[Line 42-53](/tutorials/esip-summer-mtg-2022/examples/dataset-01.txt#L42-L53)

```
funding:
  - award:
    name: "R/V Falkor 160115 SOI ProteOMZ Expedition"
    url: "https://www.bco-dmo.org/award/685695"
    source: 
        name: "Schmidt Ocean Institute"
  - award:
    name: "FG-2016-7129"
    url: "https://www.bco-dmo.org/award/875341"
    source:
        name: "Sloan Foundation"
        doi: "10.13039/100000879"
```

### Schema.org - Funding

If you have information about the awards that funded the Dataset,

- [`funding`](https://schema.org/funding)
    - [`funder`](https://schema.org/funder) (if you have information about the source of the award(s)

OR, if you only have information about the funding source of the Dataset,

- [`funder`](https://schema.org/funder)
