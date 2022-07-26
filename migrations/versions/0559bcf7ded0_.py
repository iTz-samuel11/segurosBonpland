"""empty message

Revision ID: 0559bcf7ded0
Revises: b29a99cd6318
Create Date: 2022-08-10 16:39:28.661571

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0559bcf7ded0'
down_revision = 'b29a99cd6318'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('carta_aval', 'poliza',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=20),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('carta_aval', 'poliza',
               existing_type=sa.String(length=20),
               type_=sa.INTEGER(),
               existing_nullable=False)
    # ### end Alembic commands ###
