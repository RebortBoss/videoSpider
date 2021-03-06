"""media table add is_detail column

Revision ID: bb7c7b46fba0
Revises: 1b2d2f1a1d56
Create Date: 2016-02-21 23:37:02.854690

"""

# revision identifiers, used by Alembic.
revision = 'bb7c7b46fba0'
down_revision = '1b2d2f1a1d56'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('media', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_detail', sa.Boolean(), nullable=True, default=False))

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('media', schema=None) as batch_op:
        batch_op.drop_column('is_detail')

    ### end Alembic commands ###
