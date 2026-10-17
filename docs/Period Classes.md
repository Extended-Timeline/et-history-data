# Chronological period classes

The catalog in [`periods/universal.yml`](../periods/universal.yml) organizes
historical research by date. Stable IDs let researchers use the same period
names across country, location, character, dynasty, war, and organization work.

"Universal" means a shared calendar index. It does not mean universally agreed
period boundaries or that every society has the same institutions and technology.
The exact cutoffs below are **project conventions**. They can be revised without
renaming period IDs; changes to boundaries must be recorded in review.

| ID | Türkçe | Calendar window |
|---|---|---|
| `prehistoric` | Tarih Öncesi | Before 3000 BCE |
| `ancient` | Antik | 3000 BCE to before 500 CE |
| `medieval` | Orta Çağ / Klasik Sonrası | 500 to before 1500 |
| `early_modern` | Erken Modern | 1500 to before 1800 |
| `industrial` | Sanayi / Dünya Savaşları | 1800 to before 1945 |
| `contemporary` | Çağdaş | 1945 onward |

## Date and interval rules

- Store boundaries as **quoted strings** in ET `year.month.day` notation.
  Negative years use the repository's BCE convention: `"-3000.1.1"` is 3000 BCE.
- A period includes its start and excludes its end: `start <= date < end`.
- A YAML `null` start means no lower bound; a `null` end means no upper bound.
- Consecutive periods must share the same boundary, with no overlaps or gaps.
- A boundary day belongs to the later period. `500.1.1` is `medieval`;
  `1500.1.1` is `early_modern`; `1945.1.1` is `contemporary`.
- This catalog partitions the existing ET date order. It does not introduce a
  new calendar, year-zero policy, or BCE/CE arithmetic into the converter.

Existing scenarios classify as follows:

| Scenario date | Research period |
|---|---|
| `58.2.1` | `ancient` |
| `936.1.1` | `medieval` |
| `2025.1.1` | `contemporary` |

## Research workflow

1. Select a period and region, then use that period's `research_focus` list to
   organize work. It lists subjects to collect, not facts about every society.
2. Write historical facts in the existing dated YAML files. Keep original
   country tags, location IDs, character IDs, and event dates.
3. Record the source, page/section when available, geographical coverage,
   confidence, and dating uncertainty in the research notes or contribution.
4. Preserve local terminology and local transition dates alongside the global
   calendar class. A date classification alone is never evidence of government,
   religion, culture, literacy, technology, or industrialization.

Do not add `period_id` or `age` fields to existing country/location history
blocks solely for classification. The class can be derived from the date,
avoiding duplicated metadata and unsupported fields in existing schemas.

## Regional classifications

Regional research may need categories such as a local Bronze Age, an imperial
dynasty, or a period of industrialization. Such categories can overlap these
calendar windows and have different boundaries. Keep their name, scope,
start/end, uncertainty, and supporting sources in research notes until a
separate regional catalog schema is introduced. They do not override the
global chronological class or automatically change a country's game age.

The [Routledge global medieval resources](https://routledgetextbooks.com/textbooks/9781138103399/chapters.php)
discuss the European origin of medieval periodization in a global context.
Cambridge's [Global Interactions in the Early Modern Age, 1400–1800](https://assets.cambridge.org/97805216/88673/frontmatter/9780521688673_frontmatter.pdf)
uses a different start from this catalog's 1500 convention. These references
provide context; they do not certify one mandatory world chronology.

## Relationship to EU5

This catalog is a research-data layer. The converter does **not yet read it**,
and it does not create EU5 `common/age` definitions or change `current_age`.
The existing mod and its `00_defines.txt` remain the gameplay baseline.

Later gameplay work can map these period IDs to age definitions, technology,
institutions, units, buildings, and transition rules. That mapping must be
explicit; six research classes do not require exactly six gameplay ages.

The final open interval does not claim that future history is known. A future
scenario needs a separately identified speculative data policy.

## Validation

The existing repository YAML workflow now includes `periods/**`. It checks
YAML syntax, as it does for the other history directories. Interval continuity,
unique IDs/orders, and the scenario examples must also be checked when changing
the catalog; YAML syntax alone cannot prove those properties.
