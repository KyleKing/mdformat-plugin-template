## 1.1.5 (2024-12-15)

### Fix

- correct ptw CLI args

## 1.1.4 (2024-12-15)

### Fix

- remove synced and init if no subdirectories

## 1.1.3 (2024-12-15)

### Fix

- address naming and minor nits

## 1.1.2 (2024-12-15)

### Fix

- resolve tox and toml-sort conflicts

## 1.1.1 (2024-12-14)

### Fix

- correctly remove synced directory if not found
- correct typo in directory name
- resolve ruff errors
- correct plugin name

## 1.1.0 (2024-12-14)

### Feat

- add optional synced factory code
- move tox.ini into pyproject.toml
- improve tox and update dependencies

### Fix

- don't export __version__

## 1.0.2 (2024-10-30)

### Fix

- restore pip install of flit for Windows runners
- run flit install for global python

## 1.0.1 (2024-10-30)

### Fix

- remove ruff from pre-commit

## 1.0.0 (2024-10-30)

### Feat

- drop Python 3.8

## 0.2.7 (2024-10-30)

### Fix

- generate release notes
- document the appropriate steps for versioning

## 0.2.6 (2024-08-20)

### Fix

- sync improvements from mdformat-obsidian
- add __version__

## 0.2.5 (2024-06-24)

### Fix

- remove .ruff.toml from template

## 0.2.4 (2024-06-24)

### Fix

- lower minimum Python for Windows v3.10 CI
- update minimum mdformat-mkdocs in pre-commit

### Refactor

- fix the location of the log

## 0.2.3 (2024-06-23)

### Fix

- simplify logging for post-setup script

## 0.2.2 (2024-06-23)

### Fix

- resolve potential referencing conflict with beartype

### Refactor

- fix regex to match the copier directory

## 0.2.1 (2024-06-23)

### Fix

- resolve ruff errors

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

- remove \_skip_if_exists rules
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
