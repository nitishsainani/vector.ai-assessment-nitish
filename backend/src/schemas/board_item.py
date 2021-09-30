from pydantic import BaseModel
from pydantic.fields import List


class BoardItemSchema(BaseModel):
    """
    Schema for BoardItem
    """
    title: str
    type: str
    position: int


class BoardItemPositionSchema(BaseModel):
    """
    Schema for one item position
    """
    id: int
    position: int


class BoardItemPositionsSchema(BaseModel):
    """
    Schema for new positions in Board
    """
    positions: List[BoardItemPositionSchema]
