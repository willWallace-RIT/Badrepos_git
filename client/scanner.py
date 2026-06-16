from checks.checksums import run as checksum_check
from checks.dangerous_commands import run as dangerous_check

def scan_text(text):
    findings = []
    findings += checksum_check(text)
    findings += dangerous_check(text)

    score = 0
    for f in findings:
        score += {
            "info":1,
            "warning":10,
            "high":50
        }.get(f["severity"],0)

    return {
        "risk_score": score,
        "findings": findings
    }
