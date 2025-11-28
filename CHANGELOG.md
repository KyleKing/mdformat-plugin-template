## 2.5.1 (2025-11-28)

### Fix

- remove experimental blockquote factory

## 2.5.0 (2025-11-24)

### Feat

- add shared blockquote admon factory

### Fix

- add ignores on false matches for secrets
- upgrade gitignore from GitHub Official
- m sounds like a vowel, so use 'an mdformat'

### Refactor

- restore the ctt output back to default
- reduce indentation in blockquote factory
- turn on shared modules for .ctt/default

## 2.4.4 (2025-11-23)

### Fix

- correct the CI badge link and restore package description

## 2.4.3 (2025-11-22)

### Fix

- don't run cz and both tests by default with `tox`

## 2.4.2 (2025-11-22)

### Fix

- set tox basepythons correctly
- properly sort mise.toml

## 2.4.1 (2025-11-22)

### Fix

- run touch mise.lock always

## 2.4.0 (2025-11-22)

### Feat

- fully embrace mise

## 2.3.0 (2025-11-22)

### Feat

- rename tox and test with 3.14 (#8)

## 2.2.2 (2025-11-22)

### Fix

- resolve failures with CI

## 2.2.1 (2025-11-21)

### Fix

- remove `--system` from uv install

## 2.2.0 (2025-11-21)

### Feat

- use commitizen for versioning
- migrate to uv_build
- migrate from flit to uv for package building
- migrate to PyPI Trusted Publishers for secure token-free publishing

### Fix

- resolve Jinja formating errors and missing uv_build configuration
- convert Action to templated jinja file

### Refactor

- exclusion rules for top-level files aren't necessary

## 2.1.3 (2025-11-21)

### Fix

- correct typo in CI for prek

## 2.1.2 (2025-11-21)

### Fix

- add JSON Schema checks

## 2.1.1 (2025-11-21)

### Fix

- resolve CI failures from YAML

## 2.1.0 (2025-11-21)

### Feat

- improvements from mdformat-mkdocs

## 2.0.0 (2025-11-21)

### Feat

- drop Python 3.9 support (#6)

## 1.1.8 (2025-04-09)

### Fix

- store_const to prevent default value

## 1.1.7 (2025-04-09)

### Fix

- correct documentation of TOML config

### Refactor

- modify conditional for loading conf

## 1.1.6 (2024-12-18)

### Fix

- address CLI deprecation warning

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
