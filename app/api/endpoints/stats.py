from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.item import Item, ItemType

router = APIRouter(
    prefix="/stats"
)

@router.get("/overview")
def get_stats_overview(db: Session = Depends(get_db)):
    items_seen = db.query(Item).filter(Item.completed == True).count()
    items_not_seen = db.query(Item).filter(Item.completed == False).count()
    avg_rating = db.query(func.avg(Item.rating)).filter(Item.completed == True).scalar()

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
def get_stats_by_type(db: Session = Depends(get_db)):
    books_count = db.query(Item).filter(Item.item_type == ItemType.BOOK).count()
    movies_count = db.query(Item).filter(Item.item_type == ItemType.MOVIE).count()
    albums_count = db.query(Item).filter(Item.item_type == ItemType.ALBUM).count()

    return {
        "books": books_count,
        "movies": movies_count,
        "albums": albums_count
    }