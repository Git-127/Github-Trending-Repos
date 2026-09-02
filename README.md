# 📈 Daily GitHub Trending Archive

This repository automatically fetches the daily trending repositories from GitHub and archives them.

## 🚀 How it works
- A GitHub Action runs **daily**.
- The Python script scrapes `github.com/trending`.
- Results are saved in the `trending/` folder as Markdown files.

## 🔧 Setup
No VPS needed! Powered entirely by GitHub Actions.

## 📂 Output Example
| Rank | Repository | Description | Language | Stars Today |
|------|------------|-------------|----------|-------------|
| 1    | [openai/whisper](https://github.com/openai/whisper) | Robust Speech Recognition | Python | 1.2k |
