from fastapi import FastAPI

app = FastAPI()

FLAGGED_REPOS = {
    "github.com/example/malware": "Known malware distribution"
}

@app.get("/check")
def check(url:str):
    return {
        "flagged": url in FLAGGED_REPOS,
        "reason": FLAGGED_REPOS.get(url)
    }

@app.post("/pkgbuild/check")
def pkgbuild_check(payload:dict):
    findings = []

    for repo in payload.get("repos", []):
        if repo in FLAGGED_REPOS:
            findings.append({
                "severity":"high",
                "type":"repo",
                "value":repo,
                "reason":FLAGGED_REPOS[repo]
            })

    return {
        "risk": len(findings) * 100,
        "findings": findings
    }
