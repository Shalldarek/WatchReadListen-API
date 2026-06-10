from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate

def create_item(db: Session, item_data: ItemCreate, user_id: int):
    db_item = Item(**item_data.model_dump(), user_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(Item).filter(Item.user_id == user_id).offset(skip).limit(limit).all()

def get_item(id: int, db: Session, user_id: int):
    return db.query(Item).filter(Item.id == id, Item.user_id == user_id).first()

def delete_item(id: int, db: Session, user_id: int):
    item = db.query(Item).filter(Item.id == id, Item.user_id == user_id).first()

    if not item:
        return None  
    db.delete(item)
    db.commit()
    return item

def update_item(id: int, db: Session, item_data: ItemUpdate, user_id: int):
    db_item = db.query(Item).filter(Item.id == id, Item.user_id == user_id).first()
    
    if not db_item:
        return None 

    update_data = item_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_item, key, value)

    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    
    return db_item