# Git Malware API

Prototype service for checking whether a Git repository URL has been flagged.

## Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Query

```bash
curl "http://localhost:8000/check?url=https://github.com/user/repo"
```
