from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate

def create_item(db: Session, item_data: ItemCreate):
    db_item = Item(**item_data.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Item).offset(skip).limit(limit).all()

def get_item(id: int, db: Session):
    item = db.query(Item).filter(Item.id == id).first()

    if not item:
        return f"Item with id {id} not found"  

    return item

def delete_item(id: int, db: Session):
    item = db.query(Item).filter(Item.id == id).first()

    if not item:
        return "Item not found"  

    db.delete(item)
    db.commit()
    db.refresh(item)
    return item

def update_item(id: int, db: Session, item_data: ItemUpdate):
    db_item = db.query(Item).filter(Item.id == id).first()
    
    if not db_item:
        return "Item not found"  

    update_data = item_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_item, key, value)

    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    
    return db_item
    


    