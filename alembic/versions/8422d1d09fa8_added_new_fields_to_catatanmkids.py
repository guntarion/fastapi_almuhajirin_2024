"""Added new fields to CatatanMKids

Revision ID: 8422d1d09fa8
Revises: 
Create Date: 2024-07-14 20:38:01.896128

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8422d1d09fa8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_students_id', table_name='students')
    op.drop_table('students')
    op.drop_index('ix_events_id', table_name='events')
    op.drop_table('events')
    op.add_column('catatan_mkids', sa.Column('aktivitas_kedatangan', sa.Integer(), nullable=True))
    op.add_column('catatan_mkids', sa.Column('aktivitas_iqomat', sa.Integer(), nullable=True))
    op.add_column('catatan_mkids', sa.Column('aktivitas_wudhu', sa.Integer(), nullable=True))
    op.add_column('catatan_mkids', sa.Column('aktivitas_shof', sa.Integer(), nullable=True))
    op.add_column('catatan_mkids', sa.Column('aktivitas_dzikir', sa.Integer(), nullable=True))
    op.add_column('catatan_mkids', sa.Column('aktivitas_takkhusyusholat', sa.Integer(), nullable=True))
    op.add_column('catatan_mkids', sa.Column('aktivitas_takkhusyukajian', sa.Integer(), nullable=True))
    op.add_column('catatan_mkids', sa.Column('aktivitas_nyampah', sa.Integer(), nullable=True))
    op.add_column('catatan_mkids', sa.Column('aktivitas_akhlakburuk', sa.Integer(), nullable=True))
    op.drop_column('catatan_mkids', 'aktivitas_slot')
    op.drop_column('catatan_mkids', 'aktivitas_tipe')
    op.drop_column('catatan_mkids', 'aktivitas_kode')
    op.drop_column('catatan_mkids', 'aktivitas_skor')
    op.drop_column('catatan_mkids', 'aktivitas_nama')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('catatan_mkids', sa.Column('aktivitas_nama', sa.VARCHAR(), nullable=True))
    op.add_column('catatan_mkids', sa.Column('aktivitas_skor', sa.FLOAT(), nullable=True))
    op.add_column('catatan_mkids', sa.Column('aktivitas_kode', sa.VARCHAR(), nullable=True))
    op.add_column('catatan_mkids', sa.Column('aktivitas_tipe', sa.VARCHAR(), nullable=True))
    op.add_column('catatan_mkids', sa.Column('aktivitas_slot', sa.INTEGER(), nullable=True))
    op.drop_column('catatan_mkids', 'aktivitas_akhlakburuk')
    op.drop_column('catatan_mkids', 'aktivitas_nyampah')
    op.drop_column('catatan_mkids', 'aktivitas_takkhusyukajian')
    op.drop_column('catatan_mkids', 'aktivitas_takkhusyusholat')
    op.drop_column('catatan_mkids', 'aktivitas_dzikir')
    op.drop_column('catatan_mkids', 'aktivitas_shof')
    op.drop_column('catatan_mkids', 'aktivitas_wudhu')
    op.drop_column('catatan_mkids', 'aktivitas_iqomat')
    op.drop_column('catatan_mkids', 'aktivitas_kedatangan')
    op.create_table('events',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('date', sa.DATETIME(), nullable=False),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_events_id', 'events', ['id'], unique=False)
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
