from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from wordcards.database import Base


class UserCard(Base):
    __tablename__ = "user_card"

    pk: Mapped[int] = mapped_column("id", primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", name="user_card_user_id_fkey")
    )
    card_id: Mapped[int] = mapped_column(
        ForeignKey("card.id", name="user_card_card_id_fkey")
    )
    demo_time: Mapped[str]
    study_day: Mapped[int]

    __table_args__ = (UniqueConstraint("user_id", "card_id", name="unique_user_card"),)
