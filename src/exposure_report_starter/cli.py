from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer

from exposure_report_starter.renderer import (
    load_report_input,
    render_html,
    render_markdown,
    render_pdf,
    template_directory,
)

app = typer.Typer(help="Generate exposure reports from structured inputs.")


@app.command()
def render(
    input_file: Path = typer.Argument(..., exists=True, dir_okay=False, readable=True),
    output_markdown: Path = typer.Option(
        Path("exposure-report.md"),
        "--output-markdown",
        "-m",
        help="Path for the Markdown report output.",
    ),
    output_html: Optional[Path] = typer.Option(
        None,
        "--output-html",
        "-h",
        help="Optional path to write HTML output.",
    ),
    output_pdf: Optional[Path] = typer.Option(
        None,
        "--output-pdf",
        "-p",
        help="Optional path to write PDF output.",
    ),
) -> None:
    """Render an exposure report from a JSON input file."""
    report_input = load_report_input(input_file)
    markdown_text = render_markdown(report_input, template_directory())

    output_markdown.write_text(markdown_text, encoding="utf-8")
    typer.echo(f"Markdown report written to {output_markdown}")

    html_text: Optional[str] = None
    if output_html or output_pdf:
        html_text = render_html(markdown_text)

    if output_html and html_text is not None:
        output_html.write_text(html_text, encoding="utf-8")
        typer.echo(f"HTML report written to {output_html}")

    if output_pdf and html_text is not None:
        success, message = render_pdf(html_text, output_pdf)
        if success:
            typer.echo(f"PDF report written to {output_pdf}")
        else:
            typer.echo(f"PDF output skipped: {message}")


if __name__ == "__main__":
    app()
