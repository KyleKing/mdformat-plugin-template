# Development

## API Documentation

A collection of useful resources to reference when developing new features:

- [`markdown-it-py` documentation](https://markdown-it-py.readthedocs.io/en/latest/using.html)
- [`markdown-it` (JS) documentation](https://markdown-it.github.io/markdown-it)

## Local Development

This package utilizes [uv](https://docs.astral.sh/uv) as the build engine, and [tox](https://tox.readthedocs.io) for test automation.

To install these development dependencies:

```bash
uv tool install tox --with tox-uv
# or: pipx install tox
```

To run the tests:

```bash
tox
```

and with test coverage:

```bash
tox -e py310-test
```

The easiest way to write tests, is to edit `tests/fixtures.md`

To run the code formatting and style checks:

```bash
tox -e py312-prek
```

or directly with [prek](https://github.com/j178/prek) (or pre-commit)

```bash
uv tool install prek
# or: pipx install prek, brew install prek, etc.

prek install -f
prek run --all
```

To run the pre-commit hook test:

```bash
tox -e py310-hook
```

## `ptw` testing

See configuration in `pyproject.toml` for `[tool.pytest-watcher]`

```sh
uv tool install pytest-watcher
# or: pipx install pytest-watcher

ptw .
```

## Local uv/pipx testing

Run the latest local code anywhere with uv tool.

```sh
uv tool install . --editable --force --with="mdformat>=0.7.19"
```

Or with pipx:

```sh
pipx install . --include-deps --force --editable
```

## Publish to PyPi

This project uses [PyPI Trusted Publishers](https://docs.pypi.org/trusted-publishers/) for secure, token-free publishing from GitHub Actions, with [uv](https://docs.astral.sh/uv/) for building packages.

### Initial Setup (One-time)

Before publishing for the first time, you need to configure Trusted Publishing on PyPI:

1. Go to your project's page on PyPI: `https://pypi.org/manage/project/mdformat_eb_plugin_example/settings/publishing/`
    - If the project doesn't exist yet, go to [PyPI's publishing page](https://pypi.org/manage/account/publishing/) to add a "pending" publisher
1. Add a new Trusted Publisher with these settings:
    - **PyPI Project Name**: `mdformat_eb_plugin_example`
    - **Owner**: `executablebooks`
    - **Repository name**: `mdformat-eb-plugin-example`
    - **Workflow name**: `tests.yml`
    - **Environment name**: `pypi`
1. Configure the GitHub Environment:
    - Go to your repository's `Settings` → `Environments`
    - Create an environment named `pypi`
    - (Recommended) Enable "Required reviewers" for production safety

### Publishing a Release

Update the version in `mdformat_eb_plugin_example/__init__.py`, commit the change, and push a tag in format: `v#.#.#` (e.g. `v1.3.2` for `__version__ = '1.3.2'`):

```bash
git add mdformat_eb_plugin_example/__init__.py
git commit -m "bump: version X.Y.Z"
git tag v1.3.2
git push origin main --tags
```

The GitHub Action will automatically build and publish to PyPI using Trusted Publishers (no API tokens needed!).
