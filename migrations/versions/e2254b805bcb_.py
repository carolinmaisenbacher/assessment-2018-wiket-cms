"""empty message

Revision ID: e2254b805bcb
Revises: 7581b6a51e99
Create Date: 2018-11-07 14:40:46.405723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2254b805bcb'
down_revision = '7581b6a51e99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('text', sa.Column('text', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('text', 'text')
    # ### end Alembic commands ###
