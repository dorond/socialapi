"""add content column to posts table

Revision ID: 3c156ae822ab
Revises: 835cb13adc44
Create Date: 2021-11-17 11:14:25.889868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c156ae822ab'
down_revision = '835cb13adc44'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts', 'content')
