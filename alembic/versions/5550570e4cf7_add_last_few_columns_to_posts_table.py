"""add last few columns to posts table

Revision ID: 5550570e4cf7
Revises: a43468218695
Create Date: 2021-11-17 11:38:52.897656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5550570e4cf7'
down_revision = 'a43468218695'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
