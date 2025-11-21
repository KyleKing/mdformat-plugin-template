# mdformat-eb-plugin-example

[![Build Status][ci-badge]][ci-link] [![PyPI version][pypi-badge]][pypi-link]

An [mdformat](https://github.com/executablebooks/mdformat) plugin for `<placeholder>`

## `mdformat` Usage

Add this package wherever you use `mdformat` and the plugin will be auto-recognized. No additional configuration necessary. See [additional information on `mdformat` plugins here](https://mdformat.readthedocs.io/en/stable/users/plugins.html)

### Pre-Commit

```yaml
repos:
  - repo: https://github.com/executablebooks/mdformat
    rev: 0.7.19
    hooks:
      - id: mdformat
        additional_dependencies:
          - mdformat-eb-plugin-example
```

### uvx

```sh
uvx --from mdformat-eb-plugin-example mdformat
```

Or with pipx:

```sh
pipx install mdformat
pipx inject mdformat mdformat-eb-plugin-example
```

## HTML Rendering

To generate HTML output, `eb_plugin_example_plugin` can be imported from `mdit_plugins`. For more guidance on `MarkdownIt`, see the docs: <https://markdown-it-py.readthedocs.io/en/latest/using.html#the-parser>

```py
from markdown_it import MarkdownIt

from mdformat_eb_plugin_example.mdit_plugins import eb_plugin_example_plugin

md = MarkdownIt()
md.use(eb_plugin_example_plugin)

text = "... markdown example ..."
md.render(text)
# <div>
#
# </div>
```

## Contributing

See [CONTRIBUTING.md](https://github.com/executablebooks/mdformat-eb-plugin-example/blob/main/CONTRIBUTING.md)

[ci-badge]: https://github.com/executablebooks/mdformat-eb-plugin-example/workflows/CI/badge.svg?branch=main
[ci-link]: https://github.com/executablebooks/mdformat-eb-plugin-example/actions?query=workflow%3ACI+branch%3Amain+event%3Apush
[pypi-badge]: https://img.shields.io/pypi/v/mdformat-eb-plugin-example.svg
[pypi-link]: https://pypi.org/project/mdformat-eb-plugin-example
