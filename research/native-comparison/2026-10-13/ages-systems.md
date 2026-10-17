# EU5 ages and setup systems: native-to-project comparison

Collected 2026-10-13. The native tree inspected was `D:/Games/Europa Universalis 5/Europa.Universalis.V.v1.2.5-0xdeadcode/game`, the current mounted game data. The directory name is not reliable evidence of the installed patch version, so this report does not assign a patch label. Native files were read-only. The structured comparison is in [ages-systems.yml](ages-systems.yml); evidence additions and sources are in [ages-systems-research.yml](ages-systems-research.yml) and [ages-systems-sources.yml](ages-systems-sources.yml).

The main integration issue is a mismatch between two meanings of “age.” Native EU5 has six gameplay ages in `in_game/common/age/00_default.txt`: age 1 starts at year 1 (lines 1–2), then ages 2–6 start at 1342, 1437, 1537, 1637, and 1737 (lines 50–51, 108–109, 167–168, 230–231, 306–307). These definitions carry gameplay modifiers and other settings. The project’s six global classes in `et-history-data/periods/universal.yml` instead organize the research calendar; its prehistoric/ancient boundary at `-3000.1.1` is an editorial convention, not a claim that all regions share a local historical transition. The converter emits `age_1_traditions` for every date (`etl/gen_countries.py:10,100`). Neither the global classes nor the extended end date automatically create new EU5 gameplay ages.

The mod overrides only `main_menu/common/defines` and `main_menu/setup/start`, according to the native-comparison inventory. The setup override expands the selected scenario, while most `in_game/common` catalogs remain inherited. This matters: absence of a mod-local `advances`, `laws`, `unit_types`, or `government_reforms` directory is not absence of those engine systems. Native setup definitions are useful evidence of supported state shapes, but they do not prove that the converter populates those states historically. Similarly, six native files are byte-identical vanilla copies (14, 21, 22, 24, 25, 26); they preserve vanilla baselines rather than provide new date-specific history.

The configured window is `58.2.1` through `9999.12.31` in the mod’s `loading_screen/common/defines/00_defines.txt:2–3`, compared with native `1337.4.1` through `1836.12.31`. The converter parses signed years (`etl/dates.py:15`) and selects a date-keyed snapshot (`etl/snapshot.py:29–52`), but this does not establish that EU5 loads, displays, or simulates BCE dates correctly. Prioritize an isolated engine test before relying on dates below year 1.

## Mapping matrix

The classifications below distinguish inherited native capability from data that the project actually supplies. “Unmapped” means the inspected conversion does not emit the state, not that the engine lacks it.

| System | Native evidence | Project/converter behavior | Classification and implication |
|---|---|---|---|
| Gameplay age catalog | Six definitions, native `age/00_default.txt` lines 1–307 | Global research taxonomy has six differently bounded classes; converter fixes current age | Design gap: taxonomy does not drive gameplay ages |
| Date window | Native defines start/end 1337–1836, lines 2–3 | Mod defines 58–9999, lines 2–3 | Override; extended dates require runtime validation |
| BCE dates | Inspected native age dates start at year 1 | Converter date parser accepts signed integers | Engine support unknown; do not claim either support or impossibility |
| Starting technology level | Native advances file line 1 explains level gates; individual advances use levels 2/3 at lines 14, 22, 29 | `gen_countries.py:9,78` assigns level 3 globally | Lossy: one number replaces dated, uneven advance ownership |
| Advances | Native `advances/0_age_of_traditions.txt:4–62` defines writing, law, mapmaking, colonies and prerequisites | No historical advance-state output | Unmapped: facts cannot yet set adoption by country/date |
| Agriculture | Native agriculture advance at `.../0_age_of_traditions.txt:161–173` | Research records subsistence, but no advance conversion | Unmapped: do not convert farming evidence into universal technology level |
| Institutions | Native `02_core.txt:1–15` has active flags and birthplaces | Mod has hand-maintained institution block; no diffusion timeline | Partial/manual: birthplace is not regional spread chronology |
| Government reforms | `government_reforms/monarchy.txt:12–26` defines age-gated feudal nobility | Definitions inherited; no dated reform selection output | Unmapped: do not guess reform IDs from historical descriptions |
| Legal systems | `laws/01_military_laws.txt:2–33` defines recruitment law and levy policies | Converter only handles `laws.add` on IOs (`gen_events.py:11–53`) | Unmapped country state; legal evidence can be researched independently |
| Land units | `unit_types/00_age_templates_land.txt:9–13` defines baseline light infantry | Unit catalog inherited; generated `27_armies.txt` is empty | No army deployments; definitions alone are not historical forces |
| Naval units | Native age-based navy templates in `unit_types/00_age_templates_navy.txt` | No dated fleet deployment conversion | No project fleet state |
| Country government | Native country setup has government include and ruler blocks | `gen_countries.py:68–85` emits template, ruler, consort, capital | Partial: base government is populated, reforms/laws omitted |
| Population | Native `main_menu/setup/start/06_pops.txt:1–4` starts location/pop rows | Project has population research; converter can emit population inputs, but calibration is still a project dependency | Partial: site/date estimates needed; avoid unsupported totals |
| Wars | Native `main_menu/setup/start/16_wars.txt:1` opens `war_manager`; dated war state follows | `gen_events.py:56–151` maps participants/dates and validates objective | Partial/lossy: missing sides skip; missing targets omit objectives |
| War identity | Native parser shape uses literal `war` blocks | Converter comments source ID because custom war IDs crash parser (`gen_events.py:111`) | Constraint: preserve source event ID in research audit trail |
| International organizations | Native `15_international_organizations.txt:6,11` opens manager and first organization | `gen_events.py:11–53` maps known types, members, date, variables and law additions | Partial: unknown types skipped and absent members dropped |
| Diplomacy | Native `12_diplomacy.txt:1` opens `diplomacy_manager` | `etl/generate.py:39–45` emits empty manager | Unmapped alliances, subjects, truces, other relations |
| Opinions | Native `18_opinions.txt:1` opens `diplomacy_manager` | Empty manager | Unmapped opinion modifiers |
| Rivals | Native `20_rivals.txt:1` opens `diplomacy_manager` | Empty manager | Unmapped rivals |
| Religion | Native `02_core.txt:18` starts `religion_manager`; native `13_religion.txt:1` is `building_manager` | Mod religion files are hand-maintained; `generate.py:48` excludes `13_religion` | File layout differs; religion data exists, historical distributions need evidence |
| Diseases | Native `19_diseases.txt:1` opens disease outbreak manager | `gen_events.py:182–200` emits resistance only | Lossy: other types are skipped |
| Colonies | Native `23_colonies.txt:1` opens `colony_manager` | Empty manager | Unmapped colony state |
| Situations | Native `22_situations.txt:1` opens `situation_manager` | Byte-identical vanilla copy per inventory | Inherited static baseline, not dated ET situations |
| Area preferences | Native `25_area_preferences.txt` (byte-identical file; first line blank) | Byte-identical vanilla copy | Inherited static baseline |
| AI personalities | Native `26_ai_personalities.txt` (byte-identical file; first line blank) | Byte-identical vanilla copy | Inherited static baseline |
| Development | Native `14_development.txt:1` opens `development` | Byte-identical vanilla copy | Baseline preserved, no historical development trajectory |
| Locations | Native `21_locations.txt:1` opens `locations` | Byte-identical vanilla copy | No archaeological settlement-to-location conversion |
| Town rights | Native `24_town_rights.txt:1` opens town rights manager | Byte-identical vanilla copy | Native baseline remains, no dated adjustment |
| Trade/economy | Native `03_markets.txt:1–8` opens market manager and lists markets | No broad exchange-route conversion identified in inspected generator | Research and conversion gap; represent documented links before extrapolating |
| Setup generation | Native setup files supply engine data shapes | 25 project files present; 6 identical, 19 differ; 6 copied, 5 empty managers, 2 hand-maintained categories | Mixed output: inspect copy, generation and inheritance separately |

## Most actionable gaps

**First: date-specific advance state.** The native advance catalog already offers concrete machinery for literacy/writing, agriculture, mapmaking, law, and colonies, including age and prerequisite gates. Yet every emitted country receives technology level 3, while `generate_10` has no per-country or per-date advance list. A strong research dataset can only improve the history if the integration model can distinguish invention, local use, adoption, and later diffusion. The next design step is a provenance-bearing `advance_state`/activity model with place, earliest/latest date, evidence type, and confidence, then a converter mapping reviewed facts to verified IDs. It should not infer ownership from a single find or project-wide chronological period.

**Second: documented military activity and legal institutions.** The game supports unit templates, armies, reforms, laws and dated wars, but project armies and country laws are not generated. Existing war conversion is more advanced yet still loses data when participants or target locations fail validation. For premodern history, research should prioritize atomic site/event records—projectiles, fortifications, battle damage, military vehicles, or written law fragments—while carefully separating object depiction from actual force composition and a surviving law text from state-wide enforcement. After that, converter work can decide whether a fact belongs in an event, an advance, a reform/law state, or contextual research only.

**Third: validate calendar capability.** Signed date parsing is present in converter code, but native inspected definitions only demonstrate positive start dates. A minimal game-load test should separately test negative scenario start, negative dated events, user-interface display, and age transition behavior. If the engine rejects or normalizes dates, the global history taxonomy can remain useful for research while a separate timeline representation is designed; no date compatibility claim should precede the test.

**Fourth: preserve setup semantics.** The generator intentionally mixes vanilla copies, empty managers, generated files, and hand-maintained religion/core files. Continue reviewing each emitted file against native shape and keep a data inventory so future changes never erase inherited vanilla definitions. The six exact-copy files are not “missing”; they are a deliberate base. The five empty managers are different: they encode systems whose historical states are not yet converted. That distinction should remain visible in progress reports and in data acceptance criteria.

## New fact checks for conversion design

Four sourced atoms illustrate the evidence model. Çatalhöyük has a dated concentration of copper-based finds at c.6600–6450 BC, not proof by itself of smelting. Excavators interpret Hamoukar’s destruction around 3500 BCE and sling bullets as battle evidence, but identify no aggressor; sling bullets elsewhere can also be hunting evidence. A distinct Hamoukar record notes obsidian fragments dated 4500–4000 BC by associated pottery and blade-production debris; specialized manufacture for trade is an excavation interpretation, not quantified exchange. The Standard of Ur (2550–2400 BC) shows later vehicles drawn by onagers; it is boundary context, not prehistoric fact or proof of widespread use. The already catalogued Uruk barley-distribution tablet in `research/prehistoric/bookends.yml` is deliberately cross-referenced rather than repeated. Preserve reported ranges, interpretations and source locators without clipping dates.

## Known unknowns and acceptance criteria

This inspection does not prove BCE engine behavior, the year-9999 end date’s effect, runtime requirements for ages/advances, or every copied file’s correctness. It also does not establish historical population totals, borders, ethnic identities, state-level law enforcement, army sizes, or religious distributions.

Accept a future mapping only when it uses a verified native ID and shape, preserves the source’s notation and full range, distinguishes evidence from interpretation, records only verified locations, describes conversion loss, and passes a load test without disturbing inherited definitions. Test BCE separately. For warfare, source the event and participants independently; for advances, distinguish first evidence from broad adoption; for laws/reforms, document scope and effective period rather than treating a surviving text as universal enforcement.

