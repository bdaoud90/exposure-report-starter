#!/usr/bin/env python3
"""Generate exposure reports from a Jinja2 Markdown template."""

from __future__ import annotations

import argparse
import json
import os
from dataclasses import dataclass, asdict
from datetime import date
from pathlib import Path
import shutil
import subprocess
import sys
from typing import Any

try:
    from jinja2 import Environment, FileSystemLoader, select_autoescape
except ImportError as exc:  # pragma: no cover - runtime dependency
    raise SystemExit(
        "Missing dependency: jinja2. Install with `pip install jinja2`."
    ) from exc


TEMPLATE_PATH = Path("templates") / "report.md.j2"
OUTPUT_DIR = Path("output")
OUTPUT_MD = OUTPUT_DIR / "report.md"
OUTPUT_PDF = OUTPUT_DIR / "report.pdf"


@dataclass
class TimelineItem:
    date: str
    description: str


@dataclass
class ReportData:
    report_id: str = "TBD"
    prepared_for: str = "TBD"
    prepared_by: str = "TBD"
    report_date: str = date.today().isoformat()
    executive_summary: str = "TBD"
    discovery_date: str = "TBD"
    incident_timeframe: str = "TBD"
    detection_source: str = "TBD"
    status: str = "TBD"
    incident_overview: str = "TBD"
    data_types: str = "TBD"
    records_affected: str = "TBD"
    systems_involved: str = "TBD"
    data_locations: str = "TBD"
    exposure_details: str = "TBD"
    impact_assessment: str = "TBD"
    root_cause_analysis: str = "TBD"
    actions_taken: str = "TBD"
    ongoing_actions: str = "TBD"
    recommendations: str = "TBD"
    internal_stakeholders: str = "TBD"
    external_notifications: str = "TBD"
    regulatory_requirements: str = "TBD"
    communications_notes: str = "TBD"
    timeline: list[TimelineItem] = None
    appendix: str = "TBD"

    def to_template_context(self) -> dict[str, Any]:
        data = asdict(self)
        data["timeline"] = [asdict(item) for item in (self.timeline or [])]
        if not data["timeline"]:
            data["timeline"] = [
                {"date": "TBD", "description": "Add timeline entries."}
            ]
        return data


def load_data(path: str | None) -> dict[str, Any]:
    if not path:
        return ReportData().to_template_context()

    data_path = Path(path)
    if not data_path.exists():
        raise SystemExit(f"Data file not found: {data_path}")

    if data_path.suffix.lower() in {".json"}:
        raw = json.loads(data_path.read_text())
    else:
        raise SystemExit("Only JSON input is supported for --data.")

    defaults = ReportData().to_template_context()
    defaults.update(raw)
    return defaults


def render_report(context: dict[str, Any]) -> str:
    env = Environment(
        loader=FileSystemLoader(TEMPLATE_PATH.parent),
        autoescape=select_autoescape(disabled_extensions=("md",)),
    )
    template = env.get_template(TEMPLATE_PATH.name)
    return template.render(**context)


def write_outputs(content: str) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_MD.write_text(content)

    if shutil.which("pandoc"):
        subprocess.run(
            [
                "pandoc",
                str(OUTPUT_MD),
                "-o",
                str(OUTPUT_PDF),
            ],
            check=False,
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a Markdown (and optional PDF) exposure report."
    )
    parser.add_argument(
        "--data",
        help="Path to a JSON file containing report fields.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    context = load_data(args.data)
    content = render_report(context)
    write_outputs(content)
    print(f"Wrote {OUTPUT_MD}")
    if OUTPUT_PDF.exists():
        print(f"Wrote {OUTPUT_PDF}")
    else:
        print("PDF output skipped (pandoc not available).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
