from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    original_filename = Column(String)
    system_filename = Column(String, unique=True)
    file_size_bytes = Column(Integer)
    uploaded_at = Column(DateTime, default=datetime.utcnow)
