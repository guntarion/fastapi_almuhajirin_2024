"""Add recorder_name to catatan_mkids

Revision ID: 9db0ca22171a
Revises: 8422d1d09fa8
Create Date: 2024-07-14 21:40:23.451843

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9db0ca22171a'
down_revision: Union[str, None] = '8422d1d09fa8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_students_id', table_name='students')
    op.drop_table('students')
    op.add_column('catatan_mkids', sa.Column('recorder_name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('catatan_mkids', 'recorder_name')
    op.create_table('students',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('birthdate', sa.DATE(), nullable=True),
    sa.Column('class_name', sa.VARCHAR(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_students_id', 'students', ['id'], unique=False)
    # ### end Alembic commands ###
