PATTERNS = [
    "curl ",
    "wget ",
    "eval ",
    "base64 -d",
    "chmod 777"
]

def run(text):
    findings = []

    for pattern in PATTERNS:
        if pattern in text:
            findings.append({
                "severity":"high",
                "message":f"Dangerous pattern detected: {pattern}"
            })

    return findings
