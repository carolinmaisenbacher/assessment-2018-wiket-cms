"""empty message

Revision ID: 7dbae3fb54aa
Revises: 7faed0b3a49a
Create Date: 2018-11-13 15:45:14.714318

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7dbae3fb54aa'
down_revision = '7faed0b3a49a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('active_texts',
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('text_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ),
    sa.ForeignKeyConstraint(['text_id'], ['text.id'], ),
    sa.PrimaryKeyConstraint('restaurant_id', 'text_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('active_texts')
    # ### end Alembic commands ###
