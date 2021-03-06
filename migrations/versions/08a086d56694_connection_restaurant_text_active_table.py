"""connection Restaurant, text_active table

Revision ID: 08a086d56694
Revises: 7dbae3fb54aa
Create Date: 2018-11-13 15:49:44.194146

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '08a086d56694'
down_revision = '7dbae3fb54aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('texts_active',
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.Column('text_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ),
    sa.ForeignKeyConstraint(['text_id'], ['text.id'], ),
    sa.PrimaryKeyConstraint('restaurant_id', 'text_id')
    )
    op.drop_table('active_texts')
    op.drop_column('restaurant', 'text_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('restaurant', sa.Column('text_active', postgresql.ARRAY(sa.INTEGER()), autoincrement=False, nullable=True))
    op.create_table('active_texts',
    sa.Column('restaurant_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('text_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], name='active_texts_restaurant_id_fkey'),
    sa.ForeignKeyConstraint(['text_id'], ['text.id'], name='active_texts_text_id_fkey'),
    sa.PrimaryKeyConstraint('restaurant_id', 'text_id', name='active_texts_pkey')
    )
    op.drop_table('texts_active')
    # ### end Alembic commands ###
