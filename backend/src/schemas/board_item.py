from pydantic import BaseModel


class BoardItemSchema(BaseModel):
    """
    Schema for
    """
    title: str
    type: str
    position: int
