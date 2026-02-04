from __future__ import annotations

import json
from pathlib import Path
from typing import Optional, Tuple

from jinja2 import Environment, FileSystemLoader, select_autoescape

from exposure_report_starter.models import ReportInput


TEMPLATE_NAME = "report.md.j2"


def load_report_input(path: Path) -> ReportInput:
    raw_text = path.read_text(encoding="utf-8")
    data = json.loads(raw_text)
    return ReportInput.model_validate(data)


def render_markdown(report: ReportInput, template_dir: Path) -> str:
    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=select_autoescape(enabled_extensions=("j2",)),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template(TEMPLATE_NAME)
    return template.render(report=report)


def render_html(markdown_text: str) -> str:
    try:
        import markdown
    except ImportError as exc:  # pragma: no cover - optional dependency
        raise RuntimeError(
            "Markdown rendering requires the 'markdown' package. "
            "Install it or skip HTML/PDF output."
        ) from exc

    return markdown.markdown(markdown_text, extensions=["tables", "fenced_code"])


def render_pdf(html_text: str, output_path: Path) -> Tuple[bool, Optional[str]]:
    try:
        from weasyprint import HTML
    except ImportError:
        return False, (
            "PDF rendering requires the 'weasyprint' package. "
            "Install it to enable PDF output."
        )

    HTML(string=html_text).write_pdf(str(output_path))
    return True, None


def template_directory() -> Path:
    return Path(__file__).resolve().parent / "templates"
