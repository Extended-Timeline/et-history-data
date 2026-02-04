# Country files

Country data is recorded in yml format as shown below. All countries have their own file named by their tag.

```
1:
  type: default #only needed if type is not default
  government: catholic_monarchy
  color: rgb { 60  60  60 }
  government_rank: rank_kingdom
  heir_selection: cognatic_primogeniture
  reforms:
    magna_carta_reform: yes
  privileges:
    noble_marriage_rights: yes
    clergy_literacy_rights: yes
  laws:
    marriage_law: monogamous_marriage
  religion: catholic
  primary_culture: french
  court_language: french_language
  capital: paris
  tolerated_cultures:
    english: yes
  accepted_cultures:
    catalan: yes
1000:
  regnal_numbers:
    name_john: 2
  ruler: tag_guy_of_place
  regnal_number: 1
1010.4.7:
  regent: wife_of_guy
  heir: tag_guy_ii_of_place
1020:
  ruler: tag_guy_ii_of_place
  regnal_number: 2
```

---

## Type

Type defined what type of a country a tag is, e.g. building based country, society of pops etc. 

The different options are:
default - normal location based countries (countries default to this, so type does not need to be defined for these countries)
pop - society of pops
building - building based country
army - army based country

---

## Regnal Numbers

If the country uses regnal numbers for its rulers, they should be defined alongside the ruler as shown in the example. By default, a ruler will not have a regnal number, but this can also be set manually by setting the regnal number to 0. 

Usually regnal numbers start from 1, but if the numbers can be set to start from a different number with the regnal_numbers command. This command takes a list of names with a number. This number sets the number of previous rulers for the listed name, so in the example any future John would have a regnal number of 3, as the file considers there to have been 2 previous Johns for that tag.

---

## All allowed arguments with explanations

| Argument | Value type | Required | Explanation | 
|------|----------|----------|----------|
| type | see type section | yes if not default | The type of the country, further explained in the type section |
| government | government preset | yes | The government preset the tag uses |
| color | rgb { xx  xx  xx } | yes | The color the tag will have on the map. Color values range from 0 to 255 |
| religion | religion ID | yes | The state religion of the country |
| primary_culture | culture ID | yes | The primary culture of the country |
| court_language | language ID | no | The court language of the country |
| capital | location ID | yes | The location the tag's capital is in |
| regnal_numbers | see regnal numbers section | no | Sets the number of previous rulers with given names |
| ruler | character ID | no | Sets the ruler of the country, defaults to random |
| regent | character ID | no | Sets the country to be in a regency with the given character as regent |
| heir | character ID | no | Sets the heir of the country, required in regency and in some governments where heir is not defined by laws |
| accepted_cultures | list of *culture ID: yes/no* | no | Sets cultures accepted in the country |
| tolerated_cultures | list of *culture ID: yes/no* | no | Sets cultures tolerated in the country |
| government_rank | government rank ID | no | Sets the government rank, defaults to rank_kingdom |
| heir_selection | heir selection rule ID | no | Sets the way in which the heir is selected |
| reforms | list of *reform: yes/no* | no | Sets the government reforms the country has |
| privileges | list of *privilege: yes/no* | no | Sets the estate privileges the country has |
| laws | list of *law type: law* | no | Sets the laws the country has |
| centralization_vs_decentralization | integer | no | Ranges from -100 to 100 |
| aristocracy_vs_plutocracy | integer | no | Ranges from -100 to 100 |
| serfdom_vs_free_subjects | integer | no | Ranges from -100 to 100 |
| traditionalist_vs_innovative | integer | no | Ranges from -100 to 100 |
| spiritualist_vs_humanist | integer | no | Ranges from -100 to 100 |
| mercantilism_vs_free_trade | integer | no | Ranges from -100 to 100 |
| offensive_vs_defensive | integer | no | Ranges from -100 to 100 |
| land_vs_naval | integer | no | Ranges from -100 to 100 |
| quality_vs_quantity | integer | no | Ranges from -100 to 100 |
| belligerent_vs_conciliatory | integer | no | Ranges from -100 to 100 |
| capital_economy_vs_traditional_economy | integer | no | Ranges from -100 to 100 |
| individualism_vs_communalism | integer | no | Ranges from -100 to 100 |
| outward_vs_inward | integer | no | Ranges from -100 to 100 |

---
