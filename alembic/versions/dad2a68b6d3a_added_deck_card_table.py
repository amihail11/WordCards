"""added_deck_card_table

Revision ID: dad2a68b6d3a
Revises: de8fe69ca3de
Create Date: 2024-08-07 14:33:03.359521

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dad2a68b6d3a'
down_revision: Union[str, None] = 'de8fe69ca3de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('word', sa.String(), nullable=False),
    sa.Column('meaning', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_card_id'), 'card', ['id'], unique=False)
    op.create_table('deck',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_deck_id'), 'deck', ['id'], unique=False)
    op.create_table('deck_card',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('deck_id', sa.Integer(), nullable=False),
    sa.Column('card_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['card_id'], ['card.id'], ),
    sa.ForeignKeyConstraint(['deck_id'], ['deck.id'], ),
    sa.PrimaryKeyConstraint('id', 'deck_id', 'card_id')
    )
    op.create_index(op.f('ix_deck_card_id'), 'deck_card', ['id'], unique=False)
    op.drop_index('ix_cards_id', table_name='cards')
    op.drop_table('cards')
    op.drop_index('ix_decks_id', table_name='decks')
    op.drop_table('decks')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('decks',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='decks_pkey')
    )
    op.create_index('ix_decks_id', 'decks', ['id'], unique=False)
    op.create_table('cards',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('word', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('meaning', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='cards_pkey')
    )
    op.create_index('ix_cards_id', 'cards', ['id'], unique=False)
    op.drop_index(op.f('ix_deck_card_id'), table_name='deck_card')
    op.drop_table('deck_card')
    op.drop_index(op.f('ix_deck_id'), table_name='deck')
    op.drop_table('deck')
    op.drop_index(op.f('ix_card_id'), table_name='card')
    op.drop_table('card')
    # ### end Alembic commands ###
