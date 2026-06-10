from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.dep import get_current_user
from app.core.database import get_db
from app.schemas.item import ItemCreate, ItemUpdate, ItemResponse
from app.crud import item as crud_item
from app.models.user import User


router = APIRouter(
    prefix="/items"
)

@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_new_item(
    item_in: ItemCreate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user) 
):
    return crud_item.create_item(db=db, item_data=item_in, user_id=current_user.id)


@router.get("/", response_model=List[ItemResponse])
def read_user_items(
    skip: int = 0, 
    limit: int = 10, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud_item.get_items(db=db, user_id=current_user.id, skip=skip, limit=limit)


@router.get("/{id}", response_model=ItemResponse)
def read_user_item(
    id: int, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    item = crud_item.get_item(id=id, db=db, user_id=current_user.id)
    if not item:
        raise HTTPException(status_code=404, detail="The item wasn't found")
    return item


@router.put("/{id}", response_model=ItemResponse)
def update_user_item(
    id: int, 
    item_in: ItemUpdate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    updated_item = crud_item.update_item(id=id, db=db, item_data=item_in, user_id=current_user.id)
    if not updated_item:
        raise HTTPException(status_code=404, detail="The items doesn't exist or you have no access to update it")
    return updated_item


@router.delete("/{id}", response_model=ItemResponse)
def delete_user_item(
    id: int, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    deleted_item = crud_item.delete_item(id=id, db=db, user_id=current_user.id)
    if not deleted_item:
        raise HTTPException(status_code=404, detail="The items doesn't exist or you have no access to delete it")
    return deleted_item