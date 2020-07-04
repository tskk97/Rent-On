"""empty message

Revision ID: 2cc4e4a49273
Revises: bb4d1f9a3e51
Create Date: 2020-07-04 14:22:22.406676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2cc4e4a49273'
down_revision = 'bb4d1f9a3e51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('property',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('city', sa.String(length=255), nullable=True),
    sa.Column('state', sa.String(length=255), nullable=True),
    sa.Column('zip_code', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.String(length=255), nullable=True),
    sa.Column('area', sa.Integer(), nullable=True),
    sa.Column('number_bedrooms', sa.Integer(), nullable=True),
    sa.Column('amenities', sa.String(length=255), nullable=True),
    sa.Column('furnish', sa.String(length=255), nullable=True),
    sa.Column('isAvailable', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('property_user_rel',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('property_id', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['property_id'], ['property.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('property_user_rel')
    op.drop_table('property')
    # ### end Alembic commands ###