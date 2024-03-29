# mdformat-template-noop

[![Build Status][ci-badge]][ci-link] [![PyPI version][pypi-badge]][pypi-link]

An [mdformat](https://github.com/executablebooks/mdformat) plugin for `<placeholder>`

## `mdformat` Usage

Add this package wherever you use `mdformat` and the plugin will be auto-recognized. No additional configuration necessary. See [additional information on `mdformat` plugins here](https://mdformat.readthedocs.io/en/stable/users/plugins.html)

### Pre-Commit

```yaml
repos:
  - repo: https://github.com/executablebooks/mdformat
    rev: 0.7.16
    hooks:
      - id: mdformat
        additional_dependencies:
          - mdformat-template-noop
```

### pipx

```sh
pipx install mdformat
pipx inject mdformat mdformat-template-noop
```

## HTML Rendering

To generate HTML output, `template_noop_plugin` can be imported from `mdit_plugins`. For more guidance on `MarkdownIt`, see the docs: <https://markdown-it-py.readthedocs.io/en/latest/using.html#the-parser>

```py
from markdown_it import MarkdownIt

from mdformat_template_noop.mdit_plugins import template_noop_plugin

md = MarkdownIt()
md.use(template_noop_plugin)

text = "... markdown example ..."
md.render(text)
# <div>
#
# </div>
```

## Contributing

See [CONTRIBUTING.md](https://github.com/user_ctt/mdformat-template-noop/blob/main/CONTRIBUTING.md)

[ci-badge]: https://github.com/user_ctt/mdformat-template-noop/workflows/CI/badge.svg?branch=main
[ci-link]: https://github.com/user_ctt/mdformat-template-noop/actions?query=workflow%3ACI+branch%3Amain+event%3Apush
[pypi-badge]: https://img.shields.io/pypi/v/mdformat-template-noop.svg
[pypi-link]: https://pypi.org/project/mdformat-template-noop
