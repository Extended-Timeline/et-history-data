# Location files

International organization data is recorded in yml format as shown below.

```
sample_organization:
  1234:
    type: tribal_confederation
	color: rgb { 50 50 50 }
    leader: TAG
	members:
	  add: TAG ABC XYZ
	laws:
	  add: sample_law
	areas:
	  add: place_area other_area
  1240:
    members:
	  remove: XYZ
```

---

## All generic arguments with explanations

| Argument | Value type | Required | Explanation | 
|------|----------|----------|----------|
| type | IO ID | yes | The type of the IO |
| color | color | no | Color the IO has on map |
| leader | country tag | no | Tag of the country leading the IO |
| members | add/remove: list of tags | no | Countries belonging to the IO |
| regions | add/remove: list of regions | no | Regions belonging to the IO |
| areas | add/remove: list of areas | no | Areas belonging to the IO |
| provinces | add/remove: list of provinces | no | Provinces belonging to the IO |
| locations | add/remove: list of locations | no | Locations belonging to the IO |
| laws | add/remove: list of laws | no | Laws the IO has |
| regnal_numbers |  | no | See documentation of country files |
| religion | religion ID | no | Religion of the IO, only used for autocephalous_patriarchate and sect |
| icon | icon ID | no | Icon of the IO, only used for sect and hindu_branch |
---

## IO specific arguments

#Arguments unique to: hre

| Argument | Value type |
|------|----------|
| electors | add/remove: list of tags |
| archbishop_electors | add/remove: list of tags |
| free_cities | add/remove: list of tags |
| imperial_peasant_republics | add/remove: list of tags |
| imperial_prelates | add/remove: list of tags |
| imperial_princes | add/remove: list of tags |
| imperial_authority | integer |

#Arguments unique to: middle_kingdom

| Argument | Value type |
|------|----------|
| celestial_governors | add/remove: list of tags |
| celestial_authority | integer |

#Arguments unique to: lordship_of_ireland

| Argument | Value type |
|------|----------|
| lieutenants | add/remove: list of tags |
| loyalists | add/remove: list of tags |

#Arguments unique to: japanese_shogunate

| Argument | Value type |
|------|----------|
| japanese_emperors | add/remove: list of tags |
| shugo_daimyos | add/remove: list of tags |

#Arguments unique to: ilkhanate

| Argument | Value type |
|------|----------|
| ilkhan_claimants | add/remove: list of tags |

#Arguments unique to: tatar_yoke

| Argument | Value type |
|------|----------|
| tatar_tax_collector | country tag |

#Arguments unique to: autocephalous_patriarchate

| Argument | Value type |
|------|----------|
| seat | location ID |

#Arguments unique to: sect

| Argument | Value type |
|------|----------|
| sect_favor | integer |