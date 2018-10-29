"""empty message

Revision ID: bd78d079f683
Revises: 
Create Date: 2018-10-25 17:52:30.270625

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'bd78d079f683'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('owner',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_owner_email'), 'owner', ['email'], unique=True)
    op.create_index(op.f('ix_owner_username'), 'owner', ['username'], unique=True)
    op.create_table('restaurant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=180), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('telephone', sa.String(length=40), nullable=True),
    sa.Column('street', sa.String(length=180), nullable=True),
    sa.Column('street_number', sa.String(length=40), nullable=True),
    sa.Column('city_code', sa.String(length=20), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('text_active', postgresql.ARRAY(sa.Integer()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('menu__paragraph',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('menu__paragraph')
    op.drop_table('restaurant')
    op.drop_index(op.f('ix_owner_username'), table_name='owner')
    op.drop_index(op.f('ix_owner_email'), table_name='owner')
    op.drop_table('owner')
    # ### end Alembic commands ###