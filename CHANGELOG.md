## 0.2.0 (2024-06-23)

### Feat

- replace .ruff.toml with pyproject config

### Fix

- resolve ruff errors
- more selective pre-commit stages
- remove pygrep pre-commit hooks
- correct tox python versions

### Refactor

- remove snippet for comparing configs
- initialize sync pyproject

## 0.1.7 (2024-06-22)

### Fix

- add ruff, toml, and pyright config
- add missing py.typed

## 0.1.6 (2024-06-03)

### Fix

- link to md-it documentation

## 0.1.5 (2024-04-25)

### Fix

- ignore some beartype warnings

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
