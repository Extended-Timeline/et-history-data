# Source-backed historical research

This directory stores researched facts before or alongside their integration
into existing dated history YAML. It is organized by the IDs in
[`periods/universal.yml`](../periods/universal.yml).

The first batch, collected on **13 October 2026**, contains **34 records from
15 source entries** across all six chronological classes. It is an initial
research batch, not a complete history of any period or region.

The current priority is the **entire prehistoric class**, following the user's
scope decision. Its expanded regional datasets, source catalogues, reports,
population/dating methodology and explicit remaining gaps are linked from
[`prehistoric/README.md`](prehistoric/README.md). The table below describes the
earlier cross-period batch only, not the expanded collection.

The [14 October 2026 collection](prehistoric/batches/2026-10-14/README.md)
adds 39 source-linked records targeting native-derived historical questions.
It preserves quantitative samples, phase-specific evidence, full reported
chronologies, disputes and process interpretations without applying guessed values.

The [native historical data requirements](native-history-requirements/2026-10-13/README.md)
now direct that research. Native categories define which historical states,
changes and mechanisms to investigate, independently of current mod or
converter support. The catalogue includes source-backed starter findings and
an explicit review of remaining prehistoric coverage gaps.
The earlier [native-file comparison](native-comparison/2026-10-13/README.md)
is retained as a separate technical audit of conversion and implementation.

| Period | Records | Subjects |
|---|---:|---|
| Prehistoric | 4 | Göbekli Tepe and Çatalhöyük settlement evidence |
| Ancient | 14 | Roman characters, Eastern Han capital, Armenia campaigns |
| Medieval | 4 | Abbasid succession and Baghdad/Samarra capitals |
| Early modern | 3 | English East India Company charter and identity |
| Industrial | 4 | Stockton–Darlington opening and Rocket evidence |
| Contemporary | 5 | UN signature, foundation and founding membership |

Six researched facts have been applied to the existing Roman character data;
one verifies the existing Eastern Han capital, and 27 remain collected for
mapping, chronology review, or later gameplay support. The existing generated
mod and the installed game have not been regenerated or modified by this batch.

## Sources and evidence

[`sources.yml`](sources.yml) contains stable source IDs, direct URLs, publishers,
source types and section/catalogue locators. Records reference those IDs.
The primary Roman texts are translated ancient accounts, not contemporary
records of every event; competing traditions and calendar issues are retained.

Institutional or scholarly descriptions support scoped claims. A museum's
dynasty chronology does not establish every province's owner, religion, ruler,
or population. A trading charter does not establish sovereignty. Birth dates
do not justify invented ability scores.

The British Library source was available through its search-index excerpt;
its full page could not be fetched. Those three records have medium confidence
and remain collected until fuller review.

## Record fields

Each batch has `schema_version`, `period_id`, `collected_on` and a `records`
mapping. Record IDs must remain unique across the research directory.

- `entity`: repository ID when known, otherwise a historical entity name.
- `subject`: the type of fact being researched.
- `finding`: a short original paraphrase, not a copied source passage.
- `dating`: the source's actual precision, using one of `day`, `year`, `season`,
  or `range`; prehistoric research also preserves `bp` and `relative` native
  ages, without inventing calendar conversions. Quoted ET dates are used only for day-level dates. Year ranges
  retain both reported endpoint years; they are not gameplay transition days
  or the catalog's half-open classification intervals.
- `source_refs`: source ID and a precise section or catalogue locator.
- `confidence`: `high` or `medium`, assessing this claim rather than the entire source.
- `integration`: status, optional repository-relative target/location ID, and
  notes about assumptions or remaining work.

Integration statuses:

| Status | Meaning |
|---|---|
| `applied` | The specified fact was incorporated into the existing history file. |
| `verified_existing` | Existing data agrees at the precision the source supports. |
| `collected` | Researched and saved; further mapping or interpretation is needed before application. |

`applied` describes the specific fact, not all fields of that entity. For
example, Caligula's corrected birth date does not verify the old Rome birthplace
approximation. See the accompanying integration note and backlog.

## Applied changes

The existing `characters/ROM.yml` retains its IDs and structure:

- Augustus: replace the guessed birth key with conventional `-63.9.23`.
- Tiberius: replace the guessed birth key with the preferred `-42.11.16` account.
- The used Caligula `_1` variant: correct birth to `12.8.31`.
- Remove the false Tiberius-as-Caligula's-father link.
- Both Claudius variants: correct birth to `-10.8.1` at `lyon` (Lugdunum).
- Remove the false Caligula-as-Claudius's-father link.

These changes follow [Suetonius's Augustus 5](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Suetonius/12Caesars/Augustus%2A.html),
[Tiberius 5](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Suetonius/12Caesars/Tiberius%2A.html),
[Caligula 7–8](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Suetonius/12Caesars/Caligula%2A.html)
and [Claudius 1–2](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Suetonius/12Caesars/Claudius%2A.html).

## Next research work

[`backlog.yml`](backlog.yml) records concrete gaps and acceptance conditions.
The current priority is prehistoric research and its
[`coverage.yml`](prehistoric/coverage.yml) acceptance conditions. The earlier
58 CE scenario tasks remain deferred: Roman succession dates, Antium mapping,
Armenian campaign chronology, and broader geographical coverage. The remaining
periods retain their integration tasks.

Correcting a ruler's death can require correcting a country timeline at the
same time. Accordingly the newly sourced deaths of Augustus and Tiberius are
collected separately; their existing coupled timeline keys were not partially
changed. Membership, foundation and effective-control dates likewise remain
distinct.

The YAML workflow includes this directory. Schema consistency, source links,
period classification and applied character values were also checked for this
batch; ordinary YAML parsing alone does not establish historical correctness.
