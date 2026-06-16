# Git Malware API


ai slop Prototype service for checking whether a Git repository URL has been flagged.

this kinda violate the principles arch AUR but the theory of how to check for shit at scale might be a good stsrting point for a set and forget it approach and I made the license MIT instead of GPL3 for that reason.

it ultimately puts you in the same position youn were already in \o/

you probably need to write or find some plugins for additional checks.

i dont personally want to run the centralized service BUT ONE outside of github should be the mitigation to maintain direct calls to git to a minimum.


PKGBuild Security Suite

A lightweight supply-chain security framework for PKGBUILDs and Git-based package sources.

PKGBuild Security Suite consists of two components:

1. Reputation Server — a centralized service that aggregates known-malicious repositories, package sources, and threat intelligence.
2. Client Scanner — a local PKGBUILD auditing tool that performs static analysis and queries the reputation server.

The project is designed to provide a practical first line of defense against common package supply-chain attacks while minimizing external API requests and infrastructure requirements.

---

Why This Project Exists

Modern package ecosystems increasingly rely on source code fetched directly from Git repositories.

While this model offers flexibility and rapid distribution, it also introduces risks:

- Repository compromise
- Maintainer account takeover
- Typosquatting
- Malicious package updates
- Malicious package adoption
- Runtime download attacks
- Obfuscated install scripts

Recent incidents have demonstrated that even trusted package ecosystems can be abused when attackers gain control of package sources or maintainership.

Comprehensive auditing of every repository and package source is often impractical.

This project focuses on identifying known risks quickly and cheaply.

---

Project Goals

Fast Reputation Checks

Allow clients to determine whether:

- A Git repository has previously been reported as malicious
- An AUR package has been associated with malicious activity
- A source URL appears on known threat feeds

using a single lightweight API request.

Minimize External API Usage

Rather than every client independently querying GitHub and threat-intelligence providers, the server aggregates and caches information centrally.

Benefits include:

- Reduced API rate-limit consumption
- Faster package validation
- Shared threat intelligence
- Consistent results across systems

Defense in Depth

The suite is not intended to replace:

- Code review
- Reproducible builds
- Package signing
- Sandboxed builds
- Static analysis
- Malware scanning

Instead, it provides an additional security layer that can identify known issues before package installation begins.

---

Architecture

Reputation Server

The server maintains a database of known indicators gathered from multiple sources.

Potential data sources include:

- GitHub Security Advisories
- URLHaus
- AlienVault OTX
- Community submissions
- Security research feeds
- Historical package incidents

The server stores:

- Flagged repositories
- Flagged package names
- Flagged URLs
- Flagged maintainers
- Threat metadata
- Confidence scores

Primary Endpoint

POST /pkgbuild/check

The client submits:

- Package name
- Extracted repository URLs
- Extracted source URLs

The server returns:

- Risk score
- Findings
- Threat intelligence references

---

Client Scanner

The client performs local analysis before contacting the server.

Repository Extraction

Extract Git repositories from:

source=()

entries within a PKGBUILD.

Source Validation

Identify:

- Plain HTTP downloads
- Shortened URLs
- Raw IP-based downloads
- Nonstandard source locations

Reproducibility Checks

Detect:

- Mutable branches
- Unpinned repositories
- Missing commit references

Checksum Validation

Warn when:

- Checksums are skipped
- Verification is incomplete

Dangerous Command Detection

Identify patterns such as:

- curl | bash
- wget | sh
- eval
- base64 decoding
- Runtime downloads

Suspicious Install Targets

Flag writes to locations including:

- /etc/sudoers
- ~/.ssh
- /etc/systemd/system

for additional review.

---

Plugin System

Organizations and maintainers can define custom checks.

Custom rules are placed in:

plugins/

Each rule exposes a simple interface:

def run(pkgbuild):
return findings

This allows local policy enforcement without modifying the core scanner.

Examples:

- Internal package restrictions
- Approved repository lists
- Additional compliance requirements
- Organization-specific security checks

---

Threat Model

This project helps detect:

- Known malicious repositories
- Previously reported malicious packages
- Known malicious URLs
- Common PKGBUILD abuse patterns
- Basic supply-chain attack indicators

This project does not guarantee protection against:

- Zero-day malware
- Newly compromised repositories
- Insider threats
- Sophisticated obfuscation
- Advanced persistence techniques
- Local machine compromise

A clean report should never be interpreted as proof of safety.

---

Typical Workflow

1. User downloads a PKGBUILD.
2. Client scanner performs local analysis.
3. Repository and source URLs are extracted.
4. Client sends a single request to the reputation server.
5. Risk score and findings are returned.
6. User decides whether additional review is required.

This approach keeps package validation lightweight while still leveraging centralized threat intelligence.

---

Long-Term Vision

The long-term goal is a federated reputation network for package sources.

Future features may include:

- Signed threat feeds
- Transparency logs
- Community moderation
- Reputation scoring
- Package-manager integrations
- Local mirrors
- Decentralized trust models

The objective is not to determine whether software is safe, but to provide actionable information about known risks before software is built or installed.
