from pydantic import BaseModel


class UserCardData(BaseModel):
    pk: int | None = None
    user_id: int
    card_id: int
    demo_time: str | None = None
    study_day: int | None = None
