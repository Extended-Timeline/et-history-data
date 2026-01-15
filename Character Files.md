# Character files

Character data is recorded in yml format as shown below. All characters belonging to the same tag are included in the same file named after the tag and ordered by date of birth. If a character belonged to multiple tags, they may be included under any one of those files.

```
tag_guy_of_place:
  1000.1.1:
    first_name: name_guy
    last_name: some_last_name
    nickname: the_basic
    dynasty: of_place_dynasty
    father: some_character
    birth: birth_place
    adm: 50
    dip: 50
    mil: 50
    religion: godism
    culture: cultured
    tag: TAG
    traits:
      conqueror: yes
  1081.10.22:
    death: yes
```

---

## Character ID

Every character needs an ID. It must be unique and consist of alphanumeric ascii characters and underscores only. So "Fergus Dubdétach" is not a valid ID but fergus_dubdetach is.

To ensure uniqueness it is recommended to include the tag and regnal numbers in the ID, as well as any other necessary disambiguations to ensure uniqueness. So john_smith is bad, while gbr_john_smith_1747 is good.

---

## Character name

A character can have following types of names:
- first_name, all characters should have this
- nickname, these are optional and refer to names like "the Magnificent" used with Suleiman the Magnificent.
- last_name, mostly used for republican or other non-royal characters
- dynasty, only for characters belonging to a dynasty

There are two types of name IDs. There are names that have different variants in different languages. These names have identifiers like name_henry so a German person named Heinrich would have their name recorded as name_henry and this is then localized ingame based on the character's culture. A list of names like this can be found in character_names_dynamic_l_english.yml in the localization folder. New names or new variants for existing names can and should be added as needed.

Secondly there are names that are unique or specific to only one culture, which can be recorded as plain name itself like hso_hsen_hpa without the extra name_ in front. If the name of your character is not already in the localization, remember to add it there. Most last names and nicknames belong in this category.

Additional points:
- None of the names should include regnal numbers. These are calculated by the game and should not be included in the database.
- If a character has multiple first names, they can both be included separated by a dot. So Matteo Rosso for example would have a name like name_matthew.name_russo

---

## Spouses

The spouse argument defines marriage. This needs to only be defined on one side of the marriage, usually from the side of whoever is not the ruler
```
tag_gal_of_some_other_place:
  1010.1.1:
    first_name: gal
    dynasty: of_some_other_place
    father: some_character
    birth: birth_place
    female: yes
    adm: 50
    dip: 50
    mil: 50
    religion: godism
    culture: cultured
    tag: ABC
  1021.5.3:
    spouse: tag_guy_of_place
    tag: TAG
  1056.7.2:
    spouse: --- #Divorce
  1083.9.21:
    death: yes
```
No one is born married, so the spouse argument should be on a separate date entry when the marriage took place. If a marriage ends in divorce it can be recorded as shown above, but if it ends in the death of either party, it does not need to be recorded as death automatically ends a marriage.

Spouses often come from other countries. If so, they should be assigned to the tag of their birthplace at birth and to the tag of their partner after marriage. 

---

## Traits

Traits are added with the traits argument. This argument does not take a value directly, but constitutes a separate section under which traits are added or removed with [trait ID]: yes/no Example of this is shown below.

```
  1010.1.1:
    traits:
      bastard: yes
      cruel: yes
  1030.1.1:
    traits:
      bastard: no #legitimized
```

---

## All allowed arguments with explanations

| Argument | Value type | Required | Explanation | 
|------|----------|----------|----------|
| first_name | name ID | yes | Character's first name, further explained in the character name section |
| nickname | name ID | no | Nickname like "the Bold", further explained in the character name section |
| last_name | name ID | no | Character's last name, further explained in the character name section |
| dynasty | dynasty ID | no | Character's dynasty |
| birth | location ID | yes* | Character's birth place |
| father | character ID | no | The ID of the character's father |
| mother | character ID | no | The ID of the character's mother |
| spouse | character ID | no | The ID of the character's spouse |
| female | yes/no | yes, if female | Defaults to no, female characters should have this set to yes |
| adm | integer | no | Ranges from 0 to 100 |
| dip | integer | no | Ranges from 0 to 100 |
| mil | integer | no | Ranges from 0 to 100 |
| religion | religion ID | yes* | Character's religion |
| culture | culture ID | yes* | Character's culture |
| traits | see traits section | no | Adds traits to the character |
| tag | country tag | yes* | The tag the character in living in or working for |
| estate | estate ID | no | The estate the character belongs to |
| fertility | integer | no | Ranges from 0 to 100, defaults to 50 |
| death | yes | yes, unless still alive | Sets the character as dead |

*can be generated by the script if missing, so not strictly necessary
---
