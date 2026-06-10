from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.item import ItemType
from app.schemas.item import ItemResponse
from app.services.recommender import get_random_picked

router = APIRouter(
    prefix="/pick"
)

@router.get("/", response_model=ItemResponse)
def pick_random_item(
    item_type: ItemType | None = None, 
    mood: str | None = None, 
    db: Session = Depends(get_db)  
):
    picked_item = get_random_picked(db=db, item_type=item_type, mood=mood)
    
    if not picked_item:
        raise HTTPException(
            status_code=404, 
            detail="Any item in the queue wasn't found."
        )

    return picked_item