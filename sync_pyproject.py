"""Sync top-level pyproject.toml."""

from pathlib import Path

import tomlkit


def merge() -> None:
    """Merge ctt output into top-level pyproject.toml."""
    ctt_subdir = ".ctt/default"
    ctt_pyproject = Path(ctt_subdir) / "pyproject.toml"
    ctt_doc = tomlkit.parse(ctt_pyproject.read_text())

    tl_pyproject = Path("pyproject.toml")
    tl_doc = tomlkit.parse(tl_pyproject.read_text())

    synced_keys = {*ctt_doc["tool"].keys()} - {"flit", "pytest-watcher", "mypy"}
    for key in synced_keys:
        tl_doc["tool"][key] = ctt_doc["tool"][key]

    tl_pyproject.write_text(tomlkit.dumps(tl_doc))


if __name__ == "__main__":
    merge()
