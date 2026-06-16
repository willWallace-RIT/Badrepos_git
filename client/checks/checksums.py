def run(text):
    findings = []

    if "SKIP" in text:
        findings.append({
            "severity":"warning",
            "message":"Checksum verification skipped"
        })

    return findings
