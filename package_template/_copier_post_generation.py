"""Post-Generation Script to be run from Copier."""

import shutil
from pathlib import Path


def _log(message: str) -> None:
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


def evaluate_configuration() -> None:
    copier_text = Path(".copier-answers.yml").read_text(encoding="utf-8")
    copier_dict = {
        line.split(":")[0]: line.split(":")[-1].strip()
        for line in copier_text.split("\n")
        if ":" in line
    }

    pth_admon = Path("_synced/admon_factories")
    if pth_admon.is_dir() and copier_dict.get("sync_admon_factories") != "true":
        _log(f"Removing {pth_admon}. To keep, set 'sync_admon_factories=true'")
        shutil.rmtree(pth_admon)


def delete_myself() -> None:
    """Delete this file after completing the main script."""
    Path(__file__).unlink()


if __name__ == "__main__":
    _log("Running self-deleting post-setup script.")
    cleanup()
    evaluate_configuration()
    delete_myself()
