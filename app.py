import os

import streamlit as st

from src.graph import run_research

from src.export import (
    export_pdf,
    export_markdown
)

st.set_page_config (
    page_title="Multi-Agent Research Assistant",
    page_icon= "🔎",
    layout="wide"
)

st.title(
    "🔎 Multi-Agent Research Assistant"
    )

st.markdown(
        """
Researches a topic using:

- Research Agent
- Critic Agent
- Writer Agent
- Reviewer Agent

Built with LangGraph.
"""
)

with st.sidebar:

    st.header("Settings")

    max_iterations = st.slider(
        "Max Research Iterations",
        min_value=1,
        max_value=5,
        value=2
    )

query = st.text_area(
    "Enter a research question",
    height=120
)

run_button = st.button(
    "Run Research"
)

if run_button:
    if not query.strip():
        st.warning(
            "Please enter a query."
        )
    else:
        status_placeholder = st.empty()

        status_placeholder.info(
            "Running research workflow..."
        )

        result = run_research(
            query=query,
            max_iterations=max_iterations
        )
        status_placeholder.success(
            "Research workflow Completed!"
        )

        st.header("Final Report")

        st.markdown(
            result["final_report"]
        )

        st.header("Agent Status")

        st.json(
            result["agent_status"]
        )

        with st.expander(
            "Sources"
        ):

            for source in result["sources"]:
                st.write(source)


        with st.expander(
            "Error Log"
        ):

            if result["error_log"]:
                st.write(
                    result["error_log"]
                )
            else:
                st.write(
                    "No errors."
                )
        pdf_path = export_pdf(
            result["final_report"],
            "research_report.pdf"
        )

        md_path = export_markdown(
            result["final_report"],
            "research_report.md"
        )

        with open(
            pdf_path,
            "rb"
        ) as pdf_file:

            st.download_button(
                "Download PDF",
                pdf_file,
                file_name="research_report.pdf",
                mime="application/pdf"
            )

        with open(
            md_path,
            "r",
            encoding="utf-8"
        ) as md_file:

            st.download_button(
                "Download Markdown",
                md_file.read(),
                file_name="research_report.md",
                mime="text/markdown"
            )
