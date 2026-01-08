from attrs import define

from .mixins import TimestampMixin


@define
class Sport:
    name: str


@define(kw_only=True)
class Team(TimestampMixin):
    id: int
    name: str
    country: str
    sport: Sport
