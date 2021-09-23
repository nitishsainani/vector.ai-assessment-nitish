from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column
from sqlalchemy.orm import validates
from ..database import Base


class BoardItem(Base):
    """
    Board Item consist of items on the board
    id: id is the primary key
    title: title represents the title of the item in the board
    type:
    """
    __tablename__ = 'board_items'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    type = Column(String, nullable=False)
    position = Column(Integer, nullable=False, unique=True)

    @validates('position')
    def validate_position(self, key, position):
        if position < 0:
            raise ValueError("position should be >= 0")
        return position
