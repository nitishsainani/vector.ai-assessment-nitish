"""init

Revision ID: 38a9e10fd1ba
Revises: 
Create Date: 2021-09-23 17:32:45.527226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38a9e10fd1ba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'board_items',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('type', sa.String, nullable=False),
        sa.Column('position', sa.Integer, nullable=False, unique=True),
    )


def downgrade():
    op.drop_table('board_items')
