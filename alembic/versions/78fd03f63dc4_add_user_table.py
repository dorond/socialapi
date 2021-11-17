"""Add user table

Revision ID: 78fd03f63dc4
Revises: 3c156ae822ab
Create Date: 2021-11-17 11:23:51.094217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78fd03f63dc4'
down_revision = '3c156ae822ab'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )


def downgrade():
    op.drop_table('users')
    pass
