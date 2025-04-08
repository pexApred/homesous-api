"""create homesous_api schema

Revision ID: ed87b556b9ab
Revises: 
Create Date: 2025-04-07 13:26:01.410305

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ed87b556b9ab'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute("CREATE SCHEMA homesous_api")


def downgrade():
    op.execute("DROP SCHEMA homesous_api CASCADE")