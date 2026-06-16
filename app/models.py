from sqlalchemy import Column, Integer, String, Float
from .database import Base

class FlaggedRepo(Base):
    __tablename__ = "flagged_repos"

    id = Column(Integer, primary_key=True)
    repo_url = Column(String, unique=True, index=True)
    source = Column(String)
    confidence = Column(Float, default=1.0)
    reason = Column(String)
