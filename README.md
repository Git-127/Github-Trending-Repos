# GitHub Trending Archive

> A lightweight, automated archive of GitHub's daily trending repositories.

<p align="center">
  <strong>Discover what is trending on GitHub, every day.</strong><br>
  Automatically collected. Cleanly organized. Easy to explore.
</p>

<p align="center">
  <a href="#how-it-works">How It Works</a>
  &nbsp;&nbsp;•&nbsp;&nbsp;
  <a href="#repository-structure">Structure</a>
  &nbsp;&nbsp;•&nbsp;&nbsp;
  <a href="#local-usage">Usage</a>
  &nbsp;&nbsp;•&nbsp;&nbsp;
  <a href="#automation">Automation</a>
</p>

---

## Overview

**GitHub Trending Archive** captures GitHub's trending repositories and stores a snapshot for each day.

For every trending repository, the scraper records:

| Field           | Description                          |
| :-------------- | :----------------------------------- |
| **Rank**        | Position in the daily trending list  |
| **Repository**  | Repository name and GitHub link      |
| **Description** | Short repository description         |
| **Language**    | Primary programming language         |
| **Stars Today** | Stars displayed on the trending page |

The scraper retrieves the GitHub Trending page, parses its repository entries, and builds a Markdown report from the collected data.
Each snapshot is saved under the `trending/` directory using the current date as its filename.

---

## How It Works

```text
                    ┌──────────────────────┐
                    │   GitHub Trending    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     scraper.py      │
                    │                      │
                    │  Fetch page         │
                    │  Parse repositories │
                    │  Extract metadata    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Daily Markdown     │
                    │      Snapshot        │
                    │                      │
                    │ trending/YYYY-MM-DD  │
                    │        .md           │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    GitHub Actions    │
                    │                      │
                    │  Commit changes      │
                    │  Push automatically  │
                    └──────────────────────┘
```

The workflow runs automatically every day at **10:00 UTC**, while also allowing a manual dispatch from GitHub Actions.

---

## Repository Structure

```text
.
├── .github/
│   └── workflows/
│       └── schedule.yml
│
├── trending/
│   ├── 2026-09-01.md
│   ├── 2026-09-02.md
│   └── ...
│
├── scraper.py
├── requirements.txt
└── README.md
```

The generated reports follow the format:

```markdown
# GitHub Trending - YYYY-MM-DD

| Rank | Repository | Description | Language | Stars Today |
|------|------------|-------------|----------|-------------|
| 1    | owner/repo | ...         | Python   | 1,234       |
| 2    | owner/repo | ...         | Go       | 987         |
```

This format is generated directly by the scraper.

---

## Features

### Daily snapshots

A new Markdown file is generated for each day, creating a simple historical archive of GitHub Trending.

### Zero-maintenance automation

GitHub Actions handles the entire update cycle automatically:

```text
Schedule
   │
   ▼
Checkout repository
   │
   ▼
Set up Python 3.12
   │
   ▼
Install dependencies
   │
   ▼
Run scraper
   │
   ▼
Generate today's snapshot
   │
   ▼
Commit changes
   │
   ▼
Push to repository
```

The workflow uses `actions/checkout@v4`, `actions/setup-python@v5`, Python 3.12, installs `requirements.txt`, runs `scraper.py`, and pushes changes when the generated files differ.

### Simple data extraction

The scraper collects repository name, description, programming language, star count, and repository URL.

### Resilient parsing

Individual repository parsing failures are skipped rather than stopping the entire scraping process.

---

## Local Usage

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repository>.git
cd <your-repository>
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Run the scraper

```bash
python scraper.py
```

The script creates the `trending/` directory when necessary and writes the generated snapshot there.

---

## Automation

The GitHub Actions workflow is defined in:

```text
.github/workflows/schedule.yml
```

The scheduled trigger is:

```yaml
schedule:
  - cron: '0 10 * * *'
```

A manual trigger is also available through:

```yaml
workflow_dispatch:
```

The workflow has permission to write repository contents so it can commit and push updated snapshots.

---

## Why This Exists

GitHub Trending is useful for discovering projects that are gaining attention, but individual daily rankings are easy to lose.

This project turns those ephemeral rankings into a **searchable historical archive**.

Over time, the repository can become useful for:

```text
Trend discovery
      ↓
Historical comparison
      ↓
Technology observation
      ↓
Repository discovery
      ↓
Engineering research
```

---

## Data Flow

```text
GitHub
  │
  │  Trending repositories
  ▼
Requests
  │
  ▼
BeautifulSoup
  │
  │  Parse repository cards
  ▼
Structured repository data
  │
  ▼
Markdown generator
  │
  ▼
trending/YYYY-MM-DD.md
  │
  ▼
Git commit
  │
  ▼
GitHub repository
```

The scraper fetches `https://github.com/trending`, parses the page with BeautifulSoup, and extracts repository information from the repository article elements.

---

## Tech Stack

| Technology         | Purpose                        |
| :----------------- | :----------------------------- |
| **Python**         | Scraping and report generation |
| **Requests**       | HTTP requests                  |
| **BeautifulSoup**  | HTML parsing                   |
| **GitHub Actions** | Scheduled automation           |
| **Markdown**       | Daily reports                  |

## Project Philosophy

```text
Small script
      +
Simple data format
      +
Native GitHub automation
      =
A useful long-term archive
```

No database is required.

No external scheduler is required.

No dashboard is required.

The repository itself becomes the archive.

---

## Limitations

This project depends on the structure of GitHub's Trending page. Changes to GitHub's HTML markup may require updates to the scraper selectors.

The scraper also relies on the information currently exposed by the Trending page, including repository metadata and displayed star counts.

---

<p align="center">
  <sub>Built with Python and GitHub Actions.</sub><br>
  <sub>A small archive of what the GitHub community is building.</sub>
</p>

## Support the Project

<p align="center"> <strong>Find it useful?</strong><br> Star the repository, share it with someone who would enjoy it, or contribute a PR. </p>

<p align="center"> <a href="https://github.com/<your-username>/<your-repository>"> ★ Star on GitHub </a> &nbsp;&nbsp;•&nbsp;&nbsp; <a href="https://github.com/<your-username>/<your-repository>/fork"> Fork & Contribute </a> &nbsp;&nbsp;•&nbsp;&nbsp; <a href="https://github.com/<your-username>/<your-repository>/issues/new"> Suggest an Improvement </a> </p>
