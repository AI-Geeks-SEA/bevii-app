"""text vector

Revision ID: 48d387c50676
Revises: bbbdf965e498
Create Date: 2021-09-19 10:41:13.625519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48d387c50676'
down_revision = 'bbbdf965e498'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('text_vector', sa.String(length=3000), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'text_vector')
    # ### end Alembic commands ###
