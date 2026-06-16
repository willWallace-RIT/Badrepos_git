# Git Malware API




ai slop Prototype service for checking whether a Git repository URL has been flagged.

this kinda violate the principles arch AUR but the theory of how to check for shit at scale might be a good stsrting point for a set and forget it approach.

it ultimately puts you in the same position youn were already in \o/

you probably need to write or find some plugins for additional checks.


## Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Query

```bash
curl "http://localhost:8000/check?url=https://github.com/user/repo"
```

---

Git Malware API

A lightweight reputation service for Git repositories.

Git Malware API is designed as a first line of defense for package managers, PKGBUILD maintainers, CI/CD pipelines, and automated build systems that consume code from public Git repositories.

The project's goal is not to detect every form of malware, compromise, or supply-chain attack. Instead, it provides a fast, centralized reputation check that allows clients to identify repositories that have already been reported, flagged, or associated with known malicious activity.

Motivation

Many package build systems—including Arch Linux's PKGBUILD ecosystem—allow arbitrary Git repositories to be referenced as package sources.

A package may appear legitimate while pointing to:

A repository that was later compromised

A repository that was replaced after account takeover

A repository known to distribute malware

A typosquatted repository

A repository associated with phishing or credential theft

A repository previously removed for policy violations


Performing comprehensive security analysis on every referenced repository is expensive and often impractical.

Git Malware API aims to provide a low-cost reputation layer that answers a simple question:

> "Has this repository already been identified as problematic by trusted sources?"



Design Philosophy

First Line of Defense

This service should never be treated as a guarantee of safety.

A repository passing a reputation check does not mean:

The code is secure

The code is malware-free

The repository has not been compromised

Future commits are trustworthy


Instead, the service helps identify repositories that are already known to be suspicious.

Minimize API Usage

Large package repositories may process thousands of packages.

Repeatedly querying GitHub, threat-intelligence providers, and malware databases for every package can quickly exhaust rate limits.

This project centralizes collection and caching of threat intelligence so that clients only need a single lightweight query.

Benefits include:

Reduced GitHub API usage

Reduced threat-feed API usage

Lower latency

Consistent reputation results

Easier auditing


Defense in Depth

Git Malware API is intended to complement—not replace—other security measures:

Package signing

Reproducible builds

Source verification

Commit signature validation

Sandboxed builds

Static analysis

Malware scanning

Human review


Intended Workflow

PKGBUILD
    │
    ▼
Extract source URL
    │
    ▼
Normalize repository
    │
    ▼
Git Malware API
    │
    ├── Known malicious
    │      ▼
    │   Warn / Reject
    │
    └── Not found
           ▼
      Continue build

Data Sources

The project is designed to aggregate information from multiple sources.

Potential sources include:

GitHub Security Advisories

GitHub abuse reports (where available)

URLHaus

AlienVault OTX

Community-maintained malware repositories

Security researcher submissions

Future self-hosted intelligence feeds


Not all sources carry equal confidence.

Each record may contain:

Source provider

Date observed

Confidence score

Reason for flagging

Supporting references


Repository Normalization

Repositories should be normalized before storage and lookup.

Examples:

https://github.com/User/Repo
https://github.com/User/Repo.git
git+https://github.com/User/Repo

become:

github.com/user/repo

This improves cache efficiency and avoids duplicate entries.

API Response

Example:

{
  "repo": "github.com/example/project",
  "flagged": true,
  "confidence": 0.91,
  "source": [
    "urlhaus",
    "otx"
  ],
  "reason": "Known malware distribution"
}

Threat Model

This project helps mitigate:

Known malicious repositories

Previously reported malware repositories

Repository typosquatting

Repositories reused after compromise

Publicly documented abuse infrastructure


This project does not fully mitigate:

Zero-day malware

New malicious repositories

Insider attacks

Build-time code generation attacks

Dependency confusion

Malicious updates after lookup

Local system compromise


Future Goals

Short-Term

GitHub advisory ingestion

URLHaus integration

OTX integration

Repository normalization

SQLite backend

FastAPI service


Medium-Term

PostgreSQL support

Docker deployment

Signed feed exports

Local mirror support

Incremental updates


Long-Term

Federated reputation servers

Community submissions

Cryptographic transparency logs

Decentralized trust scoring

Package manager integrations


Why Centralize?

The internet contains too many attack vectors and too many constantly changing repositories for individual clients to efficiently track.

By centralizing collection and caching of known-malicious repository intelligence, clients can:

Reduce duplicate API traffic

Improve lookup performance

Share threat intelligence

Reduce operational overhead


while still retaining the ability to perform deeper validation when required.

Disclaimer

Git Malware API is a reputation service, not an antivirus product.

A repository that is not listed should never be assumed safe. Reputation checks should be treated as one layer within a broader supply-chain security strategy.
