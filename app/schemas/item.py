from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from app.models.item import ItemType, Priority

class ItemBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255, description="Title name")
    item_type: ItemType = Field(..., description="Type: movie, book, or album")
    tag: Optional[str] = Field(None, max_length=100, description="Genre or label")
    priority: Priority = Field(Priority.MEDIUM, description="Priority for management")
    mood: Optional[str] = Field(None, max_length=100, description="Mood (leisure, pensivel..)")

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    title: Optional[str] = None
    item_type: Optional[ItemType] = None
    tag: Optional[str] = None
    priority: Optional[Priority] = None
    mood: Optional[str] = None
    completed: Optional[bool] = None
    rating: Optional[int] = Field(None, ge=1, le=5, description="Rating from 1 to 5")
    notes: Optional[str] = None

class ItemResponse(ItemBase):
    id: int
    completed: bool
    rating: Optional[int]
    notes: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True