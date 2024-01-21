"""add new columbs

Revision ID: 4ac21a05f417
Revises: 54bbfccde0e2
Create Date: 2024-01-19 23:52:28.258052

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '4ac21a05f417'
down_revision: Union[str, None] = '54bbfccde0e2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('lastname', sa.String(length=50), server_default='', nullable=False))
    op.add_column('user', sa.Column('number', sa.String(length=20), server_default='', nullable=False))
    op.add_column('user', sa.Column('birthday', sa.Date(), server_default=sa.text('CURRENT_DATE'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'birthday')
    op.drop_column('user', 'number')
    op.drop_column('user', 'lastname')
    # ### end Alembic commands ###

# INFO  [alembic.runtime.migration] Running upgrade 54bbfccde0e2 -> 4ac21a05f417, add new columbs