"""table update

Revision ID: 855417d40ebb
Revises: b2b340b96c4e
Create Date: 2020-06-06 17:01:20.365954

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '855417d40ebb'
down_revision = 'b2b340b96c4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('post_content', sa.Unicode(length=5000), nullable=True))
    op.add_column('user', sa.Column('first_name', sa.Unicode(length=50), nullable=True))
    op.add_column('user', sa.Column('last_name', sa.Unicode(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')
    op.drop_column('post', 'post_content')
    # ### end Alembic commands ###
