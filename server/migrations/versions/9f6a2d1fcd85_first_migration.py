"""first migration

Revision ID: 9f6a2d1fcd85
Revises: 
Create Date: 2022-06-09 08:36:41.619432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f6a2d1fcd85'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('interests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('student_interests',
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('interest_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['interest_id'], ['interests.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student_interests')
    op.drop_table('students')
    op.drop_table('interests')
    # ### end Alembic commands ###
