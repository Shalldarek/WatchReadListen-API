from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.item import ItemResponse, ItemCreate, ItemUpdate
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

@router.get("/{id}", response_model=ItemResponse)
def get_item(id: int, db: Session=Depends(get_db)):
    return crud_item.get_item(id=id,db=db)

@router.delete("/{id}", response_model=ItemResponse)
def delete_item(id: int, db: Session=Depends(get_db)):
    return crud_item.delete_item(id=id,db=db)

@router.put("/{id}", response_model=ItemUpdate)
def update_item(id: int, db: Session=Depends(get_db), item_data=ItemUpdate):
    return crud_item.update_item(id=id, db=db, item_data=item_data)