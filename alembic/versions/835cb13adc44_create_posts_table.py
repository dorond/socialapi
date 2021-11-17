"""create posts table

Revision ID: 835cb13adc44
Revises: 
Create Date: 2021-11-17 10:31:10.889995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '835cb13adc44'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', 
    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('title', sa.String(), nullable=False))


def downgrade():
    op.drop_table('posts')
    
