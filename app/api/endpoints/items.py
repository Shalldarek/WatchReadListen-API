from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.item import ItemResponse, ItemCreate
from app.crud import item as crud_item
from app.core.database import get_db 

router = APIRouter(
    prefix="/items"
)

@router.post("/", response_model=ItemResponse)
def create_new_item(item_in: ItemCreate, db: Session = Depends(get_db)):
    return crud_item.create_item(db=db, item_data=item_in)

@router.get("/", response_model=list[ItemResponse])
def read_items(db: Session = Depends(get_db)):
    return crud_item.get_items(db=db)