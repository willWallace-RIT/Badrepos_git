from fastapi import FastAPI
from sqlalchemy.orm import Session

from .database import Base, engine, SessionLocal
from .models import FlaggedRepo

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Git Malware API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/check")
def check(url: str):
    db: Session = SessionLocal()

    repo = url.lower().replace("https://", "").replace("http://", "").rstrip("/")

    hit = db.query(FlaggedRepo).filter(
        FlaggedRepo.repo_url == repo
    ).first()

    return {
        "repo": repo,
        "flagged": hit is not None,
        "source": getattr(hit, "source", None),
        "reason": getattr(hit, "reason", None),
    }
