from src.export import (
    export_pdf,
    export_markdown
)

sample_report = """
# Executive Summary

This is a sample report.

# Key Findings

- Finding 1
- Finding 2

# Conclusion

Done.
"""

pdf_path = export_pdf(
    sample_report,
    "sample_report.pdf"
)

md_path = export_markdown(
    sample_report,
    "sample_report.md"
)

print(pdf_path)
print(md_path)