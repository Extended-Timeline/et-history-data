# et-history-data

**et-history-data** is a version-controlled archive of structured historical data in **YAML format** for the *Extended Timeline (ET)* mod. This project is designed to support the transition of ET to *Europa Universalis V (EU5)* by making the historical game content modular, readable, and easy to convert using automation tools.

Each file represents the historical evolution of a province or region over time through date-stamped entries. This format allows for fine-grained control and easier collaboration on historical accuracy.

## 🧭 Goals

- Represent dynamic historical data (ownership, population, buildings, etc.) in a consistent, flexible format
- Provide clean, machine-readable source data for EU5 modding tools
- Enable collaborative modding through Git-based workflows

## Chronological period classes

[`periods/universal.yml`](periods/universal.yml) defines six shared research
classes: prehistoric, ancient, medieval/postclassical, early modern,
industrial/world wars, and contemporary. Boundaries are project conventions,
not claims that all societies changed at the same time.

See [Period Classes](docs/Period%20Classes.md) for dates, research topics,
regional interpretation, sources, and the later connection to EU5 gameplay ages.

## Historical research

[`research/`](research/README.md) collects source-backed facts by period, with
dating precision, confidence, integration status, and a research backlog.
[`research/sources.yml`](research/sources.yml) records source URLs and section
locators; facts are applied to the existing history schemas when mapping and
chronology are sufficiently supported.
