from fastapi import FastAPI, Depends, APIRouter
from ...schemas.board_item import BoardItemSchema
from sqlalchemy.orm import Session
from ...database import get_db
from ...models import BoardItem


router = APIRouter()


@router.post("/")
def create_board_item(details: BoardItemSchema, db: Session = Depends(get_db)):
    to_create = BoardItem(
        title=details.title,
        type=details.type,
        position=details.position,
    )
    db.add(to_create)
    db.commit()
    return {
        "success": True,
        "created_id": to_create.id
    }


@router.get("/")
def get_board_items(db: Session = Depends(get_db)):
    return db.query(BoardItem).all()
