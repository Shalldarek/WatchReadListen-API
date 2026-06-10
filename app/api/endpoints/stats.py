from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.core.dep import get_current_user
from app.core.database import get_db
from app.models.item import Item, ItemType
from app.models.user import User

router = APIRouter(
    prefix="/stats"
)

@router.get("/overview")
def get_stats_overview(
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user) 
):
    items_seen = db.query(Item).filter(Item.completed == True, Item.user_id == current_user.id).count()
    items_not_seen = db.query(Item).filter(Item.completed == False, Item.user_id == current_user.id).count()
    
    avg_rating = db.query(func.avg(Item.rating)).filter(Item.completed == True, Item.user_id == current_user.id).scalar()

    if avg_rating is None:
        final_rating = 0.0
    else:
        final_rating = round(avg_rating, 1)

    return {
        "total_completed": items_seen,
        "total_in_queue": items_not_seen,
        "average_rating": final_rating
    }

@router.get("/by-type")
def get_stats_by_type(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    books_count = db.query(Item).filter(Item.item_type == ItemType.BOOK, Item.user_id == current_user.id).count()
    movies_count = db.query(Item).filter(Item.item_type == ItemType.MOVIE, Item.user_id == current_user.id).count()
    albums_count = db.query(Item).filter(Item.item_type == ItemType.ALBUM, Item.user_id == current_user.id).count()

    return {
        "books": books_count,
        "movies": movies_count,
        "albums": albums_count
    }