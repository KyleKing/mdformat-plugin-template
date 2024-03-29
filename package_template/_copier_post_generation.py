"""Post-Generation Script to be run from Copier."""

import json
import re
import shutil
from dataclasses import dataclass
from pathlib import Path

# Don't print any output if matching directories like:
# /private/var/folders/1f/gd24l7210d3d8crp0clcm4440000gn/T/copier.main.update_diff.7eb725cw/.git/
# /private/var/folders/1f/gd24l7210d3d8crp0clcm4440000gn/T/copier.main.recopy_diff.gnos2law/.git/
_re_copier_dir = re.compile(r"copier\.[^\.]+\.\w+_diff\.")
_IS_PROJ = not _re_copier_dir.search(Path(__file__).absolute().as_posix())


@dataclass
class Config:
    package_name_kebab: str
    plugin_name: str
    repository_url: str


_CONFIG_PATH = Path(__file__).with_suffix(".json")
_CONFIG = Config(**json.loads(_CONFIG_PATH.read_text()))


def _log(message: str) -> None:
    if _IS_PROJ:
        print(message)  # noqa: T201


def cleanup() -> None:
    """Remove files and folders that are no longer used."""
    paths = []
    directories = []

    for pth in paths:
        if pth.is_file():
            _log(f"Removing: {pth}")
            pth.unlink()
    for dir_pth in directories:
        if dir_pth.is_dir():
            _log(f"Deleting: {dir_pth}")
            shutil.rmtree(dir_pth)


def delete_myself() -> None:
    """Delete this file after completing the main script."""
    Path(__file__).unlink()
    _CONFIG_PATH.unlink()


if __name__ == "__main__":
    _log(
        f"""
The 'mdformat_{_CONFIG.plugin_name}' package has been updated (or created)!

1. Review the changes and commit. Merge conflicts may either be '*.rej' files or as inline git diffs
2. Install dependencies with 'poetry install --sync'
3. Run `./run --help` to show the available actions
4. Run `./run main --keep-going` to try running all default tasks after the changes
5. If this is a new project, you could create the GitHub repo with:

    ```sh
    gh repo create "{_CONFIG.package_name_kebab}" --source=. --remote=origin --push \
        --homepage="{_CONFIG.repository_url}" --public
    ```
""",
    )
    cleanup()
    delete_myself()
