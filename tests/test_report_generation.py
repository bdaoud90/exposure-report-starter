import textwrap

from report import DISCLAIMER_TEXT, generate_markdown_report


SAMPLE_INPUT = {
    "report_title": "Exposure Report: Q1 Review",
    "generated_at": "2024-02-01T09:30:00Z",
    "overview": "This report summarizes identified exposure points for Q1.",
    "exposures": [
        {
            "id": "EXP-002",
            "name": "North Ridge Facility",
            "role": "Supplier",
            "risk_level": "Medium",
            "summary": "Single-source dependency for critical components.",
        },
        {
            "id": "EXP-001",
            "name": "Coastal Warehouse",
            "role": "Storage",
            "risk_level": "High",
            "summary": "Flood risk during seasonal storms.",
        },
    ],
    "recommendations": [
        "Diversify supplier base for critical components.",
        "Establish secondary storage location outside flood zones.",
    ],
}


def test_markdown_report_contains_required_sections():
    report = generate_markdown_report(SAMPLE_INPUT)

    for heading in [
        "# Exposure Report: Q1 Review",
        "## Overview",
        "## Exposure Details",
        "## Recommendations",
        "## Disclaimer",
    ]:
        assert heading in report

    assert "_Generated at: 2024-02-01T09:30:00Z_" in report
    assert DISCLAIMER_TEXT in report


def test_markdown_report_includes_exposure_details_in_order():
    report = generate_markdown_report(SAMPLE_INPUT)

    expected_block = textwrap.dedent(
        """
        ### Coastal Warehouse (Storage)
        - **ID:** EXP-001
        - **Risk Level:** High
        - **Summary:** Flood risk during seasonal storms.

        ### North Ridge Facility (Supplier)
        - **ID:** EXP-002
        - **Risk Level:** Medium
        - **Summary:** Single-source dependency for critical components.
        """
    ).strip()

    assert expected_block in report


def test_markdown_report_recommendations_are_listed():
    report = generate_markdown_report(SAMPLE_INPUT)

    assert "- Diversify supplier base for critical components." in report
    assert "- Establish secondary storage location outside flood zones." in report
