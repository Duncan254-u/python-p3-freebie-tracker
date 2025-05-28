"""create freebies table

Revision ID: f4b9ba6d292a
Revises: 
Create Date: 2025-05-28 06:45:20.608435

"""
from alembic import op
import sqlalchemy as sa


revision = 'f4b9ba6d292a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('freebies',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('item_name', sa.String(), nullable=False),
        sa.Column('value', sa.Integer(), nullable=False),
        sa.Column('company_id', sa.Integer(), sa.ForeignKey('companies.id'), nullable=False),
        sa.Column('dev_id', sa.Integer(), sa.ForeignKey('devs.id'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    
    op.create_index(op.f('ix_freebies_company_id'), 'freebies', ['company_id'])
    op.create_index(op.f('ix_freebies_dev_id'), 'freebies', ['dev_id'])


def downgrade() -> None:
    op.drop_index(op.f('ix_freebies_dev_id'), table_name='freebies')
    op.drop_index(op.f('ix_freebies_company_id'), table_name='freebies')
    op.drop_table('freebies')
