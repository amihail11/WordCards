from time import localtime, strftime

from pydantic import BaseModel


class UserCardData(BaseModel):
    pk: int | None = None
    user_id: int
    card_id: int
    demo_time: str = strftime("%Y-%m-%d %H:%M:%S", localtime())
    study_day: int = 0
    status: str = "new"
