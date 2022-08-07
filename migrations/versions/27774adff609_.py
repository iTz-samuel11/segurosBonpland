"""empty message

Revision ID: 27774adff609
Revises: b11b77959c7f
Create Date: 2022-08-05 23:09:00.538778

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27774adff609'
down_revision = 'b11b77959c7f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('clave', sa.Column('fecha', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('clave', 'fecha')
    # ### end Alembic commands ###