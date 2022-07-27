"""empty message

Revision ID: abcf2a442cc1
Revises: 68bf02e8c967
Create Date: 2022-07-27 04:59:39.483116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abcf2a442cc1'
down_revision = '68bf02e8c967'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'poliza',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=10),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'poliza',
               existing_type=sa.String(length=10),
               type_=sa.INTEGER(),
               existing_nullable=True)
    # ### end Alembic commands ###