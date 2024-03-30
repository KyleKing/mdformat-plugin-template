## 0.1.4 (2024-03-30)

### Fix

- add yamllint config

## 0.1.3 (2024-03-30)

### Fix

- correct leftover reference to mdformat_admon
- use precise pre-commit Action tag

### Refactor

- remove _skip_if_exists rules
- use pytest-beartype in tox and ptw

## 0.1.2 (2024-03-29)

### Fix

- resolve differences with mdformat-obsidian when copied
- bump pre-commit workflow

## 0.1.1 (2024-03-29)

### Fix

- correct ruff config
- resolve yamllint errors

## 0.1.0 (2024-03-29)

### Feat

- replace yamlfix with yamllint and add toml-sort
- finish replacing references to gfm
- begin replacing instances of gfm with plugin_name
- replace with mdformat-plugin template repository
- initialize package template from subset of calcipy_template
- initialize based on calcipy_template

### Fix

- resolve pre-commit issues
- sync top-level pre-commit config
- sort pyproject.toml
- update copier-post-generation script
- extend skip if exists
- rename source code directory

### Refactor

- replace template files with gfm_alerts
- intermediary rename
- run pre-commit
