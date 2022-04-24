"""empty message

Revision ID: 01d3af3438b6
Revises: de332fd7a749
Create Date: 2022-04-24 16:33:29.504106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01d3af3438b6'
down_revision = 'de332fd7a749'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('my_courses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('liked', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('my_courses', schema=None) as batch_op:
        batch_op.drop_column('liked')

    # ### end Alembic commands ###
