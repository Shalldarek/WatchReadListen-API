import enum
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Text, DateTime, Enum
from sqlalchemy.orm import relationship
from app.core.database import Base

class ItemType(str, enum.Enum):
    MOVIE = "movie"
    BOOK = "book"
    ALBUM = "album"

class Priority(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    item_type = Column(Enum(ItemType), nullable=False)
    tag = Column(String, nullable=True)
    priority = Column(Enum(Priority), default=Priority.MEDIUM, nullable=False)
    mood = Column(String, nullable=True)
    completed = Column(Boolean, default=False, nullable=False)
    rating = Column(Integer, nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

user = relationship("User", back_populates="items")