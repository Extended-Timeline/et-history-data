# Location files

Location data is recorded in yml format as shown below. Each location has its own file, sorted in folders by continent, subcontinent, region and area.

```
1234:
  name: sampleplace
  owner: TAG
  controller: TAG
  cores: 
    TAG: yes
    ABC: yes
    XYZ: yes
  city:
    rank: town
    setup: scandinavian_town
  resource: stone
  buildings:
    castle:
      level: 1
    monastery:
      level: 1
      owner: PAP #only needed if building owner is different from location owner
  market: yes
  institutions:
    feudalism: yes
    legalism: yes
  roads:
    neighbouringplace: yes
  modifiers:
    skane_herring_market: yes
    
1240.5.7:
  owner: YYY #Treaty of ABC, location given to YYY
  controller: YYY
  cores:
    XYZ: no #XYZ forced to renounce their claim
  buildings:
    castle:
      level: 0 #Castle destroyed
  market: no
```

---

## Cities

Some locations may have cities. For such locations, as city section needs to be added. This section is to have two arguments: rank and setup. Rank can be none, town or city. Setting the rank to none sets the location to not have a city. Setup must be a valid town setup defined in in_game\common\town_setups

---

## Buildings

Buildings are defined in a separate section. Each building must have a level defined. Setting the level to zero removes the building. Buildings can also have an owner defined. The owner should only be defined if it is different from the location owner.

---

## All allowed arguments with explanations

| Argument | Value type | Required | Explanation | 
|------|----------|----------|----------|
| name | localization key | no | Name of the location, defaults to the location ID |
| owner | country tag | yes, unless uncolonized | The country that owns the location |
| controller | country tag | yes, unless uncolonized | The country that controls the location |
| cores | list of *country tag: yes/no* | no | Sets countries that have cores on this location |
| city | see cities section | no | Defines a city in the location |
| resource | resource ID | yes | The raw material in the location |
| buildings | see buildings section | no | Sets the buildings in the location |
| market | yes/no | no | Sets whether the location has a market, defaults to no |
| institutions | list of *institution ID: yes/no* | no | Sets what institutions are present in the location |
| roads | list of *location ID: yes/no* | no | Sets the locations connected to this location via road, it is sufficient to only record a connection one way |
| modifiers | list of *modifier ID: yes/no* | no | Sets modifiers present in the location |

---
