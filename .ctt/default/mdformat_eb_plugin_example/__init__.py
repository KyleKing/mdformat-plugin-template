"""An mdformat plugin for `eb_plugin_example`."""

__version__ = "0.0.1"

from .plugin import POSTPROCESSORS, RENDERERS, add_cli_options, update_mdit

__all__ = ("POSTPROCESSORS", "RENDERERS", "add_cli_options", "update_mdit")
