# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pyyaml>=6.0.2",
#     "tomlkit>=0.13.3",
# ]
# ///

"""Delete `_skip_if_exists` files from the ctt output so they re-render.

copier honors `_skip_if_exists` against the ctt output directories exactly as it
does against a real project, so once such a file exists under `.ctt/` it is never
written again and the committed render drifts from `package_template/` silently.
Removing the paths first makes every ctt run a clean render.

A path staged for its first commit (not yet in HEAD) is also unstaged here. Without
that, deleting it leaves the working tree byte-identical to HEAD for that path, and
if it is the only dirty path in the repo, copier's local-template clone sees no
uncommitted changes to snapshot and its internal `git commit` aborts with "nothing
to commit", crashing the render before it can recreate the file.

Run before `copier-template-tester`, never after.
"""

import subprocess
from pathlib import Path

import tomlkit
import yaml

_ROOT = Path(__file__).parent


def _output_dirs() -> list[Path]:
    ctt_doc = tomlkit.parse((_ROOT / "ctt.toml").read_text(encoding="utf-8"))
    return [_ROOT / name for name in ctt_doc.get("output", {})]


def _skipped_paths() -> list[str]:
    copier_doc = yaml.safe_load((_ROOT / "copier.yml").read_text(encoding="utf-8"))
    return copier_doc.get("_skip_if_exists", [])


def clear() -> None:
    """Remove every `_skip_if_exists` path from every configured ctt output."""
    for directory in _output_dirs():
        for relative in _skipped_paths():
            path = directory / relative
            if path.is_file():
                path.unlink()
                subprocess.run(  # noqa: S603
                    ["git", "rm", "--cached", "--ignore-unmatch", "--quiet", str(path)],
                    cwd=_ROOT,
                    check=True,
                )


if __name__ == "__main__":
    clear()
