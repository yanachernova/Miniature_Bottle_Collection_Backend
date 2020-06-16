"""empty message

Revision ID: 312c5204b13d
Revises: 
Create Date: 2020-05-19 12:18:41.797810

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '312c5204b13d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('consumers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('consumer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['consumer_id'], ['consumers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bottles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('country', sa.String(length=255), nullable=False),
    sa.Column('image', sa.String(length=255), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bottles')
    op.drop_table('categories')
    op.drop_table('consumers')
    # ### end Alembic commands ###
