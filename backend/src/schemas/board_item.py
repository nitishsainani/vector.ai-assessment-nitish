from pydantic import BaseModel


class BoardItemSchema(BaseModel):
    """
    Schema for BoardItem
    """
    title: str
    type: str
    position: int
