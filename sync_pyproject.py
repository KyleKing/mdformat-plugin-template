# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "tomlkit>=0.13.3",
# ]
# ///

"""Sync top-level pyproject.toml."""

from pathlib import Path

import tomlkit


def merge() -> None:
    """Merge ctt output into top-level pyproject.toml."""
    ctt_subdir = ".ctt/default"
    ctt_pyproject = Path(ctt_subdir) / "pyproject.toml"
    ctt_doc = tomlkit.parse(ctt_pyproject.read_text())

    tl_pyproject = Path("pyproject.toml")
    tl_doc = tomlkit.parse(tl_pyproject.read_text(encoding="utf-8"))

    synced_keys = {*ctt_doc["tool"].keys()} - {
        "pytest-watcher",
        "mypy",
        "tox",
        "commitizen",
        "uv",
    }
    for key in synced_keys:
        tl_doc["tool"][key] = ctt_doc["tool"][key]

    per_file_ignores = tl_doc["tool"]["ruff"]["lint"]["per-file-ignores"]
    for key in ("tests/*.py",):
        per_file_ignores[f"package_template/{key}"] = per_file_ignores[key]
        per_file_ignores[f"{ctt_subdir}/{key}"] = per_file_ignores[key]

    tl_pyproject.write_text(tomlkit.dumps(tl_doc), encoding="utf-8")


if __name__ == "__main__":
    merge()
