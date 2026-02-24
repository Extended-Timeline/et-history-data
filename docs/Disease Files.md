# Disease Files

Disease data is recorded in yml format as shown below.

```
bobonic_plague_resistance_01:
  1200:
    type: resistance
	disease: bubonic_plague
    value: 0.1
    regions:
      add: one_region other_region
measles_outbreak_01:
  1300:
    type: outbreak
	disease: measles
    infected: 1
    origin: place
    areas:
      add: one_area other_area
```

---

## All allowed arguments with explanations

| Argument | Value type | Required | Explanation | 
|------|----------|----------|----------|
| type | resistance/outbreak | yes | Type of the entry |
| disease | disease type | yes | Type of the disease |
| value | float | yes for resistance | The strength of disease resistance |
| infected | integer? | yes for outbreak | ? |
| origin | location ID | yes for outbreak | The location where the outbreak started |
| artist | character ID | no | The character who created the artwork |
| continents | add/remove: list of continents | no | Affected continents |
| regions | add/remove: list of regions | no | Affected regions |
| areas | add/remove: list of areas | no | Affected areas |
| provinces | add/remove: list of provinces | no | Affected provinces |
| locations | add/remove: list of locations | no | Affected locations |
---
