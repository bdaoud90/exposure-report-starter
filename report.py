from __future__ import annotations

from datetime import datetime
from typing import Iterable


DISCLAIMER_TEXT = (
    "This report is for informational purposes only and does not constitute legal advice."
)


def _format_exposure_items(exposures: Iterable[dict]) -> str:
    lines = []
    for exposure in sorted(exposures, key=lambda item: item["id"]):
        lines.append(f"### {exposure['name']} ({exposure['role']})")
        lines.append(f"- **ID:** {exposure['id']}")
        lines.append(f"- **Risk Level:** {exposure['risk_level']}")
        lines.append(f"- **Summary:** {exposure['summary']}")
        lines.append("")
    return "\n".join(lines).rstrip()


def generate_markdown_report(data: dict) -> str:
    title = data["report_title"]
    generated_at = data["generated_at"]
    exposures = data.get("exposures", [])
    recommendations = data.get("recommendations", [])

    if isinstance(generated_at, datetime):
        generated_at = generated_at.isoformat()

    exposure_section = _format_exposure_items(exposures)
    recommendation_lines = [f"- {item}" for item in recommendations]
    recommendations_text = "\n".join(recommendation_lines) if recommendation_lines else "- None"

    parts = [
        f"# {title}",
        "",
        f"_Generated at: {generated_at}_",
        "",
        "## Overview",
        data["overview"],
        "",
        "## Exposure Details",
        exposure_section if exposure_section else "No exposures identified.",
        "",
        "## Recommendations",
        recommendations_text,
        "",
        "## Disclaimer",
        DISCLAIMER_TEXT,
        "",
    ]
    return "\n".join(parts).rstrip() + "\n"
