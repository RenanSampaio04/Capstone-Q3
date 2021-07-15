"""empty message

Revision ID: 388a88989dc7
Revises: 
Create Date: 2021-07-15 10:13:38.768102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '388a88989dc7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('login', sa.String(length=150), nullable=False),
    sa.Column('password_hash', sa.String(length=511), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('login')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('calories', sa.Float(), nullable=True),
    sa.Column('section', sa.String(length=150), nullable=True),
    sa.Column('is_veggie', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('total', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf')
    )
    op.create_table('restaurant_tables',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('seats', sa.Integer(), nullable=True),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('total', sa.Float(), nullable=True),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.Column('empty', sa.Boolean(), nullable=True),
    sa.Column('login', sa.String(length=150), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('login'),
    sa.UniqueConstraint('number')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('estimated_arrival', sa.DateTime(), nullable=True),
    sa.Column('cooking', sa.Boolean(), nullable=True),
    sa.Column('ready', sa.Boolean(), nullable=True),
    sa.Column('delivered', sa.Boolean(), nullable=True),
    sa.Column('paid', sa.Boolean(), nullable=True),
    sa.Column('table_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['table_id'], ['restaurant_tables.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products_orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products_orders')
    op.drop_table('orders')
    op.drop_table('restaurant_tables')
    op.drop_table('users')
    op.drop_table('products')
    op.drop_table('employees')
    # ### end Alembic commands ###
