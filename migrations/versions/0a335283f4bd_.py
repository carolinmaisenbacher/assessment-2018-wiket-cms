"""empty message

Revision ID: 0a335283f4bd
Revises: c2be0c8d8fda
Create Date: 2018-11-19 19:14:02.984582

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a335283f4bd'
down_revision = 'c2be0c8d8fda'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dish', sa.Column('position', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('dish', 'position')
    # ### end Alembic commands ###
