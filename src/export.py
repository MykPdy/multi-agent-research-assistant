from pathlib import Path

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

EXPORT_DIR = Path("exports")

EXPORT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

def export_markdown(
        report: str,
        filename: str
) -> str:
    """
    Save report as markdown
    """

    path = EXPORT_DIR / filename

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(report)

    return str(path)

def export_pdf(
        report: str,
        filename: str
) -> str:
    pdf_path = EXPORT_DIR / filename

    doc = SimpleDocTemplate(
        str(pdf_path)
    )

    styles = getSampleStyleSheet()

    elements = []

    for line in report.splitlines():
        if line.startswith("# "):
            elements.append(
                Paragraph(
                    line[2:],
                    styles["Heading1"]
                )
            )

            elements.append(
                Spacer(1, 12)
            )

        elif line.startswith("## "):
            elements.append(
                Paragraph(
                    line[3:],
                    styles["Heading2"]
                )
            )

            elements.append(
                Spacer(1,8)
            )

        elif (
            line.startswith("- ")
            or line.startswith("* ")
        ):
            elements.append(
                Paragraph(
                    f"• {line[2:]}",
                    styles["BodyText"]
                )
            )

        elif not line.strip():
            elements.append(
                Spacer(1, 6)
            )

        else:
            elements.append(
                Paragraph(
                    line,
                    styles["BodyText"]
                )
            )
    doc.build(elements)

    return str(pdf_path)
