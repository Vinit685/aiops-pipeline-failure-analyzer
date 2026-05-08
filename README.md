# AIOps Pipeline Failure Analyzer

An AI-powered Jenkins pipeline failure analyzer that uses Ollama (TinyLlama) running locally on AWS EC2 to diagnose CI/CD failures and sends instant Telegram bot alerts with AI-generated root cause analysis.

## Architecture

Jenkins Pipeline Failure → Post-Build Hook (curl) → analyzer.py (Flask API) → Ollama/TinyLlama → Telegram Bot Alert

## Tech Stack

- Jenkins — CI/CD pipelines
- Python + Flask — Analyzer API
- Ollama + TinyLlama — Local LLM inference
- Telegram Bot API — Alert delivery
- AWS EC2 (t2.medium) — Host

## Pipelines Covered

- Dependency-Failure — Simulates missing package errors
- Docker-Build-Failure — Simulates broken Dockerfile
- Test-Failure — Simulates failing unit tests

## Author

Vinit Suryavanshi — DevOps and Cloud Engineer
LinkedIn: https://linkedin.com/in/vinit-suryavanshi-241b66291
GitHub: https://github.com/Vinit685
