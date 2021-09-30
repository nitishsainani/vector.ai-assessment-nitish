from fastapi import FastAPI, Depends, APIRouter
from ...schemas import BoardItemSchema, BoardItemPositionsSchema
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


@router.post("/reorder/")
def update_board_items(data: BoardItemPositionsSchema, db: Session = Depends(get_db)):
    # FIXME: Not sure if this is the efficient way to do it
    print(data.positions)
    id_positions_map = {}
    for item in data.positions:
        id_positions_map[item.id] = item.position

    all_items = db.query(BoardItem).all()
    # adding bogus values
    for i, item in enumerate(all_items):
        item.position = -i * 100
        db.add(item)
    db.commit()

    for item in all_items:
        item.position = id_positions_map.get(item.id, item.position)
        db.add(item)
    db.commit()
    return data
