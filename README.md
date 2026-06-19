# Multi-Agent Research Assistant

An AI-powered research system that uses multiple specialized agents to perform deep research, critique findings, generate structured reports, and review output quality before delivering a final research document.

---

## Overview

Traditional LLM applications often generate answers in a single step, which can lead to:

* Incomplete research
* Missing perspectives
* Hallucinated information
* Poor report structure

This project addresses these challenges through a **Multi-Agent Architecture** where specialized AI agents collaborate to produce comprehensive research reports.

The system combines:

* Web Search
* Large Language Models
* Agentic Workflows
* Iterative Research Refinement
* Automated Report Generation
* Quality Review Mechanisms

---

## Features

### Multi-Agent Workflow

#### Research Agent

* Analyzes web search results
* Extracts key insights
* Produces structured research notes

#### Critic Agent

* Reviews research quality
* Identifies missing information
* Suggests additional research directions

#### Writer Agent

* Generates professional research reports
* Organizes findings into structured sections

#### Reviewer Agent

* Validates report completeness
* Checks logical consistency
* Reviews formatting and report quality

---

### Search Integration

* Tavily Search API
* Multi-source web research
* Structured result processing

---

### Performance Optimization

* Query caching
* Reduced API usage
* Faster repeated searches

---

### Report Generation

Produces reports containing:

* Executive Summary
* Introduction
* Key Findings
* Detailed Analysis
* Conclusion
* References

---

## Architecture

```text
User Query
     │
     ▼
Search Layer
     │
     ▼
Research Agent
     │
     ▼
Critic Agent
     │
     ▼
Research Refinement
     │
     ▼
Writer Agent
     │
     ▼
Reviewer Agent
     │
     ▼
Final Research Report
```

---

## Tech Stack

### Languages

* Python

### AI & Agent Frameworks

* LangGraph
* LangChain

### LLM Providers

* Groq (Llama 3.1)
* Google Gemini

### Search

* Tavily Search API

### Frontend

* Streamlit

### Utilities

* Logging
* Caching
* Environment Configuration

---

## Project Structure

```text
RESEARCH_ASSISTANT/

├── src/
│   ├── agents/
│   │   ├── research.py
│   │   ├── critic.py
│   │   ├── writer.py
│   │   └── reviewer.py
│   │
│   ├── cache.py
│   ├── config.py
│   ├── graph.py
│   ├── logger.py
│   ├── search.py
│   └── state.py
│
├── cache/
├── exports/
├── docs/
├── tests/
│
├── app.py
├── requirements.txt
├── README.md
└── .env.example
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd RESEARCH_ASSISTANT
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_key
GOOGLE_API_KEY=your_gemini_key
TAVILY_API_KEY=your_tavily_key
```

---

## Running the Application

### CLI

```bash
python app.py
```

### Streamlit

```bash
streamlit run app.py
```

---

## Example Workflow

Input:

```text
Impact of Artificial Intelligence on Healthcare
```

Workflow:

1. Search Layer gathers information
2. Research Agent extracts insights
3. Critic Agent identifies gaps
4. Research is refined
5. Writer Agent generates report
6. Reviewer Agent validates report quality
7. Final report is returned

---

## Current Status

### Completed

* Search Layer
* Research Agent
* Critic Agent
* Writer Agent
* Reviewer Agent
* Caching System
* State Management
* Logging Framework
* GitHub Integration

### In Progress

* Streamlit UI
* PDF Export
* Citation Engine
* Advanced Review Workflows

---

## Future Enhancements

* PDF report export
* Source citation validation
* Multi-model routing
* Research memory
* Docker deployment
* Cloud deployment
* Report versioning

---

## Why This Project?

This project demonstrates practical experience with:

* Agentic AI Systems
* LangGraph Workflows
* Retrieval-Augmented Research
* Multi-Agent Collaboration
* LLM Orchestration
* Production-Oriented Python Development

It is designed as a portfolio-grade AI Engineering project showcasing how multiple AI agents can collaborate to perform complex research tasks more effectively than a single-agent system.

---

## Author

Mayank Pandey

Software Developer | Salesforce | AWS | Generative AI
