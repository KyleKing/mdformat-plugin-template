"""Unit tests for eb_plugin_example plugin components."""

from __future__ import annotations

import pytest

from mdformat_eb_plugin_example._synced.admon_factories import parse_tag_and_title


@pytest.fixture
def md_with_plugin():
    """Fixture providing a MarkdownIt instance with the plugin applied."""
    import markdown_it  # noqa: PLC0415

    from mdformat_eb_plugin_example.mdit_plugins import eb_plugin_example_plugin  # noqa: PLC0415

    md = markdown_it.MarkdownIt()
    md.use(eb_plugin_example_plugin)
    return md


@pytest.mark.parametrize(
    ("input_text", "expected_tags", "expected_title"),
    [
        ("note", ["note"], "Note"),  # Single tag becomes title
        ("note This is a title", ["note"], "This is a title"),
        ('note "Quoted title"', ["note"], "Quoted title"),
        (
            'note warning "Multiple word title"',
            ["note", "warning"],
            "Multiple word title",
        ),
        ("", [""], ""),  # Empty input
        ("   ", [""], ""),  # Whitespace input
        ('"Only quoted"', ['"only'], 'quoted"'),  # Actual parsing behavior
    ],
)
def test_parse_tag_and_title(input_text, expected_tags, expected_title):
    """Test parsing of tag and title from admonition meta text."""
    tags, title = parse_tag_and_title(input_text)
    assert tags == expected_tags
    assert title == expected_title


def test_plugin_import():
    """Test that the plugin can be imported."""
    from mdformat_eb_plugin_example.mdit_plugins import eb_plugin_example_plugin  # noqa: PLC0415

    assert callable(eb_plugin_example_plugin)


def test_plugin_application(md_with_plugin):
    """Test that the plugin can be applied to MarkdownIt."""
    # Test basic markdown still works
    result = md_with_plugin.render("# Hello\n\nWorld")
    assert "<h1>Hello</h1>" in result
    assert "World" in result


def test_mdformat_integration():
    """Test that the plugin integrates with mdformat."""
    import mdformat  # noqa: PLC0415

    # Test basic formatting still works
    result = mdformat.text("# Hello\n\nWorld", extensions={"eb_plugin_example"})
    assert result == "# Hello\n\nWorld\n"

    # Test admonition formatting
    input_text = "!!! note Test\n    Content"
    result = mdformat.text(input_text, extensions={"eb_plugin_example"})
    assert "!!! note Test" in result
    assert "Content" in result
