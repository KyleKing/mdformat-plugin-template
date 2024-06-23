# noqa: INP001
"""Post-Generation Script to be run from Copier."""

import json
import re
import shutil
from dataclasses import dataclass
from pathlib import Path

# Prevent printing in triplicate when matching directories like:
# /private/var/folders/1f/gd24l7210d3d8crp0clcm4440000gn/T/copier.main.update_diff.7eb725cw/.git/ # noqa: E501
# /private/var/folders/1f/gd24l7210d3d8crp0clcm4440000gn/T/copier.main.recopy_diff.gnos2law/.git/ # noqa: E501
_re_copier_dir = re.compile(r"\/[a-z0-9]{30}\/T\/copier\.[^\/]+\/\.git\/$")
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
    remove_list = Path("remove-if-found.txt")
    if not remove_list.is_file():
        return
    for line in remove_list.read_text().split("\n"):
        if not line:
            continue
        pth = Path(line)
        if pth.is_file():
            _log(f"Removing: {pth}")
            pth.unlink()
        elif pth.is_dir():
            _log(f"Deleting: {pth}")
            shutil.rmtree(pth)
    remove_list.unlink()


def delete_myself() -> None:
    """Delete this file after completing the main script."""
    Path(__file__).unlink()
    _CONFIG_PATH.unlink()


if __name__ == "__main__":
    _log(
        f"""
The 'mdformat_{_CONFIG.plugin_name}' package has been updated (or created)!

1. Review the changes and commit
    1. Merge conflicts may either be '*.rej' files or as inline git diffs
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
