"""An mdformat plugin for `eb_plugin_example`."""

__version__ = "0.0.1"

__plugin_name__ = "eb_plugin_example"

# FYI see source code for available interfaces:
#   https://github.com/executablebooks/mdformat/blob/5d9b573ce33bae219087984dd148894c774f41d4/src/mdformat/plugins.py
from .plugin import POSTPROCESSORS, RENDERERS, add_cli_argument_group, update_mdit

__all__ = ("POSTPROCESSORS", "RENDERERS", "add_cli_argument_group", "update_mdit")
