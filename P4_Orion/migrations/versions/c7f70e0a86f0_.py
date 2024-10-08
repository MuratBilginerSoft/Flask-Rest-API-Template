"""empty message

Revision ID: c7f70e0a86f0
Revises: None
Create Date: 2024-09-17 05:06:53.198658

"""

# revision identifiers, used by Alembic.
revision = 'c7f70e0a86f0'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authenticationlogs',
    sa.Column('Id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('UserId', sa.String(length=300), nullable=True),
    sa.Column('Status', sa.String(length=10), nullable=True),
    sa.Column('ChangeStatusAt', sa.String(length=30), nullable=True),
    sa.Column('CreatedBy', sa.String(length=300), nullable=True),
    sa.Column('CreatedAt', sa.String(length=30), nullable=True),
    sa.Column('ChangedBy', sa.String(length=300), nullable=True),
    sa.Column('ChangedAt', sa.String(length=30), nullable=True),
    sa.Column('Revision', sa.Integer(), nullable=True),
    sa.Column('DeleteFlag', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('authentications',
    sa.Column('Id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('UserId', sa.String(length=300), nullable=True),
    sa.Column('Email', sa.String(length=100), nullable=True),
    sa.Column('Password', sa.String(length=300), nullable=True),
    sa.Column('Token', sa.String(length=300), nullable=True),
    sa.Column('ConfirmStatus', sa.Integer(), nullable=True),
    sa.Column('CreatedBy', sa.String(length=300), nullable=True),
    sa.Column('CreatedAt', sa.String(length=30), nullable=True),
    sa.Column('ChangedBy', sa.String(length=300), nullable=True),
    sa.Column('ChangedAt', sa.String(length=30), nullable=True),
    sa.Column('Revision', sa.Integer(), nullable=True),
    sa.Column('DeleteFlag', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('Id'),
    sa.UniqueConstraint('Email'),
    sa.UniqueConstraint('UserId')
    )
    op.create_table('reqtimers',
    sa.Column('Id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('UserId', sa.String(length=300), nullable=True),
    sa.Column('SessionId', sa.String(length=300), nullable=True),
    sa.Column('FunctionName', sa.String(length=100), nullable=True),
    sa.Column('StartTime', sa.String(length=30), nullable=True),
    sa.Column('EndTime', sa.String(length=30), nullable=True),
    sa.Column('CompletionTime', sa.Float(), nullable=True),
    sa.Column('Status', sa.String(length=10), nullable=True),
    sa.Column('CreatedBy', sa.String(length=300), nullable=True),
    sa.Column('CreatedAt', sa.String(length=30), nullable=True),
    sa.Column('ChangedBy', sa.String(length=300), nullable=True),
    sa.Column('ChangedAt', sa.String(length=30), nullable=True),
    sa.Column('Revision', sa.Integer(), nullable=True),
    sa.Column('DeleteFlag', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('resetpasswords',
    sa.Column('Id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('UserId', sa.String(length=300), nullable=True),
    sa.Column('Email', sa.String(length=100), nullable=True),
    sa.Column('Token', sa.String(length=300), nullable=True),
    sa.Column('Status', sa.Integer(), nullable=True),
    sa.Column('CreatedBy', sa.String(length=300), nullable=True),
    sa.Column('CreatedAt', sa.String(length=30), nullable=True),
    sa.Column('ChangedBy', sa.String(length=300), nullable=True),
    sa.Column('ChangedAt', sa.String(length=30), nullable=True),
    sa.Column('Revision', sa.Integer(), nullable=True),
    sa.Column('DeleteFlag', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('users',
    sa.Column('Id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('UserId', sa.String(length=300), nullable=True),
    sa.Column('Email', sa.String(length=100), nullable=True),
    sa.Column('Name', sa.String(length=30), nullable=True),
    sa.Column('Surname', sa.String(length=30), nullable=True),
    sa.Column('Company', sa.String(length=100), nullable=True),
    sa.Column('Role', sa.String(length=100), nullable=True),
    sa.Column('ImagePath', sa.String(length=500), nullable=True),
    sa.Column('CreatedBy', sa.String(length=300), nullable=True),
    sa.Column('CreatedAt', sa.String(length=30), nullable=True),
    sa.Column('ChangedBy', sa.String(length=300), nullable=True),
    sa.Column('ChangedAt', sa.String(length=30), nullable=True),
    sa.Column('Revision', sa.Integer(), nullable=True),
    sa.Column('DeleteFlag', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('Id'),
    sa.UniqueConstraint('Email'),
    sa.UniqueConstraint('UserId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('resetpasswords')
    op.drop_table('reqtimers')
    op.drop_table('authentications')
    op.drop_table('authenticationlogs')
    # ### end Alembic commands ###
