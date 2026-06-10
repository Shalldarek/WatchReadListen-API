from operator import or_
import random
from sqlalchemy.orm import Session
from app.models.item import Item
from app.models.item import ItemType

PRIORITY_WEIGHTS = {
    "high": 5,
    "medium": 3,
    "low": 1
}

def get_random_picked(db: Session, item_type: ItemType | None = None, mood: str | None = None):
    query = db.query(Item).filter(Item.completed == False)
    
    if item_type:
        query = query.filter(Item.item_type == item_type)
    if mood:
        query = query.filter(or_(Item.mood.ilike(f"%{mood}%"), Item.tag.ilike(f"%{mood}%")))
        
    candidates = query.all()

    if not candidates:
        return None

    weights = [PRIORITY_WEIGHTS[c.priority.value] for c in candidates]
    picked_item = random.choices(candidates, weights=weights, k=1)[0]
    
    return picked_item