"""Test Helpers."""

_SHOW_TEXT = True  # PLANNED: Make configurable based on pytest CLI


def _print(content: str, show_whitespace: bool) -> None:
    if show_whitespace:
        raise NotImplementedError("To use, port logic from `mdformat_mkdocs`")

    for line in content.split("\n"):
        print(line)  # noqa: T201


def print_text(output: str, expected: str, show_whitespace: bool = False) -> None:
    """Conditionall print text for debugging."""
    if _SHOW_TEXT:
        print("--  Output  --")  # noqa: T201
        _print(output.strip(), show_whitespace)
        print("-- Expected --")  # noqa: T201
        _print(expected.strip(), show_whitespace)
        print("--  <End>   --")  # noqa: T201
