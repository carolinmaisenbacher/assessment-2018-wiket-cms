"""empty message

Revision ID: 7995860c02c9
Revises: b52a0d706a9d
Create Date: 2018-11-12 20:35:16.251061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7995860c02c9'
down_revision = 'b52a0d706a9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('dish', 'vegan',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('dish', 'vegetarian',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('dish', 'vegetarian',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('dish', 'vegan',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###
