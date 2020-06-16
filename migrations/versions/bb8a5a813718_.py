"""empty message

Revision ID: bb8a5a813718
Revises: 312c5204b13d
Create Date: 2020-06-09 17:46:59.115920

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb8a5a813718'
down_revision = '312c5204b13d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bottles', sa.Column('country_esp', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bottles', 'country_esp')
    # ### end Alembic commands ###
