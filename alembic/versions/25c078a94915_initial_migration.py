"""initial migration

Revision ID: 25c078a94915
Revises: 
Create Date: 2024-05-31 20:38:47.004128

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "25c078a94915"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "cards",
        sa.Column("card_id", sa.Integer(), nullable=False),
        sa.Column("word", sa.String(), nullable=False),
        sa.Column("meaning", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("card_id"),
    )
    op.create_index(op.f("ix_cards_card_id"), "cards", ["card_id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_cards_card_id"), table_name="cards")
    op.drop_table("cards")
    # ### end Alembic commands ###
