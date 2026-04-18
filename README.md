# Network-automation-project
Network Security Automation & Audit Pipeline

A Python-based network security automation tool that connects to network devices, performs security audits, parses logs using NLP, generates HTML reports, and delivers automated email alerts — building an end-to-end detection and compliance pipeline.

Project Overview

This pipeline automates the process of auditing network device security configurations and analyzing logs for anomalies. It was built to demonstrate how Python can be used to enforce security baselines, detect suspicious activity, and reduce manual analyst workload through automation.
Key capabilities:

Automated backup of running device configurations via SSH
Security compliance auditing against a defined baseline
Log ingestion and NLP-based event classification
Structured HTML report generation
Automated email delivery of audit results


Architecture
devices.csv
    │
    ▼
    
main.py (Orchestrator)
    │
    ├── backup.py       → SSH connection, config backup, log retrieval
    ├── audit.py        → Security baseline compliance checks
    ├── log_parser.py   → Regex + NLP log parsing and classification
    ├── report.py       → HTML report generation
    ├── emailer.py      → Automated email delivery via SMTP
    ├── logger.py       → Application logging
    └── configuration.py → Environment variables and CSV reader


Security Considerations

All credentials stored in .env file — never hardcoded
SSH used for all device connections
Email transmission uses TLS encryption
Backups stored locally with timestamps for audit trail
Application logs maintained for troubleshooting
